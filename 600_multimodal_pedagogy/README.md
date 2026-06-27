# 600 — Multimodal Pedagogy
**Systemic Dignity Infrastructure: Audio & Visual Syndication**

---

## What Is This Folder?

This folder holds all the pieces needed to turn the written academic research into things people can actually **listen to**. Think of it like this:

- The working papers in `300_working_papers/` are the **blueprints** — precise, technical documents written for academics and policy reviewers.
- This folder (`600_multimodal_pedagogy/`) takes those blueprints and turns them into **spoken words** — podcast episodes a person on the street, a caseworker, or a civic leader can actually hear and understand.

The teaching method used here is called **Organic Vernacular Pedagogy (OVP)**. That means we never start with a theory. We start with a body — with what it physically feels like to be hungry, scared, or invisible — and then we build the explanation from there.

---

## Folder Structure

```
600_multimodal_pedagogy/
│
├── README.md                   ← This file. Explains the whole folder.
│
├── ovp_podcast_manifest.md     ← The master planning document. Describes the teaching
│                                  philosophy, the eight population types, and the format
│                                  rules for every audio track.
│
├── cycle_retrospective.md      ← Documents all structural changes and accomplishments
│                                  made during the initial content generation cycle.
│
├── ovp_audio_scripts/          ← The written scripts for each podcast episode.
│   │                              These are the words that will be read aloud.
│   │                              Each track contains Episodes 1, 2, and 3.
│   │
│   ├── track_1_acute.md        ← For people who just lost housing suddenly (e.g. lost job,
│   │                              eviction). Their minds still work. The danger is panic.
│   │
│   ├── track_2_chronic.md      ← For people who have been on the street a long time.
│   │                              Their bodies are collapsing. They need food and a
│   │                              locked door before anything else is possible.
│   │
│   ├── track_3_institutional.md← For people cycling between jail, the ER, and the street.
│   │                              The system keeps catching and releasing them. The episode
│   │                              explains why the normal job market will never take them,
│   │                              and what the cooperative model offers instead.
│   │
│   ├── track_4_vulnerability.md← For people with mental illness or substance dependency.
│   │                              The street makes both conditions worse. The episode
│   │                              explains why sobriety-first requirements are physically
│   │                              impossible in an unsheltered environment.
│   │
│   ├── track_5_hidden.md       ← For people living in their cars. They are invisible to
│   │                              the system. The episode explains the vehicle as a
│   │                              depreciating asset trap and offers the Tenancy Bridge.
│   │
│   ├── track_6_relational_engineering.md
│   │                           ← For practitioners and system designers. Explains why
│   │                              large shelters fail biologically and how small pod
│   │                              structures (12-15 people) restore trust and safety.
│   │
│   ├── track_7_tripartite_coalition.md
│   │                           ← For policy makers and funders. Explains why clinical
│   │                              money, private capital, and municipal zoning must be
│   │                              legally locked together to solve the crisis.
│   │
│   └── track_8_civic_capital.md
│                               ← For philanthropists and civic investment boards. Explains
│                                  why charity fails structurally and how to convert
│                                  discretionary giving into guaranteed civic infrastructure.
│
└── manifests/
    └── multimodal_deployment_manifest.json
                                ← A machine-readable JSON file listing every track,
                                   its script path, and its deployment status. Used
                                   to automate uploading to podcast platforms when
                                   an audio provider (e.g., ElevenLabs) is connected.
```

---

## How Audio Gets Made (The Missing Step)

The scripts are **words on a page**. Turning them into actual audio files requires an external voice generation service. This is called a **text-to-speech provider**.

The process works like this:

1. You copy the script text (or automate it via code).
2. You send that text to a service like **ElevenLabs**, **Google Text-to-Speech**, or similar.
3. That service returns a `.mp3` or `.wav` audio file.
4. That audio file gets saved into `/home/user0/git/publishing/500_podcasts/03_mastered_tracks/`.

**Currently**: No API key for an audio provider has been configured. Audio generation requires the Sysop to either:
- Manually paste scripts into a provider's website, **or**
- Provide an API key to automate the process programmatically.

---

## Status Summary

| Track | Topic | Episodes Drafted | Audio Status |
|-------|-------|-----------------|--------------|
| 1 | Acute Economic Dislocation | ✅ Eps 1, 2, 3 | ⏳ Awaiting audio provider |
| 2 | Chronic Physiological Collapse | ✅ Eps 1, 2, 3 | ⏳ Awaiting audio provider |
| 3 | Institutional Cycling | ✅ Eps 1, 2, 3 | ⏳ Awaiting audio provider |
| 4 | Severe Psychiatric/Substance Vulnerability | ✅ Eps 1, 2, 3 | ⏳ Awaiting audio provider |
| 5 | Hidden/Vehicular Homelessness | ✅ Eps 1, 2, 3 | ⏳ Awaiting audio provider |
| 6 | Relational Engineering | ✅ Eps 1, 2, 3 | ⏳ Awaiting audio provider |
| 7 | The Tripartite Coalition | ✅ Eps 1, 2, 3 | ⏳ Awaiting audio provider |
| 8 | Civic Capital Alignment | ✅ Eps 1, 2, 3 | ⏳ Awaiting audio provider |
