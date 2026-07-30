"""
NAS Authentication Provider

Synology NAS 인증을 담당한다.
"""

class NASAuthProvider:
    """
    Synology NAS 인증 Provider
    """

    async def authenticate(
        self,
        username: str,
        password: str,
    ) -> bool:
        """
        NAS 인증

        아직 구현하지 않는다.
        """
        raise NotImplementedError