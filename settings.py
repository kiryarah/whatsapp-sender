import os


twilio_settings = {
    'url': f"https://api.p.2chat.io/open/whatsapp/check-number/{os.getenv('base_phone')}/",
    'payload': {},
    'headers': {
        'X-User-API-Key': 'UAKf8a73063-ee4c-4902-bcc2-7ce5e21bb3f9',
    }
}
