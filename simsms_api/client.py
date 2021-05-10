import time
import requests
import transliterate


from . import exceptions
from . import services


class SimSms:
    """
    Официальная документация: https://simsms.org/new_theme_api.html
    Репозитортй на github.com: https://github.com/daveusa31/simsms_api
    
    Доступные методы:
        balance
        get_user_info
        get_activation_status
    """

    __API_URL = "https://simsms.org/priemnik.php"
    __available_countries = [
        "RU",
        "KZ",
        "UA",
        "RO",
        "UK",
        "AR",
        "BR",
        "VN",
        "HT",
        "DE",
        "GE",
        "DO",
        "EG",
        "IL",
        "ID",
        "ES",
        "KH",
        "CA_V",
        "KE",
        "KG",
        "CO",
        "XK",
        "LA",
        "LV",
        "LT",
        "MY",
        "MX",
        "NL",
        "NZ",
        "PY",
        "PL",
        "PT",
        "US",
        "US3",
        "PH",
        "FI",
        "FR",
        "HR",
        "CL",
        "SE",
        "EE",
    ]
    __available_services = [
        "opt28",
        "opt97",
        "opt86",
        "opt46",
        "opt61",
        "opt44",
        "opt10",
        "opt38",
        "opt56",
        "opt118",
        "opt25",
        "opt78",
        "opt81",
        "opt3",
        "opt89",
        "opt39",
        "opt76",
        "opt112",
        "opt51",
        "opt26",
        "opt99",
        "opt92",
        "opt45",
        "opt27",
        "opt40",
        "opt32",
        "opt21",
        "opt2",
        "opt43",
        "opt6",
        "opt68",
        "opt77",
        "opt35",
        "opt108",
        "opt1",
        "opt30",
        "opt420",
        "opt110",
        "opt103",
        "opt111",
        "opt16",
        "opt94",
        "opt71",
        "opt80",
        "opt60",
        "opt37",
        "opt8",
        "opt42",
        "opt105",
        "opt114",
        "opt75",
        "opt33",
        "opt4",
        "opt100",
        "opt17",
        "opt96",
        "opt15",
        "opt7",
        "opt22",
        "opt47",
        "opt73",
        "opt116",
        "opt101",
        "opt113",
        "opt95",
        "opt70",
        "opt0",
        "opt115",
        "opt109",
        "opt83",
        "opt84",
        "opt107",
        "opt57",
        "opt18",
        "opt53",
        "opt48",
        "opt49",
        "opt117",
        "opt90",
        "opt119",
        "opt58",
        "opt98",
        "opt91",
        "opt55",
        "opt82",
        "opt29",
        "opt34",
        "opt52",
        "opt104",
        "opt9",
        "opt66",
        "opt41",
        "opt72",
        "opt85",
        "opt11",
        "opt24",
        "opt67",
        "opt54",
        "opt901",
        "opt20",
        "opt65",
        "opt88",
        "opt93",
        "opt59",
        "opt69",
        "opt31",
        "opt19",
        "opt106",
        "opt5",
        "opt102",
        "opt74",
        "opt13",
        "opt14",
        "opt23",
    ]
    __last_request_from_get_sms = 0

    def __init__(self, api_key):
        """
        Параметры:
            api_key : str
                Ваш api ключ со страницы https://simsms.org/user/
        """
        self.api_key = api_key

    def balance(self):
        """
        Баланс аккаунта
        Возрат:
            balane : float
        """
        params = {
            "metod": "get_balance",
        }
        balance = self.__request(params)["balance"]
        return float(balance)

    def get_user_info(self):
        params = {"metod": "get_userinfo"}
        return self.__request(params)

    def aviable_numbers(self, country: str, service="any"):
        params = {
            "metod": "get_count_new",
            "service": service,
            "country": country,
        }
        return self.__request(params)

    def get_service_price(self, country: str, service="any"):
        """
        Получение стоимости активации.
        """
        params = {
            "metod": "get_service_price",
            "service": service,
            "country": country,
        }
        return float(self.__request(params)["price"])

    def get_number(self, country: str, service="any"):
        params = {
            "metod": "get_number",
            "service": service,
            "country": country,
        }
        response = self.__request(params)

        number = response["number"]

        response["number"] = response["CountryCode"].replace("+", "") + number

        return response

    def number_already_used(self, order_id: int, service="any"):
        params = {
            "metod": "ban",
            "service": service,
            "id": int(order_id),
        }
        return self.__request(params)

    def get_sms(self, country: str, order_id: int, service="any"):
        if self.__last_request_from_get_sms > time.time() - 30:
            need_sleep = 30 - (time.time() - self.__last_request_from_get_sms)
            print(need_sleep)
            time.sleep(need_sleep)

        params = {
            "metod": "get_sms",
            "service": service,
            "country": country,
            "id": int(order_id),
        }

        self.__last_request_from_get_sms = time.time()

        return self.__request(params)

    def denial(self, country: str, order_id: int, service="any"):
        params = {
            "metod": "denial",
            "service": service,
            "country": country,
            "id": int(order_id),
        }
        return self.__request(params)

    def get_clearsms(self, order_id: int, service="any"):
        params = {
            "metod": "get_clearsms",
            "service": service,
            "id": int(order_id),
        }
        return self.__request(params)

    def get_proverka(sefl, number: int, service="any"):
        params = {
            "metod": "get_proverka",
            "service": service,
            "number": int(number),
        }
        return self.__request(params)

    def get_2fa(self, secret: int):
        params = {
            "metod": "get_2fa",
            "secret": int(secret),
        }
        return self.__request(params)

    def redirect(self, order_id: int, number_redirect: int, service="any"):
        params = {
            "metod": "redirect",
            "id": int(order_id),
            "number_redirect": int(number_redirect),
        }
        return self.__request(params)

    def redirect_confirm(self, order_id: int, number_redirect: int, service="any"):
        params = {
            "metod": "redirect_confirm",
            "id": int(order_id),
            "number_redirect": int(number_redirect),
        }
        return self.__request(params)

    def __request(self, params):
        params["apikey"] = self.api_key

        available_services = self.__available_services
        available_countries = self.__available_countries

        if "service" in params:
            if "any" == params["service"]:
                params["service"] = services.Any

            elif not params["service"] in available_services:
                print(params["service"])
                raise exceptions.InvalidService("Invalid service specified")

        if "country" in params and params["country"] in available_countries:
            raise exceptions.InvalidCountry("invalid country specified")

        response = requests.post(self.__API_URL, params=params)

        try:
            response = response.json()
        except:
            error_text = response.text
            error_text = transliterate.translit(error_text, "ru", reversed=True)
            raise exceptions.ApiError(error_text)

        if "response" in response:
            response_text = response["response"]
            if "error" == str(response_text):
                raise exceptions.ApiError(response["error_msg"])

            elif response_text.isdigit() and int(response_text) in [5, 6, 7]:
                if 5 == response["response"]:
                    error_text = "Exceeded the number of requests per minute"
                    raise exceptions.ApiError(error_text)

                elif 6 == response["response"]:
                    error_text = "You are banned for 10 minutes because you have accumulated negative karma"
                    raise exceptions.ApiError(error_text)

                elif 7 == response["response"]:
                    error_text = "Exceeded the number of simultaneous threads. Wait for a text message from previous orders"
                    raise exceptions.ApiError(error_text)

        return response
