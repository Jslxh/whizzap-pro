import pandas as pd
import os
import faiss
import numpy as np


class FaissEngine:
    def __init__(
        self,
        contacts_path="data/contacts.csv",
        index_path="data/faiss.index"
    ):
        self.contacts_path = contacts_path
        self.index_path = index_path
        self.contacts_df = None
        self.index = None

    def load_contacts(self):
        if not os.path.exists(self.contacts_path):
            raise FileNotFoundError("Contacts file not found")

        self.contacts_df = pd.read_csv(self.contacts_path)

    def build_index(self):
        self.load_contacts()

        roles = self.contacts_df["role"].astype(str).tolist()
        dim = 128
        vectors = np.zeros((len(roles), dim), dtype="float32")

        for i, role in enumerate(roles):
            for ch in role:
                vectors[i][ord(ch) % dim] += 1

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(vectors)
        faiss.write_index(self.index, self.index_path)

    def search(self, role: str, top_k: int = 1):
        if self.index is None:
            self.index = faiss.read_index(self.index_path)
            self.load_contacts()

        dim = self.index.d
        vec = np.zeros((1, dim), dtype="float32")

        for ch in role:
            vec[0][ord(ch) % dim] += 1

        _, indices = self.index.search(vec, top_k)

        results = []
        for idx in indices[0]:
            row = self.contacts_df.iloc[int(idx)]
            results.append({
                "name": row["name"],
                "role": row["role"],
                "phone": str(row["phone"])
            })

        return results
