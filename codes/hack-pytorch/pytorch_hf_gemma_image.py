# PyTorch + Transformers

import torch
from transformers import AutoProcessor, AutoModelForMultimodalLM
from dotenv import load_dotenv
from PIL import Image
import os


def load_image(path):
  if not os.path.exists(path):
    raise FileNotFoundError(f"找不到本地图片文件: {path}")
  return Image.open(path).convert("RGB")


load_dotenv(".env/hf.env")


MODEL_ID = "google/gemma-4-E4B-it"

# Load model
processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForMultimodalLM.from_pretrained(
    MODEL_ID,
    dtype="auto",
    device_map="cpu"
)

# Prompt - add image before text
messages = [
    {
        "role": "user", "content": [
            {"type": "image",
             #  "url": "https://raw.githubusercontent.com/google-gemma/cookbook/refs/heads/main/Demos/sample-data/GoldenGate.png"
             #  "image": load_image("data/images/pexels-vitaliy-haiduk-326720599-32995485.jpg")
             "image": load_image("data/images/avatar.png")
             },
            {"type": "text", "text": "What is shown in this image?"}
        ]
    }
]

# Process input
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    add_generation_prompt=True,
).to(model.device)
input_len = inputs["input_ids"].shape[-1]

# Generate output
outputs = model.generate(**inputs, max_new_tokens=512)
response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)

# Parse output
output = processor.parse_response(response)
print(output)

# Output:
# {'role': 'assistant', 'content': "This image is a photograph taken from an elevated viewpoint, likely an overpass or a tall building, overlooking a multi-lane highway on a bright, sunny day.\n\nHere's a breakdown of what is visible:\n\n*   **Highway:** A wide, modern highway dominates the foreground and midground, featuring multiple lanes going in both directions. Traffic is moderately present.\n*   **Traffic:** Several vehicles are visible, including cars, trucks (some large semi-trucks), and SUVs, traveling along the road.\n*   **Infrastructure:** In the background, there is a large **elevated freeway or bridge** spanning across the landscape. Streetlights are visible along the road.\n*   **Environment:** The area surrounding the highway features greenery, including trees and brush, suggesting a semi-urban or suburban setting. The sky is bright and clear, indicating good weather.\n*   **Color/Mood:** The image has a warm, slightly desaturated, and faded aesthetic, giving it a vintage or sun-bleached look.\n\nIn summary, it is a **busy, elevated shot of a highway interchange or major road system under a bright sky.**"}
