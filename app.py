from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def temperature():
	cityname = (request.form['name']).capitalize()
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid=545b6bc00ae6265f871ac2212005c0c0')
	json_object = r.json()
	if json_object['cod'] == '404':
	  return render_template("error.html", message = "City not found") 
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

@app.route('/currentloction')
def currloc():
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
	return render_template("currentloction.html", temp = temp_c, mintemp = mintemp_c, maxtemp = maxtemp_c, sky = sky,cityname=cityname, url= iconurl, hum = hum)   

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':  
   app.run(debug = True)  










