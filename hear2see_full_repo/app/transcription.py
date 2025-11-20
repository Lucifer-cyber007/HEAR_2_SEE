
from vosk import Model, KaldiRecognizer
import subprocess, wave, json, os

VOSK_PATH = "models/vosk-model-small-en-us-0.15"
vosk_model = Model(VOSK_PATH)

def transcribe_audio(audio_path, style):
    if audio_path is None:
        return "(no audio)", ""
    # Convert audio to 16kHz
    wav16 = audio_path + "_16k.wav"
    subprocess.run(['ffmpeg','-y','-i',audio_path,'-ar','16000','-ac','1',wav16])
    wf = wave.open(wav16, "rb")
    rec = KaldiRecognizer(vosk_model, wf.getframerate())
    rec.SetWords(True)
    txt = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            txt += json.loads(rec.Result()).get("text","") + " "
    txt += json.loads(rec.FinalResult()).get("text","")
    prompt = f"{txt}, {style} lighting"
    return txt.strip(), prompt.strip()
