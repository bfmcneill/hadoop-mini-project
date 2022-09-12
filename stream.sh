# ensure python and shell files format is compatable with unix
sh ./fffix.sh

# ensure python files are executable

chmod +x ./*.py

# reset HDFS input directory
hadoop fs -rm -r input

# place data on HDFS for processing
hadoop fs -mkdir input
hadoop fs -copyFromLocal data.csv input/data.csv

# reset HDFS output directory
hadoop fs -rm -r output

# step 1
hadoop jar \
/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-files mapper_1.py,reducer_1.py \
-mapper mapper_1.py \
-reducer reducer_1.py \
-input input/data.csv \
-output output/all_accidents

# step 2
hadoop jar \
/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-files mapper_2.py,reducer_2.py \
-mapper mapper_2.py \
-reducer reducer_2.py \
-input output/all_accidents \
-output output/make_year_count

