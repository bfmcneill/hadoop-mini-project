# MapReduce Mini Project

The goal of this project is to show how MapReduce can be used to process data and produce a report for the total number of accidents per make and year of vehicle.  The raw input is automotive incident records by VIN and record date.  The raw data is formatted in a way that is convenient for storage (deduplicated where possible) but not convenient for analytics.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.  See deployment notes on how to deploy the project on a live system [**](#deployment)

### Prerequisites

- Verify Python 3 is installed on your local machine

```bash
python -V

$ Python 3.x.x
```

### Installing
- Install Python 3 via [pyenv](https://github.com/pyenv/pyenv)
- Install Python 3 via [python.org](https://www.python.org/)
- [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Running the tests

### End to end test

- this bash pipeline will allow testing on local machine. parallel processing example shown in [deployment](#deployment)

```bash
cat data.csv | python mapper_1.py | sort | python reducer_1.py | python mapper_2.py | sort | python reducer_2.py
```

## Deployment

- [Download Hortonworks HDP](https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html)
  - select VirtualBox
  - Note - During testing I could not find an easy way to get the docker version to run on x86 as well as either version (docker / VirtualBox) to run on M1 Apple silicon even when using Rosetta. 



- start hortonworks via VirtualBox
- copy data.csv

## Versioning

[SemVer](https://semver.org/) is used for versioning. For the versions available, see the tags on this repository.

## Authors
 - Ben McNeill - *Initial Work* - [bfmcneill](https://github.com/bfmcneill)
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



## Acknowledgments

- [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
- [CONTRIBUTING.md Template](https://gist.github.com/PurpleBooth/b24679402957c63ec426)
- [https://choosealicense.com/](https://choosealicense.com/)