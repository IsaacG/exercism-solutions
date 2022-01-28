"""Diffie Hellman utilities."""
import random


def private_key(p: int) -> int:
    """Return a random private key."""
    return random.randint(2, p - 1)


def public_key(p: int, g: int, private: int) -> int:
    """Return a public key."""
    return g ** private % p


def secret(p: int, public: int, private: int) -> int:
    """Return a shared secret key."""
    return public ** private % p
