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
- **Lookup Medication Info:** Query clinical information from
  the OpenFDA public API directly in the terminal.

## 🔌 External API Integration

CuidadoCLI integrates the **[OpenFDA API](https://api.fda.gov)**,
a free public database maintained by the U.S. Food and Drug
Administration, allowing users to query clinical information
about medications directly from the terminal.
No API key required. Access it via menu option `3. Consultar informações do medicamento`.

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

## 🚀 Deploy

CuidadoCLI is a CLI application publicly available via GitHub.

**1. Clone the repository on the entrega-intermediaria branch:**
```bash
git clone https://github.com/GabrielMSM2/CuidadosCLI.git
cd CuidadosCLI
git checkout entrega-intermediaria
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the application:**
```bash
python src/main.py
```

👉 **Public repository:** https://github.com/GabrielMSM2/CuidadosCLI

## 🔧 Technologies Used

- **Python** — Core language
- **Pytest** — Automated testing
- **Flake8** — Code standardization
- **Requests** — HTTP communication with external API
- **GitHub Actions** — Pipeline automation