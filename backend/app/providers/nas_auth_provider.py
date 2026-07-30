"""
NAS Authentication Provider

Synology DSM 인증을 담당한다.
"""

import httpx

from app.core.config import settings


class NASAuthProvider:
    """
    Synology NAS 인증 Provider
    """

    async def authenticate(
        self,
        username: str,
        password: str,
    ) -> bool:

        url = f"{settings.NAS_BASE_URL}/webapi/entry.cgi"

        params = {
            "api": "SYNO.API.Auth",
            "version": "7",
            "method": "login",
            "account": username,
            "passwd": password,
            "session": "AITF",
            "format": "sid",
        }

        print("=" * 60)
        print("NAS_BASE_URL :", settings.NAS_BASE_URL)
        print("REQUEST URL  :", url)
        print("PARAMS       :", params)
        print("=" * 60)

        try:
            async with httpx.AsyncClient(
                verify=settings.NAS_VERIFY_SSL,
                timeout=httpx.Timeout(30.0),
                http2=False,
                headers={
                    "Connection": "close",
                },
            ) as client:

                response = await client.get(
                    url=url,
                    params=params,
                    follow_redirects=True,
                )

            print("STATUS :", response.status_code)
            print("BODY   :", response.text)

            response.raise_for_status()

            result = response.json()

            return result.get("success", False)

        except Exception as e:
            print(type(e))
            print(e)
            raise