# CuidadoCLI 💊

![CI Pipeline](https://github.com/GabrielMSM2/CuidadosCLI/actions/workflows/ci.yml/badge.svg)

O **CuidadoCLI** é uma aplicação de linha de comando desenvolvida para auxiliar
cuidadores e familiares na organização de horários de medicamentos. O foco
principal é a simplicidade e a confiabilidade, garantindo que o registro e a
consulta de remédios sejam feitos de forma rápida e segura.

## 👤 Integrante

- **Gabriel Moreira Souto Mayor** — RA 22552411

## 🎯 Problema Real

Dificuldade no controle de múltiplos horários de medicamentos para idosos
ou pessoas em tratamentos contínuos.

## ⚙️ Integração Contínua (CI)

Este projeto implementa um pipeline de CI via GitHub Actions. A cada
atualização no código, o servidor executa automaticamente a análise
estática (Flake8) e os testes (Pytest).

## ✨ Funcionalidades

- **Registrar Medicamento:** Cadastro de nome e horário com validação de
  dados. As informações são persistidas em um banco de dados em nuvem.
- **Listar Medicamentos:** Visualização de todos os itens cadastrados,
  buscados em tempo real no banco de dados.
- **Consultar Informações do Medicamento:** Consulta de informações clínicas
  via API pública OpenFDA, diretamente pelo terminal.

## 🗄️ Banco de Dados

O CuidadoCLI utiliza o **[Supabase](https://supabase.com)** (PostgreSQL)
como banco de dados em nuvem, substituindo o armazenamento em memória.
Todos os medicamentos cadastrados são persistidos e continuam disponíveis
entre execuções.

**Tabela:** `medications` (colunas: `id`, `name`, `time`, `created_at`)

## 🔌 Integração com API Externa

O CuidadoCLI integra a **[OpenFDA API](https://api.fda.gov)**, base pública
do FDA americano, permitindo consultar informações clínicas de medicamentos
diretamente pelo terminal. Nenhuma chave de API é necessária. Acesse pelo
menu opção `3. Consultar informações do medicamento`.

## 💻 Como Instalar e Rodar

**1. Clone o repositório**
```bash
git clone https://github.com/GabrielMSM2/CuidadosCLI.git
cd CuidadosCLI
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto com suas credenciais do Supabase:
Exemplo:
SUPABASE_URL=sua_url_do_projeto_supabase
SUPABASE_KEY=sua_chave_publishable_do_supabase
> As credenciais ficam disponíveis em Project Settings → API no Supabase.

**4. Execute o projeto**
```bash
python src/main.py
```

**5. Execute os testes locais**
```bash
python -m pytest tests/
```

## 🚀 Deploy

O CuidadoCLI é uma aplicação CLI disponível publicamente via GitHub.

👉 **Repositório público:** https://github.com/GabrielMSM2/CuidadosCLI

## 🔧 Tecnologias Utilizadas

- **Python** — Linguagem principal
- **Supabase (PostgreSQL)** — Banco de dados em nuvem
- **Pytest** — Testes automatizados
- **Flake8** — Padronização de código
- **Requests** — Comunicação HTTP com API externa
- **GitHub Actions** — Automação de Pipeline