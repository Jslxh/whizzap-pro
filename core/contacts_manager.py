import pandas as pd
from pathlib import Path


class ContactsManager:
    def __init__(self, path="data/contacts.csv"):
        self.path = Path(path)

        if not self.path.exists():
            df = pd.DataFrame(columns=["name", "role", "phone"])
            df.to_csv(self.path, index=False)

    def load(self):
        return pd.read_csv(self.path)

    def add_contact(self, name: str, role: str, phone: str):
        df = self.load()
        df.loc[len(df)] = [name.strip(), role.lower().strip(), str(phone)]
        df.to_csv(self.path, index=False)

    def update_contact(self, index: int, name: str, role: str, phone: str):
        df = self.load()
        df.loc[index] = [name.strip(), role.lower().strip(), str(phone)]
        df.to_csv(self.path, index=False)

    def delete_contact(self, index: int):
        df = self.load()
        df = df.drop(index).reset_index(drop=True)
        df.to_csv(self.path, index=False)
