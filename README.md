# CuidadoCLI 💊

[![CI Pipeline](https://github.com/GabrielMSM2/CuidadosCLI/actions/workflows/ci.yml/badge.svg)](https://github.com/GabrielMSM2/CuidadosCLI/actions)

O **CuidadoCLI** é uma aplicação de linha de comando desenvolvida para auxiliar cuidadores e familiares na organização de horários de medicamentos. O foco principal é a simplicidade e a confiabilidade, garantindo que o registro e a consulta de remédios sejam feitos de forma rápida e segura.

🎯 **Problema Real:** Dificuldade no controle de múltiplos horários de medicamentos para idosos ou pessoas em tratamentos contínuos.

⚙️ **Integração Contínua (CI):** Este projeto implementa um pipeline de CI via GitHub Actions. A cada atualização no código, o servidor executa automaticamente a análise estática (Flake8) e os testes (Pytest).

✨ **Funcionalidades:**
- **Registrar Medicamento:** Cadastro de nome e horário com validação de dados.
- **Listar Medicamentos:** Visualização de todos os itens cadastrados no sistema.

💻 **Como Instalar e Rodar:**

**1. Clone o repositório:**
```bash
git clone [https://github.com/GabrielMSM2/CuidadosCLI.git](https://github.com/GabrielMSM2/CuidadosCLI.git)
cd CuidadosCLI
```

**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Execute o projeto:**
```bash
python src/main.py
```

**4. Execute os testes locais:**
```bash
python -m pytest tests/
```

🛠️ Tecnologias Utilizadas:

Python (Linguagem principal)

Pytest (Testes automatizados)

Flake8 (Padronização de código)

GitHub Actions (Automação de Pipeline)