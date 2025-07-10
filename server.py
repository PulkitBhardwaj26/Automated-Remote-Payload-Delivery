from flask import Flask, render_template, send_file, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/client.py')
def serve_client():
    try:
        # Serve client.py file from current directory
        return send_file('client.py', as_attachment=True)
    except Exception as e:
        return f"Internal Server Error: {e}", 500

@app.route('/upload', methods=['POST'])
def upload_screenshot():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    upload_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    return jsonify({'message': f'File {file.filename} uploaded successfully.'})

if __name__ == '__main__':
    app.run(port=5000)
