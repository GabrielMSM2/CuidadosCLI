# CuidadoCLI 💊

![CI Pipeline](https://github.com/GabrielMSM2/CuidadosCLI/actions/workflows/ci.yml/badge.svg)

CuidadoCLI is a command-line application designed to help
caregivers and family members manage medication schedules.
The main focus is simplicity and reliability, ensuring that
medication records and queries are done quickly and safely.

## 🎯 Real Problem
Difficulty managing multiple medication schedules for elderly
people or patients undergoing continuous treatment.

## ⚙️ Continuous Integration (CI)
This project implements a CI pipeline via GitHub Actions.
On every code update, the server automatically runs static
analysis (Flake8) and automated tests (Pytest).

## ✨ Features
- **Register Medication:** Add medication name and schedule
  with data validation.
- **List Medications:** View all items registered in the
  system.

## 💻 How to Install and Run

**1. Clone the repository**

```bash

git clone https://github.com/GabrielMSM2/CuidadosCLI.git

cd CuidadosCLI

```

**2. Install dependencies**

```bash

pip install -r requirements.txt

```

**3. Run the project**

```bash

python src/main.py

```

**4. Run local tests**

```bash

python -m pytest tests/

```

## 🔧 Technologies Used
- **Python** — Core language
- **Pytest** — Automated testing
- **Flake8** — Code standardization
- **GitHub Actions** — Pipeline automation
