# Aerial Object Detection with YOLOv8

Real time object detection on drone footage using YOLOv8 trained on the VisDrone dataset.

## Demo
Coming soon — training completed on NVIDIA RTX 3050 GPU locally

## Problem
Default YOLOv8 model trained on COCO dataset fails on aerial drone footage 
because it was never trained on top-down views. 
This project solves that by fine-tuning YOLOv8 on VisDrone — 
a dataset specifically built for drone vision.

## Results
| Class | mAP50 |
|-------|-------|
| Overall | 0.155 |
| Car | 0.541 |
| Bus | 0.231 |
| Van | 0.154 |
| Truck | 0.132 |
| Pedestrian | 0.121 |

## Dataset
VisDrone2019 — 10 classes, 1618 training images, aerial drone footage

## Tech Stack
- YOLOv8 (Ultralytics)
- PyTorch
- OpenCV
- Python

## How to Run
```bash
pip install ultralytics opencv-python
python detect.py
```
