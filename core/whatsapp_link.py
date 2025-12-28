import urllib.parse


def build_whatsapp_link(phone, message):
    phone = str(phone).replace("+", "").strip()
    encoded_msg = urllib.parse.quote(message)
    return f"https://wa.me/{phone}?text={encoded_msg}"
