import gradio as gr
from skimage.color import rgb2gray


# TODO: text, audio, image
# TODO: chatbot

def transform_image(img):
  return rgb2gray(img)


demo = gr.Interface(fn=transform_image, inputs=gr.Image(), outputs="image")
demo.launch()
