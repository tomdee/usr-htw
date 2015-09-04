import urllib2, urllib, json, subprocess,sys, time
url = "https://api.forecast.io/forecast/%s?units=si&exclude=minutely,hourly,daily,alerts,flags" % sys.argv[1]
while True:
	result = urllib2.urlopen(url).read()
	data = json.loads(result)
	subprocess.call("""curl -sS -i -XPOST 'http://influxdb:8086/write?db=tomdee' --data-binary 'temperature,type=forecast,location=vicksburg value=%s
humidity,type=forecast,location=vicksburg value=%s
visibility,type=forecast,location=vicksburg value=%s
apparentTemperature,type=forecast,location=vicksburg value=%s
pressure,type=forecast,location=vicksburg value=%s
windSpeed,type=forecast,location=vicksburg value=%s
cloudCover,type=forecast,location=vicksburg value=%s
windBearing,type=forecast,location=vicksburg value=%s
ozone,type=forecast,location=vicksburg value=%s
precipIntensity,type=forecast,location=vicksburg value=%s'""" %
	(data['currently']['temperature'],data['currently']['humidity']*100,data['currently']['visibility'],data['currently']['apparentTemperature'],data['currently']['pressure'],data['currently']['windSpeed'],data['currently']['cloudCover'],data['currently']['windBearing'],data['currently']['ozone'],data['currently']['precipIntensity']),
	shell=True)
	time.sleep(600)


