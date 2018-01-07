import pytest

from rai.account import Account
from rai.rpc import get_connection


url = get_connection()


@pytest.fixture
def account(json_fixture_file):
    wallet = json_fixture_file('wallet_with_accounts.json')
    address = wallet['accounts'][0]

    return Account(address)


@pytest.fixture
def account_stub(responses, fixture_file):

    def callback(request):
        body = fixture_file('account.json')

        return 200, {}, body

    responses.add_callback(responses.POST,
                           url,
                           callback=callback,
                           content_type='application/json')
