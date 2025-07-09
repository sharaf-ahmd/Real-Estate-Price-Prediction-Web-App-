from flask import Flask,request,jsonify
from flask_cors import CORS
import util




app=Flask(__name__)
CORS(app)


@app.route('/get_city')
def get_city():
    response=jsonify({
        'city':util.get_city()
    })
    response.headers.add('Access-ControlAllow-Origin','*')
    return response

@app.route('/predict_price',methods=['POST'])
def predict_price():
    city=request.form['city']
    land_size=float(request.form['land'])
    house_size=float(request.form['house'])
    lat=float(request.form['lat'])
    lon=float(request.form['lon'])


    response=jsonify({
        'Prediction':util.get_prediction(city,land_size,house_size,lat,lon)
    })
    return response



if __name__=='__main__':
    app.run(debug=True)