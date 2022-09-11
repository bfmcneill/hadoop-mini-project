# MapReduce Mini Project

The goal of this project is to show how MapReduce can be used to process data and produce a report for the total number of accidents per make and year of vehicle. The raw input is automotive incident records by VIN and record date. The raw data is formatted in a way that is convenient for storage (deduplicated where possible) but not convenient for analytics.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment notes on how to deploy the project on a live system [\*\*](#deployment)

### Prerequisites

- Verify Python 2.7.x is the local interpreter

```bash
python -V

$ Python 2.7.x
```

- Optionally: if using windows make sure you have an ssh client
  - [bitvise](https://www.bitvise.com/ssh-client-download)
  - [putty](https://www.putty.org/)

### Installing

- Install Python 2 via [pyenv](https://github.com/pyenv/pyenv)
- Install Python 2 via [python.org](https://www.python.org/)
- [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Running the tests

### End to end test

- To run a local test on small subset of data run the bash pipeline
  - script is located at `scripts/local.sh`
  - script requires an argument to be passed which is the relative path to data

```bash
sh scripts/local.sh ./data/data.csv
```

## Deployment

- [Download Hortonworks HDP](https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html)

  - select VirtualBox
  - Note - During testing I could not find an easy way to get the docker version to run on x86 as well as either version (docker / VirtualBox) to run on M1 Apple silicon even when using Rosetta.

- start Hortonworks via VirtualBox
- copy data.csv

## Versioning

[SemVer](https://semver.org/) is used for versioning. For the versions available, see the [tags](https://github.com/bfmcneill/hadoop-mini-project/tags) on this repository.

## Authors

- Ben McNeill - _Initial Work_ - [bfmcneill](https://github.com/bfmcneill)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
- [CONTRIBUTING.md Template](https://gist.github.com/PurpleBooth/b24679402957c63ec426)
- [https://choosealicense.com/](https://choosealicense.com/)
