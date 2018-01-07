# 🗿 rai

**rai** is a high-level client for interacting with [Raiblocks](https://raiblocks.net/) nodes.

## Donations

This library is open source and free to use, but i have a day job and bills to pay. Your contribution keeps this project going. 

XRB xrb_3yiuq5i34en3u4patnedsa8umqwyyyuomt999b3te9qmkhhujjrh345web61
BTC 121QcrzmFsYfxpJYneTS4N6yKDdU8GGfXa
ETH 0x56Aab3cDA7Ea02953aE394F9ffA3f7b80ed8b6DE
LTC LerFT8YP7Q9etp2M3EsJxLZJYeFCZLV6wQ

## Install

```
pip install rai
```

rai requires a running Raiblocks node.

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