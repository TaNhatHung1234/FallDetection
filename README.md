# Fall Detection

Hệ thống phát hiện ngã (Fall Detection) sử dụng **YOLOv8** để phát hiện người và **MediaPipe** để ước lượng tư thế (pose estimation).

Dự án đang ở giai đoạn nền tảng: phát hiện người + vẽ skeleton. Logic phân loại ngã sẽ được phát triển tiếp.

## ✨ Tính năng hiện tại

- Phát hiện người bằng YOLOv8n
- Ước lượng pose bằng MediaPipe Pose
- Vẽ bounding box + skeleton lên video
- Hỗ trợ chạy với video mẫu hoặc webcam
- Có Dockerfile và CI/CD cơ bản

## 📁 Cấu trúc dự án

```
FallDetection/
├── data/                  # Video mẫu
│   ├── sample1.mp4
│   └── sample2.webm
├── src/
│   ├── detector.py        # Person Detector (YOLOv8)
│   ├── pose_estimator.py  # Pose Estimator (MediaPipe)
│   └── main.py            # Entry point
├── tests/
│   └── test_detector.py
├── .github/workflows/
│   ├── python-ci.yml
│   └── docker-build.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🛠 Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/TaNhatHung1234/FallDetection.git
cd FallDetection
```

### 2. Tạo môi trường ảo (khuyến nghị)

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
# hoặc
.venv\Scripts\activate         # Windows
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

> **Lưu ý**: Lần đầu chạy sẽ tự động tải model `yolov8n.pt`.

## 🚀 Cách chạy

### Chạy với video mẫu

```bash
cd src
python main.py
```

Mặc định chương trình sẽ chạy file `../data/sample1.mp4`.

### Đổi nguồn video / webcam

Mở file `src/main.py` và sửa dòng:

```python
cap = cv2.VideoCapture("../data/sample1.mp4")
```

Thành:

```python
# Webcam
cap = cv2.VideoCapture(0)

# Hoặc video khác
cap = cv2.VideoCapture("../data/sample2.webm")
```

Nhấn phím **`q`** để thoát.

## 🐳 Chạy bằng Docker

```bash
docker build -t fall-detection .
docker run --rm -it fall-detection
```

## 📦 Dependencies chính

- `ultralytics` (YOLOv8)
- `mediapipe`
- `opencv-python`
- `numpy`, `pandas`, `scikit-learn`, `tensorflow`, `matplotlib`, `seaborn`

## 🧪 Testing

Hiện tại có file test cơ bản:

```bash
pytest tests/
```

## 📌 Roadmap (dự kiến)

- [ ] Thêm logic phát hiện ngã dựa trên keypoints (góc xương, tỷ lệ chiều cao, tốc độ thay đổi pose...)
- [ ] Hỗ trợ nhiều người trong cùng frame
- [ ] Alert (âm thanh / gửi thông báo)
- [ ] Giao diện Streamlit / Gradio
- [ ] Tối ưu tốc độ inference (TensorRT / ONNX)

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo Issue hoặc Pull Request.

## 📄 License

Dự án đang ở giai đoạn phát triển.
---

**Author**: [TaNhatHung1234](https://github.com/TaNhatHung1234)
