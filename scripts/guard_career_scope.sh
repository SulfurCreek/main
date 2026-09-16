#!/usr/bin/env bash
# PreToolUse guard：把「個人成長 session」限制成「全部可讀、只有 career/ 可寫」。
#
# 為什麼需要：該 session 的工作是讀取 repo 內既有產出（規格書、skill、wiki、分析結果），
# 萃取成個人職能與履歷素材。它**不該**回頭改那些產出——改了會跟主幹撞衝突、
# 也會讓「證據來源」與「證據解讀」混在同一個人手上（實際已發生：該分支刪掉主幹
# 刻意保留的 hackmd-api 空殼、並反覆改 resume-craft 與 CLAUDE.md）。
#
# 行為：
#   * 只在 GUARDED_BRANCHES 列出的分支上生效，其他分支一律放行。
#   * 放行 career/ 底下的寫入，以及 repo 以外的路徑（scratchpad／暫存檔）。
#   * 其餘一律 deny，並在訊息裡告訴它該怎麼做（寫進 career/_requests-to-main.md）。
#   * 任何非預期狀況（拿不到分支、jq 不存在、路徑解析失敗）一律 fail-open 放行，
#     這是護欄不是安全機制，不該因為自己壞掉就卡住整個 session。

set -uo pipefail

GUARDED_BRANCHES=(
  "claude/happy-lamport-ljis8c"
)

WRITABLE_PREFIX="career/"

allow() { exit 0; }

payload=$(cat 2>/dev/null) || allow
[ -n "$payload" ] || allow
command -v jq >/dev/null 2>&1 || allow

file_path=$(printf '%s' "$payload" | jq -r '.tool_input.file_path // .tool_input.notebook_path // empty' 2>/dev/null) || allow
[ -n "$file_path" ] || allow

repo_root=$(git rev-parse --show-toplevel 2>/dev/null) || allow
[ -n "$repo_root" ] || allow

branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null) || allow
[ -n "$branch" ] || allow

guarded=0
for b in "${GUARDED_BRANCHES[@]}"; do
  [ "$branch" = "$b" ] && guarded=1
done
[ "$guarded" -eq 1 ] || allow

# 絕對路徑化後判斷是否落在 repo 內
case "$file_path" in
  /*) abs="$file_path" ;;
  *)  abs="$PWD/$file_path" ;;
esac
abs=$(printf '%s' "$abs" | sed 's://*:/:g')

case "$abs" in
  "$repo_root"/*) rel="${abs#"$repo_root"/}" ;;
  *) allow ;;   # repo 以外（scratchpad、/tmp）不管
esac

case "$rel" in
  "$WRITABLE_PREFIX"*) allow ;;
esac

reason="邊界限制：這條分支（${branch}）是個人成長／履歷 session，對 repo 內的產出是**唯讀**的，只能寫 ${WRITABLE_PREFIX} 底下的檔案。\
被擋下的路徑：${rel}。\
需要改動 career/ 以外的東西（skill、wiki、CLAUDE.md、規格書、分析產出）時，不要自己動手——把需求寫進 career/_requests-to-main.md，由主幹管理 session（Repo Steward）判斷後統一施作。\
讀取不受限制：要引用任何產出當職能證據，直接 Read 即可。"

jq -nc --arg r "$reason" '{
  hookSpecificOutput: {
    hookEventName: "PreToolUse",
    permissionDecision: "deny",
    permissionDecisionReason: $r
  }
}' 2>/dev/null || allow
exit 0
