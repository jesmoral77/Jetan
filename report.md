# Designing and Evaluating Jetan Agents

**Student:** [Name]<br>
**Private repository:** [URL]<br>
**Access:** [Confirm `fractal13` has read access]<br>
**Submitted commit:** [Hash]

## 1. Deterministic Evaluation Functions

### Reading-Based Design Principles

[Cite at least one assigned paper. Explain the principles you used and one
principle you did not adopt.]

### Evaluation 1

**Definition:** [Precise reproducible definition]<br>
**Information used and intentionally ignored:** [ ]<br>
**Scaling/range:** [ ]<br>
**Expected relationship to utility:** [ ]<br>
**Computational cost:** [ ]<br>
**Known weakness:** [ ]

### Evaluation 2 and Motivation

**Definition:** [Precise reproducible definition]<br>
**Information used and intentionally ignored:** [ ]<br>
**Scaling/range:** [ ]<br>
**Expected relationship to utility:** [ ]<br>
**Computational cost:** [ ]<br>
**Known weakness:** [ ]<br>
**Revision evidence:** [Exact changes from Evaluation 1 and the evidence or
failure that motivated them]

### Evaluation 3 and Motivation

**Definition:** [Precise reproducible definition]<br>
**Information used and intentionally ignored:** [ ]<br>
**Scaling/range:** [ ]<br>
**Expected relationship to utility:** [ ]<br>
**Computational cost:** [ ]<br>
**Known weakness:** [ ]<br>
**Revision evidence:** [Exact changes from Evaluation 2 and the evidence or
failure that motivated them]

### Hand-Checked Positions and Tests

| Position | Perspective | Eval 1 | Eval 2 | Eval 3 | Why these values are reasonable |
|---|---|---:|---:|---:|---|
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

## 2. LLM Cutoff Evaluator

**Exact model tag:** [ ]<br>
**Endpoint category:** [Do not record API-key values]<br>
**Temperature:** [ ]<br>
**Requested seed and observed reproducibility:** [ ]<br>
**Deterministic fallback evaluator:** [ ]

### Prompt and Response Contract

[Provide the exact final prompt or a complete appendix reference. Explain the
`{"score": NUMBER}` schema, strict parsing, duplicate-key rejection, finite
range, perspective, and fallback.]

### Prompt Revision

| Version | Representative response and limitation | Exact change | Evidence after change |
|---|---|---|---|
| Initial | [ ] | [ ] | [ ] |
| Revised | [ ] | [ ] | [ ] |

## 3. Direct LLM Move Agent

### Prompt, Sensors, and Response Contract

[Provide the exact final prompt or appendix reference. Explain board, legal
moves, escape state, recent history, `{"move": "..."}`, validation, and the
deterministic legal fallback.]

### Prompt Revision

| Version | Representative response and limitation | Exact change | Evidence after change |
|---|---|---|---|
| Initial | [ ] | [ ] | [ ] |
| Revised | [ ] | [ ] | [ ] |

## 4. Stage A: Deterministic Evaluator and Depth Development

### Stage A1: Evaluation Functions

**Depth:** 1<br>
**Opponent:** supplied random agent<br>
**Seeds:** 0, 1<br>
**Colors:** both<br>
**Maximum plies:** 100<br>
**Other command/configuration details:** [ ]<br>
**Depth verification from `maximum_depth`:** [ ]

For every table below, “Mean think time” means the focal tested agent's
color-specific cumulative time: `orange_time` when it is Orange and `black_time`
when it is Black. Retain all scheduled attempts. Mark unavailable metrics as
`N/A`, never as zero, and state the contributing attempt count for every mean.

| Agent | Games | W | D | L | Mean utility | Mean plies | Mean think time | Mean generated actions | Mean evaluated states | Failures |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `minimax_1` | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| `minimax_2` | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| `minimax_3` | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

### Provisional Evaluator Selection

[Name the selected evaluator. Justify selection using utility first, then
resource evidence and representative decisions.]

### Stage A2: Depths 1 and 2

**Selected evaluator:** [ ]<br>
**Opponent:** supplied random agent<br>
**Seeds:** 0, 1<br>
**Colors:** both<br>
**Maximum plies:** 100<br>
**Depth verification from `maximum_depth`:** [ ]

| Depth | Games | W | D | L | Mean utility | Mean plies | Mean think time | Mean generated actions | Mean evaluated states | Failures |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2 | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

Reuse the selected evaluator's depth-1 results from Stage A1. Describe one
position or match segment in which depth changed the selected move or backed-up
value. Explain the effectiveness and decision-cost tradeoff.

### Final Deterministic Configuration

**Evaluator:** [ ]<br>
**Depth (`1` or `2`):** [ ]<br>
**Selection justification using the supplied performance priorities:** [ ]

## 5. Stage B: Final Modality Comparison

**Seeds:** 0, 1<br>
**Colors:** both<br>
**Maximum plies:** 60<br>
**Cumulative think-time limit per player:** 3600 seconds or documented override<br>
**Selected deterministic depth:** [1 or 2]<br>
**LLM cutoff-evaluator depth:** 1<br>
**LLM-evaluator request limit:** 100 per move search<br>
**Commands and machine/runtime context:** [ ]<br>
**Depth verification from `maximum_depth`:** [ ]

