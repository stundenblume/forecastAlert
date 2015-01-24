/*******************************************
 * Name.......:  forecastAlert
 * Description:  This program will check the wind forecast for defined locations, if the forecast is in a flyable range, it will inform you
 * Author.....:  Sebastian Setz
 * Date.......:  2015-01-24
 * Project....:  -
 * Contact....:  http://Sebastian.Setz.name
 * License....:  This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
 * Credit.....:  -
 * Keywords...:  python, paragliding, kitesurfing, flyable, kiteable, alert, forecast
 * History....:  2015-01-24 - release
 ********************************************/


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import forecastio

# get your APIkey at http://developer.forecast.io
api_key = "f421991e6fe4d17a34cbf67ec3e24eaa"

# Name of the location, lat location, lon location, flyable winddirection from[°], to[°]
locations = [["Petten",52.7621289,4.6689374,250,310],["Norderney",53.7119469,7.2426931,330,10],["Fehmarn",54.4686978,11.158683,340,110],["Fuerte",28.1608674,-14.2247672,0,360]]

kmhFaktor=1.609344 # to calculate kmh from mph
minWS=12 # minimal WS where flying is possible
maxWS=30 # maximal flyable WS

# this def will check if the WD is in range and returns 0 or 1
def checkWR(richtung, von, bis):
	if von > bis:
		if richtung>=von or richtung<=bis:
			return 1
		else:
			return 0
	else:
		if richtung>=von and richtung<=bis:
			return 1
		else:
			return 0
			
print "min WS: "+str(minWS)+" kmh"
print "max WS: "+str(maxWS)+" kmh"

for location in locations:
	
	print "======================"
	print "Getting Information :"
	print location
	print "---------------------"

	# pulling forecast from http://forecast.io
	forecast = forecastio.load_forecast(api_key, location[1], location[2])
	
	for data in forecast.hourly().data:
		# check if WD and WS is in a flyable range for the location
		if checkWR(data.windBearing, location[3], location[4]) and data.windSpeed*kmhFaktor>=minWS and data.windSpeed*kmhFaktor<=maxWS:
			print ""+location[0]+"! "+str(data.time)[2:-3]+", "+str(data.windBearing)+"[°], "+str(data.windSpeed*kmhFaktor)[:4]+"[kmh], "+str(data.temperature)+"[°C], Niederschlag:"+str(data.precipIntensity)
	
