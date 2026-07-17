---
name: minwon-draft
description: Generate copy-paste-ready 국민신문고 민원 / 안전신문고 안전신고 (Korean government e-petition & safety-report) content from raw facts. Structures the petition with a field-developed, adversarially-refined 6-section assert-then-confirm method, verifies every statute citation against the live law.go.kr data via the korean-law-mcp connector (or flags them for manual check), runs an adversarial self-review, and outputs a ready-to-submit 제목 + 내용 plus a response-contingency plan. Use whenever the user wants to draft/write/file a 민원, 국민신문고, 안전신문고, 불법주정차/안전 신고, 고충민원, 진정, or 정부 질의, or pastes facts and asks for petition content.
user-invocable: true
argument-hint: [paste the raw facts, or a path to a file/notes containing them]
---

# minwon-draft — compose a 국민신문고 민원 from raw facts

You turn whatever raw material the user pastes (facts, a goal, an agency, some
statutes, a prior agency reply) into **copy-paste-ready** 국민신문고 content: a
`제목` and a plain-text `내용`, plus the recommended 민원종류/기관/channel, a citation
table, and a response-contingency plan.

This skill is **self-contained** — it carries its own method and works from any
folder, with no dependency on any particular project being open.

**Prime directive:** the primary deliverable is the submission payload (제목 +
내용), and 내용 is **plain text**, not markdown (the 국민신문고 box is a plain
textarea). Everything else is supporting output.

Read the reference files as you reach each pass — do not preload them all.

---

## Pass 0 — Intake & classify

The user's raw input is: **$ARGUMENTS** (if empty, use what they pasted in chat;
if they gave a file path, read it).

Extract these fields. Move fast, but **calibrate inference to what's at stake** —
this is a legal-administrative document, so a fabricated fact is worse than an
extra question. Apply this hierarchy:

- **Infer freely:** presentation choices (tone, ordering, section labels) and
  low-risk context (신청인 지위 phrasing, which framing disclaimer fits).
- **Never infer — these are load-bearing:** dates, numbers, 법적 지위/자격, agency
  conduct, quoted text (조문·고시·prior reply wording), and the exact 법적 효과 the
  user wants (what a favorable answer is). If one is missing, insert a **visible
  placeholder** — `⟦확인 필요: 위반 일시⟧`, `⟦확인 필요: 대상 기관⟧` — not a guess.
- Ask **one** compact batch of questions (AskUserQuestion) only for a genuinely
  load-bearing unknown you cannot leave as a placeholder (typically: the target
  agency, or the exact conclusion they want confirmed).

Mark any low-risk assumption inline with `⟦가정: …⟧`. **Do not label the output
제출용/ready-to-submit while any `⟦확인 필요: …⟧` placeholder remains** — say plainly
which facts the user must fill before submitting.

1. **신청인 지위** — who is petitioning (시민 / 사업자 / 예비 창업자 / 이용자 등).
2. **민원 성격** — 개인 구제 vs 정책 질의 vs 문언 해석 vs 이의/clearance. Drives the
   framing disclaimer.
3. **대상 기관** — which agency/office. If jurisdiction is ambiguous, note it and
   plan to recommend parallel filing (methodology Play 6).
4. **쟁점 / 목표** — the substantive question, and **what a favorable answer looks
   like** (you need this to build assert-then-confirm and the branch table).
5. **사실관계** — dates, numbers, events, prior 민원 numbers. Keep them absolute.
6. **근거 법령·고시** — every statute/notice at issue (to verify in Pass 1).
7. **선행 답변** — if this is a follow-up, the prior reply text (for concede-and-
   narrow, methodology feedback loop).

Then read `references/anatomy.md` → pick **민원종류 + channel** from its chooser
(default: 일반민원 on 국민신문고). **If it is a safety/enforcement report (불법주정차,
시설물 결함, 교통·자동차 위반), the channel is 안전신문고 — read that chooser's
"⚠️ 안전신문고 채널 주의" block now**, because its ≈1,600자 hard cap, field truncation,
and photo-interval rules change how you draft (and what you tell the user to shoot).
Read `references/methodology.md` for the strategic frame.

## Pass 1 — Verify citations (korean-law-mcp)

Read `references/law_verify.md`. For **every** statute/판례 you will cite, verify it
against the live law.go.kr data using the **korean-law-mcp** connector (bundled with
this plugin — see the repo README for install; the model calls its MCP tools
directly). Capture the verbatim 조문본문 + 시행일자. Typical tools:

- `search_law` — confirm the law exists and get its **시행일자 / MST** (that you are
  quoting the in-force version, not a superseded one).
