import random, json, re, string, os, threading
from bs4 import BeautifulSoup as bs
import sys, requests,time
from time import sleep
from datetime import datetime
current = datetime.now()
if sys.version_info >= (3, 0):
    from urllib.parse import urlencode, quote_plus

useragent = random.choice(["Instagram 9.2.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)", "Instagram 9.6.0 (iPhone8,1; iPhone OS 9_3_1; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+", "Instagram 22.0.0.15.68 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935F; hero2lte; samsungexynos8890; en_US)"])
header_ = {'Connection' : 'close',
           'Accept' : '*/*',
           'Content-type' : 'application/x-www-form-urlencoded; charset=UTF-8',
           'Cookie2' : '$Version=1',
           'Accept-Language' : 'en-US',
           'User-Agent' : useragent}
url = 'https://i.instagram.com/api/v1/'
ig_sig_key = '012a54f51c49aa8c5c322416ab1410909add32c966bbaa0fe3dc58ac43fd7ede'
sig_key_versi = '4'

list_mail = ["vintomaper.com","tovinit.com","mentonit.net"]
url_ = "https://cryptogmail.com/"

def banner():
     os.system("clear")
     print("""
     \x1b[35;1m___\x1b[35;1m______\x1b[35;1m______\x1b[35;1m___  __
    \x1b[35;1m/  _\x1b[35;1m/ ____\x1b[35;1m/ ____\x1b[35;1m/ / / /\x1b[100m\x1b[32;1mA\x1b[0m
    \x1b[35;1m/ /\x1b[35;1m/ / __\x1b[35;1m/ __/ \x1b[35;1m/ /_/ /\x1b[100m\x1b[32;1mS\x1b[0m
  \x1b[35;1m_/ /\x1b[35;1m/ /_/ \x1b[35;1m/ /___\x1b[35;1m/ __  /\x1b[100m\x1b[32;1mE\x1b[0m
 \x1b[35;1m/___/\x1b[35;1m\____/\x1b[35;1m_____\x1b[35;1m/_/ /_/\x1b[100m\x1b[32;1mX\x1b[0m
\x1b[30;1m──────────────────────────────""")

def get_teks(accept, key):
        cek = requests.get(url_+"api/emails/"+key, headers={"accept": accept}).text
        if "error" in cek:
                return "-"
        else:
                return cek

def get_random(digit):
        lis = list("abcdefghijklmnopqrstuvwxyz0123456789")
        dig = [random.choice(lis) for _ in range(digit)]
        return "".join(dig), random.choice(list_mail)

def run(email):
        result = []
        no = 0
        while True:
                no += 1
                try:
                        raun = requests.get(url_+"api/emails?inbox="+email).text
                        if "404" in raun:
                                continue
                        elif "data" in raun:
                                z = json.loads(raun)
                                for data in z["data"]:
                                        res = get_teks("text/html,text/plain",data["id"])
                                        sc = bs(res.encode("utf-8"), "html.parser")
                                        cs = sc.find("td", attrs={"style":"padding:10px;color:#565a5c;font-size:32px;font-weight:500;text-align:center;padding-bottom:25px;"}).text
                                        result.append(str(cs))
                                        requests.delete(url_+"api/emails/"+data["id"])
                                break
                        else:
                                continue
                except (KeyboardInterrupt,EOFError):
                                break
                if no >= 10:
                     break
        return result

