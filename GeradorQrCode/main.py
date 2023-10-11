from flask import Flask, render_template, request
import qrcode
from PIL import Image
import base64
import io

app = Flask(__name__)

# Função para criar o código QR
def generate_qr_code(url):
    qr = qrcode.make(url)
    # Salvando o QR code em memória
    qr_byte_array = io.BytesIO()
    qr.save(qr_byte_array, format='PNG')
    qr_byte_array = qr_byte_array.getvalue()
    qr_base64 = base64.b64encode(qr_byte_array).decode('utf-8')
    return qr_base64

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = None
    if request.method == 'POST':
        url = request.form['url']
        qr_code = generate_qr_code(url)
    return render_template('index.html', qr_code=qr_code)

if __name__ == '__main__':
    app.run(debug=True)
