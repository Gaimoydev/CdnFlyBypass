import requests

def request(url, guard, guardret, capt=None):
    print(f"guard: {guard}, guardret: {guardret}")
    s = requests.session()

    if capt is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'Cookie': f'guard={guard}; guardret={guardret}'
        }
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'Cookie': f'guard={guard}; guardret={guardret}; capt={capt}'
        }

    response = s.get(url, headers=headers)
    print(response.text)
    return response.text

if __name__ == '__main__':
    request("https://speedon.91av.live/", "3d10a9fbUMBi172180323161", "AlcG")