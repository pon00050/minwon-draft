# methodology.md — the strategic backbone

This method is **one reusable structure** applied across unrelated legal domains
(a business-licensing clearance, a financial-regulation 해당 여부 question, an
administrative 고시 interpretation, an anti-discrimination query). The same six-part
structure, assert-then-confirm tactic, and "every answer is usable" discipline
apply whether the 민원 is about a licence, a fee, or a service refusal. So the method
is domain-general; only the facts and statutes change.

The mental model underneath everything: **a front-line official finds it costlier
to rebut a stated conclusion than to reason from a blank page, will punt when
jurisdiction is fuzzy, and will concede a procedural-law violation when it is
cited explicitly.** Every technique below exploits one of those three.

---

## The six plays

### Play 1 — Assert-then-confirm (the core move)
State the favorable conclusion as your understanding, then ask only for
agreement. The clerk's cheap path becomes "yes, correct"; any correction still
yields a citable written interpretation. Never write a neutral "is this the
case?" and never a "you are wrong." → see `rhetoric.md` for the exact 문형.

**Calibrate to the analytical layer.** Sort each statement into 법규(rule) /
사실(fact) / 포섭(subsumption). **Assert ① and ②** (rule verified, fact evidenced —
don't hedge a provable fact); **ask ③ by default** — the subsumption is what the
agency decides, and asserting it lets a one-line "전제가 틀렸습니다" foreclose the
inquiry. Diagnose where the dispute lives: *disputed facts* → carry evidence;
*disputed legal effect* → ask ③ and **split off any systemic/enforcement-gap
question** so a premise-denial can't kill it. → rhetoric.md ("Calibrate to the
analytical layer").

### Play 2 — Every answer is pre-wired to a next move
Before submitting, build a branch table: favorable / evasive / unfavorable /
silent → the action each triggers. If any branch has no favorable action,
re-engineer the question. A "no such rule exists" answer is often *more* useful
than a "yes" — it documents a regulatory gap. Silence is not failure; a lapsed
처리기한 is itself the §18 trigger for the next rung.

### Play 3 — Minimize the attack surface
Include only what helps. Delete true-but-risky material that hands the responder
a comparison or rejection hook (e.g. deleting competitor precedents from a
clearance request). Delete self-adverse framing ("my test failed, so I need a
loophole") — it invites strict interpretation. This is a *discipline of omission*,
not of hedging: the sentences stay confident (see `rhetoric.md` G-rules).

### Play 4 — Anti-punt routing
Pre-draw the jurisdictional line inside the question so it cannot be bounced:
"interpretation of your own 고시 text is your office's job, distinct from the
individual adjudication delegated to X." Make the last question a 이송 request so a
wrong-office filing is redirected, not rejected. When a punt is still possible,
phrase it so the punt itself produces useful info ("if this runs on an internal
review standard instead, please provide that standard").

### Play 5 — Verify, don't assume
Every statute quoted is checked against law.go.kr for wording + 시행일자;
terminology is verified per domain, never remembered. → `law_verify.md`.

### Play 6 — Multi-channel triangulation + the escalation ladder
Never hang one substantive question on a single window. Ask parallel agencies so
jurisdiction can't be punted; use agency B's answer to pin agency A; convert an
inter-agency contradiction into its own lever. Then climb only as far as needed:

```
국민신문고 일반민원        (informal, cheap, probing)   ← this skill drafts here
   ↓ unfavorable/unclear
문서24 공식 공문           (legal weight upgrade)
   ↓ refused
정보공개청구 (open.go.kr)  (obtain internal materials = future evidence)
   ↓ no/'insufficient' response
정보공개 §18 이의신청       (procedural-violation succession)
   ↓ parallel
국민권익위 고충민원         (policy-fix recommendation)   ← this skill can also draft here
   ↓ parallel, non-binding
장관 직접 서한             (courtesy political channel)
   ↓ main line
행정심판 청구              (취소+의무이행, binding 재결)
```

Each rung is **cumulative**: its output (공문, written admission, non-response) is
cited as evidence in the next. The clocks drive the ladder — 민원처리법 14일,
정보공개법 10일/20일, 행정심판 청구기한 90일. Track every clock; a missed agency clock
becomes your procedural defect, a missed *own* clock forfeits a right.

---

## Feedback loop after an answer arrives (질문별 대조 → v2)

1. Match the answer line-by-line against each question.
2. **Adversarially re-read it**: separate what is *actually confirmed* from what
   you *assumed/inferred*. (A common high-value catch is a first pass mis-scoring an
   evasive answer as "answered" via a misattributed citation. Guard against your own
   motivated reasoning.)
3. Fire a narrowed **v2** that concedes the settled points ("이미 확인되었으므로
   재확인 불요") and concentrates fire on the genuinely-open 1–2 items. Re-asking a
   settled point lowers your credibility.

---

## Procedural law as a separate lever
Cite procedural statutes alongside substantive ones to close escape routes:
민원 처리에 관한 법률 §9(부당반송 금지)·§16(이송의무)·§18, 행정절차법 §23①(처분이유 명시),
행정심판법 §27(청구기한). "답을 안 준다"는 사실 자체가 다음 단계를 여는 별도 트리거다.

## Two-track hedge
Never make one 민원/track the sole path to the goal. Keep an independent track
alive so no single refusal is fatal. When the record turns adversarial (a formal
처분 exists), stop feeding the counterparty off-record chances — put everything on
the record, because the real venue is 행정심판/헌법소원.

## Document discipline (for the optional archival wrapper)
Split every saved record into an **IMMUTABLE block** (the verbatim submission,
never edited post-hoc, citable as evidence) and a **living analysis block**
(답변 · 질문별 대조 · 응답 시 Action, updated over time). This keeps the record
court-usable and tamper-evident. → wrapper layout in `anatomy.md`.
