
import os, socket, traceback, gradio as gr
from app.ui_frontend import build_ui

def find_port(start=7860, end=7880):
    for p in range(start,end+1):
        try:
            s = socket.socket()
            s.bind(("0.0.0.0",p))
            s.close()
            return p
        except:
            continue
    return 7860

port = find_port()
os.environ["GRADIO_SERVER_PORT"] = str(port)

demo = build_ui(pipe=None)
demo.launch(share=True, server_port=port, server_name="0.0.0.0")
