import MySQLdb as mdb
import sys
from position import Position
# Handler taking care of the operations on the Database

def connectToDB():
    return mdb.connect('localhost', 'mdepart_user', 'mdepartRaspberry', 'mDepart')
    
def closeDBConnection( connection ):
    if connection:
            connection.close()

def executeOnDB(connection, query ):
    try:
        cursor = connection.cursor(mdb.cursors.DictCursor)
        print( query )
        cursor.execute( query )
    
        rows = cursor.fetchall()
        print rows
    
        if len( rows ) == 0:
            return None
        elif len( rows ) == 1:
            return rows[0]
        else:
            return rows
    
    except mdb.Error, e:
        print "[Error] %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    
    finally:
        closeDBConnection( connection )

def display( result_of_query ):
    if type( result_of_query ) is list:
	print len( result_of_query )+" results in query"
	for result in result_of_query:
	    print result
    else:
	print result_of_query

# Treatment functions
def translateToPosition( tuple ):
    position = Position()
    position.lat = tuple["latitude"]
    position.lon = tuple["longitude"]
    return position

def getHomeFromDB( connection ):
    return translateToPosition( executeOnDB( connection, "SELECT positions.latitude, positions.longitude FROM locations JOIN positions ON locations.position_id=positions.id WHERE locations.name = 'home';" ) )

def insertIss( connection, Date, Duration ):
    executeOnDB( connection, "INSERT INTO iss (timestamp, date, duration) VALUES (NOW(), FROM_UNIXTIME(%s), '%s');" % ( Date, Duration ) );

def insertTransport( connection, line, direction, time, location_id ):
    executeOnDB( connection, "INSERT INTO transportation (timestamp, line, direction, time_of_arrival, location_id ) VALUES (CURTIME(), %s, %s, %s, %d);" % (line, direction, time, location_id) )

def addLocationByPosition( connection, name, lat, lon, is_transportation ):
    executeOnDB( connection, "INSERT INTO positions (latitude, longitude) VALUES ('%s', '%s');" % ( lat, lon ) )
    tuple = executeOnDB( connection, "SELECT id FROM positions WHERE latitude = '%s' AND longitude = '%s';" % ( lat, lon ) )
    id = tuple[ 'id' ]
    print id
    executeOnDB( connection, "INSERT INTO locations (name, position_id, is_transportation_stop) VALUES (%s, %d, %s);" % (name, id, is_transportation) )

connection = connectToDB()
insertIss( connection, '1400538608', '123' )
