#!/bin/usr/env python3

import urllib.request
import json
import turtle


## Trace the ISS - earth-orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

## Call the webserv
trackiss = urllib.request.urlopen(eoss)

## put into file object
ztrack = trackiss.read()

## JSON 2 Python data structure
result = json.loads(ztrack.decode('utf-8'))

## display our Pythonic data
print("\n\nConverted Python data")
print(result)
input('\nISS data retrieved & converted. Press any key to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)

screen.setworldcoordinates(-180, -90, 180,90)
screen.bgpic("iss_map.gif")

screen.register_shape("spriteiss.gif")
iss = turtle.Turtle()
iss.shape("spriteiss.gif")
iss.setheading(90)

lon = round(float(lon))
lat = round(float(lat))

iss.penup()
iss.goto(lon, lat)
turtle.mainloop()
