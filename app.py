from flask import Flask,request,jsonify,make_response
from flask_cors import CORS
from flask_restful import Resource,Api
import time,json,os
from subprocess import check_output

app = Flask(__name__)
app.config["SECRET_KEY"] = "somesecretkey"
CORS(app)                                                   #Cross Origin Resource Sharing
api = Api(app)

class Code(Resource):
    def post(self):
        print("Request recieved: ")
        code = (json.loads(request.data)[0])['code']
        ts = time.time()
        fname = "files/"+str(ts)+".py"
        f = open(fname,"w+")
        f.write(code)
        f.close()
        out = check_output(["python",fname]).decode('utf-8')
        os.remove(fname)
        print(out)
        return out       

api.add_resource(Code,"/code")

@app.route('/')
def index():
    return "<h1>Working</h1>"

if __name__ == "__main__":
    app.run(debug=True)