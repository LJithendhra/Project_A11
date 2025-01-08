from roboflow import Roboflow
import supervision as sv
import cv2

# Initialize Roboflow model
rf = Roboflow(api_key="Shio1S5Io8iSBklhgIqj")
project = rf.workspace().project("vehicle-detection-qzo8n")
model = project.version(1).model

# Get predictions from the model using your actual image
result = model.predict("images/4E376976-3ABD-4E49-8BD9-8AC0C83BC433_65d404f899173.webp", confidence=40, overlap=30).json()

# Extract labels from the predictions
labels = [item["class"] for item in result["predictions"]]

# Use the correct method to convert predictions to Detections
detections = sv.Detections.from_roboflow(result)

# Initialize annotators
label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

# Read the input image from the correct path
image = cv2.imread("images/4E376976-3ABD-4E49-8BD9-8AC0C83BC433_65d404f899173.webp")

# Annotate the image with bounding boxes
annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)

# Annotate the image with labels
annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections, labels=labels)

# Display the annotated image
sv.plot_image(image=annotated_image, size=(16, 16))