- `get_law_text` — fetch the exact 조문 전문 to quote verbatim.
- `legal_analysis` (`mode: verify_citations`) — hallucination check: confirms the
  조문 exists **and** that the title you attached to it matches the real one
  (`[CONTENT_MISMATCH]` catches "제750조(계약해제)"-style errors).
- `search_admin_rule` / `get_admin_rule` — for **행정규칙** (고시·훈령·예규·지침): these
  ARE verifiable via the connector (unlike the raw 법령 API).
- `search_precedents` / `get_precedent_text` — for 판례 citations.

**Procedural provisions get the same treatment as substantive ones.** Do NOT carry a
generic ladder ("민원처리법 처리기한 14일", 이송의무, 이유제시 의무, 이의신청 기간) into a matter
from memory — 처리기한, 소관 duty, and remedy windows vary by 민원종류, agency rule,
statutory exception, and whether the agency action is a 처분. Verify each procedural
article you cite (`민원 처리에 관한 법률`, `행정절차법`, `행정심판법`, `정보공개법` 등) live, and
confirm the deadline/duty actually applies to *this* filing type before stating it.
Anything unverified → `⚠️ 미검증`, same rule.

**If the korean-law-mcp connector is not available** (not installed, or no LAW_OC
key was provided at install), do NOT block the draft: produce it and tag every
unverified citation `⚠️ 미검증 — 제출 전 재확인`, and tell the user in the delivery
summary how to enable verification (README: one-line install + free key). A
citation that could not be verified is tagged, **never silently quoted.** Run the
terminology self-check for this domain (don't hardcode — see `law_verify.md`).

## Pass 2 — Draft

Read `references/anatomy.md` (skeleton) and `references/rhetoric.md` (voice), and
`references/examples.md` for the exemplar closest to this 민원's purpose. Assemble:

- The **6-단 plain-text body**: 안녕하십니까 → 신청인 지위 + framing disclaimer →
  사실관계 → 확인이 필요한 조항 (verbatim, verified) → 질의 사항 (【질문 N】,
  assert-then-confirm each) → 관련 법령 (substantive **and** procedural) → 회신 요청
  (scope-limit + 결론 먼저 + 이송 fallback) → optional human closing → 감사합니다.
- The **제목** from the anatomy title pattern.
- Every question in assert-then-confirm form; last question = 이송 request.
- Confident 존댓말; 어미 whitelist; zero 금지 표현.

## Pass 3 — Adversarial self-review (do not skip — this is the signature step)

Simulate the front-line clerk's incentives and red-team your own draft:

- [ ] **Self-adverse statements deleted** (no "my X failed, so I need a loophole").
- [ ] **Attack surface minimized** — remove true-but-risky comparisons/precedents
      that hand the reader a rejection hook.
- [ ] **Anti-punt** — each interpretive question scoped to the office's lane
      (문언 해석 vs 위탁 심사); a punt is still made to produce useful info.
- [ ] **No softeners** appended to assert-then-confirm; no 금지 표현 anywhere.
- [ ] **Understatement** — no unprovable predictions ("반드시 …할 것"); use "배제할 수
      없다". Guard against mis-scoring your own claims as stronger than they are.
- [ ] **Layer check — 법규 / 사실 / 포섭.** Assert the rule (verified) and the fact
      (evidenced — don't hedge a provable fact); **ask the subsumption** the agency
      must determine ("…이 본 사실관계에 적용되는지 확인 요청"), never assert it as settled
      ("…적용되는 것으로 이해됩니다"); and **split off any systemic/enforcement-gap
      question** so a one-line premise-denial can't foreclose it (rhetoric.md —
      "Calibrate to the analytical layer").
- [ ] **Every citation verified** or tagged `⚠️ 미검증 / 재검증 권장 / 행정규칙 — 수기 검증`.
- [ ] **Procedural claims verified too** — every 처리기한/이송의무/이의신청 기간 cited is
      checked live AND confirmed to apply to this 민원종류, not assumed from a generic
      ladder. No load-bearing `⟦확인 필요: …⟧` placeholder left in a "제출용" draft.
- [ ] **Every question maps to a favorable branch.** Build the **응답 시 Action**
      table (favorable / evasive / unfavorable / silent → next move). If any
      branch is a dead end, re-engineer the question.
- [ ] Terminology correct for this domain (verified, not remembered).

## Pass 4 — Deliver

Output, in this order:

1. **민원종류 · 기관 · 채널** — one line (e.g. "일반민원 · ○○부 ○○과 · 국민신문고").
   If jurisdiction was ambiguous, note the recommended parallel filing.
2. **제목** — in its own fenced block, plain text, ready to paste.
3. **내용** — in its own fenced block, **plain text** (bare-line headers), ready to
   paste. Any assumption marked `⟦가정: …⟧` for the user to confirm/edit.
   **Report the character count** below the block — measure it, don't eyeball. Use
   the bundled helper (optional; you may also count inline if Python is absent):
   ```bash
   python scripts/count_chars.py <내용파일> <채널>
   ```
   (or pipe the text: `... count_chars.py - 안전신문고`). It prints all three counts
   and a PASS/WARN/OVER verdict against the channel cap. **안전신문고 ≈ 1,600자 hard cap
   → keep ≤ 1,400자.** If it says WARN/OVER, trim before delivering, not after. For
   안전신문고, also emit the **structured field values** (차량번호 / 발생일시 / 위반장소)
   separately, and restate the full 차량번호/식별자 inside 내용 (fields truncate).
4. **인용 검증표** — table: 법령·조 | 시행일자 | 상태(✅ 검증 / 재검증 권장 / 행정규칙 수기 /
   ⚠️ 미검증).
5. **응답 시 Action** — the contingency table from Pass 3.
6. **다음 단계** — the recommended next escalation rung *if* this answer is
   unfavorable/silent (from methodology Play 6), stated in one line.
7. **Offer** to save the archival `.md` wrapper (anatomy.md layout) into the
   current project's 국민신문고/ folder (or ask where). Do not save unprompted; do
   not invent PII. The wrapper starts as a **draft** (신청번호 placeholder); when the
   user later pastes the submission confirmation, complete it per **Pass 5**.

Finally, a short **pre-submission checklist** the user can eyeball:
- [ ] 제목 anchors the governing 제도/조항 and ends in a verb-noun ask
- [ ] Every 【질문】 is assert-then-confirm; last one is a 이송 request
- [ ] Every quoted 조문 is verified (or tagged) with 시행일자
- [ ] Framing disclaimer present; no 금지 표현; confident tone
- [ ] 내용 char count measured and within the channel cap (Pass 4 step 3)
- [ ] Each answer branch has a prepared next move

## Pass 5 — Record capture (post-submission)

Triggered when the user pastes the **접수 확인 화면** (신청/신고번호 assigned) — often a
later turn. This completes the archival wrapper offered in Pass 4 so the record
mirrors the live submission and is court-usable. Do not invent any field; copy only
what the confirmation shows.

1. **Fill the IMMUTABLE block** with what the portal assigned/recorded: 신청·신고번호,
   신고일시, 신고인(이름/연락처 as shown), 처리기관, 접수경로, and — for 안전신문고 — the
   **structured fields as actually stored** (차량번호 / 발생일시 / 위반장소 / 위·경도) and
   the **첨부 파일 촬영시각·구분(G/C/S)**. The 내용 is the verbatim submitted text.
2. **Rename the file to the convention** `{민원번호}_{기관}_{주제}_{YYYYMMDD}.md`. If the
   actual channel differed from the draft's assumption (e.g. drafted as 국민신문고 but
   filed on 안전신문고), fix the {기관}/channel in both the filename and the header.
