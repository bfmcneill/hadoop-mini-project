cat $1 | python3.6 mapper_1.py | sort | python3.6 reducer_1.py | python3.6 mapper_2.py | sort | python3.6 reducer_2.py
