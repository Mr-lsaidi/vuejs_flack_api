from flask import Flask, jsonify, request, redirect
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@cross_origin(origin='computer_vision', headers=['Content-Type', 'Authorization'])
def index():
    if (request.method == 'POST'):
        #local url of the image
        url = request.form['image_url']
        print(url)

        #local data of the image
        data = request.files['data']
        print(data)

        #the algo..........................................................#

        #return the ids|json|rest of the product
        example_ids = [1643,3214,53444]
        example_json = {"product_id": 12, "url": "http//.....something...."}
        return jsonify({"restult1" : example_ids} ,{"restult2" : example_json} )
    else:
        return jsonify({"computer_vision_api" : "hello !"})

if __name__ == "__main__":
    app.run(debug=True)