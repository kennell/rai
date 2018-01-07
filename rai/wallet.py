from .rpc import make_rpc
from .account import Account


class Wallet:

    def __init__(self, id, password=None):
        self.id = id
        self.password = None

    @property
    def is_locked(self):
        """
            Returns True if wallet is locked and requires a password, False if not locked
        """
        rsp = make_rpc(
            {
                "action": "wallet_locked",
                "wallet": self.id
            }
        )
        return True if rsp['locked'] == "1" else False


    @property
    def total_balance(self):
        """
            Returns the total balance for the wallet
        """
        rsp = make_rpc(
            {
                'action': 'wallet_balance_total',
                'wallet': self.id
            }
        )
        return rsp['balance']

    @property
    def total_pending(self):
        """
            Returns the total pending amount for the wallet
        """
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
        """
            Returns all accounts in the wallet
        """
        return self._get_accounts()

    def __str__(self):
        return self.id

    def __repr__(self):
        return '<Wallet {}>'.format(self.address)