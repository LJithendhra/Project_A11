from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from detection import process_video, calculate_distance

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

@app.post("/process-video/")
async def process_uploaded_video(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        output_path = os.path.join(UPLOAD_DIR, "processed_" + file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f" Processing video: {file_path}")
        
        detections = process_video(file_path, output_path)

        print(f" Detections sent to frontend: {detections}")  # Debugging

        return JSONResponse(content={"detections": detections})
    
    except Exception as e:
        print(f" Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/calculate-distance")
def get_distance(bbox: str):
    try:
        bbox = list(map(int, bbox.split(",")))
        distance, estimated_time = calculate_distance(bbox)
        return {"distance": distance, "estimated_time": estimated_time}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
