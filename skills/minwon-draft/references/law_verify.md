# law_verify.md — verify every citation against law.go.kr before it goes in

**Principle (non-negotiable):** every 법령·조문 quoted in a 민원 is verified against
the live law.go.kr data for (a) exact wording and (b) 시행일자. Never quote a
statute from memory, a tracker summary, or web search. A wrong or stale citation
invites a rebuttal that discredits the whole filing.

This skill performs that verification through the **korean-law-mcp** connector,
which is bundled with this plugin (installed as an MCP server; see the repo README).
It wraps the 법제처(법령정보) Open API so the model can fetch in-force statute text,
행정규칙, and 판례 directly — no local Python client and no project checkout required.

> **Credit:** verification is powered by **korean-law-mcp** (MIT) —
> https://github.com/chrisryugj/korean-law-mcp. It needs a free 법제처 OpenAPI key
> (`LAW_OC`), which the plugin prompts for once at install (~1 min to get one at
> https://open.law.go.kr/LSO/openApi/guideList.do).

---

## How to verify (preferred — korean-law-mcp tools)

For each distinct 조/판례 you intend to cite, call the connector's tools:

- **`search_law "<법령명>"`** — confirm the law exists; read its **시행일자 / MST**
  (so you quote the in-force version, with 약칭·제명변경·시행예정 개정 flagged).
- **`get_law_text`** (by MST + 조, e.g. 제49조) — fetch the exact 조문 전문 to quote
  verbatim, with 항·호 and `<개정 …>` tags intact.
- **`legal_analysis` with `mode: verify_citations`** — hallucination check: confirms
  the 조문 exists **and** that the title you attached matches the real one
  (`[CONTENT_MISMATCH]` catches "제750조(계약해제)"-style content errors). Run this on
  the finished draft's citation set.
- **`search_admin_rule` / `get_admin_rule`** — for **행정규칙** (고시·훈령·예규·지침·기준).
  These ARE verifiable through the connector — a capability the raw 법령 API lacks.
  Health/welfare/safety work leans on 고시 constantly, so use these, don't skip.
- **`search_precedents` / `get_precedent_text`** — for 판례 citations.

Run one lookup per distinct 조 you cite. Quote the returned 조문본문 verbatim inside
`확인이 필요한 조항`, and put the 시행일자 in the 인용 검증표.

---

## Failure modes (all handled — a failed fetch must NEVER become a quote)

1. **Connector not installed / no LAW_OC key given at install.** The MCP tools are
   unavailable or return an auth error. **Do not block the draft.** Produce it with
   every unverified citation tagged `⚠️ 미검증 — 제출 전 재확인`, and tell the user in the
   delivery summary how to enable verification (README: one-line plugin install +
   free key). The draft is still useful; only the ✅ 검증 marks are withheld.
2. **조 number wrong / law not found.** `get_law_text` returns nothing or an error.
   Re-check the 조 number and the 법령명 (try `search_law` / `suggest_law_names` first).
   If still unresolved, verify by hand at https://www.law.go.kr or https://casenote.kr
   and mark the citation **"재검증 권장"**.
3. **행정규칙 not located.** Most 고시/훈령/예규 are reachable via `search_admin_rule`,
   but coverage varies. If a specific 고시 can't be pulled, verify at
   https://www.law.go.kr → **행정규칙 검색**, quote verbatim by hand, and mark
   **"행정규칙 — 수기 검증 (YYYY-MM-DD, 시행 …)"**.

If law.go.kr is unreachable entirely, produce the draft and tag every citation
`⚠️ 미검증` — say so plainly in the delivery summary.

---

## Terminology self-check (verify per domain — do NOT hardcode)

Domain-specific terminology should be *discovered by verification*, not assumed.
Ministries get renamed, articles get amended, and near-synonyms carry different
legal weight. Treat the following only as **reminders of the failure class**, then
run the same check for whatever domain the current 민원 is in:

- **Ministry renames change the 소관부처.** e.g. 미래창조과학부 → 과학기술정보통신부 (2017),
  안전행정부 → 행정자치부 → 행정안전부. `search_law` returns the *current* 소관부처 — trust
  it over any older summary or your own memory.
- **위임 vs 위탁** are legally distinct (내부 위임 vs 외부 위탁) and change who actually
  decides. Do not treat them as interchangeable, and never "correct" a correctly-used
  민법 `위임`/`위임장`/`위임청구` to 위탁.
- The `<개정 YYYY.M.D>` tag in a 조문 tells you when the clause last changed; if it is
  newer than the summary you were working from, trust the API, not the summary.

Before you commit a term or an article number, the live law.go.kr data (via the
connector) is the authority — tracker summaries and memory are not.
