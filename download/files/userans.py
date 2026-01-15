import requests
import random
import time
import webbrowser


g = "\033[92m"
m = "\033[91m"


print(' SYYAD : @BBBBYB2 ')
time.sleep(2)
token = input(g+"enter token : ")
id = input(g+"enter id : ")
webbrowser.open('https://t.me/+MGhCyyBLJOs0MWIy')

def send_telegram(user):
    msg = f"""----------------------------------
user:{user}

tele:@BBBBYB2
---------------------------------"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={
        "chat_id": id,
        "text": msg
    })


cookies = {
    'csrftoken': '3-AXH888ykZYw8H9eXVBT9',
    'datr': 'lrZeaQhJAeHDi5rJ_7JE4rq9',
    'ig_did': '966C7F6A-A3C1-45F4-988B-64CF95C2A261',
    'mid': 'aV62lgABAAHlpmLhtrX1gX587w_E',
    'dpr': '2.1988937854766846',
    'ig_nrcb': '1',
    'wd': '891x1639',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '/',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'x-asbd-id': '359341',
    'x-csrftoken': '3-AXH888ykZYw8H9eXVBT9',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1031930579',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': '8m26ob:k3i7xk:on10gs',
}

while True:
    m1 = random.choice('qwertyuiopasdfghjklzxcvbnm')
    m2 = random.choice('0123456789')
    m3 = random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')
    m4 = random.choice('qwertyuiopasdfghjklzxcvbnm0123456789')
    m5 = random.choice('qwertyuiopasdfghjklzxcvbnm0123456789')

    syyad = [
        m1+m2+m3+m4+m5,
        m2+'_'+m4+'_'+m1,
        m1+'.'+m2+'.'+m5,
        m1+m2+'.'+m3+m4+m5,
        m1+m2+'_'+m3+m4+m5,
        m1+m3+m2+m5+'_',
        m1+m3+m2+m5+'.'+m1,
        m1+m1+'_'+m4+m2,
        m1+m1+'.'+m4+m2
    ]

    for user in syyad:
        data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1768331420:AcdQANvG64eDIcEMklDCw5RLOY4kTL1uW1IHdLgYXP2JPZoWcmRfU/RuSaLfuK0Ht0VGEOUhPPYJ5uSbgJflRYX3Evv6Ug1AbtXnDRRX5kab6lBCrxzqTfASdcyLgO17fS4JOpplZEK0y/HH4jHM6c4=',
            'email': 'drhdgh@gmail.com',
            'failed_birthday_year_count': '{}',
            'first_name': 'syyad',
            'username': user,
            'opt_into_one_tap': 'false',
            'use_new_suggested_user_name': 'true',
            'jazoest': '21682',
        }

        r = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
            cookies=cookies,
            headers=headers,
            data=data,
        ).text

        if '"status":"ok"' in r:
            print(g+f"GOOD {user}")
            send_telegram(user)
        else:
            print(m+f"BAD  {user}")

        time.sleep(1)