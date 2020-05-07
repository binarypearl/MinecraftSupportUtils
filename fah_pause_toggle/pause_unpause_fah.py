#!/usr/bin/env python3

import subprocess
import re
import time
import argparse
import sys

ip_of_mc_server = ""
port = "25565"

# hard code for now, use argparse:
parser = argparse.ArgumentParser(description='Get IP and port')

parser.add_argument('-s', help='server ip')
parser.add_argument('-p', help='port')

results = parser.parse_args()

ip_of_mc_server = results.s
port = results.p

if ip_of_mc_server == None:
    print ("pause_unpause_fah.py -s server_ip [-p port]")
    sys.exit(1)

ip_of_mc_server = results.s
#print ("port is: " + results['-p'])

#list_of_current_users = []
previous_user_count = "0"
current_user_count = "0"

# have do an initial run to see if we should pause or unpause upon first load
# gahh, this is ugly
p = subprocess.Popen(["./mc_status.py", ip_of_mc_server], stdout=subprocess.PIPE, universal_newlines=True)

output = p.communicate()[0]
output = output.rstrip('\n')

match_object = re.search('^(online_count)(:)(.*)', output)

if match_object:
    current_user_count = match_object.group(3)

    if current_user_count == "0":
        p = subprocess.Popen(["/usr/bin/FAHClient", "--command-address", ip_of_mc_server, "--send-unpause"], stdout=subprocess.PIPE, universal_newlines=True)
        output = p.communicate()[0]
        output = output.rstrip('\n')

        print ("output of FAH unpause: " + str(output))

    else:
        p = subprocess.Popen(["/usr/bin/FAHClient", "--command-address", ip_of_mc_server, "--send-pause"], stdout=subprocess.PIPE, universal_newlines=True)
        output = p.communicate()[0]
        output = output.rstrip('\n')

        print ("output of FAH unpause: " + str(output))

# Just a 1 second pause...
time.sleep(1)

while 1:
    p = subprocess.Popen(["./mc_status.py", ip_of_mc_server], stdout=subprocess.PIPE, universal_newlines=True)

    output = p.communicate()[0]
    output = output.rstrip('\n')

    match_object = re.search('^(online_count)(:)(.*)', output)

    if match_object:
        current_user_count = match_object.group(3)

        #print ("previous_user_count: ***" + previous_user_count + "***")
        #print ("current_user_count: ***" + current_user_count + "***")

        if previous_user_count != current_user_count:
            if current_user_count == "0":
                print ("We unpause FAH here")

                p = subprocess.Popen(["/usr/bin/FAHClient", "--command-address", ip_of_mc_server, "--send-unpause"], stdout=subprocess.PIPE, universal_newlines=True)
                output = p.communicate()[0]
                output = output.rstrip('\n')

                print ("output of FAH unpause: " + str(output))

            else:
                print ("We pause FAH here")

                p = subprocess.Popen(["/usr/bin/FAHClient", "--command-address", ip_of_mc_server, "--send-pause"], stdout=subprocess.PIPE, universal_newlines=True)
                output = p.communicate()[0]
                output = output.rstrip('\n')

                print ("output of FAH unpause: " + str(output))

        previous_user_count = current_user_count

        time.sleep(1)
