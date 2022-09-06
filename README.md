# Howework 1: Write a "good" Github Repo

Team 12's submission for [HW1](https://github.com/txt/se22/blob/main/docs/hw1.md) for CSC-510.

![example branch parameter](https://github.com/team-12-csc-510/hw1/actions/workflows/main.yml/badge.svg?branch=main)
[![DOI](https://zenodo.org/badge/529930397.svg)](https://zenodo.org/badge/latestdoi/529930397)
----
## Table Of Contents
- [Installation](#installation)
- [License](#license)
- [Team](#team)
----

## Installation

Requires [Python] v3.9+.
Clone the repository and move into the project directory and install the project dependencies. <br>

To install the dependencies/packages required for the project install [Poetry]


```shell
curl https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
```

To get started you need [Poetry]'s bin directory `(/Users/<username>/Library/Python/python-version/bin)` in your `PATH`
environment variable.

> Refer [here](https://stackoverflow.com/questions/60768676/what-is-the-default-install-path-for-poetry) for configuring poetry path correctly.


You can test that everything is set up by executing:
```shell
poetry --version
```

Configure [Poetry] virtual environment by

```shell
poetry env use python3
poetry install
```


----
## License

This project is licensed under MIT license available in [LICENSE](https://github.com/team-12-csc-510/hw1/blob/main/LICENSE.md) file

----

## Team
Name  | Unity id
------------- | -------------
Aditya Tewari  | adtewari
Naman Bhagat  | nbhagat2
Ritwik Tiwari  | rtiwari2
Saksham Thakur  | sthakur5
Shubhender Singh  | ssingh54

---

[Python]: <https://python.org>
[Poetry]: <https://python-poetry.org/>
