import re

# regex for IP address validation IPv4


def IP_validation(IP):
    regex = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
    return bool(re.fullmatch(regex, IP))


my_ip_address = '127.0.0.1'
result = IP_validation(my_ip_address)
print(result)