3. **Record submission-time observations in the LIVING block** (not the IMMUTABLE
   one): field truncation, photo-interval shortfalls, char count, anything that
   affects processing — each with the prepared next move. If the user later corrects
   a live field (e.g. fixes a truncated 차량번호), update the value and note the
   correction with its date; preserve the original defect in the living history.
4. Keep IMMUTABLE (verbatim submission) and LIVING (답변 · 대조 · Action, updated over
   time) strictly separated — see `references/anatomy.md` wrapper layout.

---

## Notes
- **Scope (v1):** 국민신문고 일반민원 + 고충민원, and 안전신문고 안전신고 (safety/enforcement
  reports — heed the "⚠️ 안전신문고 채널 주의" block in `anatomy.md`: ≈1,600자 cap, field
  truncation, photo-interval rules). For 문서24 공문 / 정보공개청구 / 행정심판, recommend
  the rung (Play 6) but say those documents are out of v1 scope.
- **Follow-ups:** if a prior reply was pasted, open with thanks + concede the
  settled points ("이미 확인되었으므로 재확인 불요") and narrow to the open 1–2 items.
- **Domain-general:** the terminology in the reference files is **illustration
  only**. Verify this domain's statutes and terms fresh every time (Pass 1).
- **Not legal advice — say so in delivery.** This skill drafts a document; it does
  not determine legal rights. Verified 조문 text does not guarantee the correct legal
  interpretation of it; an agency's answer may not be legally binding; and 처리기한/구제
  기간 must be independently confirmed for the specific matter. When you deliver, add a
  one-line reminder that the user should confirm load-bearing legal effect and
  deadlines before relying on them — especially before any 이의신청/행정심판 rung.
