# Case Studies
A collection of case studies, where i frame a problem and solve it using various technologies mostly big data but not limited to. Problems associated with this real life case studies are solved using various Big Data technologies. You might think that some of the problems can be solved using better way, easier way,or don't even require big data technology  but the whole point of this repository is to put Big Data technologies into use to solve the problems associated with the particular case study.

Big Data Technologies Used : 
1. Apache Kafka
2. Apache HBase
3. Apache Hive
4. Apache Spark
    - 4.1 SparkSQL
    - 4.2 SparkMLLib
    - 4.3 SparkStream
    - 4.4 GraphX
5. Apache Flink
6. Apache Hadoop
    - 6.1 Map Reduce
    - 6.2 Chained Map Reduce
    - 6.3 Map Only
    - 6.4 Reduce Only
    - 6.5 Map-Partition-Reducer 
7. Apache Pig
8. Apache Druid
9. Apache Storm
10. Apache Flume
11. Apache Sqoop
12. ElasticSearch 
At the moment solving problems using Map Reduce.

Docker Usage: <br/>
1. Start cloudera-manager automatically
```console
username@hostname:~$ sudo apt-get update
username@hostname:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io
username@hostname:~$ sudo docker run --hostname=quickstart.cloudera --privileged=true -t -i -d -v /your/local_path/to/code/:/src --publish-all=true -p 8888:8888 -p 80:80 -p 7180:7180 cloudera/quickstart /home/cloudera/cloudera-manager --express
```
2. Start All the big data services automatically.
```console
username@hostname:~$ sudo apt-get update
username@hostname:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io
username@hostname:~$ sudo docker run --hostname=quickstart.cloudera --privileged=true -t -i -d -v /your/local_path/to/code/:/src --publish-all=true -p 8888:8888 -p 80:80 -p 7180:7180 cloudera/quickstart /usr/bin/docker-quickstart
```
3. Start Service manually
```console
username@hostname:~$ sudo apt-get update
username@hostname:~$ sudo apt-get install docker-ce docker-ce-cli containerd.io
username@hostname:~$ sudo docker run --hostname=quickstart.cloudera --privileged=true -t -i -d -v /your/local_path/to/code/:/src --publish-all=true -p 8888:8888 -p 80:80 -p 7180:7180 cloudera/quickstart /bin/bash
```