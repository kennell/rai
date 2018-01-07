import pytest

from rai import Wallet
from rai.rpc import get_connection


url = get_connection()


@pytest.fixture
def wallet():
    return Wallet(
        'abcd1234',
        password='hunter2'
    )


@pytest.fixture
def wallet_stub(responses, fixture_file):

    def callback(request):
        body = fixture_file('wallet_with_accounts.json')

        return 200, {}, body

    responses.add_callback(responses.POST,
                           url,
                           callback=callback,
                           content_type='application/json')


@pytest.fixture
def locked_wallet_stub(responses, fixture_file):

    def callback(request):
        body = fixture_file('locked_wallet.json')

        return 200, {}, body

    responses.add_callback(responses.POST,
                           url,
                           callback=callback,
                           content_type='application/json')


@pytest.fixture
def wallet_stub_no_accounts(responses, fixture_file):

    def callback(request):
        body = fixture_file('wallet_no_accounts.json')

        return 200, {}, body

    responses.add_callback(responses.POST,
                           url,
                           callback=callback,
                           content_type='application/json')
