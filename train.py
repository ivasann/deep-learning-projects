from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8n.pt")

    results = model.train(
        data="visdrone.yaml",
        epochs=50,
        imgsz=320,
        batch=4,
        device=0,
        workers=2
    )

    print("Training complete!")