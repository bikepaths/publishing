# Urban Survival Series - X (Twitter) Syndication Plan

## Strategic Objective
Automate the 11-day promotional syndication of the Urban Survival series on X utilizing manual sysop execution blocks due to unavailable direct API access. The sequence maintains an ongoing threaded structure.

## Multi-Stage Progression

### Stage 1: Sandbox Config Generation
- **Action**: Engineer `x_promo_thread.json` configuration file defining the exact structure for 11 days.
- **Data Points per Node**:
  - `Day`: Integer (1-11)
  - `Part`: Exact internal title reference.
  - `Body`: 280-character maximum systemic summary, strictly adhering to OVP vocabulary.
  - `Hashtags`: Fixed `#UrbanSurvival #Homelessness`.
  - `URL`: Corresponding `https://bikepaths.org/blog/2026/07/...` route.
  - `ImagePrompt`: Direct visual constraints avoiding synthetic/cartoon outputs, maintaining stark architectural realism for the `generate_image` tool pipeline.

### Stage 2: Thread Linkage Script (`400_networking/x_twitter/x_promo_generator.py`)
- **Action**: Develop Python script to parse `x_promo_thread.json`.
- **Outputs**: 
  - Generates standard terminal output containing the direct Cut-and-Paste body for manual attachment.
  - Generates clickable URL-encoded Web Intent: `https://x.com/intent/tweet?text=[ENCODED]&url=[URL]`
  - Incorporates state injection capability via `--reply-to [TWEET_ID]` argument to maintain algorithmic threading continuity.

### Stage 3: Image Generation Pipeline
- **Action**: Sequentially prompt `generate_image` tool to produce 11 `.webp` visual assets.
- **Constraints**: Urban realism, objective staging, no identifying facial rendering, concrete environmental textures. Output directly into `networking/x_twitter/assets/`.

### Stage 4: Daily Execution
- **Action**: Sysop executes `python3 400_networking/x_twitter/x_promo_generator.py --day [N] --reply-to [PREVIOUS_ID]`.
- **Action**: Sysop executes manual copy-paste to X UI, attaches `.webp` asset, and publishes.
