
## Final group Project CNE 370


### Introduction 
Sharding is a method for distributing a single dataset across multiple databases, which can then be stored on multiple machines. This allows for larger datasets to be split in smaller chunks and stored in multiple data nodes, increasing the total storage capacity of the system.in this project we use docker-compose containers running MaxScale to create a sharded SQL database containing zipcodes information and writing a python script that used to connect, query, and demonstrate the merged database.
### MariaDB MaxScale Docker image

This Docker image runs the latest 2.4 version of MariaDB MaxScale.


### Building

Run the following command in this directory to build the image.

```
make build-image
```
### Running
To pull the latest MaxScale image from docker hub:
```
docker pull mariadb/maxscale:latest
```
To run the MaxScale container overriding the container instance name to 'mxs':
```
docker run -d --name mxs mariadb/maxscale:latest
```

### Configuration

```
docker-compose.yml
```

This file is used as a blueprint to build your docker containers. You can specify how many and what type of containers you want to build.

The default configuration for the container is fairly minimalist and can be found in this configuration file. At a high level the following is enabled:

REST API with default user and password (admin / mariadb) listening to all hosts (0.0.0.0)

### Configure via REST API
The REST API by default listens on port 8989. To interact with this from the docker host, requires a port mapping to specified on container startup. The example below shows listing the current services via curl:
```
docker run -d -p 8989:8989 --name mxs mariadb/maxscale:latest
curl -u admin:mariadb -H "Content-Type: application/json" http://localhost:8989/v1/services
```
### MaxScale docker-compose setup
The MaxScale docker-compose setup contains MaxScale configured with a three node master-slave cluster. To start it, run the following commands in this directory.
```
docker-compose build
```
After MaxScale and the servers have started (takes a few minutes), you can find the readwritesplit router on port 4006 and the readconnroute on port 4008. The user maxuser with the password maxpwd can be used to test the cluster. Assuming the mariadb client is installed on the host machine:
### Building Container and Running Code
Go into the /maxscale directory and run the following to build your containers
```
sudo docker-compose up -d
```
Confirm that your containers have been successfully built. You should see the containers you've specified in docker-compose.yml.
```
sudo docker-compose ps
```

### maxscale.cnf
This file configures your MaxScale instance. Docker-compose.yml calls upon this file to build the MaxScale container.

### Shard_query.py
This is the Python script. You can configure it to retrieve specific data from the database.


```
$ mysql -umaxuser -pmaxpwd -h 127.0.0.1 -P 4006 test
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 10.2.12 2.2.9-maxscale mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [test]>
```

### Install python3 and pymysql
```
sudo apt-get install python3.6
```
```
sudo apt-get install python3-pymysql
```

```
Go into the /maxscale-docker directory and run the following to execute the python script

python3 Shard_query.py 

```
### python code 
```
A python script is then used to connect, query, and demonstrate the merged database.
```

```
import pymysql


db = pymysql.connect(host="172.20.0.4", port=4000, user="maxuser", passwd="maxpwd")
cursor = db.cursor()

print('The last 10 rows of zipcodes_one are:')
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one LIMIT 9990,10;")
results = cursor.fetchall()
for result in results:
	print(result)

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
```

## Results of the zipcode_one & zipcode_two:

```
The last 10 rows of zipcodes_one are:
```
(40843, 'STANDARD', 'HOLMES MILL', 'KY', 'PRIMARY', '36.86', '-83', 'NA-US-KY-HOLMES MILL', 'FALSE', '', '', '')
(41425, 'STANDARD', 'EZEL', 'KY', 'PRIMARY', '37.89', '-83.44', 'NA-US-KY-EZEL', 'FALSE', '390', '801', '10204009')
(40118, 'STANDARD', 'FAIRDALE', 'KY', 'PRIMARY', '38.11', '-85.75', 'NA-US-KY-FAIRDALE', 'FALSE', '4398', '7635', '122449930')
(40020, 'PO BOX', 'FAIRFIELD', 'KY', 'PRIMARY', '37.93', '-85.38', 'NA-US-KY-FAIRFIELD', 'FALSE', '', '', '')
(42221, 'PO BOX', 'FAIRVIEW', 'KY', 'PRIMARY', '36.84', '-87.31', 'NA-US-KY-FAIRVIEW', 'FALSE', '', '', '')
(41426, 'PO BOX', 'FALCON', 'KY', 'PRIMARY', '37.78', '-83', 'NA-US-KY-FALCON', 'FALSE', '', '', '')
(40932, 'PO BOX', 'FALL ROCK', 'KY', 'PRIMARY', '37.22', '-83.78', 'NA-US-KY-FALL ROCK', 'FALSE', '', '', '')
(40119, 'STANDARD', 'FALLS OF ROUGH', 'KY', 'PRIMARY', '37.6', '-86.55', 'NA-US-KY-FALLS OF ROUGH', 'FALSE', '760', '1468', '20771670')
(42039, 'STANDARD', 'FANCY FARM', 'KY', 'PRIMARY', '36.75', '-88.79', 'NA-US-KY-FANCY FARM', 'FALSE', '696', '1317', '20643485')
(40319, 'PO BOX', 'FARMERS', 'KY', 'PRIMARY', '38.14', '-83.54', 'NA-US-KY-FARMERS', 'FALSE', '', '', '')
```
```
The first 10 rows of zipcodes_two are:
```
```
(42040, 'STANDARD', 'FARMINGTON', 'KY', 'PRIMARY', '36.67', '-88.53', 'NA-US-KY-FARMINGTON', 'FALSE', '465', '896', '11562973')
(41524, 'STANDARD', 'FEDSCREEK', 'KY', 'PRIMARY', '37.4', '-82.24', 'NA-US-KY-FEDSCREEK', 'FALSE', '', '', '')
(42533, 'STANDARD', 'FERGUSON', 'KY', 'PRIMARY', '37.06', '-84.59', 'NA-US-KY-FERGUSON', 'FALSE', '429', '761', '9555412')
(40022, 'STANDARD', 'FINCHVILLE', 'KY', 'PRIMARY', '38.15', '-85.31', 'NA-US-KY-FINCHVILLE', 'FALSE', '437', '839', '19909942')
(40023, 'STANDARD', 'FISHERVILLE', 'KY', 'PRIMARY', '38.16', '-85.42', 'NA-US-KY-FISHERVILLE', 'FALSE', '1884', '3733', '113020684')
(41743, 'PO BOX', 'FISTY', 'KY', 'PRIMARY', '37.33', '-83.1', 'NA-US-KY-FISTY', 'FALSE', '', '', '')
(41219, 'STANDARD', 'FLATGAP', 'KY', 'PRIMARY', '37.93', '-82.88', 'NA-US-KY-FLATGAP', 'FALSE', '708', '1397', '20395667')
(40935, 'STANDARD', 'FLAT LICK', 'KY', 'PRIMARY', '36.82', '-83.76', 'NA-US-KY-FLAT LICK', 'FALSE', '752', '1477', '14267237')
(40997, 'STANDARD', 'WALKER', 'KY', 'PRIMARY', '36.88', '-83.71', 'NA-US-KY-WALKER', 'FALSE', '', '', '')
(41139, 'STANDARD', 'FLATWOODS', 'KY', 'PRIMARY', '38.51', '-82.72', 'NA-US-KY-FLATWOODS', 'FALSE', '3692', '6748', '121902277')
```
```
The largest zipcode number in zipcodes_one is:
```
```
(47750,)
```
```
The smallest zipcode number in zipcodes_two is:
```
```
(38257,)
```
