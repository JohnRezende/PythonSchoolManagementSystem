# Sistema de Gerenciamento Escolar

Este projeto foi desenvolvido por mim, João Victor Alves de Rezende, durante a disciplina de **Raciocínio Computacional**, do curso de **Análise e Desenvolvimento de Sistemas**.

## 📚 Sobre o Projeto

Este é um sistema simples de gerenciamento de uma escola hipotética. O sistema foi construído utilizando a linguagem Python e faz uso da biblioteca `json` para persistência de dados em arquivos locais.

O objetivo principal é proporcionar uma experiência prática com lógica de programação, manipulação de arquivos, estruturação de menus e operações básicas de CRUD (Create, Read, Update, Delete).

## ⚙️ Funcionalidades

O sistema permite o gerenciamento de diferentes entidades da escola, tais como:

- **Estudantes**
- **Professores**
- **Disciplinas**
- **Turmas**
- **Matrículas**

Para cada entidade, é possível realizar as seguintes operações:

- Incluir registros
- Listar registros
- Atualizar registros existentes
- Excluir registros

Além disso, o sistema realiza validações básicas, como:

- Verificação de existência de códigos únicos
- Confirmação de relacionamentos válidos entre entidades (por exemplo, só é possível cadastrar uma turma com um professor e disciplina já cadastrados)

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Biblioteca `json` (para persistência dos dados)
- Biblioteca `time` (para controle de navegação e pausas)

## 💾 Estrutura de Persistência

Os dados são armazenados nos seguintes arquivos `.json`, criados automaticamente na execução do sistema:

- `estudantes.json`
- `professores.json`
- `disciplinas.json`
- `turmas.json`
- `matriculas.json`

Esses arquivos garantem que as informações inseridas no sistema não sejam perdidas ao fechar o programa.


