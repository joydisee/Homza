import time
import requests
from position import Position
from DBhandler import *
# We'll get the location itself with the HTML5 API from the configuration page

# import socket
# import pygeoip
#To get the position through IP location

# We still need to calculate the distance and the time it takes 
def getDurationOfTravel( position1 , position2 ) :
    # Speed to walk ? (in km/h)
    speed = 5.0
    request_url = "http://router.project-osrm.org:5000/viaroute?loc="+str(position1.lat)+","+str(position1.lon)+"&loc="+str(position2.lat)+","+str(position2.lon)
    print "Sending request : %s" % request_url
    response = requests.get(request_url)
    # Analyse response (in JSON)
    responseJSON = response.json;
    pprint( responseJSON )
    if response_JSON.status == 0:
        route_length = response_JSON.route_summary.total_distance
        time_to_go = route_length / ( speed * 1000.0 / 3600.0 )
        nameToPrint = "test"
        print nameToPrint
        print "Take %.2f seconds to go from %s to %s" % (time_to_go, position1.name, position2.name)
    
    return time_to_go
            

def getDurationOfTravelFromHomeTo( position ):
    home = getHomeFromDB()
    return getDurationOfTravel( home , position )

#JE commente tout ca parce que ca marche pas et que je voudrais tester la suite quand meme
position1 = getHomeFromDB()
#position1.name = "test home"
#position1.lat = 53.2734
#position1.lon = -7.77832031
position2 = Position()
position2.name = "test destination"
position2.lat = 48.8424001
position2.lon = 2.2341749
getDurationOfTravel( position1, position2 )

# r = requests.get(r'http://jsonip.com')
# ip= r.json()['ip']
# print 'Your IP is', ip 
# 
# 
# gi = pygeoip.GeoIP('GeoIP.dat')
# #GeoIP.dat is necessary for country finding
# print "Country=", gi.country_name_by_addr(ip)
# 
# gi = pygeoip.GeoIP('GeoLiteCity.dat')
# gi = r.json()['city']
# print "City=", gi.record_by_addr(ip)

#def get_IP_location( IP ):
  
  
