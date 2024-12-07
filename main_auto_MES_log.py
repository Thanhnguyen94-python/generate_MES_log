import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Hàm để xử lý tạo tệp mới
def create_files():
    model = entry_model.get()
    line = entry_line.get()
    date = entry_date.get()
    time = entry_time.get()
    user = entry_user.get()
    side = entry_side.get()

    if not date.isdigit() or not time.isdigit():
        messagebox.showerror("Error", "Ngày và Giờ phải là số!")
        return

    folder_name = f"{date}_{model}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    if not file_path.get():
        messagebox.showerror("Error", "Bạn chưa chọn tệp!")
        return

    try:
        with open(file_path.get(), 'r') as file:
            lines = file.readlines()

        for line_content in lines:
            line_content = line_content.strip()
            filename = f"{line}_{date}{time}_{line_content}.txt"
            file_content = ";".join([f"{model}", f"{line_content}", f"{line}", "SHIP", f"{user}", "0", f"{date}", f"{time}", "0;0;1;0", f"{side}", "336;0;"])

            file_path_to_save = os.path.join(folder_name, filename)
            with open(file_path_to_save, 'w') as new_file:
                new_file.write(file_content)

        messagebox.showinfo("Success", "Tạo tệp thành công!")

    except Exception as e:
        messagebox.showerror("Error", f"Có lỗi xảy ra: {e}")

# Hàm để chuyển đổi văn bản thành chữ hoa
def to_uppercase(event):
    current_text = event.widget.get()
    event.widget.delete(0, tk.END)
    event.widget.insert(0, current_text.upper())

# Hàm kiểm tra chỉ nhập số
def validate_number_input(char, text_var, max_length=10):
    if char.isdigit() or char == "":
        return True
    return False

# Hàm chọn tệp
def choose_file():
    selected_file = filedialog.askopenfilename(title="Chọn tệp dữ liệu", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if selected_file:
        label_file_name.config(text=f"Tệp đã chọn: {os.path.basename(selected_file)}")
        file_path.set(selected_file)

# Khởi tạo giao diện GUI
root = tk.Tk()
root.title("Tạo Tệp từ Dữ Liệu")
root.geometry("600x500")  # Đặt kích thước cửa sổ lớn hơn một chút
root.config(bg="#f0f0f0")  # Thêm màu nền nhẹ cho cửa sổ

# Khởi tạo biến lưu đường dẫn tệp
file_path = tk.StringVar()

# Tạo Frame chứa các trường nhập liệu
frame_input = tk.Frame(root, padx=20, pady=20, bg="#f0f0f0")
frame_input.grid(row=0, column=0, sticky="nsew")

# Các Label và Entry trong Frame
tk.Label(frame_input, text="Model:", font=("Arial", 10), bg="#f0f0f0").grid(row=0, column=0, pady=5, sticky="w")
entry_model = tk.Entry(frame_input, font=("Arial", 10))
entry_model.grid(row=0, column=1, pady=5)
entry_model.bind("<KeyRelease>", to_uppercase)

tk.Label(frame_input, text="Line:", font=("Arial", 10), bg="#f0f0f0").grid(row=1, column=0, pady=5, sticky="w")
entry_line = tk.Entry(frame_input, font=("Arial", 10))
entry_line.grid(row=1, column=1, pady=5)
entry_line.bind("<KeyRelease>", to_uppercase)

tk.Label(frame_input, text="Date:", font=("Arial", 10), bg="#f0f0f0").grid(row=2, column=0, pady=5, sticky="w")
entry_date = tk.Entry(frame_input, font=("Arial", 10))
entry_date.grid(row=2, column=1, pady=5)
entry_date.config(validate="key", validatecommand=(root.register(validate_number_input), '%S', '%P'))

tk.Label(frame_input, text="Time:", font=("Arial", 10), bg="#f0f0f0").grid(row=3, column=0, pady=5, sticky="w")
entry_time = tk.Entry(frame_input, font=("Arial", 10))
entry_time.grid(row=3, column=1, pady=5)
entry_time.config(validate="key", validatecommand=(root.register(validate_number_input), '%S', '%P'))

tk.Label(frame_input, text="User:", font=("Arial", 10), bg="#f0f0f0").grid(row=4, column=0, pady=5, sticky="w")
entry_user = tk.Entry(frame_input, font=("Arial", 10))
entry_user.grid(row=4, column=1, pady=5)
entry_user.bind("<KeyRelease>", to_uppercase)

tk.Label(frame_input, text="Side:", font=("Arial", 10), bg="#f0f0f0").grid(row=5, column=0, pady=5, sticky="w")
entry_side = tk.Entry(frame_input, font=("Arial", 10))
entry_side.grid(row=5, column=1, pady=5)
entry_side.bind("<KeyRelease>", to_uppercase)

# Thêm nút chọn tệp
button_choose_file = tk.Button(root, text="Chọn Tệp", font=("Arial", 12), bg="#4CAF50", fg="white", relief="flat", command=choose_file)
button_choose_file.grid(row=6, column=0, columnspan=2, pady=10)

# Label để hiển thị tên tệp đã chọn
label_file_name = tk.Label(root, text="Tệp chưa được chọn", font=("Arial", 10), bg="#f0f0f0")
label_file_name.grid(row=7, column=0, columnspan=2, pady=5)

# Tạo nút để xử lý việc tạo tệp
button_create = tk.Button(root, text="Tạo Tệp", font=("Arial", 12), bg="#008CBA", fg="white", relief="flat", command=create_files)
button_create.grid(row=8, column=0, columnspan=2, pady=20)

# Chạy vòng lặp GUI
root.mainloop()
