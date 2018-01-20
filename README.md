# 🗿 rai

[![PyPI](https://img.shields.io/pypi/v/rai.svg)](https://pypi.python.org/pypi/rai) [![Code Climate](https://img.shields.io/codeclimate/maintainability/kennell/rai.svg)](https://codeclimate.com/github/kennell/rai) [![Travis](https://img.shields.io/travis/kennell/rai.svg)](https://travis-ci.org/kennell/rai)

**rai** is a high-level, pythonic client for interacting with [Raiblocks](https://raiblocks.net/) nodes. It allows you to easily build applications that make use of the Raiblocks cryptocurrency.

<sub>⚠ rai is not yet suited for use in production systems. It only covers a limited set of node functionality and things may break in future versions.</sub>

## Donations

Your contribution keeps this project going ❤️

* <sub>XRB `xrb_3yiuq5i34en3u4patnedsa8umqwyyyuomt999b3te9qmkhhujjrh345web61`</sub>
* <sub>BTC `121QcrzmFsYfxpJYneTS4N6yKDdU8GGfXa`</sub>
* <sub>ETH `0x56Aab3cDA7Ea02953aE394F9ffA3f7b80ed8b6DE`</sub>
* <sub>LTC `LerFT8YP7Q9etp2M3EsJxLZJYeFCZLV6wQ`</sub>

## Install

```
pip install rai
```

<sub>Note: rai requires a running Raiblocks node with RPC enabled. Read more about [installing and configuring a node here](docs/installation.md).</sub>

## Usage example

```python
from rai import Wallet


wallet = Wallet(id='4A84E2353EA3F363094EC7844A33B395E2BFDFCE19506FAFC37C73E7653D430F')
print(wallet.total_balance)
# 2500000000
block = wallet.send(
    source='xrb_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000',
    destination='xrb_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000',
    amount='1000000'
)
print(block)
# 000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F
```

## ToDo priority

* Implement all RPC calls
* Write Sphinx documentation
* Add usage examples
* Test coverage
