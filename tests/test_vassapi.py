from vassapi import Client


def test_client_init():
    vass = Client("some host", "some token")
