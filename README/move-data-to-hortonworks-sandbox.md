start virtual box

## load data via GUI

- navigate to ambari ui localhost:8080
- login with maria_dev

> need to wait until all services have started up (10-15 minutes)

## connect to HDP instance with terminal

ssh maria_dev@127.0.0.1:2222

- clone git repo to HDP
- run local end to end test as maria_dev

```bash
sh scripts/local.sh ./data/data.csv
```

output:

```bash
[maria_dev@sandbox-hdp hadoop-mini-project]$ sh scripts/local.sh ./data/data.csv
2003__Nissan    1
2015__Mercedes  1
2016__Mercedes  1
2017__Toyota    1
```

- copy data to HDFS

```bash
[maria_dev@sandbox-hdp hadoop-mini-project]$ hadoop fs -mkdir input
[maria_dev@sandbox-hdp hadoop-mini-project]$ hadoop fs -copyFromLocal ./data/data.csv input/data.csv

```
