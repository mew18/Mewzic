from flask import Flask, request
import transform
import os
from werkzeug.utils import secure_filename

#  min the number of imports

# tweak port settings
# instance relative config allows u to change dir path VIMP
server = Flask(__name__, instance_relative_config=True)

# coz template html does not server REST reqs

@server.route('/')
def upload_file():
    return render_template('../client/app.html')

@server.route("/get", methods=["POST", "GET"])
# u know u can change routes to diff dir to exec diff function
def get_mid():
    if request.method == 'POST':
        f = request.files['file']

        server.instance_path = "./server/"
        uploads_dir = os.path.join(server.instance_path, 'user_data')
        os.makedirs(uploads_dir, exist_ok=True)

        f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
        # transform.generate()

        # think of going back to home page after this
        # print(transform.generate())
        return 'midi uploaded successfully'

# m8 optimize the shit out of this


@server.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        print("\n\n\nPREDICTING ........")
        print(transform.generate())
    return "GENERATED"


if __name__ == "__main__":
    print("SERVER started in BackGround")
    server.run(host="127.0.0.1", port=666, debug=True)
