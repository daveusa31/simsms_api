# [SIMSMS](https://simsms.org)
Официальная [документация](https://simsms.org/new_theme_api.html)

[![Build Status](https://travis-ci.com/daveusa31/simsms_api.svg?branch=master)](https://travis-ci.com/daveusa31/simsms_api)
[![PyPi Package Version](https://img.shields.io/pypi/v/simsms_api.svg?style=flat-square)](https://pypi.python.org/pypi/simsms_api)
[![PyPi status](https://img.shields.io/pypi/status/simsms_api.svg?style=flat-square)](https://pypi.python.org/pypi/simsms_api)
[![Downloads](https://pepy.tech/badge/simsms_api)](https://pepy.tech/project/simsms_api)
[![Supported python versions](https://img.shields.io/pypi/pyversions/simsms_api.svg?style=flat-square)](https://pypi.python.org/pypi/simsms_api)



## Установка и использование:
```sh 
pip install simsms-api
```

```python 
import simsms_api

sms = simsms_api.SimSms(simsms_api_key)
tg = simsms_api.services.Telegram # Telegram
aviable_numbers = sms.aviable_numbers("ru", service=tg)["total"]

if 0 < aviable_numbers:
    print("Есть {} доступных номеров".format(aviable_numbers))

    balance = sms.balance()
    tg_price = sms.get_service_price("ru", service=tg)


    if balance >= tg_price:
        print("Денег хватает")
        activate = sms.get_number("ru", service=tg)
        print(activate)
        input("Нажмите inter, когда отправите смс")
        while True:
            order = sms.get_sms("ru", activate["id"], service=tg)
            if None != order["text"]:
                print(order["text"])
                break
        
    else:
        text = "У вас на балансе {} руб, а активация стоит {} руб"
        text = text.format(balance, price)
        print(text)
else:
    print("Нет доступных номеров")
```


# Таблица стран:
№ | Код | Страна
------------ | ------------- | -------------
1 | RU | Россия
2 | KZ | Казахстан
3 | UA | Украина
4 | RO | Румыния
5 | UK | Англия
6 | AR | Аргентина
7 | BR | Бразилия
8 | VN | Вьетнам
9 | HT | Гаити
10 | DE | Германия
11 | GE | Грузия
12 | DO | Доминикана
13 | EG | Египет (Virtual)
14 | IL | Израиль
15 | ID | Индонезия
16 | ES | Испания
17 | KH | Камбоджа
18 | CA_V | Канада (Virtual)
19 | KE | Кения
20 | KG | Киргизия
21 | CO | Колумбия
22 | XK | Косово
23 | LA | Лаос
24 | LV | Латвия
25 | LT | Литва
26 | MY | Малайзия
27 | MX | Мексика
28 | NL | Нидерланды
29 | NZ | Новая Зеландия
30 | PY | Парагвай
31 | PL | Польша
32 | PT | Португалия
33 | US | США
34 | US3 | США (Virtual)
35 | PH | Филиппины
36 | FI | Финляндия
37 | FR | Франция
38 | HR | Хорватия
39 | CL | Чили
40 | SE | Швеция
41 | EE | Эстония



# Таблица сервисов:
№ | Код | Название
------------ | ------------- | -------------
1 | opt28 | 1688.com
2 | opt97 | 32red.com
3 | opt86 | Adidas & Nike
4 | opt46 | Airbnb
5 | opt61 | Alibaba | Taobao
6 | opt44 | Amazon
7 | opt10 | AOL
8 | opt38 | Auto.RU
9 | opt56 | Badoo
10 | opt118 | Band.us
11 | opt25 | BetFair
12 | opt78 | Blizzard
13 | opt81 | Bolt
14 | opt3 | BurgerKing
15 | opt89 | Careem
16 | opt39 | CDKeys.com
17 | opt76 | CityMobil
18 | opt112 | CoinBase
19 | opt51 | CONTACT
20 | opt26 | Craigslist
21 | opt99 | Dent
22 | opt92 | DiDi
23 | opt45 | Discord
24 | opt27 | Dodopizza + PapaJohns
25 | opt40 | DoorDash
26 | opt32 | Drom.RU
27 | opt21 | EasyPay
28 | opt2 | Facebook
29 | opt43 | FastMail
30 | opt6 | Fiverr
31 | opt68 | G2A.COM
32 | opt77 | Gameflip
33 | opt35 | GetTaxi
34 | opt108 | Glovo | Raketa
35 | opt1 | GMail, YTube
36 | opt30 | GrabTaxi
37 | opt420 | Grailed
38 | opt110 | Grindr
39 | opt103 | iCard
40 | opt111 | IMO
41 | opt16 | Instagram
42 | opt94 | JD.com
43 | opt71 | Kakaotalk
44 | opt80 | Lastpass
45 | opt60 | Lazada
46 | opt37 | Line Messenger
47 | opt8 | LinkedIn
48 | opt42 | LiveScore
49 | opt105 | LocalBitcoins
50 | opt114 | Locanto.com
51 | opt75 | Lyft
52 | opt33 | Mail.RU (без гарантии)
53 | opt4 | Mail.ru Group
54 | opt100 | Mamba
55 | opt17 | MeetMe
56 | opt96 | MiChat
57 | opt15 | Microsoft
58 | opt7 | Microsoft Office 365
59 | opt22 | MoneyRawr
60 | opt47 | MrSpeedy
61 | opt73 | Naver
62 | opt116 | Neteller
63 | opt101 | Netflix
64 | opt113 | OfferUp
65 | opt95 | OlaCabs
66 | opt70 | OLX + goods.ru
67 | opt0 | Onrealt.ru
68 | opt115 | Oracle Cloud
69 | opt109 | Paddy Power
70 | opt83 | PayPal + Ebay
71 | opt84 | POF.com
72 | opt107 | Prom.UA
73 | opt57 | Proton Mail
74 | opt18 | Qiwi
75 | opt53 | Rambler
76 | opt48 | Shopee
77 | opt49 | Skout
78 | opt117 | Skrill
79 | opt90 | Snapchat
80 | opt119 | Sneakersnstuff
81 | opt58 | Steam
82 | opt98 | Streetbees
83 | opt91 | Suomi24
84 | opt55 | TAN (micropayment)
85 | opt82 | Tango
86 | opt29 | Telegram
87 | opt34 | Tencent QQ
88 | opt52 | Ticketmaster
89 | opt104 | TikTok
90 | opt9 | Tinder
91 | opt66 | Twilio
92 | opt41 | Twitter
93 | opt72 | Uber
94 | opt85 | Venmo
95 | opt11 | Viber
96 | opt24 | WebMoney&ENUM
97 | opt67 | WeChat
98 | opt54 | Weebly
99 | opt901 | Weebly 2
100 | opt20 | WhatsAPP
101 | opt65 | Yahoo
102 | opt88 | Yalla.live
103 | opt93 | Zoho
104 | opt59 | Авито
105 | opt69 | ВКонтакте (без гарантии)
106 | opt31 | Друг Вокруг
107 | opt19 | Любой другой (без гарантии)
108 | opt106 | Магнит
109 | opt5 | Одноклассники (без гарантии)
110 | opt102 | Пятерочка
111 | opt74 | Такси Максим
112 | opt13 | Фотострана
113 | opt14 | Юла (без гарантии)
114 | opt23 | Яндекс




# To do





