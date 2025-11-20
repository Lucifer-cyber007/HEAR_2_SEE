
import os, subprocess, tempfile, torch
from diffusers import StableDiffusionPipeline
from app.storage import save_audio
from app.utils import NEGATIVE_PROMPT

MODEL_DIR = "diffusion/sd_fused_model"

pipe = None
if os.path.exists(MODEL_DIR):
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_DIR, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    ).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_video(prompt, steps, frames, fps, cfg, seed, slow, audio_file):
    if pipe is None:
        return None
    tmp = tempfile.mkdtemp()
    for i in range(frames):
        gen = torch.Generator(device=pipe.device).manual_seed(seed+i)
        img = pipe(prompt, num_inference_steps=steps, guidance_scale=cfg,
                   negative_prompt=NEGATIVE_PROMPT, generator=gen).images[0]
        img.save(f"{tmp}/frame_{i:03d}.png")
    out_path = f"data/output_videos/output_{seed}.mp4"
    real_fps = max(1, fps//2) if slow else fps
    subprocess.run([
        "ffmpeg","-y","-framerate",str(real_fps),
        "-i",f"{tmp}/frame_%03d.png",
        "-c:v","libx264","-pix_fmt","yuv420p",
        out_path
    ])
    return out_path
