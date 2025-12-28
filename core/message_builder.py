from typing import Optional
import re

class MessageBuilder:

    def __init__(self, default_signature: Optional[str] = "Whizzap"):
        self.default_signature = default_signature

    def _clean_prompt(self, prompt: str) -> str:
        text = prompt.lower()

        remove_phrases = [
            "send message to",
            "send a message to",
            "send message",
            "inform",
            "notify",
            "about",
            "regarding",
            "please",
        ]

        for phrase in remove_phrases:
            text = text.replace(phrase, " ")

        role_words = [
            "hr", "human resources", "class teacher", "teacher",
            "correspondent", "administrator", "principal",
            "dean", "director", "coordinator", "exam",
            "vice principal", "system administrator"
        ]

        for role in role_words:
            text = text.replace(role, " ")

        text = re.sub(r"\s+", " ", text).strip()
        return text

    def build(self, prompt: str, recipient_name: str, tone: str = "neutral") -> str:
        core_text = self._clean_prompt(prompt)

        if any(w in core_text for w in ["organize", "arrange", "conduct"]):
            clean_text = re.sub(r"\b(to\s+)?organize\b", "organizing", core_text)
            body = f"Kindly requesting you to proceed with {clean_text}."

        elif any(w in core_text for w in ["hall", "allocation"]):
            body = f"This is to inform you regarding {core_text}."

        elif any(w in core_text for w in ["meeting", "schedule", "review"]):
            body = f"This message is regarding {core_text}."

        else:
            body = f"This is to inform you regarding {core_text}."

        body = body[0].upper() + body[1:]

        if tone == "formal":
            return (
                f"Hello {recipient_name},\n\n"
                f"{body}\n\n"
                f"Regards,\n{self.default_signature}"
            )
        else:
            return (
                f"Hi {recipient_name},\n\n"
                f"{body}\n\n"
                f"{self.default_signature}"
            )
