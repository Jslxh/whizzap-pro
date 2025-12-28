import pandas as pd
from typing import Optional


class RoleExtractor:
    """
    Extract role directly from contacts dataset.
    """

    def __init__(self, contacts_path: str = "data/contacts.csv"):
        self.contacts_path = contacts_path
        self.roles = self._load_roles()

    def _load_roles(self):
        df = pd.read_csv(self.contacts_path)
        return [str(r).lower() for r in df["role"].unique()]

    def extract_role(self, prompt: str) -> Optional[str]:
        if not prompt:
            return None

        prompt_lower = prompt.lower()

        for role in self.roles:
            if role in prompt_lower:
                return role

        return None
