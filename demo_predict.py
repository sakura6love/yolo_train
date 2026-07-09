from ultralytics import YOLO

model = YOLO("yolov8n.pt", task="detect") 

results = model(source=0)