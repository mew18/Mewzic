from flask import Flask, request
from flask.helpers import flash
import get_req
import os
from werkzeug.utils import secure_filename

# tweak port settings
# instance relative config allows u to change dir path VIMP
server = Flask(__name__, instance_relative_config=True)

# coz template html does not server REST reqs
@server.route('/')
def upload_file():
   return render_template('../client/app.html')


@server.route("/",methods=["POST", "GET"])
# u know u can change routes to diff dir to exec diff function

def get_mid():    

    if request.method == 'POST':
        
        f = request.files['file']
        
        server.instance_path = "./server/"
        uploads_dir = os.path.join(server.instance_path, 'user_upload_data')
        os.makedirs(uploads_dir, exist_ok=True)

        # f.filename = "user_ip.mid"
        f.save(os.path.join(uploads_dir,secure_filename(f.filename)))
        # f.save(f.filename)

        # think of going back to home page after this
        return 'midi uploaded successfully'

# m8 optimize the shit out of this
def pred():
    print("Importing libraries ....")
    from keras.models import load_model
    import numpy as np

    data=get_req.get_data()

    # data = request.get_json()
    
    pred_ip = np.reshape(data, (1, len(data), 1))
    pred_ip = pred_ip/len(pred_ip)

    print("Predicting  ....")
    model = load_model('./model/mewzic_model.h5')
    prediction = model.predict(pred_ip)

    #  process the data from midi into array and then feed into the model , maybe think of adding that convert file separetly

    # print_tensor(prediction)
    pred_op = np.around(prediction, 2)
    pred_op = ' '.join(map(str, prediction))
    return pred_op

if __name__ == "__main__":
    print("SERVER started in BackGround")
    server.run(host="127.0.0.1",port=666,debug=True)
