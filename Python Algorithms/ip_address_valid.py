import re

def IP_validation(IP):
    """
    Validate an IPv4 address using regular expressions.

    Args:
        IP (str): The IPv4 address to be validated.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    # Regular expression pattern for IPv4 validation
    regex = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
    
    # Use re.fullmatch() to match the entire input string against the pattern
    return bool(re.fullmatch(regex, IP))

# Example usage
my_ip_address = '127.0.0.1'
result = IP_validation(my_ip_address)
print(f"Is '{my_ip_address}' a valid IPv4 address? {result}")

