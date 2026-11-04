# 01 — Humanizer / Anti-Slop Landscape

Research date 2026-11-04. `web_search` had no API key this session; all findings come from direct fetches (GitHub
REST, `raw.githubusercontent.com`, Wikipedia raw wikitext). Stars drift.

## 1. Local skill: `~/.dsh/skills/humanizer` (symlink → `blader/humanizer` v3.1.0, MIT)

One file, `SKILL.md`, 397 lines / ~31 KB / ~4,900 words. No build step; `scripts/validate-package.py` is a packaging
linter only.

| Layer | Contents |
|---|---|
| Frontmatter | `name`, one-sentence `description` (trigger surface), `license`, `metadata.version` |
| Rationale | 6 causes of AI texture (staging, rhythm-by-rule, inflation, formatting-by-rule, leftovers, wrong reader); claim that word habits decay per model release while structural habits persist |
| Procedure | mark tells → draft → check (read aloud, fact-diff) → write final |
| Voice | sample overrides every rule incl. the dash rule; genre decides warmth |
| Output modes | pasted / file / embedded |
| Patterns A–F | 26 numbered tells (lines 55–381) |
| When not to act | quotations, titles, pre-2022 text, human-voice details |
| Source | Wikipedia "Signs of AI writing" |

**Numbering and priority — the load-bearing decision.** Patterns 1–26, strongest first, in six groups: A staging
(1–5), B rhythm by rule (6–11), C inflation (12–18), D formatting (19–21), E chat leftovers (22–25), F wrong reader
(26). Rule: **§1–§5 justify an edit on one sighting**; anything marked *weak alone* (9, 10, 11, 21, 25) needs company
in the same passage. That is the main defence against over-editing. `AGENTS.md` keeps the order an invariant: numbers
gap-free, a new tell earns a number only if no existing pattern implies it; the validator derives the count from
headings and caps the file at 5,500 words.

**Entry format (all 26):** `### N. Name` → **Watch for:** literal phrase inventory → **Problem:** why the model does
it → **Before:** → **After:**. §8 uses **Rule:** instead. Many entries escalate by scale — phrase → sentence →
paragraph ("Challenges and Legacy" stock sections) → document (send-off paragraphs). That escalation, from the
Wikipedia page, is the most reusable idea in the file.

**"When not to act":** phrases inside quotations, titles, proper names, or text that *discusses* the phrase;
salutations; text written before 2022-11-30; plus the admission that human judges perform near chance, so several
tells together are the safeguard. A "keep these" list follows: specific odd detail, mixed feelings, dated references,
first-person choice, genuine aside.

**Output modes.** Pasted (default): remaining-pattern list + final rewrite. File mode: rewrite only, prose only,
code/paths/link targets untouched, then a short summary. Embedded (PR, commit, doc): final text only. **Voice:** a
sample overrides every rule incl. §8; without one, genre decides warmth — opinion genres keep hesitation and humour,
reference text stays neutral.

## 2. Repo inventory

