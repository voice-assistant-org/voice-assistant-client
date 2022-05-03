"""Host data models."""

from dataclasses import dataclass


@dataclass
class States:
    """Respresent states of voice assistant device."""

    input_muted: bool
    output_muted: bool
    output_volume: int


@dataclass
class DeviceInfo:
    """Represent info about voice assistant device."""

    name: str
    version: str
    uuid: str
    language: str
    area: str
