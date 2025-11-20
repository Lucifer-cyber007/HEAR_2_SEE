Thanks — I fixed and rewrote a clean, GitHub-ready **README.md** for the full `hear2see/` repo (ready to paste). Below is the complete README content. I also included the path to the notebook file you uploaded so you can download/open it locally.

---

# README.md (ready to paste)

# Hear2See — Audio → Prompt → Video 🎬🔊→🎥

**Hear2See** converts audio into short AI-generated videos. It transcribes uploaded/recorded audio using an offline Vosk ASR model, converts the transcript into a text prompt (editable), and then generates frames with a text-to-image diffusion model (Stable Diffusion 1.5 + optional LoRA). Frames are stitched into an MP4 video.

---

## Features

* Offline transcription using **Vosk** (no external API).
* Editable prompt interface: auto-generate prompt from transcript, then edit.
* Text → video generation via Stable Diffusion (fused SD1.5) with LoRA support.
* Save input audio, generated frames, and final MP4 files to Drive / disk.
* Colab-friendly or local development (GPU recommended for generation).
* Gradio frontend (Blocks) with step-by-step flow (Transcribe → Edit → Generate).
* Slow-mode option (halves FPS for clearer frame viewing).
* Metadata logging (per-run JSONL).

---

## Repo layout (recommended)

```
hear2see/
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── ui_frontend.py           # Gradio UI (Blocks) — main frontend
│   ├── transcription.py         # Vosk logic: load model, transcribe, save audio
│   ├── video_generation.py      # SD + LoRA rendering: frames → MP4
│   ├── storage.py               # Save audio/video/frames + metadata
│   ├── utils.py                 # helpers: prompt builder, audio converters
│   └── launcher.py              # robust Gradio launcher for Colab/local
├── models/
│   └── vosk-model-small-en-us-0.15/    # Vosk official small model (0.15)
├── diffusion/
│   ├── sd_fused_model/          # fused SD1.5 model dir (user-provided)
│   └── lora_out/                # LoRA weights (optional)
├── data/
│   ├── input_audio/
│   ├── frames/
│   ├── output_videos/
│   └── metadata.jsonl
├── notebooks/
│   ├── Hear2See_Frontend_Colab.ipynb
│   └── Diagnostics_Vosk.ipynb
├── scripts/
│   ├── download_vosk.sh
│   └── convert_audio.sh
├── server/
│   └── main.py                  # optional FastAPI server
└── assets/
    ├── logo.png
    └── sample_audio/
```

---

## Quick start (Colab / local)

> **Edit only the path constants** in notebook or `app` code if your Drive paths differ.

### 1. Install requirements

```bash
pip install -r requirements.txt
# Typical entries: gradio, diffusers, transformers, accelerate, torch, ffmpeg-python, vosk
```

### 2. Vosk model (download once)

```bash
# Example: download Vosk small model (0.15) into ./models/
mkdir -p models
wget -q https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip -O /tmp/vosk-small.zip
unzip -q /tmp/vosk-small.zip -d models/
rm /tmp/vosk-small.zip
```

### 3. Place fused Stable Diffusion model

If you have a fused SD1.5 directory (e.g. `sd_fused_model/` containing `unet/` etc.), put it under `diffusion/sd_fused_model/`. If not, set `MODEL_DIR` in the notebook to your model path.

### 4. Run the Gradio UI (Colab)

* Open `notebooks/Hear2See_Frontend_Colab.ipynb` (or paste the notebook cells in a Colab notebook).
* Mount Drive, set the `BASE` path, run cells in order.
* Launch the UI cell (the launcher finds a free port and creates a public share link when `share=True`).

---

## How the pipeline works (high level)

1. **Upload / record audio** via Gradio UI.
2. Audio is saved to `data/input_audio/` (unique name).
3. Audio re-sampled to 16k mono WAV → Vosk transcribes offline.
4. Transcript is converted to a suggested prompt (style options: cinematic / realistic / anime).
5. User edits prompt (optional).
6. The Stable Diffusion pipeline renders `frames` images (seeded per-frame to ensure variety).
7. `ffmpeg` stitches frames into MP4, saved to `data/output_videos/`.
8. A metadata JSON line is appended to `data/metadata.jsonl` with audio path, video path and params.

---

## Important files & places to edit

* `notebooks/Hear2See_Frontend_Colab.ipynb` — recommended: paste the provided cells in Colab.
* `app/ui_frontend.py` — Gradio UI (if running locally).
* `app/transcription.py` — change `VOSK_MODEL_DIR` if necessary.
* `app/video_generation.py` — change `MODEL_DIR` or LoRA file names if required.
* `data/` — storage for saved inputs & outputs.

---

## Troubleshooting (common issues)

* **Vosk fails to load model**: ensure the model directory has `am/`, `conf/`, `graph/` and `model.conf` (or use the official small model directory structure). If mounting from Google Drive, copy to local disk before loading (Drive sometimes causes permissions/IO issues).
* **Diffusers import errors**: ensure compatible package versions (transformers, tokenizers). Use a fresh Colab runtime and install required versions in the first cells.
* **Gradio port conflicts**: the launcher auto-finds a free port in range 7860-7880; if errors persist, restart the runtime and re-run cells in order.
* **No GPU available locally**: CPU generation will be extremely slow — use Colab with GPU for reasonable speeds.

---

## Suggested improvements / next steps

* Fine-tune LoRA with more images (150 images is usually low; 400–1,000 gives better coverage).
* Add a confidence threshold + fallback in transcription.
* Add a basic scheduler for background generation jobs, so UI remains responsive.
* Deploy as a Hugging Face Space (for public demo) or FastAPI backend with React frontend.

---

## License & credits

MIT License © 2025 Hear2See Team

Credits:

* Vosk (offline ASR) — alphacephei/vosk
* Stable Diffusion + diffusers — Hugging Face
* Gradio — gradio.app

---

## Example metadata entry (metadata.jsonl)

```json
{
  "timestamp":"2025-11-12T15:42:13Z",
  "audio_path":"/content/drive/MyDrive/hear2see/input_audio/audio_20251112T154213Z_ab12cd34.wav",
  "video_path":"/content/drive/MyDrive/hear2see/output_videos/hear2see_20251112T154213Z_ab12cd34.mp4",
  "prompt":"a rainy city bench at night, cinematic lighting, depth of field, high detail, film grain",
  "steps":26,"frames":24,"fps":6,"cfg":7.0,"seed":1234,"slow_mode":true
}
```

---
