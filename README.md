# minwon-draft

A [Claude Code](https://claude.com/claude-code) skill that turns raw facts into
**copy-paste-ready Korean government e-petition content** — 국민신문고 민원 and
안전신문고 안전신고.

You paste the facts (an issue, an agency, some statutes, maybe a prior agency
reply); it returns a submission-ready **제목** and plain-text **내용**, plus the
recommended 민원종류/기관/channel, a statute-citation table, and a response-contingency
plan for every way the agency might answer.

It is built around a specific, repeatable method:

- **6-section assert-then-confirm structure** — state the favorable conclusion as
  your understanding and ask the office only to confirm it, so every answer
  (including a refusal) comes back citable and usable.
- **Live statute verification** — every 조문 you quote is checked against the live
  law.go.kr data via the [korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp)
  connector, with 시행일자, so you never quote a stale or hallucinated article.
- **Adversarial self-review** — the draft is red-teamed against a skeptical
  front-line clerk's incentives before it is delivered.
- **안전신문고-aware** — respects the portal's ~1,600-character 내용 cap, silent field
  truncation, and photo-interval rules for auto-과태료 enforcement reports.

> The method is **domain-general**. The bundled examples (a payments-clearance
> question, an anti-discrimination query, a traffic-safety report) are illustrations
> only — the skill verifies every statute and term fresh for whatever your 민원 is
> about.

---

## Install

Requires Claude Code.

```
/plugin marketplace add pon00050/minwon-draft
/plugin install minwon-draft@minwon-draft-marketplace
```

During install you'll be asked for a **법제처 Open API key (`LAW_OC`)**. This is
what powers live statute verification. It is **free and takes about a minute**:

1. Go to <https://open.law.go.kr/LSO/openApi/guideList.do>
2. Sign up / log in, then request **"Open API 사용 신청"**
3. You'll be issued an 인증키(OC) — paste it into the install prompt.

The key is stored as a sensitive value and used only to call law.go.kr through the
bundled `korean-law-mcp` server.

### No key? It still works.

You can leave the key blank. The skill will still draft the full petition — it just
tags each statute citation `⚠️ 미검증 — 제출 전 재확인` for you to verify by hand at
<https://www.law.go.kr> before submitting. Add the key later to turn on automatic
verification.

---

## Use

Ask Claude Code in natural language, or invoke the skill directly:

```
/minwon-draft:minwon-draft <paste your facts here>
```

Examples of what triggers it:

- "불법주정차 신고 내용 좀 써줘 — 우리 집 앞 소화전에 계속 주차하는 차가 있어"
- "이 사실관계로 국민신문고 민원 초안 만들어줘: …"
- "○○부 고시 해석을 물어보는 질의를 쓰고 싶어"

It walks through intake → citation verification → drafting → adversarial review →
delivery, and offers to save an archival record you can complete once you have the
접수 확인번호.

**Scope (v1):** 국민신문고 일반민원 + 고충민원, and 안전신문고 안전신고. For 문서24 공문,
정보공개청구, and 행정심판, it recommends the right next step but does not draft those
documents.

---

## How verification works

Verification is delegated to **[korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp)**
(MIT), a mature MCP server wrapping the 법제처 국가법령정보 Open API. This plugin
declares it as a bundled MCP server, so installing the plugin also wires up the
connector — no separate setup beyond the free key.

The skill uses it to:

- confirm a law exists and fetch its **시행일자 / MST** (`search_law`),
- pull exact 조문 전문 to quote verbatim (`get_law_text`),
- run a hallucination check that catches wrong article titles (`legal_analysis`,
  `mode: verify_citations`),
- verify **행정규칙** — 고시·훈령·예규 (`search_admin_rule` / `get_admin_rule`),
- verify 판례 (`search_precedents` / `get_precedent_text`).

If you already run `korean-law-mcp` as your own connector, that works too — the
skill just calls whatever `korean-law` tools are available.

---

## Privacy

- Your `LAW_OC` key is stored locally by Claude Code as a sensitive value; it is
  never committed to this repo.
- Draft petitions and saved records stay on your machine. The `.gitignore` keeps
  `국민신문고/` records and `.env` files out of version control by default.

---

## Credits & license

- Skill and method: MIT License (see [LICENSE](LICENSE)).
- Statute verification: **[korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp)**
  by Chris (MIT) — please star their project; this skill relies on it.
- Statute data: 법제처 국가법령정보 (law.go.kr) Open API.
