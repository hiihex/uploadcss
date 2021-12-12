from flask import Flask, render_template, request, jsonify, Response
import shortuuid, os
app = Flask(__name__)

css_watermark = "/* Css hosted on uploadcss.io. Service created by Kacper Slenzak */ \n"

@app.route('/')
def index():
    return render_template('index.html')

def uploadCssFile(code):
    unique_file_name = shortuuid.uuid()
    file_path = os.path.join('/Users/kacperslenzak/Dev/uploadcss.io/static/uploads', f'{unique_file_name}.css')
    with open(file_path, "a") as f:
        f.write(css_watermark)
        f.write(code)
    return unique_file_name

@app.route('/upload_code', methods=['POST'])
def uploadCode():
    if request.method == "POST":
        css_code = request.form['code']
        captcha = request.form['captcha']
    if captcha == "":
        error_message = jsonify({"message":"Please complete the captcha!"})
        return error_message, 500
    uploaded_file = uploadCssFile(css_code)
    return {"filename":uploaded_file}