| Repo | URL | ★ | Lang | Approach | File shape |
|---|---|---|---|---|---|
| blader/humanizer | https://github.com/blader/humanizer | 64.7k | EN | 26 numbered structural tells, rewrite prompt | 1 `SKILL.md` + plugin manifests + validator |
| hardikpandya/stop-slop | https://github.com/hardikpandya/stop-slop | 18.6k | EN | 8 rules + 3 refs + 1–10 self-score | `SKILL.md` (68 ln) + `references/{phrases,structures,examples}.md` |
| epoko77-ai/im-not-ai | https://github.com/epoko77-ai/im-not-ai | 6.4k | KO | Language taxonomy, severity, routing, over-edit gate | 4 skills + `docs/{taxonomy,evidence,integration}` + scripts |
| Nanako0129/sepia | https://github.com/Nanako0129/sepia | 3.6k | EN | Fiction narrative architecture, 3 passes, 4 operations | `SKILL.md` + `research/` + `evals/` + per-venue rules |
| AIScientists-Dev/academic-humanizer | https://github.com/AIScientists-Dev/academic-humanizer | 3.3k | EN | Domain: papers/grants, claims tied to evidence | skill + domain rules |
| MrGeDiao/shuorenhua | https://github.com/MrGeDiao/shuorenhua | 2.5k | ZH | Fact-preserving, scenario-split rewrite | skill + scripts |
| Aboudjem/humanizer-skill | https://github.com/Aboudjem/humanizer-skill | 301 | EN | 55 patterns, 5 voices, 0–100 score, CLI | `skills/humanizer/SKILL.md` + `cli/` + `docs/` |
| matsuikentaro1/humanizer_academic | https://github.com/matsuikentaro1/humanizer_academic | 297 | EN | Academic medical variant | skill + refs |
| Hyacehila/humanizer-zh-next | https://github.com/Hyacehila/humanizer-zh-next | 240 | ZH | blader fork retuned for Chinese | `SKILL.md` |
| iKora128/stop-ai-slop-jp | https://github.com/iKora128/stop-ai-slop-jp | 476 | JA | stop-slop + Japanese-specific layers | `SKILL.md` + 3 refs (52 KB) |
| eric-tramel/slop-guard | https://github.com/eric-tramel/slop-guard | 167 | EN | Deterministic linter, 24 rules/200+ heuristics, MCP | Python pkg + `benchmark/` |
| sam-paech/auto-antislop | https://github.com/sam-paech/auto-antislop | 207 | EN | **Decoder-level**: slop n-grams → preference set → FTPO fine-tune | Python pipeline, arXiv:2510.15061 |
| Wikipedia "Signs of AI writing" | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | — | EN | Descriptive field guide; upstream of most above | advice page, 14 sections |
| **bushrabeg/turkce-humanizer** | https://github.com/bushrabeg/turkce-humanizer | 97 | **TR** | 2 phases, 5 registers, 5 absolute bans, author-profile learning | `SKILL.md` + `docs/` + `examples/` |
| **genmedya/turkish-native-humanizer** | https://github.com/genmedya/turkish-native-humanizer | 0 | **TR** | 87 `K`-patterns, 3 axes + fidelity layer, TDK-aware | `SKILL.md` (330 ln) + `references/` + `scripts/` + `tests/` |
| durmazoguzhan/turkish-humanify · DevVettel/turkish-humanizer · RizgarOzan/turkce-humanizer · batuhan-bas/trilingua | — | 3–12 | TR | Thin single-file Turkish restatements of the blader list | `SKILL.md` each |

**Prior-art warning.** Turkish humanizers already exist (five above; one has 87 patterns and a register model). "From
scratch" must mean *architecturally*, not *first of its kind*. What is left to differentiate: severity + evidence
discipline, Turkish-grounded grammar rules, a runnable check. None of the Turkish repos ship a benchmark or a
rejected-rules file.

### Per-tool notes

**stop-slop (18.6k).** Main structural rival. Un-numbered by design: 8 imperative rules (cut filler, break formulaic
structures, active voice, be specific, put the reader in the room, vary rhythm, trust readers, cut quotables) →
12-item **Quick Checks** gate → 5-dimension self-score (Directness, Rhythm, Trust, Authenticity, Density), "below
35/50: revise". Detail sits in three lazily-loaded refs: `phrases.md` (throat-clearing, emphasis crutches, jargon,
adverbs, meta-commentary, vague declaratives), `structures.md` (binary contrasts, negative listing, dramatic
fragmentation, rhetorical setups, false agency, narrator-from-a-distance, rhythm, word patterns), `examples.md`.
*Better:* cheap always-loaded file; the score gives a stopping condition. *Worse:* no severity model, so nothing says
how many sightings justify an edit; the adverb ban flattens voice.

**im-not-ai (KO, 6.4k).** Most sophisticated architecture found, closest analogue for Turkish.
10 categories × 85 sub-patterns (71 published), each `ID | Sev | Trigger | Prescription | quick`.
**S1 critical** (one occurrence ≈ certain AI), **S2 high** (1–2 natural, 3+ AI → density-based removal), **S3 low**
(rhythm, only in combination). `quick: true` = surface-detectable, compiled into a ~50-rule single-call rulebook;
`quick: false` = document-level judgement, strict path only. A pre-scoring shim emits `route_hint`: light = 1 call,
can exit "this is already fine"; standard = 2; heavy = 3+ for dense slop or >15k chars. Four hard rules: meaning
immutable; only detected spans touched; genre preserved; **no over-editing — warn above 30% change rate, hard stop
above 50%**. Out-of-scope list (numbers, units, dates, proper nouns, quoted speech, statutory text, terms of art)
makes the gate auditable. Two things to steal outright: (1) **category A is translationese** — English syntax in
Korean morphology: forced pronouns, `~를 통해` for every *through/via*, double passives, left-branching relative clauses,
mechanical first/second/third scaffolding; (2) **they publish rejected rules** — "always redistribute `~를 통해`" was
killed because native Korean uses it twice as often as translated Korean, and a pronoun rule got a scope guard because
humans used `그는` more than AI did. Without that file a Turkish skill ships English intuitions as Turkish rules.

