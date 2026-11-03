# Narrative & Worldbuilding Rules (`narrative-rules.md`)
# Sub-Agent Domain: @game-writer / @narrative-director

## 1. The 120-Character Dialogue Rule
In modern game UI, player retention drops when walls of text appear on screen. Subtitles, dialogue bubbles, and radio barks must deliver emotional impact with radical economy of language.

- **Hard Limit:** Maximum 120 characters (including spaces and punctuation) per spoken chunk.
- **Rule of Punch:** One thought or emotion per bubble.
- **Formatting Standard:**
  ```markdown
  [CharacterID] (Stage Direction): "Dialogue line here with punch and subtext." [<= 120 chars]
  ```

### Good vs. Bad Examples:
- ❌ **Bad (Expository Slop, 178 chars):**
  > "As you know, ever since the Sun-Shatter destroyed our capital three hundred years ago, we have been forced to scavenge for obsidian batteries in these dangerous ruined caverns."
- ✅ **Good (Atomic, Punchy, Subtextual, 78 chars):**
  > "Keep your boots out of the black water. The batteries leak when they crack."

---

## 2. The Lore Tier System
To prevent narrative debt and conflicting canon, every piece of world lore is categorized into three strict tiers:

### Tier 1: `[Established]`
- **Definition:** Immutable, verified, production-locked canon.
- **Rules:** Cannot be altered without an executive director override. All mechanics, dialogues, and visual assets must align with this tier.

### Tier 2: `[Provisional]`
- **Definition:** Active working hypothesis during feature development.
- **Rules:** Usable by artists and designers for prototyping, but subject to revision before passing the `cd-narrative` gate.

### Tier 3: `[Under Review]`
- **Definition:** Flagged for inconsistency, ludonarrative dissonance, or tonal drift.
- **Rules:** Frozen from active production until resolved by `@narrative-director`.

---

## 3. Sensory Grounding & Anti-Slop Directive
- Ground every description in tactile, physical reality: grease, cold stone, ozone smell, iron weight.
- Banished Words: "ancient mystery", "unfathomable darkness", "destined hero", "boundless power", "epic journey".
- Replace adjectives with verifiable mechanics and visual cues.
