from flask import Flask, request, render_template, flash, redirect, url_for
# import transform
import os
from werkzeug.utils import redirect, secure_filename

# instance relative config allows u to change dir path VIMP
server = Flask(__name__, instance_relative_config=True,template_folder='../client/')
server.static_folder = '../client/'
server.secret_key = "joe mama"

@server.route('/')
def upload_file():
    return render_template('app.html')

@server.route("/upload", methods=["POST", "GET"])
def get_mid():
    if request.method == 'POST':
        try:
            f = request.files["file"]
            server.instance_path = "./server/"
            uploads_dir = os.path.join(server.instance_path, 'user_data')
            os.makedirs(uploads_dir, exist_ok=True)
            f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
            flash("Generated")
            # return render_template('app.html') # add a flash
        except:
            flash("Generated")
            # return "Please Upload a valid midi file"
    flash("Generated")
    return render_template('app.html')
    # return "Error in Uploading midi file, Please try again"

@server.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        try:
            # transform.generate()
            print("GENERATING.....")
            flash("Generated")
            # return render_template('app.html') # add a flash
        except:
            flash("Generated")
            return "Error in generating music"
    flash("Generated")
    return "Error in the predict function "

if __name__ == "__main__":
    print("SERVER started in BackGround")
    server.run(host="127.0.0.1", port="5000", debug=True)
 
