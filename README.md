# MessageCipher
![unittests passing](https://github.com/hazzery/MessageCipher/actions/workflows/unittests.yml/badge.svg)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

MessageCipher is a hobby project I started whilst studying discrete mathematics
in my first year at the University of Canterbury.
It contains code that implements the Caesar Cipher and Affine Cipher algorithms,
as well as a very basic implementation of an RSA crypto-system.

The primary purpose of displaying this project is to demonstrate my commitment
to writing code that is easily human understandable, well documented, and maintainable.

## How to run

The main.py file demonstrates very basic usage of this program.
To execute this file in a terminal, run
```bash
python3 main.py
```
inside the project directory

To instead execute the unit tests, run
```bash
python3 -m unittest discover -s tests
```
