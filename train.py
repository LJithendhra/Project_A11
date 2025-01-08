import torch
from ultralytics import YOLO
import yaml

# 1. Set up hyperparameters
epochs = 50  # Number of epochs to train
batch = 32  # Batch size
img_size = 640  # Image size
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# 2. Load custom dataset configuration (config.yaml)
with open('config.yaml', 'r') as f:
    data_cfg = yaml.safe_load(f)

# 3. Load YOLOv8 segmentation model
model = YOLO("yolo11n.pt")  # Pre-trained YOLOv8 segmentation model

# 4. Modify model for custom dataset (if needed)
model.classes = [0, 1, 2, 3, 4, 5, 6, 7]  # Adjust based on your number of classes

# 5. Define training function
def train_yolov11():
    # Set up the training configuration
    model.train(
        data='config.yaml',  # Pass the path to the dataset configuration file as a string
        epochs=epochs,  # Number of epochs
        batch=batch,  # Batch size (correct argument)
        imgsz=img_size,  # Image size
        device=device,  # Device (GPU or CPU)
        workers=4,  # Number of workers for data loading (adjust as needed)
        name="yolov11_train",  # Training run name (output folder)
        save_period=5,  # Save model every 5 epochs (or as needed)
    )

# 6. Start training
if __name__ == "__main__":
    train_yolov11()
