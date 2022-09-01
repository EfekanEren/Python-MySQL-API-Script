from ast import main
from turtle import update
import requests
import json
import pymysql
import sys
import datetime

x = datetime.datetime.now()

proxies = {
    'http': 'PROXY',
    'https': 'PROXY'
}
                                                                                                                                                           
r=requests.get('API URL', proxies=proxies)
package_json=r.json()

con = pymysql.connect(host = 'localhost', user = 'benutzername', passwd = 'passwort', db = 'dbname')
cursor = con.cursor()

def validate_string(val): 
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val

print (json.dumps (package_json))

# y = json.loads(package_json)

# Tiefsttemperatur, Höchsttemperatur, Luftfeuchtigkeit
temp = package_json["main"]["temp"]
max_temp = package_json["main"]["temp_max"]
min_temp = package_json["main"]["temp_min"]
lf = package_json["main"]["humidity"]
druck = package_json["main"]["pressure"]
wind = package_json["wind"]["speed"]
s_a = package_json["sys"]["sunrise"]
s_u = package_json["sys"]["sunset"]
wolken = package_json["clouds"]["all"]


zeit = x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + "-" + x.strftime("%H:%M:%S")



sql = "INSERT INTO tabellenname (zeit, temperatur, maxtemperatur, tiefsttemperatur, feuchtigkeit, druck, windgeschwindigkeit, sonnenaufgang, sonnenuntergang, wolken) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (zeit, temp, max_temp, min_temp, lf, druck, wind, s_a, s_u, wolken)

cursor.execute(sql, val)
con.commit()

sys.exit()