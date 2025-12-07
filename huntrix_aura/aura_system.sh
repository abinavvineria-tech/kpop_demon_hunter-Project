#!/usr/bin/env bash
# huntrix_aura.sh — Huntrix Aura System for Termux
# Abinav edition: error-free, menu-driven, with rituals, quests, streaks, and blessings.

set -euo pipefail
IFS=$'\n\t'

# Config paths
STATE_DIR="${HOME}/.huntrix"
STATE_FILE="${STATE_DIR}/aura_state.json"
LOG_FILE="${STATE_DIR}/aura_log.tsv"
BACKUP_DIR="${STATE_DIR}/backups"

# Defaults
VERSION="1.3.0"
APP_NAME="Huntrix Aura"
MIN_BLESS_COOLDOWN=0.5        # Blessing cooldown now 0.5 seconds
MIN_RITUAL_COOLDOWN=900       # 15 minutes in seconds
DAILY_CHECKIN_AURA=5
RITUAL_AURA=8
QUEST_AURA=13
BLESS_AURA=21
STREAK_BONUS_BASE=2
LVL_STEP=100

# Utilities
timestamp() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }
now_epoch() { date -u +"%s"; }
date_local() { date +"%Y-%m-%d %H:%M:%S %Z"; }

mkdir -p "${STATE_DIR}" "${BACKUP_DIR}"

# Minimal JSON helpers
json_init() {
  cat > "${STATE_FILE}" <<EOF
{
  "user":"${USER}",
  "aura":0,
  "level":0,
  "streak":0,
  "last_checkin":"",
  "last_ritual_epoch":0,
  "last_bless_epoch":0,
  "total_rituals":0,
  "total_quests":0,
  "total_blessings":0,
  "created_at":"$(timestamp)",
  "updated_at":"$(timestamp)",
  "version":"${VERSION}"
}
EOF
}

json_get() {
  local key="$1"
  grep -E "\"${key}\"" "${STATE_FILE}" | head -n1 | sed -E 's/.*"'"${key}"'":[ ]*"?(.*[^",])"?,?/\1/'
}

