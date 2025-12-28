from core.faiss_engine import FaissEngine

engine = FaissEngine(
    contacts_path="data/contacts.csv",
    index_path="data/faiss.index"
)

engine.load_contacts()
engine.build_index()

print("FAISS index created successfully.")
