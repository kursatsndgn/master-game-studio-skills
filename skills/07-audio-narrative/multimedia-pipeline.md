# Multimedia Audio & Cutscene Pipeline (`multimedia-pipeline.md`)
# Integrations: openvoice (voice cloning), remotion (code-based cutscenes)
# Sub-Agent Domain: @audio-narrative-engineer

## 1. Overview
The multimedia pipeline automates game voiceover generation and cinematic cutscene production without expensive motion capture suites. By coupling neural voice synthesis (`openvoice`) with programmatic React-based video rendering (`remotion`), high-fidelity cinematics can be rendered directly from narrative scripts.

---

## 2. OpenVoice Neural Voice Generation Workflow

```text
Narrative Script (<= 120 chars) --> Emotion & Pitch Tags --> OpenVoice Audio Synthesis --> Audio Normalization (-14 LUFS) --> Godot AudioStream / Remotion Timeline
```

### Voice Profile Manifest (`voice_profiles.json`)
```json
{
  "characters": {
    "kaelen": {
      "reference_audio": "assets/audio/voices/kaelen_ref.wav",
      "base_pitch": -1.5,
      "speaking_rate": 0.95,
      "target_lufs": -14.0
    },
    "varro": {
      "reference_audio": "assets/audio/voices/varro_ref.wav",
      "base_pitch": -3.0,
      "speaking_rate": 0.88,
      "target_lufs": -14.0
    }
  }
}
```

---

## 3. Remotion Programmatic Cutscene Engine (React / TypeScript)

Cutscenes, intro logos, and story transitions are defined entirely as React components rendered to MP4/WebM:

```tsx
import { Composition, Sequence, Audio, Img } from 'remotion';

export const NarrativeCutscene: React.FC<{
  dialogueAudioUrl: string;
  subtitleText: string;
  artworkUrl: string;
}> = ({ dialogueAudioUrl, subtitleText, artworkUrl }) => {
  return (
    <div style={{ flex: 1, backgroundColor: '#0a0a0a', position: 'relative' }}>
      {/* 2D Art Plane with slow Ken Burns pan */}
      <Sequence from={0} durationInFrames={180}>
        <Img
          src={artworkUrl}
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
      </Sequence>

      {/* Voiceover Track */}
      <Audio src={dialogueAudioUrl} />

      {/* Synchronized Subtitle Overlay (Strict <= 120 chars) */}
      <div style={{
        position: 'absolute',
        bottom: 60,
        left: 0,
        right: 0,
        textAlign: 'center',
        color: '#ffffff',
        fontSize: 32,
        fontFamily: 'Inter, sans-serif',
        textShadow: '0 2px 8px rgba(0,0,0,0.9)'
      }}>
        {subtitleText}
      </div>
    </div>
  );
};
```
