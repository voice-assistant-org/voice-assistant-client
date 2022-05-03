"""Host client custom errors."""


class ClientError(Exception):
    """Base error."""


class AuthError(ClientError):
    """Authentication error."""
