import requests
import urllib3

# HTTPS 인증서 경고 끄기
urllib3.disable_warnings()

url = "https://192.168.100.2:5001/webapi/entry.cgi"

params = {
    "api": "SYNO.API.Auth",
    "version": "7",
    "method": "login",
    "account": "박기태",
    "passwd": "1042210qQ!",
    "session": "AITF",
    "format": "sid",
}

print("요청 시작...")

response = requests.get(
    url=url,
    params=params,
    verify=False,
    timeout=30,
)

print("상태코드 :", response.status_code)
print("응답본문 :")
print(response.text)