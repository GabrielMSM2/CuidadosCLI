CuidadoCLI 💊

[![CI Pipeline](https://github.com/GabrielMSM2/CuidadosCLI/actions/workflows/ci.yml/badge.svg)](https://github.com/GabrielMSM2/CuidadosCLIactions)

O CuidadoCLI é uma aplicação de linha de comando desenvolvida para auxiliar cuidadores e familiares na organização de horários de medicamentos. O foco principal é a simplicidade e a confiabilidade, garantindo que o registro e a consulta de remédios sejam feitos de forma rápida e segura.

🎯 Problema Real
Dificuldade no controle de múltiplos horários de medicamentos para idosos ou pessoas em tratamentos contínuos, o que pode levar a esquecimentos ou erros de dosagem.

⚙️ Integração Contínua (CI)
Este projeto implementa um pipeline de CI (Continuous Integration) via GitHub Actions.
A cada atualização no código, o servidor executa automaticamente:

Análise Estática (Flake8): Garante que o código siga os padrões de formatação e qualidade PEP-8.

Testes Automatizados (Pytest): Valida as funcionalidades de registro e listagem de medicamentos.

Verificação de Ambiente: Garante que todas as dependências do projeto estão funcionando corretamente.

✨ Funcionalidades
Registrar Medicamento: Cadastro de nome e horário com validação de dados.

Listar Medicamentos: Visualização de todos os itens cadastrados no sistema.

Segurança: Sistema de testes que impede a subida de código com erros para o repositório principal.

💻 Como Instalar e Rodar
Clone o repositório:

Bash
git clone https://github.com/GabrielMSM2/CuidadosCLI.git
cd CuidadosCLI
Instale as dependências:

Bash
pip install -r requirements.txt
Execute o projeto:

Bash
python src/main.py
Execute os testes locais:

Bash
python -m pytest tests/
🛠️ Tecnologias Utilizadas
Python (Linguagem principal)

Pytest (Testes automatizados)

Flake8 (Padronização de código)

GitHub Actions (Automação de Pipeline)