import base64


def base_64_decode(encoded_text):
    return base64.urlsafe_b64decode(encoded_text).decode('utf-8',
                                                         errors='replace')
