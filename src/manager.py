class MedicationManager:
    def __init__(self):
        self.medications = []

    def add_medication(self, name, time):
        if not name or not name.strip():
            raise ValueError("O nome do medicamento não pode ser vazio.")
        if not time or not time.strip():
            raise ValueError("O horário não pode ser vazio.")

        med = {"name": name.strip(), "time": time.strip()}
        self.medications.append(med)
        return med

    def list_medications(self):
        return self.medications
