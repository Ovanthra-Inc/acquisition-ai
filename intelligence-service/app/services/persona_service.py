from enum import Enum
from typing import Dict, Any

class PersonaType(Enum):
    CONSULTATIVE = "consultative"
    DIRECT = "direct"
    RELATABLE = "relatable"
    VISIONARY = "visionary"

class PersonaService:
    @staticmethod
    def get_persona_modifiers(persona: PersonaType) -> Dict[str, str]:
        """Returns specific instructions and tone modifiers for each persona."""
        modifiers = {
            PersonaType.CONSULTATIVE: {
                "tone": "helpful, curious, and expert",
                "instruction": "Focus on asking thoughtful questions about their current workflow. Position Ovanthra as a strategic partner."
            },
            PersonaType.DIRECT: {
                "tone": "concise, confident, and results-oriented",
                "instruction": "Get straight to the value proposition. Use bullet points for impact. Minimize small talk."
            },
            PersonaType.RELATABLE: {
                "tone": "casual, friendly, and shared-struggle oriented",
                "instruction": "Use a first-name basis. Reference common industry headaches and use slightly more informal language."
            },
            PersonaType.VISIONARY: {
                "tone": "inspiring, forward-thinking, and bold",
                "instruction": "Focus on the future of AI and how they can lead their industry. Use evocative and ambitious language."
            }
        }
        return modifiers.get(persona, modifiers[PersonaType.CONSULTATIVE])

    def get_prompt_context(self, persona_name: str) -> str:
        try:
            persona = PersonaType(persona_name.lower())
        except ValueError:
            persona = PersonaType.CONSULTATIVE
            
        mods = self.get_persona_modifiers(persona)
        return f"Your tone is {mods['tone']}. {mods['instruction']}"
