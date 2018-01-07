from .rpc import make_rpc
from .account import Account

class Wallet:

    def __init__(self, id, password=None):
        self.id = id
        self.password = None


    @property
    def total_balance(self):
        rsp = make_rpc(
            {
                'action': 'wallet_balance_total',
                'wallet': self.id
            }
        )
        return rsp['balance']

    @property
    def total_pending(self):
        rsp = make_rpc(
            {
                'action': 'wallet_balance_total',
                'wallet': self.id
            }
        )
        return rsp['pending']

    def _get_accounts(self):
        rsp = make_rpc(
            {
                'action': 'account_list',
                'wallet': self.id
            }
        )
        return [Account(address=acc) for acc in rsp['accounts']]

    @property
    def accounts(self):
        return self._get_accounts()

    def __str__(self):
        return self.id