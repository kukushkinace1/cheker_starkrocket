import time
import requests
from tqdm import tqdm

# Список адресов из файла
with open('addresses.txt', 'r') as f:
    addresses = [line.strip() for line in f]

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru,en;q=0.9,ru-RU;q=0.8,zh-TW;q=0.7,zh;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://starkrocket.xyz/airdrop',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

total_point = 0

for address in tqdm(addresses, ncols=70):
    params = {
        'address': address.lower(),
    }
    try:
        response = requests.get('https://starkrocket.xyz/api/check_wallet', params=params, headers=headers)
        if response.json()['result']['points']:
            point = int(response.json()['result']['points'])
            total_point+=point

            with open('wallets_with_drop.txt', 'a') as output:
                print(f"{address}: {point}", file=output)
    except:
        pass
    time.sleep(2)

print(f'{total_point} всего поинтов')
