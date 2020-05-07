#!/usr/bin/python3

# STILL UNDER DEVELOPMENT - 05-06-2020

import urllib.request
import json
import subprocess
import re

minecraft_dir = "/home/smiller/sandbox/minecraft/"
minecraft_world = "notimetowaste"
second_backup_dir = "/mnt/backups/shaun/"

with urllib.request.urlopen('https://launchermeta.mojang.com/mc/game/version_manifest.json') as response:
    content = response.read()

latest_release_json_output = json.loads(content)

latest_release = latest_release_json_output["latest"]["release"]

# Because they put the latest url at top, we can get wait using 0 here...JSON is so weird.
latest_url = latest_release_json_output["versions"][0]["url"]
#print (latest_url)

process = subprocess.run(['/usr/bin/jar', 'xf', minecraft_dir + 'server.jar', 'version.json'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
    
#print(process.stdout)

# Get version of minecraft to replace:
version_json_file_object = open(minecraft_dir + 'version.json', 'r')

for record in version_json_file_object:
    match_object = re.search('(\"id\": )(\")(.*?)(\",)', record)

    if match_object:
        version_to_replace = match_object.group(3)    

# Backup:
process = subprocess.run(['cp', '-vpr', minecraft_dir + minecraft_world, minecraft_dir + minecraft_world + '-' + version_to_replace], check=True, stdout=subprocess.PIPE, universal_newlines=True)

process = subprocess.run(['tar', '-cvpf', second_backup_dir + minecraft_world + "-" + version_to_replace + ".tar", minecraft_world], check=True, stdout=subprocess.PIPE, universal_newlines=True)

# Get pid of current java process and kill it:
# ps -ef | grep server.jar | grep -v grep | awk '{print $2}' | xargs kill -9
#process = subprocess.run(['ps', '-ef', '|', 'grep', 'server.jar', '|', 'grep', '-v', 'grep'],  check=True, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
#p1 = Popen(['ps', '-ef'], stdout=PIPE)
#p2 = Popen(['grep', 'server.jar', stdout=PIPE)
#p3 = Popen(['grep', '-v', 'grep', stdout=PIPE)

###output = subprocess.check_output("ps -ef | grep server.jar | grep -v grep | awk '{print $2}' | xargs kill -9", shell=True)

# Now download latest server.jar:
###urllib.request.urlretrieve(latest_url, 'server.jar')

# Now start the server back up:
###output = subprocess.check_output("nohup java -Xmx1024M -Xms1024M -jar /home/smiller/minecraft/server.jar", shell=True)
