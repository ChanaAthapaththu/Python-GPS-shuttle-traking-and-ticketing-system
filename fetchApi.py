import requests
import json

pload = { 'Origin':'https://esfm.dialog.lk',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept':'*/*',}


r = requests.post('https://esfm.dialog.lk/api-v2/tracker/get_states',data = 'hash=8b64f84b0b87681b0ac92a81a565670b&list_blocked=true&trackers=%5B473754%2C473755%2C473757%2C473758%5D',headers=pload)


j = r.json()

latitude=j['states']['473758']['gps']['location']['lat']
longitude=j['states']['473758']['gps']['location']['lng']
movement_status=j['states']['473758']['movement_status']

print("Metro Shuttle")
print ("Latitude : ",latitude)
print ("Longitude : ",longitude)
print ("Movement Status: "+movement_status)