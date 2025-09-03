import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files():
    """Переименовывает файлы в выбранной папке в порядковые номера."""
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    try:
        files = os.listdir(folder_path)
        if not files:
            messagebox.showinfo("Ошибка", "В выбранной папке нет файлов.")
            return

        files.sort()  # Сортируем файлы, чтобы переименование шло в определенном порядке
        for index, filename in enumerate(files):
            if os.path.isfile(os.path.join(folder_path, filename)): # Обрабатываем только файлы
                name, ext = os.path.splitext(filename)
                new_name = f"{index + 1:03}{ext}"  # Форматируем номер, например, 001, 002, ...
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_name)

                try:
                    os.rename(old_path, new_path)
                except OSError as e:
                    messagebox.showerror("Ошибка", f"Ошибка при переименовании файла {filename}: {e}")
                    return

        messagebox.showinfo("Успех", "Файлы успешно переименованы.")

    except OSError as e:
        messagebox.showerror("Ошибка", f"Ошибка при работе с папкой: {e}")


# Создание главного окна
root = tk.Tk()
root.title("Переименование файлов")
root.geometry("300x100")

# Кнопка для выбора папки
browse_button = tk.Button(root, text="Выбрать папку", command=rename_files)
browse_button.pack(pady=20)

root.mainloop()