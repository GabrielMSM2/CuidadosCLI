from manager import MedicationManager


def main():
    manager = MedicationManager()
    print("=== Bem-vindo ao CuidadoCLI ===")
    print("O seu assistente para horários de medicamentos.")

    while True:
        print("\n1. Registrar Medicamento")
        print("2. Listar Medicamentos")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome do remédio (ex: Aspirina): ")
            time = input("Horário (ex: 08:00): ")
            try:
                manager.add_medication(name, time)
                print("✅ Remédio registrado com sucesso!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif choice == '2':
            meds = manager.list_medications()
            if not meds:
                print("\n--- Nenhum remédio registrado ainda. ---")
            else:
                print("\n--- Remédios Registrados ---")
                for med in meds:
                    print(f"- {med['name']} às {med['time']}")

        elif choice == '3':
            print("Saindo... Cuide-se bem!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
