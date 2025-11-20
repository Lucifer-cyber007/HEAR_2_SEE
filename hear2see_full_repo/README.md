🎬🔊 Hear2See — Audio → Prompt → Video (Offline + Diffusion)

Hear2See is a fully offline, modular system that converts audio → transcript → video, combining:

Vosk 0.15 Offline ASR

Stable Diffusion (fused SD-1.5) with optional LoRA

Gradio UI frontend

Automatic audio/video saving + metadata logging

Colab-friendly launcher

This repository includes a clean, production-ready modular codebase and a complete folder structure for running and extending Hear2See.

🚀 Features
🔊 Speech → Text (Offline)

Uses Vosk 0.15 small model (40MB)

No internet required

Converts any uploaded/recorded audio (WAV, MP3, M4A, OGG, FLAC)

Auto-normalizes audio to 16kHz WAV internally

📝 Text → Prompt

Automatic prompt builder (cinematic / anime / realistic)

Users can edit transcript before generating video

🎥 Text → Video (Diffusion)

Uses Stable Diffusion 1.5 fused model (local folder)

Frame-by-frame rendering

Video stitching using ffmpeg

Slow Mode (½ FPS)

💾 Storage Engine

Saves uploaded audio to data/input_audio/

Saves videos to data/output_videos/

Stores frames optionally

Logs all runs to data/metadata.jsonl

🖥️ UI & Deployment

Gradio Blocks UI (fully responsive)

Robust launcher for Colab (port management, queue compatibility)

Local launcher for desktop use

📁 Repository Structure
hear2see/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── app/
│   ├── __init__.py
│   ├── ui.py                      # Full Gradio frontend (Blocks)
│   ├── transcription.py           # Vosk ASR logic
│   ├── video_generation.py        # Stable Diffusion rendering backend
│   ├── storage.py                 # Audio/video saving + metadata
│   ├── utils.py                   # Prompt builder + helpers
│   └── launcher_local.py          # Local/Colab safe launcher
│
├── models/
│   └── vosk-model-small-en-us-0.15/   # Official Vosk ASR model directory
│
├── diffusion/
│   ├── sd_fused_model/            # Stable Diffusion 1.5 model folder (user provided)
│   └── lora_out/                  # (Optional) LoRA weights + training logs
│       ├── pytorch_lora_weights.safetensors
│       ├── training_args.json
│       ├── logs/
│       └── samples/
│
├── data/
│   ├── input_audio/               # All saved audio files
│   ├── output_videos/             # All generated videos
│   ├── frames/                    # (Optional) saved individual frames
│   └── metadata.jsonl             # One JSON record per generation
│
├── notebooks/
│   ├── Hear2See_Frontend_Colab.ipynb     # Full working Colab notebook
│   ├── LoRA_Training_Notebook.ipynb      # For fine-tuning LoRA
│   ├── Diagnostics_Vosk.ipynb            # For fixing/validating ASR models
│   └── Experiments/
│
├── scripts/
│   ├── download_vosk.sh             # Script to download Vosk 0.15 small model
│   ├── convert_audio.sh             # Batch 16kHz conversion helper
│   └── train_lora.sh                # CLI LoRA training boilerplate
│
├── server/
│   ├── main.py                      # (Optional) FastAPI backend
│   └── api/
│       ├── transcription_api.py
│       ├── video_api.py
│       └── health_check.py
│
└── assets/
    ├── logo.png
    ├── sample_audio/
    └── sample_output/

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
