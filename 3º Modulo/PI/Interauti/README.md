# Interauti

Sistema de gerenciamento de tarefas desenvolvido especialmente para atender às necessidades da comunidade autista.

## Funcionalidades

- Autenticação de usuários
- Criação, edição e exclusão de tarefas
- Marcação de tarefas como concluídas
- Definição de data de vencimento
- Interface intuitiva e acessível
- Design responsivo

## Tecnologias Utilizadas

- Node.js
- Express.js
- MongoDB
- EJS
- Bootstrap 5
- Font Awesome

## Requisitos

- Node.js 14.x ou superior
- MongoDB 4.x ou superior
- NPM ou Yarn

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/interauti.git
cd interauti
```

2. Instale as dependências:
```bash
npm install
```

3. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
PORT=3000
MONGODB_URI=mongodb://localhost:27017/interauti
JWT_SECRET=sua_chave_secreta_muito_segura
NODE_ENV=development
```

4. Inicie o servidor:
```bash
npm run dev
```

O servidor estará rodando em `http://localhost:3000`.

## Estrutura do Projeto

```
interauti/
├── controllers/     # Controladores da aplicação
├── models/         # Modelos do MongoDB
├── routes/         # Rotas da aplicação
├── views/          # Templates EJS
├── public/         # Arquivos estáticos
├── middleware/     # Middlewares
├── app.js          # Arquivo principal
└── package.json    # Dependências
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Seu Nome - [@seu_twitter](https://twitter.com/seu_twitter) - seu.email@exemplo.com

Link do Projeto: [https://github.com/seu-usuario/interauti](https://github.com/seu-usuario/interauti)
