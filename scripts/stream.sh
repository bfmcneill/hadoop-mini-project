hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-mapper mapper_1.py \
-reducer reducer_1.py \
-input input/data.csv \
-output output/all_accidents

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-mapper mapper_2.py \
-reducer reducer_2.py \
-input output/all_accidents \
-output output/make_year_count