**sepia (3.6k).** Surface is the *last* layer. Cites StoryScope (61,608 stories): narrative structure alone detects AI
fiction at 93.2% macro-F1, and human surface rewriting moved detection only
95.5 → 93.9. Three passes (narrative → discourse flow → surface), four operations (write /
review-only / refactor-minimal / recreate), per-venue rules on one shared checklist. *Better:* only repo with an eval
harness and research ledger; "diagnose without editing" is a good product idea. *Worse:* fiction-specific, 30-feature
rubric too big to load per call.

**Smaller entries.** *Aboudjem/humanizer-skill* (301): 55 patterns, 5 voices, CLI scoring 0–100 from four *measurable*
signals (burstiness chief among them) rather than pattern counts — makes "vary rhythm" quantitative, but burstiness
becomes an end in itself and there is no severity model. *slop-guard* (167): purely deterministic, 24 configurable
rules over 200+ literal and structural heuristics, no LLM judge, score + band + violations, exposed as MCP — a good
pre-pass and regression check, useless as a rewriter since it cannot separate deliberate choice from tell.
*sam-paech/auto-antislop* (207): different paradigm — sample the model, find over-represented n-grams, build a
preference set, fine-tune against slop (FTPO). Not reusable in a prompt skill, but it justifies the *frequency* rule:
a phrase is a tell in proportion to how rarely a careful writer would produce it on purpose.

**Japanese stop-ai-slop-jp (476).** Best model for *adapting* rather than translating. Keeps the 8 rules but re-roots
them: the real cause is "absence of the writer" (主体の不在) — who claims what. Adds language-bound layers stop-slop lacks:
full-width dash `──` → colon or line break, `・` enumeration → `と`/`や`, katakana metaphor inflation (`思考のOSをアップデート` →
`考え方を変える`), no `「」` round ordinary adjectives, **propositional H2 headings** (`○○は△△だ` turns each section into a
mini-TED talk; use noun phrases). 52 KB of refs with before/after.

**Turkish prior art.** `bushrabeg/turkce-humanizer` v3.2: two phases (unconditional strip, then conditional rhythm
insertion), five registers (legal-administrative, academic-institutional, analytic-journalism, essay-blog, literary),
five absolute bans (em dash, semicolon, fragment, connector-initial isolated sentence, comma before contrastive
conjunction), and an author-profile step learning breath length from 2–3 samples. `genmedya/turkish-native-humanizer`
supersedes it: 87 patterns on **A machine signature** (punctuation inflation, monotone sentence length, `-mektedir`
epidemic, connector piles, empty praise, cliché closers, aphorism, copula avoidance), **B translation smell**
(imported subordinate-clause skeleton, wrong case suffix, generic verb, noun pile, database language, SaaS calque,
`bir` inflation), **C human rhythm** (no breath point, no self-correction, no conversational connector, no aspect
suffix), plus layer K59–K66 (register / fidelity / final check) above all three, and a divergence note from its
upstream on whether the five bans apply when *judging* someone else's text (they do not; TDK permits the semicolon).
The machine-vs-translation split is the right frame for Turkish and should be adopted.

## 3. Structural tells everyone agrees on

Structural = shape of the argument, not a word list; ranked by number of independent sources.

| # | Tell | Where it appears |
|---|---|---|
| 1 | Negative parallelism / not-X-but-Y | blader §1 (one sighting), stop-slop *Binary Contrasts* (10 variants), Wikipedia §3.3, Japanese rule 8, Korean C, Turkish K6 `sadece X değil`; also split across sentences, and as clipped negative tails |
| 2 | One-line closer / dramatic fragment | Paragraph restated as a pull-quote, repeat-closers after every section, row-of-fragments ("No aesthetic prior. No nostalgia.") |
| 3 | Forced triads | Threes whether or not meaning has three parts; paragraph-scale (three parallel examples + lesson) |
| 4 | Staged run-up | "Let's dive in", "Here's the thing", "Honestly?" — announcement substituting for claim |
| 5 | Arguing with no one | Refuting an objection that appears nowhere; fake alternatives ("a tempting approach would be…") |
| 6 | Inflation / borrowed authority | Ordinary fact dressed as pivotal or legacy; unnamed "experts say"; prestige outlet lists; send-offs ("the future looks bright") |
| 7 | Uniform rhythm | Metronomic sentence length, identical paragraph shapes, same closing beat — the one tell measurable without semantics |
| 8 | Formatting by rule | Bold label on every item, emoji/arrow decoration, heading capitalization, rule between sections, heading restated as first sentence |
| 9 | False agency / narrator-from-a-distance | Inanimate subject with human verb ("the decision emerges"); "people tend to…" with nobody in the room |
| 10 | Chat residue and hedging artifacts | "Great question!", cutoff disclaimers, stacked qualifiers, "it is worth noting" |
| 11 | Summary ending | Conclusion that repeats instead of adding; stock "challenges and outlook" sections |
| 12 | Document about itself | Describing method, sourcing reliability, or layout instead of subject |

