cat $1 | \
python mapper_1.py | sort | \
python reducer_1.py | \
python mapper_2.py | sort | \
python reducer_2.py