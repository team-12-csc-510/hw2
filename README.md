# Howework 2-5: Take a working system (written in LUA) and write it in any other language(Python)

Team 12's submission for [HW2-5](https://github.com/txt/se22/blob/main/docs/hw2345.md) for CSC-510.

![example branch parameter](https://github.com/team-12-csc-510/hw2/actions/workflows/main.yml/badge.svg?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7094291.svg)](https://doi.org/10.5281/zenodo.7094291)
[![codecov](https://codecov.io/gh/team-12-csc-510/hw2/branch/main/graph/badge.svg?token=UUKFDSSVL5)](https://codecov.io/gh/team-12-csc-510/hw2)

## Table Of Contents

- [Installation](#installation)
- [License](#license)
- [Homeworks](#homeworks)
- [Team](#team)

______________________________________________________________________

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

______________________________________________________________________

## License

This project is licensed under MIT license available in [LICENSE](https://github.com/team-12-csc-510/hw1/blob/main/LICENSE.md) file

______________________________________________________________________

## Homeworks

Name  | Status | Tasks
------------- | -------------| -------------
Homework 2  |  ✓ | Get this going for the `Num` and `Sym` class (below) and the tests cases `the`, `sym`, `num`, `bignum`.|
Homework 3  |  ✓ | Get this going for the `Cols`, `Row`, `Data` class and the test cases `eg.csv, eg.data, eg.stats`.|
Homework 4  |  ✓ | Add all the bling from HW1. Also, add post-commit hooks to auto run all the test cases, the code coverage checks (if your language supports then), and the documentation generators.  For more on what kinds of documentation is acceptable, see [the web site from lecture1](https://user-images.githubusercontent.com/29195/130997647-d933884e-8e5c-4f0c-a367-6a5d69bb1df1.png).|
Homework 5  |  ⬜ |For five other groups from cs510 (picked at random), apply the Project1 [rubric](https://github.com/txt/se22/blob/main/docs/proj1.md#rubric).  Important note: whatever scores you offer, these will **not** change the other group's scores.|

______________________________________________________________________

## Team

Name  | Unity id
------------- | -------------
Aditya Tewari  | adtewari
Naman Bhagat  | nbhagat2
Ritwik Tiwari  | rtiwari2
Saksham Thakur  | sthakur5
Shubhender Singh  | ssingh54

______________________________________________________________________

[poetry]: https://python-poetry.org/
[python]: https://python.org
