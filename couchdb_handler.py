from couchdb import *
import time
from couchdb.design import ViewDefinition
import urllib2

# Creates a connection
def connect_to_db():
	#couch.resource.credentials = ("admin", "admin")
	return Server('http://localhost:5984')

# Creates a DB or loads it
def create_or_load_db( couch, database_name ):
	# Try to get the database 
	try:
		return couch[ database_name ]
	# Or create it if it is not already
	except ResourceNotFound:
		return couch.create( database_name )

def add_user( user, macs ):
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	
	# Let's check if the user exists already by trying to get it, and if it is not here, it means we can add it 
	try:
		#You can then use the object *db* to directly check a document through its _id, remember that we use urls as ids since a url is unique
		doc = db[ user ]
		#The object *doc* contains the document from the users databse which _id is url_rss
		print "[couch-add_user] %s is already a user in the database" % user
	except ResourceNotFound:
		dict_field_values = {
			'_id'  : user,
			'macs'  :macs
		}
		#The object *db* has a create method, and this is how you create a document
		return db.create( dict_field_values )

def create_view_for_macs():
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	
	rpt_view = ViewDefinition(
			'list',
			'macs',
			'''function(doc) {
				for( i in doc.macs ){
                 		emit( doc.macs[i], doc._id  );}
			}''')
	rpt_view.sync( db )

def retrieve_user_for_mac( mac ):
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	
	for row in db.view( "_design/list/_view/macs" ):
		if mac == row.key:
			row_id = row.id
	return row_id

def check_users( address_mac, user_mac, unknown_mac ):
#user_mac is a list of the people already registred in our DB
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )
	for row in db.view( "_design/list/_view/macs" ):
		if address_mac == row.key:
			user_mac.append(address_mac)
			break
		else:
			unknown_mac.append(address_mac)
			break

#Returns a list containing all known MAC addresses
def retrieve_known_macs():
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )
	known_macs = []

	for row in db.view( "_design/list/_view/macs" ):
		known_macs.append( row.key )

	return known_macs
			
def update_last_seen_time( user, time ):
	
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	

	doc = db[ user ]
	doc['last_seen_time'] = time

	db.save(doc)

def retrieve_time():
	localtime=time.localtime()
	timeString =time.strftime("%Y%m%d%H%M%S",localtime)
	human_time=time.strftime("%Y/%m/%d  %H:%M:%S",localtime)
	return human_time,timeString

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

def compare_list(list1, list2):
	list_common_macs=[]
    	for i in range (0,len(list1)):
		for j in range(0, len(list2)):
			if list1[i]==list2[j]:
				list_common_macs.append(list1[i])
	return list_common_macs

