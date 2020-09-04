from flask import Flask, request, render_template, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
import shutil

# instance relative config allows u to change dir path VIMP
server = Flask(__name__, instance_relative_config=True, template_folder='../client/')
server.static_folder = '../client/'
server.secret_key = "joe mama"


@server.route('/')  # this decides if you need to run html or not
def init():
    return render_template('app.html')


@server.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        try:
            f = request.files["file"]
            server.instance_path = "./server/"
            uploads_dir = os.path.join(server.instance_path, 'user_data')
            os.makedirs(uploads_dir, exist_ok=True)
            f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
            flash("Uploaded", 'upload')
            return redirect(request.referrer)
        except Exception as e:
            print(e)
            return "Catch :Error in Uploading ,Please Upload a valid midi file"
    else:
        return redirect(request.referrer)


@server.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        try:
            import find_mid
            if find_mid.mid_exist() == True:
                import transform
                print(transform.generate())
                # try:
                #     shutil.copy("./server/user_data/output.mp3", "client/")
                # except Exception as e:
                #     print(e)
                #     print("Again error in moving")
                flash("Generated", 'predict')
                return redirect(url_for('predict'))
            else:
                return "Please Upload a valid midi file, then Generate Music"
        except Exception as e:
            print(e)
            return str(e)
            # return "Catch: Error in Generating Music"
    else:
        return redirect(url_for('init'))
        # return redirect(request.referrer)


if __name__ == "__main__":
    print("SERVER started in BackGround")
    server.run(host="127.0.0.1", port="5000", debug=True)
