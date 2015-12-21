#You absolutely need these 2 imports at the beginning of your script to be able to use these functions, also you must be in the same folder
from couchdb_handler import *
import couchdb


#Create a new user
user = "Ilyass"
macs = ["8C:3A:E3:3E:56:26"]
url_img = 'https://lh6.googleusercontent.com/-wE_smH6tICw/ThTE50L4KNI/AAAAAAAASVI/M8LjNWA7dNs/w1051-h701-no/IMG_3687.JPG'
music = "ilyass.mp3"
#The function add_user checks if the user is already existing in the database
add_user( user, macs ,url_img,music)

user = "Joe"
macs = ["BC:77:37:E7:0B:49", "34:FC:EF:CB:A1:BB" ]
url_img = 'https://lh6.googleusercontent.com/kY8GSNBoURvFIXX2ox55AmN1QF7p-RbZsOhw_QyRsw=w717-h701-no'
music = "joe.mp3"
add_user( user, macs ,url_img,music)

user = "Yahya"
macs = ["98:D6:F7:6A:52:13", "80:56:F2:70:85:DB" ]
url_img = 'https://lh4.googleusercontent.com/-yGbpROABGlw/UHFTVY4qQ9I/AAAAAAAAAKg/AiluU0GSaIE/w601-h602-no/IMG_3361.JPG'
music = "yahya.mp3"
add_user( user, macs ,url_img,music)

user = "Gael"
macs = ["40:78:6A:C2:1C:06","80:56:F2:08:AE:45"]
url_img = 'https://cbsmontrealchapter.files.wordpress.com/2015/02/gael.jpg'
music = "gael.mp3"
add_user( user, macs ,url_img,music)

user = "Adrien"
macs = ["40:B8:37:AC:87:69","34:68:95:ED:54:73"]
url_img = 'data:image/jpeg;base64,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'
music = "adrien.mp3"
add_user( user, macs ,url_img,music)


#Creates a view in CouchDB which allows us to use retrieve_user_for_mac( mac 
create_view_for_macs( )
create_view_for_house()
# Retrieve the user corresponding to a MAC address
#mac = "98:D6:F7:6A:52:13"
#retrieve_user_for_mac( mac )


#Update a user's last_seen_time

#update_last_seen_time( "ilyass", "now" )
#update_last_seen_time( "lussylver", "yesterday" )
#update_last_seen_time( "joe", "tomorrow" )

#How to display data
all_status = display_status()
for list_user in all_status:
	print str(list_user[0]), "=", str(list_user[1])