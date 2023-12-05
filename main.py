import pywhatkit


def send_msg(text, phone):
    pywhatkit.sendwhatmsg_instantly(
        phone_no=phone,
        message=text,
        tab_close=True
        )

    print(f'{phone}: отправлено!')


text = 'Hello my friend!'
