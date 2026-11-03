# Quality Gate: Creative Direction & Narrative (`cd-narrative.md`)
# Gate ID: GATE-01-CD-NARRATIVE

## 1. Purpose
The `cd-narrative` gate ensures that narrative design, dialogue writing, and world lore conform to strict studio quality standards before any voice recording, cutscene rendering, or game-engine implementation begins.

---

## 2. Hard Gate Requirements (Pass/Fail)

| Check ID | Requirement | Validation Method | Hard Limit |
|---|---|---|---|
| **CD-N01** | Dialogue Character Ceiling | Automated regex/linter | `<= 120 characters` per subtitle/speech line |
| **CD-N02** | Lore Classification | Manual & semantic audit | Every lore entry marked as `[Established]`, `[Provisional]`, or `[Under Review]` |
| **CD-N03** | Subtext Verification | Narrative Director review | Zero on-the-nose exposition; character intentions veiled through action |
| **CD-N04** | Conlang Consistency | Phonology & Glossary check | Vocabulary strictly follows defined phonotactic rules and root tables |
| **CD-N05** | No AI Slop Check | Slop-detector script | Rejection of generic fantasy clichés and purple prose |

---

## 3. Checklist for Sub-Agents (`@game-writer` / `@narrative-director`)

- [ ] All dialogues formatted as atomic units with speaker tag, emotional stage direction, and text `<= 120 chars`.
- [ ] No lore contradictions against previously committed `[Established]` world truths in `.claude/memory-system.md`.
- [ ] Conlang terms include phonetic pronunciation guide (IPA or phonetic respelling) for `@audio-narrative-engineer`.
- [ ] Interactive branching points provide genuine agency (minimum 2 diverging narrative states or consequences).

---

## 4. Gate Sign-Off Protocol
```markdown
### Gate Clearance Record
- **Date:** YYYY-MM-DD
- **Target Feature:** F0X: Narrative Arc Name
- **Auditor:** @narrative-director
- **Status:** [PASSED / REJECTED]
- **Notes:** All dialogue chunks validated below 120 characters. Ready for voice synthesis.
```
