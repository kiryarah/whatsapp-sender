import requests
# from settings import twilio_settings
from time import sleep
# import json

# headers = twilio_settings.get('headers')
# payload = twilio_settings.get('payload')
# url = twilio_settings.get('url')


# def check_phone(url, phone):
#     url += f'{phone}'
#     response = requests.request("GET", url, headers=headers, data=payload)

#     try:
#         response.json()['on_whatsapp']
#         return True

#     except KeyError:
#         return False


def write_to_file(file, item):
    with open(file, 'a', encoding='utf-8') as write_file:
        write_file.write(item + '\n')


def read_phones_file(file):
    with open(file, encoding='utf-8') as read_file:
        phone = read_file.readline().strip()

        while phone:
            if whapi_check_phone(phone=phone) == 'valid':
                write_to_file('valid_numbers.txt', phone)
                print(f'{phone} written')
            else:
                write_to_file('invalid_numbers.txt', phone)
                print('Invalid number')

            sleep(7)
            phone = read_file.readline().strip()


def whapi_check_phone(phone):

    url = "https://gate.whapi.cloud/contacts"

    payload = {
        "blocking": "wait",
        "force_check": False,
        "contacts": [phone]
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer bLkkA3xhkBBlH6sZhyGF5j4rVM9iHwPo"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json().get('contacts')[0].get('status')


read_phones_file('numbers.txt')
