
NEGATIVE_PROMPT = "text, watermark, lowres, blurry, distortions"

def build_prompt(txt, style):
    return f"{txt}, {style} lighting"
