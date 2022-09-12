cat $1 | ./mapper_1.py | sort | ./reducer_1.py | ./mapper_2.py | sort | ./reducer_2.py
