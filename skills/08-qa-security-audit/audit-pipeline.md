# QA, Security Audit & Anti-Slop Filter (`audit-pipeline.md`)
# Integrations: strix (security audit), no-ai-slop (filter), skillspector (compliance)
# Sub-Agent Domain: @qa-auditor

## 1. Overview
The QA pipeline acts as the final perimeter defense before code, assets, or scripts merge into the repository. It performs automated security analysis on engine scripts, detects generic AI slop, and guarantees skill specification compliance.

---

## 2. Strix Security Vulnerability Auditing

`strix` evaluates Godot GDScript and Unity C# code for critical security flaws:

| Vulnerability Type | Threat Vector | Prevention Standard |
|---|---|---|
| **Arbitrary Deserialization** | `bytes_to_var()` or untrusted JSON saves | Strict schema validation before parsing; ban arbitrary object deserialization |
| **Multiplayer Packet Spoofing** | Client-authoritative damage or movement | Server-authoritative physics simulation; client sends inputs only |
| **Path Traversal** | Dynamic mod/asset loading from disk | Sanitize file paths using whitelisted base directories only |

---

## 3. The `no-ai-slop` Filtration Engine

The anti-slop engine runs heuristic and semantic pattern matching against narrative and design documents:

### Slop Heuristic Rules:
1. **Adjective Stacking:** Rejects sequences of 3+ consecutive emotive adjectives (e.g. *"dark, mysterious, unfathomable abyss"*).
2. **Generic Filler Vocabulary:** Triggers warnings on words: *tapestry, testament, echo, beacon, symphony, dance of shadows*.
3. **Empty Mechanics:** Flags design sentences that describe feeling without a quantifiable metric (e.g. *"The combat feels fluid and engaging"* -> REJECT; *"The recovery animation takes 12 frames with 4 active hitbox frames"* -> PASS).

---

## 4. Skillspector Compliance Checklist
- [ ] Every markdown skill contains a defined metadata header with `Sub-Agent Domain`.
- [ ] Code examples are syntactically valid (GDScript, Python, TypeScript).
- [ ] All cross-skill references point to existing markdown paths.
- [ ] Director gates (`cd-narrative`, `ql-story-ready`) have explicit pass/fail matrices.
