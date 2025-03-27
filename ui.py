
# web.py
"""Web interface for my_library using Gradio."""

import gradio as gr
import requests
from PIL import Image
from io import BytesIO

# API endpoint
API_URL = "http://127.0.0.1:5555/process/"

def process_image(image):
    """Send the image to the API and get the processed result."""
    # Convert PIL image to bytes
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format="JPEG")
    img_byte_arr = img_byte_arr.getvalue()
    
    # Send to API
    files = {'file': img_byte_arr}
    response = requests.post(API_URL, files=files)
    
    if response.status_code == 200:
        # Convert response to PIL image
        result_image = Image.open(BytesIO(response.content))
        return image, result_image
    else:
        return image, None

# Create Gradio interface
with gr.Blocks(title="My Library Demo") as demo:
    gr.Markdown("# My Library Image Processing")
    
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type="pil", label="Input Image")
        
        with gr.Column():
            output_image = gr.Image(type="pil", label="Processed Image")
    
    process_btn = gr.Button("Process Image")
    process_btn.click(
        fn=process_image,
        inputs=[input_image],
        outputs=[input_image, output_image]
    )
    
    gr.Markdown("## How It Works")
    gr.Markdown("""
    This demo showcases the capabilities of My Library.
    Upload an image, click 'Process Image', and see the result.
    """)

# Launch the interface
if __name__ == "__main__":
    demo.launch(share=False)