
import gradio as gr
from app.transcription import transcribe_audio
from app.video_generation import generate_video
from app.utils import build_prompt

def build_ui(pipe):
    with gr.Blocks(title="Hear2See — Audio → Prompt → Video") as demo:
        gr.Markdown("## Hear2See — Upload audio → Transcript → Video")

        with gr.Row():
            with gr.Column():
                audio = gr.Audio(sources=["microphone","upload"], type="filepath", label="Upload Audio")
                style = gr.Radio(["cinematic","realistic","anime"], value="cinematic")
                trans_btn = gr.Button("Transcribe")

            with gr.Column():
                transcript = gr.Textbox(label="Transcript", lines=4)
                prompt = gr.Textbox(label="Prompt", lines=4)

            with gr.Column():
                steps = gr.Slider(10,50,value=25,label="Steps")
                frames = gr.Slider(8,48,value=16,label="Frames")
                fps    = gr.Slider(2,24,value=6,label="FPS")
                cfg    = gr.Slider(4,12,value=7,label="CFG")
                seed   = gr.Slider(1,9999,value=1234,label="Seed")
                slow   = gr.Checkbox(True,label="Slow Mode")
                gen_btn = gr.Button("Generate Video")
                output = gr.Video(label="Output Video")

        trans_btn.click(transcribe_audio, inputs=[audio, style], outputs=[transcript, prompt])
        gen_btn.click(generate_video, inputs=[prompt, steps, frames, fps, cfg, seed, slow, audio], outputs=[output])
    return demo
