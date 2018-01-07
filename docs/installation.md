# Installation

## Install rai

You can install **rai** via pip, the Python package manager:

```bash
pip install rai
```

## Install node

rai requires a running Raiblocks node with RPC enabled. This can be the standalone `rai_node`, the `rai_wallet` GUI or any other compatible implementation.

* You can download the latest release of rai_node and rai_wallet [here](https://github.com/clemahieu/raiblocks).
* A [Docker image](https://github.com/clemahieu/raiblocks/wiki/Docker-node) is also available.
* Read the [instructions](https://github.com/clemahieu/raiblocks/wiki/Running-rai_node-as-a-service) on configuring and running rai_node as a service.

## Node config

In your `config.json`, ensure RPC is enabled and the node is listening to your local interface.

```
"rpc_enable": "true",
    "rpc": {
        "address": "::1",
        "port": "7076",
        "enable_control": "true",
        "frontier_request_limit": "16384",
        "chain_request_limit": "16384"
    }
```


You can verify your node is running using curl:
```bash
curl -g -d '{ "action": "version" }' [::1]:7076
```

If your node uses a different port or is on a different host, you need to set the following enviroment variables:

```
RAI_HOST=<your_host> (default: [::1])
RAI_PORT=<your_port> (default: 7076)
```
