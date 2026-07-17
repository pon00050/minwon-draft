# anatomy.md — the document skeleton, title, channel, and wrapper

## CRITICAL: the submission payload is PLAIN TEXT

국민신문고's 내용 field is a plain textarea. The section headers below are emitted
as **bare text lines, not markdown** (no `#`, no `**`). If you output `## 질의 사항`
it pastes literally. Reserve markdown only for the optional archival `.md` wrapper.

---

## The 6-단 body skeleton (copy-paste payload)

Order never inverts: greeting → who I am + what this is → facts → the clause at
issue → numbered questions → cited law → written-reply request → thanks.

```
안녕하십니까.

저는 [신청인 지위: "…한 시민입니다" / "…을 준비 중인 예비 창업자입니다" / "…이용자입니다"].
[민원 성격 프레이밍 한 문장: "본 민원은 A(개인 구제/특정 업소 처벌)가 아니라
 B(정책 질의/문언 해석)입니다." — 시비조를 초반에 한 번, 확고하게 차단]

신청인 현황                     ← 또는  사실관계  /  【현황】
[콜론-라벨 key:value 줄들, 또는 번호매김 사실(1. 2. 3.), 또는 비교 표.
 날짜·수치·조항은 항상 구체·절대값. "최근에" 금지 → "2026-06-13".]

확인이 필요한 조항
본 [법령/고시] [조항]:
"[law.go.kr로 검증한 조문 verbatim — 따옴표]"
[쟁점 조문마다 반복. 필요하면 취지(입법 목적)를 한 줄 덧붙여 해석을 고정한다.]
상기 조항의 적용 방법과 관련하여 다음을 확인하고자 합니다.

질의 사항
[〔우선순위 그룹명 — 가장 직접적 경로 먼저〕   ← 선택]
【질문 1】 [결론 진술]…로 이해됩니다. 이 이해가 맞습니까?
   (근거 1~2문장. 상대의 예상 반론을 질문 안에서 미리 차단.)
   [만약 이해와 다르다면 그 법적 근거를, 명문 규정이 없어 내부 기준으로
    운용된다면 그 기준을 함께 안내하여 주시기 바랍니다.]
【질문 2】 …
   (가)/(나)/(다) 하위질문 … ← 선택 (객관식으로 유리한 선택지를 제시하면 답이 쉬워짐)
【질문 N (마지막)】 본 사안이 귀 부서 소관이 아닐 경우, 관련 부서로 이송하여 주시기 바랍니다.

관련 법령
[법령/고시 조항: 요지]        ← 한 줄에 하나, 또는 (법령|조항|내용) 3열 표
[실체 조문 + 절차 조문을 함께 나열해 회피 프레임을 닫는다:
 행정절차법 §23①, 민원처리법 §9·§16·§18 등]

회신 요청
각 질문에 대해 근거 법령·조항을 포함한 서면 회신을 요청드립니다.
[각 질문의 결론을 먼저 명시하여 회신해 주시면 이해에 도움이 되겠습니다.]
[본 질의는 문언 해석에 관한 것으로, 개별 사안 심사(…위탁)와 구별됩니다.]
[소관이 아닌 사항은 관련 부서로 이송 처리하여 주시기 바랍니다.]

[선택: 짧은 인간적/공익적 클로징 1문단 — 어조를 부드럽게, 문장은 약하게 하지 않는다.]

감사합니다.
```

Typical question count: **3–6**. Not every 민원 names all of 신청인 현황 /
확인이 필요한 조항 as separate blocks — a short policy query folds facts into flowing
paragraphs and jumps to 【질문 N】 — but the ordering never reorders.

---

## 제목 (title) pattern

`{대상 제도/법령}({근거 고시·조항 or 수치}) {핵심 쟁점} {행위명 요청} [({선행 민원번호} 후속)]`

The governing anchor goes in parentheses right after the subject; the ask is a
terminal verb-noun that classifies it. Long and fully self-describing — no vague
words. Illustrative examples (fictional — build your own from the current facts):
- `전동킥보드 공유 서비스의 이용요금 정산 구조에 대한 전자금융거래법 적용 여부 확인 요청`
- `주차장 설치기준(○○부 고시 제20XX-XXX호) 예외 항목의 적용 범위 확인 요청 (선행 민원 1AA-XXXX-XXXXXXX 후속)`
- `장애인 보조견 동반 출입 제한의 차별행위 해당 여부 및 향후 제도적 보호 방향 질의`

Terminal verb-noun options: `확인 요청` · `해석 요청` · `여부 확인 요청` · `관련 문의` ·
`이의 민원` · `해당 여부 … 질의`. Follow-ups carry the prior 신청번호.

---

## 민원종류 / channel chooser

| Situation | 민원종류 | Portal | Target |
|---|---|---|---|
| Interpret a statute/고시, get a citable ruling, clearance, or fact | **일반민원** | 국민신문고 | the 소관 부서 (drafting office) |
| Report a physical safety hazard / 불법주정차 / 시설물 결함 / 교통·자동차 위반 for enforcement | **안전신고** | **안전신문고 (safetyreport.go.kr)** | the 관할 지자체 (auto-routed). 6대 불법주정차(횡단보도·교차로모퉁이·버스정류소·소화전·어린이보호구역·인도)는 계도 없이 과태료 대상 — **⚠️ 아래 채널 주의 필독** |
| Agency error / procedural violation / policy-fix recommendation, no disposition to contest | **고충민원** | 국민신문고 (→ 국민권익위) | 권익위, numbered-paragraph form (본문 1–7 + 요청 사항 첫째/둘째/셋째) |
| Need binding legal weight (written 공문) | *(recommend)* 문서24 공문 | — | out of v1 scope; recommend as next rung |
| Need internal review materials as evidence | *(recommend)* 정보공개청구 | open.go.kr | out of v1 scope; recommend as next rung |

