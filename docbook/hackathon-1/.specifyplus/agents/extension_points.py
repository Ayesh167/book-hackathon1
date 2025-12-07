# extension_points.py placeholder
# This file will enable extension points for Gemini CLI sub-agents.

from typing import Callable, Dict

class AgentExtensionPoints:
    _extension_points: Dict[str, Callable] = {}

    def register_extension(self, name: str, func: Callable):
        """Registers a callable as an extension point."""
        print(f"Enabling extension point: {name}")
        self._extension_points[name] = func

    def get_extension(self, name: str) -> Callable:
        """Retrieves a registered extension point."""
        return self._extension_points.get(name)