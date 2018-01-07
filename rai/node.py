from .rpc import make_rpc, get_connection
from .wallet import Wallet

class Node:

    def is_available(self):
        try:
            make_rpc(
                {
                    'action': 'version'
                }
            )
            return True
        except:
            return False

    @property
    def version(self):
        rsp = make_rpc(
            {
                'action': 'version'
            }
        )
        return rsp

    @property
    def connection(self):
        return get_connection()

    @property
    def wallets(self):
        """
            Returns all Wallets available on the node
        """
        rsp = make_rpc(
            {
                'action': 'wallet_list'
            }
        )
        return [Wallet(id=wallet_id) for wallet_id in rsp['wallets']]