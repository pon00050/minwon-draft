#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for count_chars.py. Stdlib only — run: python test_count_chars.py
(exit 0 = all pass, exit 1 = failure). count_chars gates delivery in Pass 4, so
its counting and verdict boundaries are quality-control infrastructure, not a
convenience — hence real tests.
"""
import os
import sys
import subprocess
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "count_chars.py")

spec = importlib.util.spec_from_file_location("count_chars", SCRIPT)
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)

failures = []
def check(name, got, want):
    if got != want:
        failures.append(f"{name}: got {got!r}, want {want!r}")

# ── counts(): total / no_newline / no_space ──────────────────────────────────
check("LF total",            cc.counts("가나다\n라마")[0], 6)     # 5 letters + \n
check("CRLF total",          cc.counts("가나다\r\n라마")[0], 7)   # + \r
check("no_newline strips \\r\\n", cc.counts("가나다\r\n라마")[1], 5)
check("no_space strips all ws",   cc.counts("가 나\t다\n라")[2], 4)
check("trailing newline counted", cc.counts("abc\n")[0], 4)
check("korean = 1 codepoint each", cc.counts("한글")[0], 2)
check("empty string",        cc.counts("")[0], 0)
# Documented behavior: Python counts code points; astral emoji = 1 here (2 UTF-16
# units in a JS textarea). Flags a change if someone alters the counting basis.
check("astral emoji = 1 codepoint", cc.counts("😀")[0], 1)

# ── resolve_channel(): exact, aliases, normalization, unknown ────────────────
check("resolve exact",       cc.resolve_channel("안전신문고"), "안전신문고")
check("alias safety",        cc.resolve_channel("safety"), "안전신문고")
check("alias 안전신고",       cc.resolve_channel("안전신고"), "안전신문고")
check("alias 일반민원",       cc.resolve_channel("일반민원"), "국민신문고")
check("alias case+space",    cc.resolve_channel("  EPeople "), "국민신문고")
check("unknown -> None",     cc.resolve_channel("문서99"), None)
check("empty -> None",       cc.resolve_channel(""), None)

# ── verdict boundaries via subprocess (안전신문고 cap=1600, WARN >=95% => 1520) ──
def run_stdin(text, channel):
    p = subprocess.run([sys.executable, SCRIPT, "-", channel],
                       input=text.encode("utf-8"),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout.decode("utf-8", "replace")

rc, out = run_stdin("가" * 100, "안전신문고")
check("PASS rc", rc, 0); check("PASS text", "PASS" in out, True)
rc, out = run_stdin("가" * 1519, "안전신문고")   # just under 95%
check("PASS just under WARN", "PASS" in out, True)
rc, out = run_stdin("가" * 1599, "안전신문고")   # in WARN band, under cap
check("WARN rc", rc, 0); check("WARN text", "WARN" in out, True)
rc, out = run_stdin("가" * 1600, "안전신문고")   # exactly at cap => not OVER
check("at-cap not OVER", "OVER" not in out, True)
rc, out = run_stdin("가" * 1601, "안전신문고")   # over cap
check("OVER rc", rc, 1); check("OVER text", "OVER" in out, True)
rc, out = run_stdin("가" * 50, "국민신문고")     # limit None => no verdict
check("no-cap rc", rc, 0)
rc, out = run_stdin("가" * 50, "문서99")         # unknown channel
check("unknown channel note", "알 수 없는 채널" in out, True)

if failures:
    print(f"FAIL ({len(failures)} case(s)):")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("OK — all count_chars tests passed")
