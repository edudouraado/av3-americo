# 🚗 Garagem Dashboard Pro

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=FINALIZADO&color=GREEN&style=for-the-badge)
![License](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

<div align="center">
  <img src="./assets/dashboard-preview.png" alt="Preview do Dashboard" width="100%">
</div>

## 📖 Sobre o Projeto

O **Garagem Dashboard Pro** é um sistema de gestão de frota automotiva (SaaS) desenvolvido como requisito final da disciplina de **Projeto e Arquitetura de Sistemas** da **UNIFOR** (Universidade de Fortaleza).

O objetivo principal foi aplicar conceitos robustos de Engenharia de Software, focando na separação de responsabilidades, padrões de projeto e persistência de dados em nuvem.

### 🎯 Funcionalidades

- [x] **Dashboard Interativo:** Visão geral com gráficos dinâmicos de distribuição da frota.
- [x] **Gestão de Inventário (CRUD):** Cadastro, Listagem, Edição e Exclusão de veículos.
- [x] **Persistência de Dados:** Integração completa com banco de dados PostgreSQL.
- [x] **Central de Notícias:** Feed simulado com novidades do setor automotivo.
- [x] **Design Responsivo:** Interface "Mobile First" adaptável a qualquer tamanho de tela.
- [x] **Glassmorphism UI:** Estética moderna utilizando efeitos de vidro e transparência.

---

## 🚀 Tecnologias & Arquitetura

O sistema foi construído utilizando uma arquitetura distribuída **(Front-end e Back-end separados)**, respeitando os padrões **MVC** (Model-View-Controller) e **Camadas** (Layers).

### 🛠 Tech Stack

| Camada | Tecnologia | Detalhes |
| :--- | :--- | :--- |
| **Frontend** | ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=flat&logo=javascript&logoColor=%23F7DF1E) | Vanilla JS, Glassmorphism CSS, Fetch API |
| **Backend** | ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white) | API RESTful, Padrão Repository, Services |
| **Database** | ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=flat&logo=postgresql&logoColor=white) | Relacional, hospedado na Nuvem |
| **Deploy** | ![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=flat&logo=vercel&logoColor=white) ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=flat&logo=render&logoColor=white) | Front na Vercel, Back + DB no Render |

---

## 🔗 Links do Projeto

Para testar a aplicação em produção, acesse:

| Ambiente | Link |
| :--- | :--- |
| **Aplicação (Frontend)** | [Acessar Dashboard](https://av3-americo.vercel.app) |
| **API (Backend)** | [Acessar JSON](https://av3-americo.onrender.com/carros) |

---

## 📦 Como rodar localmente

Se desejar rodar o projeto na sua máquina, siga os passos abaixo:

### Pré-requisitos
* Python 3.x instalado
* Git instalado

### 1. Clone o repositório
```bash
git clone [https://github.com/edudouraado/av3-americo](https://github.com/edudouraado/av3-americo)
cd NOME-DO-REPO