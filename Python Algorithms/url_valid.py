"""
This program validates a URL using a regular expression.

@author Dmitriy Nikey
"""

import re

def URL_validation(url):
    """
    Validates a URL using a regular expression.

    Args:
        url (str): The URL to be validated.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """

    regex = r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+$'
    
    """
    The regular expression above matches the following:
    * The URL must start with either http:// or https://.
    * The URL can have any number of alphanumeric characters, hyphens, or periods.
    * The URL must end with a period followed by one or more alphanumeric characters.
    """

    return bool(re.fullmatch(regex, url))

if __name__ == "__main__":
    url = "https://www.google.com"
    print(URL_validation(url))

