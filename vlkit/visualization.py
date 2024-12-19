import hashlib


def str2color(s: str) -> tuple:
    """
    Maps a string to a consistent RGB color.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple (r, g, b) with each value in the range [0, 255].
    """
    hash_object = hashlib.sha256(s.encode('utf-8'))
    hex_digest = hash_object.hexdigest()

    r = int(hex_digest[0:2], 16)
    g = int(hex_digest[2:4], 16)
    b = int(hex_digest[4:6], 16)

    return (r, g, b)