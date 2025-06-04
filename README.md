
# 🐾 NHẬN DIỆN ĐỘNG VẬT QUA ẢNH BẰNG YOLOv8 VÀ GIAO DIỆN TKINTER

## 📌 1. Giới thiệu chung

Dự án phát triển một **ứng dụng máy tính có giao diện người dùng (GUI)** giúp nhận diện các loài động vật từ ảnh bằng cách sử dụng mô hình học sâu **YOLOv8**. Ứng dụng sử dụng thư viện `Tkinter` để thiết kế giao diện đơn giản, thân thiện, cho phép người dùng chọn ảnh và xem kết quả nhận diện nhanh chóng.

Mô hình YOLOv8 được huấn luyện trên tập dữ liệu động vật tùy chỉnh, có thể phân biệt và nhận diện **nhiều loài khác nhau** với độ chính xác cao.

---

## 📊 2. Sơ đồ hoạt động và chức năng

### 🛠️ **Quy trình hoạt động:**

graph TD
    A[Chọn ảnh từ máy tính] --> B[YOLOv8 phân tích ảnh]
    B --> C[Trích xuất thông tin đối tượng]
    C --> D[Hiển thị ảnh gốc]
    C --> E[Hiển thị kết quả nhận diện (văn bản)]

### ✅ **Chức năng chính:**
- Giao diện người dùng đơn giản với `Tkinter`
- Nhận diện nhiều loài động vật từ ảnh tĩnh
- Hiển thị kết quả dạng văn bản (tên loài, độ chính xác %)
- Hỗ trợ ảnh định dạng `.jpg`, `.jpeg`, `.png`

---

## 💡 3. Công nghệ và kỹ thuật sử dụng

- **Ngôn ngữ:** Python 3.x
- **Mô hình học sâu:** YOLOv8 (Ultralytics)
- **Giao diện người dùng:** Tkinter
- **Thư viện hỗ trợ:**
  - `ultralytics`
  - `Pillow`
  - `tkinter`

---

## 🖼️ 4. Giao diện chương trình

| Chức năng | Hình ảnh minh họa |
|----------|-------------------|
| Giao diện chính | ![Giao diện](https://i.imgur.com/AZ0RyRx.png) *(Thay bằng ảnh thật nếu có)* |

---

## ⚙️ 5. Hướng dẫn cài đặt và chạy

### A. Yêu cầu môi trường
- Python 3.8 trở lên
- Cài các thư viện cần thiết:
```bash
pip install ultralytics pillow
```

### B. Chạy chương trình
```bash
python detect_gui.py
```

### C. Cấu trúc thư mục
```
📦 animal-detector-gui/
├── detect_gui.py
├── yolov8s.pt
├── README.md
└── sample.jpg (nếu có)
```

> 📁 Đảm bảo file mô hình `yolov8s.pt` nằm cùng thư mục với `detect_gui.py`

---

## 🧠 6. Ghi chú thêm

- Mô hình YOLOv8 có thể được thay thế bằng các mô hình khác trong thư mục `runs/detect/...`
- Nếu muốn đóng gói thành `.exe`, có thể dùng `pyinstaller`:
```bash
pyinstaller --onefile --noconsole detect_gui.py
```

---

## 📞 7. Liên hệ

- Tác giả: [Lê Xuân Đạt]
- Email: brianbenn2003@gmail.com
