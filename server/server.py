from flask import Flask, request, render_template
# import transform
import os
from werkzeug.utils import secure_filename

# tweak port settings
# instance relative config allows u to change dir path VIMP
server = Flask(__name__, instance_relative_config=True,template_folder='../client/')
server.static_folder = '../client/'

# coz template html does not server REST reqs


@server.route('/')
def upload_file():
    return render_template('app.html')
0
# u know u can change routes to diff dir to exec diff function


@server.route("/upload", methods=["POST", "GET"])
def get_mid():
    if request.method == 'POST':
        try:
            f = request.files["file"]
            server.instance_path = "./server/"
            uploads_dir = os.path.join(server.instance_path, 'user_data')
            os.makedirs(uploads_dir, exist_ok=True)
            f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
            # return "midi uploaded successfully"
            return render_template('app.html')        
        except:
            return "error"
    return "Error"


@server.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        try:
            print("\n\n\nPREDICTING ........")
            # print(transform.generate())
            # return "GENERATED"
            return render_template('app.html')
        except:
            return "error"
    return "Error"

if __name__ == "__main__":
    print("SERVER started in BackGround")
    server.run(host="127.0.0.1",port="5000",debug=True)
