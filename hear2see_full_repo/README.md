Hear2See — Audio → Prompt → Video 🎬🔊→🎥

Hear2See converts audio into short AI-generated videos. It transcribes uploaded/recorded audio using an offline Vosk ASR model, converts the transcript into a text prompt (editable), and then generates frames with a text-to-image diffusion model (Stable Diffusion 1.5 + optional LoRA). Frames are stitched into an MP4 video.

Features

Offline transcription using Vosk (no external API).

Editable prompt interface: auto-generate prompt from transcript, then edit.

Text → video generation via Stable Diffusion (fused SD1.5) with LoRA support.

Save input audio, generated frames, and final MP4 files to Drive / disk.

Colab-friendly or local development (GPU recommended for generation).

Gradio frontend (Blocks) with step-by-step flow (Transcribe → Edit → Generate).

Slow-mode option (halves FPS for clearer frame viewing).

Metadata logging (per-run JSONL).
📁 Repository Structure
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


🔧 Installation
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/hear2see.git
cd hear2see

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Download Vosk 0.15 model
bash scripts/download_vosk.sh

4️⃣ (Optional) Add Stable Diffusion fused model

Copy your fused SD-1.5 model into:

diffusion/sd_fused_model/

▶️ Running the App
🔌 Run locally
python app/launcher_local.py

🌐 Running in Google Colab

Just run the notebook:

notebooks/Hear2See_Frontend_Colab.ipynb


The launcher automatically:

detects free ports

sets Colab networking options

supports share=True public UI

🔍 Workflow

Upload/Record Audio

Vosk ASR → Transcript

Prompt Builder → Style Selection

Stable Diffusion → Generate Frames

FFmpeg → MP4 Video

Save Audio, Video, Metadata

Outputs appear in:

data/input_audio/
data/output_videos/
data/metadata.jsonl

⚡ Tips & Recommendations

For video generation, use GPU runtime (A100 recommended).

Replace the fused SD model with any compatible SD1.5 folder.

LoRA training notebook included if you want custom video styles.

📜 License

MIT License © 2025 Hear2See Team
