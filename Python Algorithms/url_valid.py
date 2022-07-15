import re

# regex for url validation


def URL_validation(url):
    regex = r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+$'
    return bool(re.fullmatch(regex, url))
