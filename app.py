from flask import Flask, render_template, request, send_file
import qrcode
import hashlib
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    

@app.route('/qr', methods=['GET'])
def generate_qr():
    data = request.args.get('data')
    box_size = int(request.args.get('box_size', 10))  # 获取传递的 box_size 参数，默认为 10

    # Compute the hash of the input data (assuming it is a string)
    data_hash = hashlib.sha256(data.encode()).hexdigest()
    filename = f"{data_hash}.png"

    # Check if the QR code with the same data already exists
    if not os.path.exists(filename):
        qr = qrcode.QRCode(version=1, box_size=box_size, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        # Save the QR code image with the hash-based filename
        img.save(filename)

    # Return the QR code image to the user
    return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5123, debug=True)
