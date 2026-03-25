import cv2
from ultralytics import YOLO
from collections import defaultdict

# Load YOUR trained model
model = YOLO(r"C:\Users\Vasan\runs\detect\train8\weights\best.pt")

# Open video
cap = cv2.VideoCapture("drone_city.mp4")

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Output video writer
out = cv2.VideoWriter("output/detected.mp4",
                      cv2.VideoWriter_fourcc(*"mp4v"),
                      fps, (width, height))

print("Running detection... Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, device=0, conf=0.4, iou=0.5)
    annotated = results[0].plot()

    # Count objects
    counts = defaultdict(int)
    for box in results[0].boxes:
        label = model.names[int(box.cls)]
        counts[label] += 1

    # Display counts on frame
    y = 30
    for label, count in counts.items():
        text = f"{label}: {count}"
        cv2.putText(annotated, text, (10, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 0), 2)
        y += 35

    out.write(annotated)
    cv2.imshow("Aerial Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Done! Output saved to output/detected.mp4")