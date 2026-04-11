# CuidadoCLI 💊

[![CI Pipeline](https://github.com/GabrielMSM2/cuidado-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/GabrielMSM2/cuidado-cli/actions)

## 🎯 Apresentação e Problema Real
O **CuidadoCLI** nasceu para resolver uma dor real e muito presente na nossa sociedade: **a dificuldade no controle de horários de medicamentos para idosos ou pessoas em tratamento contínuo**. 

Muitos cuidadores (profissionais ou familiares) lidam com múltiplas tarefas diárias, o que pode levar a confusões, superdosagem ou esquecimento da medicação, colocando a saúde do paciente em risco. O público-alvo desta solução são **cuidadores, familiares e as próprias pessoas em tratamento** que precisam de uma ferramenta simples e livre de distrações.

## 💡 A Solução
Em vez de depender de anotações soltas em papel, o CuidadoCLI oferece uma aplicação de Linha de Comando (CLI) direta e eficiente. Ela permite que o cuidador registre o nome do remédio e o horário exato da administração, organizando a rotina de cuidados de forma rápida pelo terminal.

## ✨ Funcionalidades Principais
- Cadastrar novo medicamento informando nome e horário.
- Listar todos os medicamentos cadastrados para conferência.
- Validação de dados (impede o cadastro de medicamentos sem nome ou sem horário).

## 💻 Exemplo de Uso
```text
=== Bem-vindo ao CuidadoCLI ===
O seu assistente para horários de medicamentos.

1. Registrar Medicamento
2. Listar Medicamentos
3. Sair
Escolha uma opção: 1
Nome do remédio (ex: Aspirina): Losartana
Horário (ex: 08:00): 09:00
✅ Remédio registrado com sucesso!