def create():
            session = requests.Session()
            sesi = requests.Session()
            session.headers.update(header_)
            while True:
              try:
                 set_name, set_email = get_random(3)
                 ran = requests.get("https://randomuser.me/api/").json()
                 set_name = f'{str(ran["results"][0]["name"]["first"])}_{set_name}'.upper()
                 header = {
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Connection': 'keep-alive',
                        'Host': 'www.instagram.com',
                        'Referer': 'https://www.instagram.com/',
                        'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
                        'X-Instagram-AJAX': '1',
                        'X-Requested-With': 'XMLHttpRequest'
                        }
                 sesi.headers.update(header)
                 sesi.cookies.update({
                        'sessionid': '', 'mid': '', 'ig_pr': '1',
                        'ig_vw': '1920', 'csrftoken': '',
                        's_network': '', 'ds_user_id': ''
                       })
                 sesi.get('https://www.instagram.com/web/__mid')
                 sesi.headers.update({'X-CSRFToken': sesi.cookies.get_dict()['csrftoken']})
                 suges = sesi.post("https://www.instagram.com/accounts/username_suggestions/", data={"email": set_name+"@"+set_email, "name": str(ran["results"][0]["name"]["first"]).upper()}).json()
                 usernam = suges["suggestions"][0]
                 uudi = random.choice(["YCMpBgABAAEI3BpsACCjB0aLRmYC"])
                 dat = {
                     "device_id": str(uudi),
                     "email": set_name+"@"+set_email
                     }
                 send = session.post(f"{url}accounts/send_verify_email/", data=dat).json()
                 try:
                     if send["email_sent"]:
                         print ("\x1b[32;1m(\x1b[31;1m*\x1b[32;1m) \x1b[36;1mMenunggu Kode verifikasi....")
                         codec = run(set_name+"@"+set_email)[0]
                         check = session.post(f"{url}accounts/check_confirmation_code/", data={"code":codec,"device_id": str(uudi),"email":set_name+"@"+set_email}).json()
                         print ("\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mVerifikasi Kode berhasil...")
                         enc_pass = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()), "sabar123")
                         sesi.post("https://www.instagram.com/web/consent/check_age_eligibility/", data={"day":"12", "mont":"3", "year":"1999"})
                         data = {
                                  "email": set_name+"@"+set_email,
                                  "enc_password": enc_pass,
                                  "username": usernam,
                                  "first_name": str(ran["results"][0]["name"]["first"]).upper(),
                                  "month": "3",
                                  "day": "12",
                                  "year": "1999",
                                  "client_id": str(uudi),
                                  "seamless_login_enabled":"1",
                                  "tos_version":"row",
                                  "force_sign_up_code": check["signup_code"],
                                  }
                         buat = sesi.post("https://www.instagram.com/accounts/web_create_ajax/", data=data).json()
                         try:
                               if buat["account_created"] == True:
                                   with open("akun-ok.txt","a") as f:
                                        f.write(usernam+" | "+set_name+"@"+set_email+" | sabar123\n")
                                   print ("\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mSTATUS   \x1b[31;1m: \x1b[35;1mBERHASIL")
                                   print (f"\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mUSERNAME \x1b[31;1m: \x1b[37;1m{usernam}")
                                   print (f"\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mPASSWORD \x1b[31;1m: \x1b[37;1msabar123")
                                   print (f"\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mEMAIL    \x1b[31;1m: \x1b[37;1m{set_name}@{set_email}")
                                   print (f"\x1b[31;1m──────────────────────────────\n")
                                   break

                         except KeyError:
                               if "checkpoint_required" in str(buat):
                                   print ("\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mSTATUS   \x1b[31;1m: \x1b[33;1mCHECKPOINT")
                                   print (f"\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mUSERNAME \x1b[31;1m: \x1b[37;1m{usernam}")
                                   print (f"\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mPASSWORD \x1b[31;1m: \x1b[37;1msabar123")
                                   print (f"\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mEMAIL    \x1b[31;1m: \x1b[37;1m{set_name}@{set_email}")
                                   print (f"\x1b[31;1m──────────────────────────────\n")
                                   with open("akun-cp.txt","a") as f:
                                        f.write(usernam+" | "+set_name+"@"+set_email+" | sabar123"+" | "+buat['checkpoint_url']+"\n")
                                   break

                               else:
                                   print ("\x1b[32;1m(\x1b[31;1m+\x1b[32;1m) \x1b[36;1mSTATUS   \x1b[31;1m: \x1b[31;1mFAILLED")
                                   print (buat)
                                   print (f"\x1b[31;1m──────────────────────────────\n")
                                   sleep(200)
                                   break
                 except KeyError:
                       pass

              except json.decoder.JSONDecodeError:
                     print (f"\x1b[31;1m──────────────────────────────\n")
                     pass
              except requests.exceptions.ConnectionError:
                     print ("\x1b[31;1mJaringan Tidak Stabil ....")
                     sleep(5)

            create()


if __name__=='__main__':
        banner()
        create()
