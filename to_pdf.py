import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title('конвертация PDF')


canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

# лого
logo = Image.open('logo1.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# функция открытия файла
def open_file():
    brose_txt.set('загрузка...')
    file = askopenfile(parent=root, mode='rb', title='Выбрать файл', filetype=[('Pdf file', '*.pdf')])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # вывод текста
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=3)

        brose_txt.set('Загрузить')

# инструкции
instructions = tk.Label(root, text='Выберите файл PDF на компьютере для его конвертации', font='Ravie')
instructions.grid(columnspan=3, column=0, row=1)

# кнопка загрузки файла
brose_txt = tk.StringVar()
brose_button = tk.Button(root, textvariable=brose_txt, command=lambda: open_file(), font='Ravie', bg='#0C4BA5', fg='white', height=3, width=15)
brose_txt.set('Загрузить')
brose_button.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()