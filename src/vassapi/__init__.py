"""Voice Assistant Python client."""

from functools import lru_cache
from typing import Any, Optional

from .base import BaseClient
from .const import STATUS_ACTIVE, Endpoint
from .models import DeviceInfo, States


class CoreFunctionsClient(BaseClient):
    """Client with core functionality."""

    def is_running(self) -> bool:
        return self.get(Endpoint.STATUS).text == STATUS_ACTIVE  # type: ignore

    def trigger(self) -> None:
        """Trigger Voice Assistant."""
        self.get(Endpoint.TRIGGER)

    def reload(self) -> None:
        """Reload Voice Assistant."""
        self.get(Endpoint.RELOAD)

    def say(self, message: str, cache: bool = False) -> None:
        """Perform text to speech."""
        self.post(Endpoint.SAY, json={"text": message, "cache": cache})

    def skills(self) -> list[str]:
        """Get list of current skill names."""
        return self.get(Endpoint.SKILLS).json()  # type: ignore

    def run_skill(self, name: str, entities: Optional[dict] = None) -> None:
        """Run skills."""
        self.get(Endpoint.SKILLS, json={"name": name, "entities": entities or {}})

    def config(self) -> dict:
        """Get Voice Assistant's config."""
        return self.get(Endpoint.CONFIG).json()  # type: ignore

    def set_config(self, config: dict) -> None:
        """Set Voice Assistant's config."""
        self.post(Endpoint.CONFIG, json=config)

    @lru_cache
    def info(self) -> DeviceInfo:
        """Get host device info."""
        info = self.get(Endpoint.INFO).json()
        return DeviceInfo(
            name=info["name"],
            version=info["version"],
            uuid=info["uuid"],
            language=info["language"],
            area=info["area"],
        )

    def states(self) -> States:
        """Get Voice Assistant's states."""
        states = self.get(Endpoint.STATES).json()
        return States(
            input_muted=states["input_muted"],
            output_muted=states["output_muted"],
            output_volume=states["output_volume"],
        )

    def set_state(self, attribute: str, value: Any) -> None:
        """Set state of an attribute."""
        self.post(Endpoint.STATES, json={attribute: value})


class DerivedFunctionsClient(CoreFunctionsClient):
    """Client with derived functionality."""

    def set_input_mute(self, mute: bool) -> None:
        """Enable or disable microphone."""
        self.set_state("input_muted", mute)

    def set_output_mute(self, mute: bool) -> None:
        """Set volume mute of host device."""
        self.set_state("output_muted", mute)

    def set_output_volume(self, level: int) -> None:
        """Set volume level of host device."""
        self.set_state("output_volume", level)


class Client(DerivedFunctionsClient):
    """Voice Assistant client."""


__all__ = ["Client"]
