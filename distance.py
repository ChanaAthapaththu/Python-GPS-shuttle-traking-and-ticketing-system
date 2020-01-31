import requests
import json
# importing googlemaps module 
import googlemaps 
  
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyBq1BVBkJ1HdIozp8nT75MuObWGQFTe-5w') 
  
# Requires cities name 
my_dist = gmaps.distance_matrix(' 6.9271,79.8612','7.4818,79.9579466')['rows'][0]['elements'][0] 
  
# Printing the result 
print(my_dist)
distance= my_dist['distance']['text']
print('===============================')
print('Traveled Distance: ',distance)
print('===============================')
rate=float(1.5000)
if (distance.find('km') != -1):
        q=float(distance.replace('km',''))
        busfee=q*rate
        print("Bus fare:Rs",busfee)
        
        
else: 
    q=float(distance.replace('m',''))
    busfee1=rate*q/float(1000)
    print("Bus fare:Rs",busfee1)
           

