import tkinter as tk
from tkinter import messagebox
import os

# Hàm để xử lý tạo tệp mới
def create_files():
    # Lấy dữ liệu từ các trường nhập liệu
    model = entry_model.get()
    line = entry_line.get()
    date = entry_date.get()
    time = entry_time.get()
    user = entry_user.get()
    side = entry_side.get()

    # Tạo tên thư mục từ 'date' và 'model'
    folder_name = f"{date}_{model}"

    # Kiểm tra xem thư mục đã tồn tại chưa, nếu chưa thì tạo mới
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Đọc dữ liệu từ file list.txt
    try:
        with open('list.txt', 'r') as file:
            lines = file.readlines()

        # Lặp qua từng dòng trong file list.txt
        for line_content in lines:
            line_content = line_content.strip()  # Loại bỏ ký tự newline
            filename = "".join([f"{line}_",
                            f"{date}", #QR
                            f"{time}_",
                            f"{line_content}"])  # Tạo tên tệp theo nội dung dòng

            # Tạo nội dung tệp
            file_content = "".join([f"{model};",
                                 f"{line_content};", #QR
                                 f"{line};",
                                 f"SHIP;",
                                 f"{user};",
                                 f"0;",
                                 f"{date};",
                                 f"{time};",
                                 f"0;0;1;0;",
                                 f"{side};",
                                 f"336;0;"])
                                 

            # Tạo tệp mới trong thư mục đã tạo và ghi nội dung vào đó
            file_path = os.path.join(folder_name, filename)
            with open(file_path, 'w') as new_file:
                new_file.write(file_content)

        messagebox.showinfo("Success", "Tạo tệp thành công!")
    except Exception as e:
        messagebox.showerror("Error", f"Có lỗi xảy ra: {e}")
# Hàm để chuyển đổi văn bản thành chữ hoa
def to_uppercase(event):
    event.widget.delete(0, tk.END)  # Xóa nội dung hiện tại
    event.widget.insert(0, event.widget.get().upper())

# Khởi tạo giao diện GUI
root = tk.Tk()
root.title("Tạo Tệp từ Dữ Liệu")
# Thiết lập kích thước cửa sổ
root.geometry("500x400")  # Đặt chiều rộng 500px và chiều cao 400px

# Tạo các trường nhập liệu
tk.Label(root, text="Model:").grid(row=0, column=0)
entry_model = tk.Entry(root)
entry_model.grid(row=0, column=1)
entry_model.bind("<KeyRelease>", to_uppercase)  # Bind để chuyển sang chữ hoa

tk.Label(root, text="Line:").grid(row=1, column=0)
entry_line = tk.Entry(root)
entry_line.grid(row=1, column=1)
entry_line.bind("<KeyRelease>", to_uppercase)

tk.Label(root, text="Date:").grid(row=2, column=0)
entry_date = tk.Entry(root)
entry_date.grid(row=2, column=1)

tk.Label(root, text="Time:").grid(row=3, column=0)
entry_time = tk.Entry(root)
entry_time.grid(row=3, column=1)

tk.Label(root, text="User:").grid(row=4, column=0)
entry_user = tk.Entry(root)
entry_user.grid(row=4, column=1)
entry_user.bind("<KeyRelease>", to_uppercase)

tk.Label(root, text="Side:").grid(row=5, column=0)
entry_side = tk.Entry(root)
entry_side.grid(row=5, column=1)
entry_side.bind("<KeyRelease>", to_uppercase)

# Tạo nút để xử lý việc tạo tệp
button_create = tk.Button(root, text="Tạo Tệp", command=create_files)
button_create.grid(row=6, column=0, columnspan=2)

# Chạy vòng lặp GUI
root.mainloop()
