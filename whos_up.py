#You absolutely need these 2 imports at the beginning of your script to be able to use these functions, also you mest be in the same folder
from couchdb_handler import *
import time
import nmap

#Initialisation
user_mac=[]
unknown_mac=[]
up_users=0
main_up_users=[]
main_unknown_users=[]
#Checking MAC Address Status
#We create a nm object that will be used to scan the network
nm = nmap.PortScanner()
#We give the scan parameter, and perform the scan
nm.scan(hosts = '192.168.1.0/24', arguments = '-n -sP -PE -T5')
a=0
while (a<2):
	up_macs=[]
	i=0
	timeString = retrieve_time()
	while i<5:
		######### UPDATING DATABASE ##############
		for host in nm.all_hosts():	
		######### LIST MAC ADDRESS ################
			# If the status of an element is not down, we print it
			if nm[host]['status']['state'] != "down":
				try:
					if str(nm[host]['addresses']['mac']) not in up_macs:
						up_macs.append( str(nm[host]['addresses']['mac']))
				except:
					mac = 'unknown'
		###########################################

		print "UP MACS: ", up_macs
		known_macs=retrieve_known_macs()
		print "KNOWN MACS: ",retrieve_known_macs()

		######### AVAILABLE USERS ################
		up_known_macs=compare_list(up_macs,known_macs)
		nb_users_up= len(up_known_macs)
		nb_users_unknown=len(up_macs)-len(up_known_macs)

		print nb_users_up, "known users in range"
		print nb_users_unknown, "unknown users in range"


		print "UPDATE DONE FOR: " 
		for macs in up_known_macs:
			update_last_seen_time(retrieve_user_for_mac(macs),timeString)
			up_known_macs_name=retrieve_user_for_mac(macs)
			print up_known_macs_name
	
		###########################################


		#Update a user's last_seen_time
		i=i+1
		time.sleep(2)
		print display_status()
	time.sleep(180)		


	