json_set() {
  local key="$1" value="$2"
  if ! [[ "${value}" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    value="\"${value//\"/\\\"}\""
  fi
  awk -v k="${key}" -v v="${value}" '
  {
    if ($0 ~ "\""k"\"") {
      sub(/\"?'"${key}"'\"[[:space:]]*:[[:space:]]*[^,}]+/, "\""k"\": " v)
    }
    print
  }' "${STATE_FILE}" > "${STATE_FILE}.tmp"
  mv "${STATE_FILE}.tmp" "${STATE_FILE}"
}

touch_state() { json_set updated_at "$(timestamp)"; }

log_event() {
  local event="$1" delta="$2" note="$3"
  local aura level streak
  aura="$(json_get aura)"
  level="$(json_get level)"
  streak="$(json_get streak)"
  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$(date_local)" "${event}" "${delta}" "${aura}" "${level}" "${streak}" "${note}" >> "${LOG_FILE}"
}

init() {
  if [ ! -f "${STATE_FILE}" ]; then
    json_init
    log_event "init" "0" "Profile created"
  fi
}

backup_state() {
  local ts="$(date +"%Y%m%d-%H%M%S")"
  cp -f "${STATE_FILE}" "${BACKUP_DIR}/aura-${ts}.json"
  echo "Backup saved: ${BACKUP_DIR}/aura-${ts}.json"
}

restore_state() {
  local file="$1"
  if [ -z "${file}" ] || [ ! -f "${file}" ]; then
    echo "Provide a valid backup file path."
    return 1
  fi
  cp -f "${file}" "${STATE_FILE}"
  touch_state
  log_event "restore" "0" "Restored from ${file}"
  echo "Restored from ${file}"
}

lvl_required() { echo $(( ($1 + 1) * LVL_STEP )); }

try_level_up() {
  local aura level req
  aura="$(json_get aura)"
  level="$(json_get level)"
  while true; do
    req="$(lvl_required "${level}")"
    if (( $(echo "${aura} >= ${req}" | bc -l) )); then
      level=$(( level + 1 ))
      json_set level "${level}"
      log_event "level_up" "0" "Reached level ${level}"
      echo "Ascended: Level ${level} unlocked."
    else
      break
    fi
  done
  touch_state
}

add_aura() {
  local delta="$1" note="$2"
  local aura
  aura="$(json_get aura)"
  aura=$(echo "${aura} + ${delta}" | bc -l)
  json_set aura "${aura}"
  touch_state
  log_event "aura_gain" "${delta}" "${note}"
  try_level_up
}

streak_bonus() { echo $(( STREAK_BONUS_BASE + ($1 / 5) )); }

do_checkin() {
  local last today
  last="$(json_get last_checkin)"
  today="$(date +"%Y-%m-%d")"
  if [ "${last}" = "${today}" ]; then
    echo "Already checked in today."
    return 0
  fi
  local yesterday
  yesterday="$(date -d "yesterday" +"%Y-%m-%d" 2>/dev/null || date -v -1d +"%Y-%m-%d")"
  local streak="$(json_get streak)"
  if [ "${last}" = "${yesterday}" ]; then
    streak=$(( streak + 1 ))
  else
    streak=1
  fi
  json_set streak "${streak}"
  json_set last_checkin "${today}"
  local bonus="$(streak_bonus "${streak}")"
  local gain=$(( DAILY_CHECKIN_AURA + bonus ))
  add_aura "${gain}" "Daily check-in (+${bonus} streak bonus)"
  echo "Check-in complete: +${gain} aura (streak ${streak})."
}

cooldown_ok() {
  local last_epoch="$1" min_gap="$2"
  local now="$(now_epoch)"
  local diff=$(echo "${now} - ${last_epoch}" | bc -l)
  (( $(echo "${diff} >= ${min_gap}" | bc -l) ))
}

do_ritual() {
  local last_epoch="$(json_get last_ritual_epoch)"
  if cooldown_ok "${last_epoch}" "${MIN_RITUAL_COOLDOWN}"; then
    json_set last_ritual_epoch "$(now_epoch)"
    add_aura "${RITUAL_AURA}" "Huntrix ritual"
    json_set total_rituals "$(( $(json_get total_rituals) + 1 ))"
    echo "Ritual complete: +${RITUAL_AURA} aura."
  else
    echo "Ritual cooldown active."
  fi
}

do_quest() {
  read -r -p "Enter quest proof keyword: " proof
  [ -z "${proof}" ] && { echo "Quest aborted."; return 1; }
  add_aura "${QUEST_AURA}" "Quest completed (${proof})"
  json_set total_quests "$(( $(json_get total_quests) + 1 ))"
  echo "Quest complete: +${QUEST_AURA} aura."
}

do_blessing() {
  local last_epoch="$(json_get last_bless_epoch)"
  if cooldown_ok "${last_epoch}" "${MIN_BLESS_COOLDOWN}"; then
    json_set last_bless_epoch "$(now_epoch)"
    add_aura "${BLESS_AURA}" "Huntrix blessing"
    json_set total_blessings "$(( $(json_get total_blessings) + 1 ))"
    echo "Blessing received: +${BLESS_AURA} aura."
  else
    echo "Blessing cooldown active."
  fi
}

show_status() {
  local aura="$(json_get aura)"
  local level="$(json_get level)"
  local streak="$(json_get streak)"
  local req="$(lvl_required "${level}")"
  local next=$(echo "${req} - ${aura}" | bc -l)
  [ $(echo "${next} < 0" | bc -l) -eq 1 ] && next=0
  cat <<EOF
${APP_NAME} status
- Aura: ${aura}
- Level: ${level} (next at ${req}, ${next} to go)
- Streak: ${streak} days
- Total rituals: $(json_get total_rituals)
- Total quests: $(json_get total_quests)
- Total blessings: $(json_get total_blessings)
EOF
}

menu() {
  echo ""
  echo "=== ${APP_NAME} v${VERSION} ==="
  echo "1) Daily check-in"