Consensus on *why*: models choose what fits the widest audience, humans choose for one reader — blader states it,
Japanese restates it as "absence of the writer", sepia formalizes it as "self-announcing tidy shape". Every
architecture above trades *more rules* (recall) against *fewer, stricter rules* (precision).

### Universal vs English-bound

| Universal (structure) | English-bound (surface) |
|---|---|
| Negative parallelism 1 | Em dash as universal connector (US editorial habit) |
| One-line closer 2 | Title Case headings |
| Forced triads 3 | Curly/smart quotes |
| Staged run-up 4 | Hyphenated compounds after the noun (`the report is high-quality`) |
| Arguing with no one 5 | Copula avoidance via `serves as / stands as / boasts` |
| Inflated significance 6 | `-ing` riders (`highlighting, underscoring, reflecting`) |
| Uniform rhythm 7 | Wh- starters, "here's what/this/that" |
| Decoration 8 (bold, emoji, rules) | Stock vocabulary: delve, tapestry, testament, robust, pivotal |
| False agency 9 | Light verbs (`have/make/take + noun`) |
| Chat residue 10 | Passive with `by` agent |
| Summary ending 11 | `the/a` inflation and article placement |
| Document-about-itself 12 | Comma/semicolon conventions, quote nesting |

Rule of thumb: **1–6 and 9–12 survive translation** because they are argument shapes; the right column must be
re-derived per language, and several are actively wrong outside English.

## 4. What is missing for non-English — and what breaks in Turkish

**Gaps in every English repo:** no source-language axis (only im-not-ai and genmedya separate machine from translation
smell); no severity, hence no density threshold (only im-not-ai grades); no over-editing gate (only im-not-ai 30/50
and genmedya's fidelity layer); no published rejected rules (only im-not-ai); no benchmark (only sepia has any
harness, none for Turkish); register not first-class (only the two Turkish repos) — and in Turkish register *is*
grammar.

**Turkish breakpoints** (SOV, agglutinative, suffix-heavy, no articles, pro-drop, free word order, formal
`-mekte/-maktadır`):

1. **`-mektedir/-maktadır` is register, not a tell** — correct written-formal imperfective; legal and
   academic Turkish lives on it, so a blunt ban (one Turkish repo ships it) damages legitimate text.
   Defensible rule is **density**: 4+ per paragraph, or mixing it with colloquial `-ıyor` in one
   paragraph. Model: Korean A-2, suppress repetition not the form.
2. **The em-dash ban is an imported norm.** Turkish uses `—` sparingly; the local punctuation tells
   are the **semicolon bridge** (`;` joining clauses English-style), **comma before
   `ama/ancak/fakat/çünkü`** (wrong since TDK 2005), and parentheses-as-asides. genmedya's split is
   the right one: absolute in *generation*, guarded in *repair*.
3. **Article-less → the not-X-but-Y detector must change.** Formula maps to `X değil, Y`,
   `sadece/yalnızca X değil, aynı zamanda Y`, `X olmaktan çok Y` — but `değil` is ordinary negation
   and the copula `-DIr` ordinary formal assertion, so literal matching false-positives. Reliable
   signal: **contrast split across two sentences with a weight-only second half**.
4. **Agglutination → word lists useless, suffix rules matter.** "AI vocabulary" cannot be translated
   (`delve`, `tapestry` have no telling Turkish equivalent). What generalizes is suffix stacking:
   `-dığı belirtilen`, `-acağı düşünülen`, `-ması beklenen` chains — translationese's signature is
   the **left-branching participle chain** (`...olduğu ifade edilen raporda, ...edilmesi gerektiği
   vurgulandı`), the analogue of Korean A-18/A-19. Also agented passive `... tarafından yapılmıştır`
   (calque of *by*), double passive `yapılmakta olduğu`, and **`bir` inflation** for English `a/an`.
