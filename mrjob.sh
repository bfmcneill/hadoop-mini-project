hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file mapper1.py -mapper mapper1.py \
-file reducer1.py -reducer reducer1.py \
-input input/data.csv -output output/all_accidents

hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file mapper2.py -mapper mapper2.py \
-file reducer2.py -reducer reducer2.py \
-input output/all_accidents -output output/make_year_count