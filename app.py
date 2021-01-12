from flask import Flask, request, render_template, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename

# instance relative config allows u to change dir path VIMP
app = Flask(__name__, instance_relative_config=True, template_folder='client/')
app.static_folder = 'client/'
app.secret_key = "joe mama"


@app.route('/')  # this decides if you need to run html or not
def init():
    return render_template('app.html')


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        try:
            f = request.files["file"]
            app.instance_path = "server"
            uploads_dir = os.path.join(app.instance_path, 'user_data')
            # os.makedirs(uploads_dir, exist_ok=True)
            f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
            flash("Uploaded", 'upload')
            return redirect(request.referrer)
        except Exception as e:
            print(e)
            return "Catch :Error in Uploading ,Please Upload a valid midi file"
    else:
        return redirect(request.referrer)


@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        try:
            import find_mid
            if find_mid.mid_exist() == True:
                import transform
                print(transform.generate())
                flash("Generated", 'predict')
                return redirect(url_for('predict'))
            else:
                return "Please Upload a valid midi file, then Generate Music"
        except Exception as e:
            print(e)
            return str(e)

    else:
        return redirect(url_for('init'))


if __name__ == "__main__":
    print("app started in BackGround")
    app.run()
    
    
    
    
    
    
    
    
    
