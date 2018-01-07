from .rpc import make_rpc


class Account:

    def __init__(self, address):
        self.address = address

    def __str__(self):
        return self.address