5. **Pro-drop.** Forced third-person `o/onlar` is a translationese tell — Korean A-16's shape, and it
   needs the **same scope guard**: translation contexts only, since native formal Turkish uses
   pronouns more than AI does. Copy the guard, not just the rule.
6. **Free word order changes the rhythm metric.** Devrik sentences, predicate-initial emphasis and
   topic-fronting are human markers. Word-count variance under-reads Turkish (fewer, longer words):
   **vary by syllables and by predicate-final vs predicate-initial position**, and check the
   distribution of sentence-final verbs (`-dır`, `-mıştır`, `-maktadır`, `-ıyor`).
7. **Converb-driven cohesion.** Turkish links with `-arak`, `-ıp`, `-ken`, `-dıkça`, not conjunctions.
   Sentence-initial `Ayrıca / Bununla birlikte / Bu bağlamda / Söz konusu` in sequence is the AI
   pattern; the fix is a converb or nothing, not a synonym.
8. **Formal vocabulary invisible to English lists.** Local equivalents of *crucial/robust/leverage* —
   `kritik bir rol oynamak`, `sağlam/etkin bir şekilde`, `katma değer`, `sinerji`, `holistik`,
   `paradigma`, `mercek altına almak`, `ışığında` — need a curated list with usage conditions.
9. **Genre conventions collide with the rules.** Academic and legal Turkish *requires* impersonal
   passive, `-mektedir`, formulaic openers; a skill treating these as tells fails its most likely
   professional users. Register gating is mandatory.
10. **Turkish-only correctness checks** no English repo can express: `de/da` and `ki` punctuation,
    apostrophe suffixes (`Türkiye'de`, `AI'ın` vs `AI'nın`) — what human editors notice first.

**Implication.** diagnose (deterministic pre-pass: suffix/connector/punctuation/rhythm metrics, no LLM) → route by
severity density (light/standard/heavy) → rewrite only detected spans, register- gated → over-edit gate (>30% warn,
>50% stop) → re-diagnose and report.

## 5. What to copy / what to avoid

**Copy:** severity S1/S2/S3 with *weak alone* semantics (cheapest precision control available); two-axis diagnosis
machine-vs-translation; register gating plus an explicit out-of-scope span list; over-edit gate with a published
change-rate metric; before/after escalated by scale plus a "keep this" list; three output modes; `references/` split
so the always-loaded file stays small; a rejected-rules/evidence note (cheapest credibility available); one
assert-based runnable check over a small Turkish corpus — fires on seeded tells, silent on a human control paragraph.

**Avoid:** translated English word lists; absolute bans on em dash / semicolon / passive / adverbs (density survives,
absolutes do not); un-numbered rule soup (fine at 68 lines, unusable at 60+ rules with differing severities); detector
evasion as a goal (blader: detectors still flag its output, and chasing them optimizes the wrong objective);
burstiness as a target number (collides with the SOV predicate-final norm); fiction architecture inside a general
skill; 5,000-word single-file prompts — Turkish needs more rules per unit of coverage, so budget references from day
one; shipping without a Turkish benchmark, since five thin Turkish repos already exist and evidence is the only
differentiator left.

## 6. Sources

Wikipedia "Signs of AI writing" — https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing · blader/humanizer (also
local, `~/.dsh/skills/humanizer`) — https://github.com/blader/humanizer · stop-slop —
https://github.com/hardikpandya/stop-slop · im-not-ai (KO) — https://github.com/epoko77-ai/im-not-ai · stop-ai-slop-jp
(JA) — https://github.com/iKora128/stop-ai-slop-jp · sepia (arXiv:2604.03136) — https://github.com/Nanako0129/sepia ·
Aboudjem — https://github.com/Aboudjem/humanizer-skill · slop-guard — https://github.com/eric-tramel/slop-guard ·
auto-antislop (arXiv:2510.15061) — https://github.com/sam-paech/auto-antislop · shuorenhua (ZH) —
https://github.com/MrGeDiao/shuorenhua · turkce-humanizer (TR) — https://github.com/bushrabeg/turkce-humanizer ·
turkish-native-humanizer (TR) — https://github.com/genmedya/turkish-native-humanizer
