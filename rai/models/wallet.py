import requests
import json


class Wallet():

    def __init__(self, id, password=None):
        self.id = id
        self.id = password

    @property
    def total_balance(self):
        return 2500000000

    def send(self, source, destination, amount):
        return "000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F"


class Account():

    def __init__(self, address):
        self.address = address