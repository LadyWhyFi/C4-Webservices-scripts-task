#!/usr/bin/python

#roussel_yanah@hotmail.be
#23/12/2018

#SERVICE REQUESTER

#The xmlrpclib module lets you communicate from Python with any XML-RPC server written in any language

import xmlrpc.client
import xmlrpc

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
#proxy = xmlrpc.client.ServerProxy('http://localhost:9000', verbose=True)

#print((proxy.system.listMethods()))

multicall = xmlrpc.client.MultiCall(proxy)


multicall.get_weather_station_location()
multicall.get_weather_station_coordinates()
multicall.get_date()
multicall.get_line()
multicall.get_temperature()
multicall.get_wind_speed()
multicall.get_wind_direction()

results = multicall()

for result in results:
	print (result)

#print("Weather station:", multicall.get_weather_station_location())

#print("Coordinates:", multicall.get_weather_station_coordinates())

#print("=" * 50)

#print(multicall.get_temperature(), "degrees Celcius")

#print(multicall.proxy.get_wind_speed(), "Beaufort", multicall.proxy.get_wind_direction())

