# skill_registry.py placeholder
# This file will register reusable agent skills.

from typing import Dict, Callable

class AgentSkillRegistry:
    _skills: Dict[str, Callable] = {}

    def register_skill(self, name: str, skill_func: Callable):
        """Registers a reusable agent skill."""
        print(f"Registering agent skill: {name}")
        self._skills[name] = skill_func

    def get_skill(self, name: str) -> Callable:
        """Retrieves a registered agent skill."""
        return self._skills.get(name)