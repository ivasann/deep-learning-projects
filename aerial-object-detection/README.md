# 🚁 Aerial Object Detection & Tracking with YOLOv8

Real-time object detection and multi-object tracking on drone footage using YOLOv8 fine-tuned on the VisDrone dataset.

---

## 🎥 Demo

![Aerial Object Tracking Demo](demo.gif)

> YOLOv8 + ByteTrack detecting and tracking cars from aerial drone footage with persistent IDs and confidence scores.

---

## 📌 Overview

Default YOLOv8 models trained on COCO fail on aerial drone footage because they were never trained on top-down views. This project solves that by fine-tuning YOLOv8 on VisDrone — a dataset specifically built for drone vision — and adds ByteTrack for persistent multi-object tracking.

---

## 🎯 Results

| Class      | mAP@50 |
|------------|--------|
| Overall    | 0.155  |
| Car        | 0.541  |
| Bus        | 0.231  |
| Van        | 0.154  |
| Truck      | 0.132  |
| Pedestrian | 0.121  |

> Note: VisDrone is one of the most challenging aerial detection benchmarks due to small object sizes, dense scenes, and top-down occlusion. A car mAP of 0.541 is competitive for this dataset.

---

## 🗂️ Dataset

**VisDrone2019**
- 10 object classes
- 1,618 training images
- Aerial drone footage, top-down perspective
- Source: [VisDrone Dataset](https://github.com/VisDrone/VisDrone-Dataset)

---

## 🛠️ Tech Stack

- **YOLOv8** (Ultralytics) — object detection
- **ByteTrack** — multi-object tracking
- **PyTorch** — deep learning framework
- **OpenCV** — video processing
- **Python 3.10+**

---

## 📁 Project Structure

```
├── train.py          # Fine-tune YOLOv8 on VisDrone
├── detect.py         # Run detection on drone footage
├── track.py          # ByteTrack multi-object tracking with trails
├── visdrone.yaml     # Dataset configuration
├── demo.gif          # Demo output
└── README.md
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install ultralytics opencv-python lapx
```

### 2. Download VisDrone Dataset

Download from the [official repository](https://github.com/VisDrone/VisDrone-Dataset) and update paths in `visdrone.yaml`.

### 3. Train the Model

```bash
python train.py
```

Training config:
- Base model: YOLOv8n
- Epochs: 50
- Image size: 320
- Batch size: 4

### 4. Run Detection

```bash
python detect.py
```

### 5. Run Tracking

```bash
python track.py
```

---

## 🎥 Features

- **Object Detection** — detects cars, buses, vans, trucks, pedestrians and more from aerial views
- **Multi-Object Tracking** — assigns persistent IDs to each object across frames using ByteTrack
- **Movement Trails** — visualises each object's trajectory with a fading trail
- **Object Counting** — real-time count of each class overlaid on the frame
- **Video Export** — saves annotated output as MP4

---

## 📊 Training Details

| Parameter   | Value           |
|-------------|-----------------|
| Base Model  | YOLOv8n         |
| Epochs      | 50              |
| Image Size  | 320             |
| Batch Size  | 4               |
| Device      | NVIDIA RTX 3050 |
| Framework   | Ultralytics + PyTorch |

---

## 🔮 Future Work

- [ ] Implement SAHI (Slicing Aided Hyper Inference) for improved small object detection
- [ ] Export model to ONNX/TensorRT for edge deployment
- [ ] Add threat zone detection logic
- [ ] Build Streamlit dashboard for real-time monitoring
- [ ] Train on larger image size (640) for better mAP

---

## 📄 License

MIT License — free to use and modify.

---

## 🙏 Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [VisDrone Dataset](https://github.com/VisDrone/VisDrone-Dataset)
- [ByteTrack](https://github.com/ifzhang/ByteTrack)
