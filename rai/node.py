from .rpc import make_rpc, get_connection


class Node:

    def is_available(self):
        try:
            make_rpc(
                {
                    'action': 'version'
                }
            )
            return True
        except:
            return False

    @property
    def version(self):
        rsp = make_rpc(
            {
                'action': 'version'
            }
        )
        return rsp

    @property
    def connection(self):
        return get_connection()
