#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
count_chars.py — measure a 민원 내용's character count against the portal limit.

Optional helper for the `minwon-draft` skill. Use in Pass 4 before delivering a
draft so a channel character cap is caught by measurement, not at the paste box.
Pure standard library — no dependencies, no API key, runs anywhere Python 3 does.

Usage
    python count_chars.py <file> [channel]      # count a file
    python count_chars.py - [channel]           # count text from stdin
    echo "..." | python count_chars.py - 안전신문고

Channel is optional; if given (and known), the script prints headroom + a
PASS / WARN / OVER verdict against that channel's 내용 limit.

Channel caps (each carries provenance — do not treat as authoritative):
    안전신문고  = 1600   내용 field.
        Source:    direct portal observation (a draft hit ~1,597/1,600 and had to
                   be rewritten).
        Confidence: PROVISIONAL — single observation, not a cited/maintained spec.
        Applies to: 안전신문고 안전신고 내용 field.
        Recheck if: the portal UI changes, or a draft near the cap is accepted/
                   rejected differently than this predicts.
    국민신문고  = None   large; exact cap NOT observed — confirm at the portal.
    문서24     = None   out of skill v1 scope.

When you observe a new portal's real cap, add it here with the same provenance.

Counting note: this counts Python string length (Unicode code points). Korean
syllables are 1 code point each, so counts match the portal for ordinary 민원 text.
Astral characters (most emoji) are 1 code point here but 2 UTF-16 units in a
JS-based textarea counter — avoid emoji in 내용 (you shouldn't use them anyway), or
treat a near-cap count as approximate if any are present.
"""
import sys
import io

# Windows-safe UTF-8 stdout (cp949/cp1252 consoles crash on Korean print())
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ── channel 내용 character limits ─────────────────────────────────────────────
CHANNEL_LIMITS = {
    "안전신문고": 1600,   # PROVISIONAL (observed, not spec) — see provenance in docstring
    "국민신문고": None,   # large; verify at portal before trusting a number
    "문서24": None,
}
# Aliases so a loose channel string still resolves.
ALIASES = {
    "safetyreport": "안전신문고", "safety": "안전신문고", "안전신고": "안전신문고",
    "epeople": "국민신문고", "국민신문고일반민원": "국민신문고", "일반민원": "국민신문고",
    "고충민원": "국민신문고", "문서24": "문서24",
}
# Target headroom: warn once a draft is within 5% of a cap.
WARN_RATIO = 0.95


def resolve_channel(name):
    if not name:
        return None
    key = name.strip()
    if key in CHANNEL_LIMITS:
        return key
    return ALIASES.get(key.replace(" ", "").lower(), None)


def counts(text):
    total = len(text)                                   # incl. whitespace + newlines
    no_newline = len(text.replace("\n", "").replace("\r", ""))
    no_space = len("".join(text.split()))              # no whitespace at all
    return total, no_newline, no_space


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2

    src = argv[1]
    channel_arg = argv[2] if len(argv) > 2 else None

    if src == "-":
        text = sys.stdin.buffer.read().decode("utf-8")
    else:
        with open(src, encoding="utf-8") as fh:
            text = fh.read()

    total, no_newline, no_space = counts(text)

    print("== 글자수 (count_chars.py) ==")
    print(f"  전체(공백ㆍ줄바꿈 포함) : {total}")
    print(f"  줄바꿈 제외            : {no_newline}")
    print(f"  모든 공백 제외         : {no_space}")

    channel = resolve_channel(channel_arg)
    if channel_arg and not channel:
        print(f"\n  ⚠️ 알 수 없는 채널 '{channel_arg}' — CHANNEL_LIMITS에 등록되지 않음.")
        return 0
    if not channel:
        print("\n  (채널 미지정 — 한도 대조 생략. 두 번째 인자로 채널명을 주면 대조합니다.)")
        return 0

    limit = CHANNEL_LIMITS[channel]
    if limit is None:
        print(f"\n  {channel}: 확인된 hard cap 없음(포털에서 직접 확인 권장). 대조 생략.")
        return 0

    # Conservative: check the LARGEST count against the cap.
    used = total
    headroom = limit - used
    if used > limit:
        verdict = f"❌ OVER — {used - limit}자 초과. 제출 전 축약 필수."
        rc = 1
    elif used >= limit * WARN_RATIO:
        verdict = f"⚠️ WARN — 한도의 {used/limit:.0%}. 여유 {headroom}자. 축약 권장."
        rc = 0
    else:
        verdict = f"✅ PASS — 여유 {headroom}자 ({used/limit:.0%} 사용)."
        rc = 0
    print(f"\n  {channel} 한도 {limit}자 대비: {verdict}")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