If jurisdiction is ambiguous, recommend **parallel filing** to two agencies
(소관 부서 + the 위탁 실무기관), so a punt on one is covered by the other. For an
enforcement report, 안전신문고 (fast, auto-과태료) and 국민신문고 일반민원 to the
지자체 (citable 조문 answer) are natural parallel channels.

### ⚠️ 안전신문고 채널 주의

If the 민원 is a safety/enforcement report headed for **안전신문고**, three hard
constraints bite in practice — bake them into the draft, don't discover them at
the paste box:

1. **내용 글자수 한도 ≈ 1,600자 (hard cap).** This is far tighter than 국민신문고.
   A full 6-단 draft can blow past it (~1,597/1,600 → has to be rewritten). **Measure
   the char count and target ≤ 1,400자 for headroom** (see SKILL.md Pass 4 char-budget
   step). Compress verbatim 조문 quotes to their operative phrase; fold the framing
   disclaimer and human closing into one sentence each; cap 질의 at 3–4.
2. **Auxiliary structured fields truncate silently.** 안전신문고 has separate short
   inputs (차량번호, 발생일시, 위반장소). The 차량번호 field can drop the last character
   (e.g. `서울00가1234` → `서울00가123`). **Always restate the full identifier (전체 번호판
   등) inside the 내용 body**, so a truncated field can't lose it.
3. **Photo-evidence rules gate the auto-과태료.** For 6대 주민신고 items (횡단보도 등),
   most 지자체 require **2매 taken a set interval apart (통상 1분 이상)** and prefer
   **앱 현장촬영본**(촬영시각 자동각인). Same-second or gallery-uploaded ("G") photos may
   drop the report from auto-과태료 to a plain 계도/현장단속 lane. **Surface this
   requirement to the user before they shoot**, and note it in the record.

Also **emit the structured field values separately** (차량번호 / 발생일시 / 위반장소)
in Pass 4, not only the 내용 blob — 안전신문고 asks for them as discrete inputs.

#### Pre-shoot evidence checklist (give the user BEFORE they photograph)

Evidence defects are the one thing that can't be fixed after the fact — a report
already filed with same-second gallery photos can't retroactively meet the interval
rule. So when the report is photo-based and *not yet shot* (or re-shootable),
surface this first:

- [ ] **2매 이상, 촬영 간격 통상 1분 이상** (지자체별 상이 — 30초·1분·2분). 자동 과태료의 핵심 요건.
- [ ] **안전신문고 앱 현장촬영**(촬영시각·GPS 자동각인)이 갤러리 업로드("G")보다 강함.
- [ ] **번호판이 판독 가능**한 프레임 1매 + **위반 정황(횡단보도·보도·소화전 등 위치)**이 보이는 프레임 1매.
- [ ] **이동 전/후**를 담아 "계속 주차" 상태임을 입증(정차 5분 이내 vs 주차 구분).
- [ ] 촬영 즉시 신고(현장성) — 시간·장소가 어긋나면 처리기관이 반려할 수 있음.

If the photos already exist and fail this (e.g. taken ~5초 apart and gallery-uploaded
"G"), say so plainly, file anyway as a 일반 신고, and record that auto-과태료 may not
trigger — with the re-shoot path in 다음 단계.

---

## Optional archival wrapper (`.md` for the user's records — NOT the payload)

Offer to save this after delivery. Markdown here is fine. PII (신청 정보) is
captured by the user from the confirmation screen post-submission — leave
placeholders; do not invent it.

```markdown
<!-- ⚠️ IMMUTABLE RECORD — DO NOT MODIFY (신청 정보 ~ 처리기관 정보) -->
# 국민신문고 민원 접수 확인 — {신청번호 (제출 후 기입)}
> **분류:** {개인/사업} 민원 · {주제}
> **선행 민원:** {있으면 [[…]]}

## 민원 신청 내용
| 민원종류 | {일반민원(일반 민원) / 고충민원} |
| 제목 | {제목} |

### 내용 — 제출본 verbatim
{the plain-text body, exactly as submitted}

## 첨부 파일
- {파일명 또는 "없음"}

## 처리기관 정보
| 처리기관 | {부처 (실과)} |
<!-- IMMUTABLE RECORD 끝 -->

## 답변 내용
⏳ 답변 대기 중 — 수령 시 verbatim 추가.

## 응답 시 Action
| 답변 | 후속 행동 |
| {favorable} | {cite → next act} |
| {evasive/punt} | {re-send to other agency / 종합검토 통로 probe} |
| {unfavorable} | {declare 교착, pivot to fallback / escalate a rung} |
| {silence past 처리기한} | {민원처리법 §18 → 국민권익위 고충민원} |

**문서 생성:** {날짜}  **상태:** ⏳ 접수 대기
```

Naming convention: `{민원번호}_{기관}_{주제}_{YYYYMMDD}.md` once an ID is assigned;
save under the current project's 국민신문고/ folder if one exists, else ask where.
