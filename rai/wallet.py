from rai.networking import rpc


class Wallet():

    def __init__(self, id, password=None):
        self.id = id
        self.id = password

    @property
    def total_balance(self):
        rsp = rpc(
            {
                'action': 'wallet_balance_total',
                'wallet': self.id
            }
        )
        return rsp['balance']

    @property
    def total_pending(self):
        rsp = rpc(
            {
                'action': 'wallet_balance_total',
                'wallet': self.id
            }
        )
        return rsp['pending']
