def test_total_balance(wallet, wallet_stub):
    assert wallet.total_balance is not None


def test_total_pending(wallet, wallet_stub):
    assert wallet.total_pending is not None


def test_accounts_when_has_accounts(wallet, account, wallet_stub):
    accounts = wallet.accounts
    assert len(wallet.accounts) == 1
    assert accounts[0].address == account.address


def test_accounts_when_doesnt_have_accounts(wallet, wallet_stub_no_accounts):
    assert wallet.accounts == []


def test_str(wallet):
    assert str(wallet) == wallet.id


def test_repr(wallet):
    assert repr(wallet) == '<Wallet {}>'.format(wallet.id)


def test_locked_wallet(locked_wallet_stub, wallet):
    assert wallet.is_locked


def test_unlocked_wallet(wallet, wallet_stub):
    assert not wallet.is_locked
