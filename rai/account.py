from .rpc import make_rpc


class Account:

    def __init__(self, address):
        self.address = address

    def _get_balance(self):
        rsp = make_rpc(
            {
                "action": "account_balance",
                "account": self.address
            }
        )
        return rsp['balance']

    @property
    def balance(self):
        return self._get_balance()

    def _get_pending(self):
        rsp = make_rpc(
            {
                "action": "account_balance",
                "account": self.address
            }
        )
        return rsp['pending']

    @property
    def pending(self):
        return self._get_pending()

    @property
    def representative(self):
        rsp = make_rpc(
            {
                "action": "account_representative",
                "account": self.address
            }
        )
        return rsp['representative']

    def __str__(self):
        return self.address

    def __repr__(self):
        return '<Account {}>'.format(self.address)
