#!/usr/bin/env python3

import re
import sys
import operator
import csv

#initial variables

filepath="./syslog.log"
error={}
per_user={}

#open log file and read lines

with open(filepath, 'r') as f:
    for line in f.readlines():
        result = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[#0-9]*\]?]? ?\((.*)\)$", line)
        msg_type, msg_content, user = result.group(1), result.group(2), result.group(3)
        #print(msg_type, msg_content,user)

        if msg_type =="ERROR":
            if msg_content not in error.keys():
                error[msg_content]=1
            else:
                error[msg_content] += 1

        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]["ERROR"] = 0
            per_user[user]["INFO"] = 0

        if msg_type =="ERROR":
            per_user[user]["ERROR"] += 1

        if msg_type =="INFO":
            per_user[user]["INFO"] += 1

f.close()

#sort result

error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse = True)
per_user_sorted = sorted(per_user.items(), key = operator.itemgetter(0))


print(error_sorted)

print(per_user_sorted)

#write result to csv

with open("error_message.csv", "w", newline = "") as e_csv:
    error_sorted.insert(0,("Error", "Count"))
    for key, value in error_sorted:
        e_csv.write(str(key) + "," + str(value) + "\n")
e_csv.close()

with open("user_statistics.csv", "w", newline = "") as user_csv:
    header = csv.DictWriter(user_csv, delimiter=",", fieldnames = ["Username","INFO","ERROR"])
    header.writeheader()
    for key, value in per_user_sorted:
        user_csv.write(str(key) + "," + str(value["INFO"]) + "," + str(value["ERROR"]) + "\n")

user_csv.close()
    #print(per_user_sorted)


#with open("user_statistics.csv", "w", newline = "") as user_csv:
#    for key, value in per_user_sorted:
#        user_stat_csv.write(str(key) + "," + str(value["INFO"]) + "," + str(value["ERROR"] + "\n")
#user_csv.close()