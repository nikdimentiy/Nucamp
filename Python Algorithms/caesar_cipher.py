import string

def caesar(s, k, decode=False):
    """
    Encode or decode a message using the Caesar cipher.

    The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted
    a certain number of places down or up the alphabet. In this implementation, you can
    specify a key (k) to shift the letters. To decode a message, set decode=True.

    Parameters:
    s (str): The input message to be encoded or decoded.
    k (int): The key for the Caesar cipher (number of positions to shift).
    decode (bool, optional): If True, decode the message; otherwise, encode it (default is False).

    Returns:
    str: The encoded or decoded message.
    """
    if decode:
        # If decode is True, adjust the key to perform decoding.
        k = 26 - k

    # Use the translate method to shift letters in the message.
    return s.translate(
        str.maketrans(string.ascii_uppercase + string.ascii_lowercase,
                      string.ascii_uppercase[k:] + string.ascii_uppercase[:k] +
                      string.ascii_lowercase[k:] + string.ascii_lowercase[:k]))

# Example usage:
if __name__ == "__main__":
    msg = "The quick brown fox jumped over the lazy dogs"
    print("Original Message:")
    print(msg)

    # Encode the message with a key of 11
    enc = caesar(msg, 11)
    print("\nEncoded Message:")
    print(enc)

    # Decode the message with the same key (11)
    dec = caesar(enc, 11, decode=True)
    print("\nDecoded Message:")
    print(dec)
