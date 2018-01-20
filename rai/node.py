from .rpc import make_rpc, get_connection


class Node:

    def is_available(self):
        """
            Check if RPC node is available
        """
        try:
            self.version
            return True
        except Exception:
            return False

    @property
    def version(self):
        """
            Gets the version of the RPC node
        """
        rsp = make_rpc(
            {
                'action': 'version'
            }
        )
        return rsp

    @property
    def connection(self):
        """
            Show the connection string
        """
        return get_connection()
