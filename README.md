# 🗿 rai
**rai** is a high-level Python client for interacting with [Raiblocks](https://raiblocks.net/) nodes. It allows you to easily build applications that make use of the Raiblocks cryptocurrency.

## Donations

Your contribution keeps this project going ❤️

* XRB `xrb_3yiuq5i34en3u4patnedsa8umqwyyyuomt999b3te9qmkhhujjrh345web61`
* BTC `121QcrzmFsYfxpJYneTS4N6yKDdU8GGfXa`
* ETH `0x56Aab3cDA7Ea02953aE394F9ffA3f7b80ed8b6DE`
* LTC `LerFT8YP7Q9etp2M3EsJxLZJYeFCZLV6wQ`

## Install

```
pip install rai
```

<sub>Note: rai requires a running Raiblocks node with RPC enabled. This can be the standalone [`rai_node`](https://github.com/clemahieu/raiblocks/releases) or the [`rai_wallet`](https://github.com/clemahieu/raiblocks/releases) GUI. You can learn more about running and configuring nodes [here](https://github.com/clemahieu/raiblocks/wiki/Running-rai_node-as-a-service).</sub>

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