| Agent | Depth | Games | W | D | L | Mean utility | Mean plies | Mean think time | Mean generated actions | Mean evaluated states | Termination reasons/failures |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Selected deterministic minimax | [1 or 2] | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| LLM cutoff evaluator | 1 | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Direct LLM move agent | N/A | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | N/A | N/A | [ ] |

| Mean per-match LLM metric | Cutoff evaluator | Direct move agent | Denominator |
|---|---:|---:|---|
| Model calls | [ ] | [ ] | All 4 matches |
| Fallback calls | [ ] | [ ] | All 4 matches |
| Cache hits | [ ] | N/A | All 4 matches |

For each prompt revision, show at least one representative rejected response if
one occurred and identify its validation category. Exhaustive rejection-category
counts are not required because the starter exposes aggregate fallback counts.

Retain every match and failure. Cite the generated summary denominator fields
and explain unavailable metrics. Explain that the two LLM modalities do not
receive equal model-call budgets or perform equivalent work. Also account for
any depth difference between the selected deterministic agent and the depth-1
LLM cutoff evaluator.

## 6. Stage C: Deterministic Versus Direct LLM

**Deterministic evaluator:** [ ]<br>
**Deterministic depth:** [1 or 2]<br>
**Direct LLM prompt version:** [Final revised version selected before Stage C]<br>
**Model seeds:** 0, 1<br>
**Colors:** both<br>
**Maximum plies:** 60<br>
**Cumulative think-time limit per player:** 3600 seconds or documented override<br>
**Depth verification from `maximum_depth`:** [ ]<br>
**Commands and machine/runtime context:** [ ]<br>
**Seed/color configuration evidence:** [Reference the four Stage C CSV rows and
confirm that the deterministic agent does not use its configured seed]

| Direct LLM color | Model seed | Deterministic utility | Direct LLM utility | Plies | Termination reason/failure |
|---|---:|---:|---:|---:|---|
| Orange | 0 | [ ] | [ ] | [ ] | [ ] |
| Orange | 1 | [ ] | [ ] | [ ] | [ ] |
| Black | 0 | [ ] | [ ] | [ ] | [ ] |
| Black | 1 | [ ] | [ ] | [ ] | [ ] |

Record each utility from the named agent's perspective: `+1` for that agent's
win, `0` for a draw, and `-1` for that agent's loss. Compute each aggregate W/D/L
record and mean utility from the perspective of the agent named in that row.

| Agent | Games | W | D | L | Mean utility | Mean own-agent think time | Mean generated actions | Mean evaluated states | Mean model calls | Mean fallback calls |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Selected deterministic minimax | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | N/A | N/A |
| Final direct LLM | 4 | [ ] | [ ] | [ ] | [ ] | [ ] | N/A | N/A | [ ] | [ ] |

Use each agent's color-specific time. Mark unavailable values as `N/A` and
cite the generated denominator for each mean. Explain one position or match
segment that helps account for the head-to-head result. Limit conclusions to
this pairing, these seeds, and these match conditions.

## 7. Analysis Questions

1. [Which deterministic evaluator and depth produced the strongest evidence of
   effective play? Explain revision and depth effects using utility, variation
   across seeds and colors, decisions, thinking time, generated actions, and
   evaluated states.]
2. [How did the two prompt revisions and fallback policies affect validity,
   reliability, and interpretation of LLM utility?]
3. [What does Stage B show about the three modalities against random? Account
   for the distribution across seeds and colors, strategic disagreements,
   unequal depth, and model-call patterns.]
4. [What does Stage C show, and which claims remain limited by the pairing,
   seed, colors, move limit, or number of matches?]
5. [Using the supplied PEAS performance measure, which criteria were measured
   adequately, and what further evidence is needed?]

## 8. Testing and Reproducibility

**Test command/result:** [ ]<br>
**Offline/live separation:** [ ]<br>
**Registered agent names confirmed:** [ ]

[Summarize evaluator, parser, validation, fallback, budget, and scripted-client
tests.]

## 9. AI-Assistance Disclosure

**Tools:** [Names or `No AI assistance used`]<br>
**Material effect:** [ ]<br>
**Verification:** [ ]

## Submission Checklist

- [ ] Accessible `lastname-firstname-jetan-agents.pdf` with selectable text and
      semantic headings/tables.
- [ ] Three deterministic evaluation functions, depth comparison, and Stage A
      results.
- [ ] Initial and revised prompts for both LLM modalities.
- [ ] Complete Stage B results, failures, and summary denominator fields.
- [ ] Complete Stage C head-to-head results and bounded interpretation.
- [ ] Five analysis questions answered from evidence.
- [ ] Raw and summary CSV files for Stages A1, A2, B, and C retained in the
      repository.
- [ ] Private repository URL, submitted commit, and `fractal13` read access.
- [ ] Tests pass; `.env`, credentials, and secrets are absent from the repository.
- [ ] References and AI-assistance disclosure are complete.
