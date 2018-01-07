def test_balance(account, account_stub):
    assert account.balance


def test_pending(account, account_stub):
    assert account.pending


def test_str(account):
    assert str(account) == account.address


def test_repr(account):
    assert repr(account) == '<Account {}>'.format(account.address)
