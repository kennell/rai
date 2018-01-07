from .rpc import make_rpc


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
