import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO

# Load mô hình YOLOv8 đã huấn luyện
model = YOLO("runs/detect/animal_detector7/weights/best.pt")

def detect_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    # Dự đoán kết quả
    results = model(file_path)
    result = results[0]
    names = model.names

    # Hiển thị ảnh gốc
    img = Image.open(file_path).resize((400, 300))
    tk_img = ImageTk.PhotoImage(img)
    img_label.config(image=tk_img)
    img_label.image = tk_img

    # Hiển thị kết quả dạng văn bản
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)

    if result.boxes:
        output_text.insert(tk.END, "Kết quả nhận diện:\n\n")
        for i, box in enumerate(result.boxes):
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            output_text.insert(tk.END, f"{i+1}. {names[cls_id]} ({conf*100:.1f}%)\n")
    else:
        output_text.insert(tk.END, "Không phát hiện đối tượng nào.")

    output_text.config(state="disabled")

# Thiết kế giao diện
root = tk.Tk()
root.title("Nhận diện động vật bằng YOLOv8")
root.geometry("750x480")
root.resizable(False, False)

# Tiêu đề
tk.Label(root, text="NHẬN DIỆN ĐỘNG VẬT", font=("Helvetica", 16, "bold")).pack(pady=10)

# Nút chọn ảnh
tk.Button(root, text="Chọn ảnh để nhận diện", command=detect_image, font=("Arial", 11)).pack(pady=5)

# Khung hiển thị ảnh + kết quả
frame = tk.Frame(root)
frame.pack(pady=10)

img_label = tk.Label(frame, borderwidth=2, relief="groove")
img_label.pack(side="left", padx=10)

output_text = tk.Text(frame, width=30, height=18, font=("Consolas", 11), bg="#f5f5f5")
output_text.pack(side="right", padx=10)
output_text.config(state="disabled")

root.mainloop()
