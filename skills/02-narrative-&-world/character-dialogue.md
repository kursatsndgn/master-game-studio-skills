# Character Dialogue & Subtext Engine (`character-dialogue.md`)
# Sub-Agent Domain: @game-writer

## 1. Character Voice Architecture
Every NPC and playable protagonist has an individual **Voice Profile Matrix**:

```yaml
character_profile:
  id: "NPC_VARRO"
  name: "Varro the Smelter"
  origin: "Lower Khor Foundry"
  lore_tier: "[Established]"
  
  voice_parameters:
    vocabulary_tier: "Technical / Pragmatic"
    syntax_tempo: "Staccato, short clauses"
    catchphrases: [] # Strictly forbidden (avoids cartoonish clichés)
    vocal_subtext: "Hiding lung sickness caused by sulfur vapors"
    
  dialogue_constraints:
    max_char_count: 120
    preferred_verbs: ["weld", "crack", "drain", "cool", "weigh"]
```

---

## 2. The 3-Tier Subtext Analyzer
Before finalizing any dialogue exchange, run it through the Subtext Filter:

1. **Surface Text (What is literally said):**
   > *"The bolts on this bridge were tightened thirty years ago."* (57 chars)
2. **Subtext (What the character actually means):**
   > *"If you make me run across this bridge with that payload, we will both fall."*
3. **Behavioral Cue (Physical performance / animation trigger):**
   > Character pauses, kicks a loose rivet into the chasm, doesn't meet the player's eye.

---

## 3. Name Generation Engine
Names are procedurally generated using the conlang syllable grammar:
- **Foundry Clan:** *Khor-Var*, *Tor-Kael*, *Brak-Dun* (heavy plosives and velar stops).
- **River Navigators:** *Vel-Mira*, *Lin-Sora*, *Ael-Vea* (liquids, open vowels).
- **Outcasts / Scavengers:** *Zul-Ren*, *Kash-Tir*, *Vok* (monosyllabic or harsh sibilants).
