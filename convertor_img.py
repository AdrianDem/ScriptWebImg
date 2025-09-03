import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def convert_to_webp(input_path, output_path):
    """
    Конвертирует изображение в формат WebP.

    Args:
        input_path: Путь к входному изображению.
        output_path: Путь для сохранения выходного изображения WebP.
    """
    try:
        img = Image.open(input_path)
        img.save(output_path, "webp")
        print(f"Изображение успешно сконвертировано: {output_path}")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")

def select_files():
    """
    Отображает диалоговое окно выбора файлов и запускает конвертацию.
    """
    file_paths = filedialog.askopenfilenames(
        title="Выберите изображения для конвертации",
        filetypes=[
            ("Изображения", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff"),
            ("Все файлы", "*.*")
        ]
    )
    if file_paths:
        output_dir = filedialog.askdirectory(title="Выберите выходную директорию")
        if output_dir:
            for file_path in file_paths:
                base_name = os.path.basename(file_path)
                name, ext = os.path.splitext(base_name)
                output_path = os.path.join(output_dir, name + ".webp")
                convert_to_webp(file_path, output_path)

# Создание главного окна
root = tk.Tk()
root.title("Конвертер изображений в WebP")

# Кнопка для выбора файлов
select_button = tk.Button(root, text="Выбрать изображения", command=select_files)
select_button.pack(pady=20)

# Запуск главного цикла обработки событий
root.mainloop()