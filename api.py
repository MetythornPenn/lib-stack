# api.py
"""FastAPI-based API for my_library."""

import io
import torch
import numpy as np
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from my_library import main_function, process_data

app = FastAPI(
    title="My Library API",
    description="API for my_library processing capabilities",
    version="0.1.0"
)

# Global variables for loaded models
model = None
device = None

@app.on_event("startup")
async def load_model():
    """Load model on startup."""
    global model, device
    
    # Determine the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Load model (replace with your actual model loading code)
    # model = load_your_model("path/to/model")
    
    print(f"Model loaded successfully on {device}")

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to My Library API!", "status": "online"}

@app.post("/process/")
async def process_image(file: UploadFile = File(...)):
    """Process an image with my_library."""
    # Read the uploaded file
    image_data = await file.read()
    
    # Convert to numpy array
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        return {"error": "Invalid image data"}
    
    # Process the image
    processed_img = main_function(img)
    
    # Convert back to bytes for returning
    _, img_encoded = cv2.imencode('.jpg', processed_img)
    
    # Return as a streaming response
    return StreamingResponse(
        io.BytesIO(img_encoded.tobytes()), 
        media_type="image/jpeg"
    )
