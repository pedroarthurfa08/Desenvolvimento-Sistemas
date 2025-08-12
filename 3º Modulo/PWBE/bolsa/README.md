# Sistema de Controle de Investimentos em Ações (Bolsa de Valores do Brasil)

## Descrição

Aplicação web para controle de operações de compra e venda de ativos da bolsa de valores, com autenticação de usuários, cálculos automáticos e proteção de dados individuais.

---

## Funcionalidades

- Cadastro e login de usuários (com validação e senha criptografada)
- CRUD completo de operações de investimento (compra/venda)
- Visualização de todas as operações do usuário
- Filtro de operações por código de ativo
- Cálculo automático de valor bruto, taxa B3 (0,03%) e valor líquido
- Proteção de rotas: cada usuário só acessa suas operações
- Interface responsiva com EJS e Bootstrap

---

## Entidades Principais

### Usuário
- id
- nome
- email
- senha (hash)

### Operação
- id
- data_operacao
- tipo (compra/venda)
- codigo_ativo (ex: ITSA4, BBSE3, BCFF11, GOGL34)
- quantidade
- preco_unitario
- valor_bruto (calculado)
- taxa_b3 (calculado)
- valor_liquido (calculado)
- usuario_id (relacionamento)

---

## Tecnologias Utilizadas
- Node.js
- Express.js
- EJS
- PostgreSQL
- express-session
- bcryptjs
- dotenv
- validator
- Bootstrap (CDN)

---

## Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd Bolsa
   ```
2. **Instale as dependências:**
   ```bash
   npm install
   ```
3. **Configure o banco de dados:**
   - Crie um banco PostgreSQL e execute o script `database_creation.sql`.
   - Crie um arquivo `.env` na raiz do projeto com as variáveis de conexão:
     ```
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_HOST=localhost
     DB_PORT=5432
     DB_DATABASE=seu_banco
     ```
4. **Inicie a aplicação:**
   ```bash
   npm start
   ```
5. **Acesse no navegador:**
   ```
   http://localhost:3000
   ```

---

## Estrutura de Pastas
- `controllers/` — Lógica dos controladores (usuário, operação)
- `models/` — Modelos de dados (usuário, operação)
- `routes/` — Definição das rotas
- `views/` — Templates EJS (páginas, partials, layout)
- `public/` — Arquivos estáticos (CSS)
- `db/` — Configuração de conexão com o banco

---

## Observações
- Certifique-se de que o arquivo `.env` não está versionado (adicione ao `.gitignore`).
- O projeto pode ser expandido para incluir relatórios, gráficos, importação de notas de corretagem, etc. 