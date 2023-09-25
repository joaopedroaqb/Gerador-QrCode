import tkinter as tk
import qrcode
from PIL import Image, ImageTk

# Função para criar o código QR
def generate_qr_code():
    url = entry.get()  # link inserido pelo usuário
    qr = qrcode.make(url)
    qr.save('qrcode.png')
    
    # Exibe o código QR na interface gráfica
    qr_image = Image.open('qrcode.png')
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.photo = qr_photo

# Cria a janela principal
root = tk.Tk()
root.title('Gerador de QR Code')

# Cria um frame para organizar os widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Onde coloca o link
url_label = tk.Label(frame, text='Insira o link:', font=('Helvetica', 12))
url_label.grid(row=0, column=0, columnspan=2, pady=10)

entry = tk.Entry(frame, width=40)
entry.grid(row=1, column=0, columnspan=2, padx=10)

# Botão 
generate_button = tk.Button(frame, text='Gerar QR Code', font=('Helvetica', 12), command=generate_qr_code)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

#Exibi o Qr code
qr_label = tk.Label(frame)
qr_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
