# MessageCipher
![unittests passing](https://github.com/hazzery/MessageCipher/actions/workflows/unittests.yml/badge.svg)
[![codecov](https://codecov.io/gh/hazzery/MessageCipher/graph/badge.svg?token=6GQA3I43XT)](https://codecov.io/gh/hazzery/MessageCipher)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hazzery/MessageCipher/master.svg)](https://results.pre-commit.ci/latest/github/hazzery/MessageCipher/master)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

MessageCipher is a hobby project I started whilst studying discrete mathematics
in my first year at the University of Canterbury.
It contains code that implements the Caesar Cipher and Affine Cipher algorithms,
as well as a very basic implementation of an RSA crypto-system.

The primary purpose of displaying this project is to demonstrate my commitment
to writing code that is easily understandable, well documented, and maintainable.

## How to use

MessageCipher is intended to be used as a library, not as a standalone program.
To use MessageCipher in your codebase, you need to install it using pip.
This can be done one of two ways, either by directly cloning the git repository:
```bash
pip install message_cipher@git+https://github.com/hazzery/MessageCipher.git
```
Or by installing from a tarball archive (available for download from the releases page).
```bash
pip install /path/to/MessageCipher-1.2.0.tar.gz
```
Make sure to replace `/path/to/MessageCipher-1.2.0.tar.gz` with the correct path to the archive
you downloaded from GitHub.


Once installed, you can import from MessageCipher like so:
```python
from message_cipher.rsa_system import RSA

public_key, private_key = RSA()
```

```python
from message_cipher.rsa_encrypter import RsaEncrypter

product = ...
exponent = ...

encryption_key = RsaEncrypter(product, exponent)
```

## Example Usage
The main.py file demonstrates very basic usage of this program.
To execute this file in a terminal, run the following inside the project directory
```bash
python3 main.py
```

# Licence
This project is licenced under version 3 of the GNU AGPL

![AGPLv3](https://www.gnu.org/graphics/agplv3-with-text-162x68.png)