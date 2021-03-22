

from flask import Flask, render_template, request
import requests


app = Flask(__name__)
@app.route('/')
def index():
	r1 = requests.get('https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_ENmL9U377EwxiUFtSpLd4B5fuhUQC')
	json_object1 = r1.json()
	cityname = json_object1["location"]["city"]

	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid=545b6bc00ae6265f871ac2212005c0c0')
	json_object = r.json()
	temp_k = float(json_object['main']['temp'])
	temp_c = round((temp_k - 273.15) , 2)
	mintemp_k = float(json_object['main']['temp_min'])
	mintemp_c = round((temp_k - 273.15) , 2)
	maxtemp_k = float(json_object['main']['temp_max'])
	maxtemp_c = round((temp_k - 273.15) , 2)
	sky = (json_object['weather'][0]['description']).capitalize()
	hum = json_object['main']['humidity']
	iconurl =str("http://openweathermap.org/img/w/"+json_object['weather'][0]['icon'] +".png")
	return render_template("weather.html", temp = temp_c, mintemp = mintemp_c, maxtemp = maxtemp_c, sky = sky,cityname=cityname, url= iconurl, hum = hum)   





if __name__ == "__main__":
    app.run(debug = True)
