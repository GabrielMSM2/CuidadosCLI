import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()


class MedicationManager:
    def __init__(self):
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        self.client = create_client(url, key)

    def add_medication(self, name, time):
        if not name or not name.strip():
            raise ValueError("O nome do medicamento não pode ser vazio.")
        if not time or not time.strip():
            raise ValueError("O horário não pode ser vazio.")

        med = {"name": name.strip(), "time": time.strip()}
        self.client.table("medications").insert(med).execute()
        return med

    def list_medications(self):
        response = self.client.table("medications").select("*").execute()
        return response.data
