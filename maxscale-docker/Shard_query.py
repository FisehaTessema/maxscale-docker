#Name Fiseha Tessema
#Email. fmtessema@student.rtc.edu
#date 03/19/2022
#class CNE 370 


import pymysql

#connect to database 
db = pymysql.connect(host="172.23.0.2", port=4001, user="maxuser", passwd="maxpwd")
cursor = db.cursor()
# print the first 10 rows of zipcodes_one
print('The last 10 rows of zipcodes_one are:')
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one LIMIT 9990,10;")
results = cursor.fetchall()
for result in results:
	print(result)
# print the first 10 rows of zipcodes_two
print('The first 10 rows of zipcodes_two are:')
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two LIMIT 10")
results = cursor.fetchall()
for result in results:
	print(result)

print('The largest zipcode number in zipcodes_one is:')
cursor = db.cursor()
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
results = cursor.fetchall()
for result in results:
	print(result)

print('The smallest zipcode number in zipcodes_two is:')
cursor = db.cursor()
cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two ORDER BY Zipcode ASC LIMIT 1;")
results = cursor.fetchall()
for result in results:
      print(result)
 
