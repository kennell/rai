from .account import Account
from .rpc import make_rpc


class Wallet:

    def __init__(self, id, password=None):
        self.id = id
        self.password = None

    @property
    def is_locked(self):
        """
            Returns True if wallet is locked and requires a password,
            False if not locked
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

    @property
    def accounts(self):
        rsp = make_rpc(
            {
                'action': 'account_list',
                'wallet': self.id
            }
        )
        return [Account(address=acc) for acc in rsp['accounts']]

    def create_account(self):
        """
            Create new account in the wallet
        """
        rsp = make_rpc(
            {
                'action': 'account_create',
                'wallet': self.id
            }
        )
        return Account(address=rsp['account'])

    def remove_account(self, account):
        """
            Remove account from wallet
            :param account: XRB address string or <Account> instance
            :return: True if account was removed, False if not
        """
        if type(account) == Account:
            account = account.address
        rsp = make_rpc(
            {
                'action': 'account_remove',
                'wallet': self.id,
                'account': account
            }
        )
        return True if rsp['removed'] == '1' else False

    def contains(self, account):
        """
            Returns True if Wallet contains account, else False
            :param account: XRB address string or <Account> instance
        """
        if type(account) == str:
            return account in [a.address for a in self.accounts]
        elif type(account) == Account:
            return account.address in [a.address for a in self.accounts]
        else:
            return False

    def __contains__(self, account):
        return self.contains(account)

    def __str__(self):
        return self.id

    def __repr__(self):
        return '<Wallet {}>'.format(self.id)
