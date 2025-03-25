# Sistema de Gerenciamento de Tarefas Simples

## Solicitação do Cliente:
>Prezado,
>
>Necessitamos de um sistema simples para gerenciar as tarefas da nossa equipe. Atualmente, utilizamos planilhas e e-mails, o que se tornou ineficiente.
>
>O sistema deve permitir que um usuário (identificado por um nome e e-mail únicos) possa criar, atribuir, atualizar e deletar tarefas. Cada tarefa deve ter um título, descrição, data de vencimento e status (pendente, em andamento, concluída).
>
>O sistema deve garantir que cada tarefa seja atribuída a um único usuário. Além disso, gostaríamos de ter a possibilidade de filtrar as tarefas por usuário, status e data de vencimento.
>
>É fundamental que o sistema seja rápido e responsivo, mesmo com um grande número de tarefas.
>
>A segurança dos dados é crucial, e o acesso deve ser restrito a usuários autenticados. Queremos também que o sistema seja fácil de manter e escalar no futuro.
>

**1. Análise da Solicitação**
- ***Casos de Uso***: (Ex: Criar Tarefa, Atribuir Tarefa, Atualizar Tarefa, Listar Tarefas, Deletar Tarefa)
- ***Requisitos Funcionais:*** (Ex: Usuários podem criar tarefas com título, descrição, data de vencimento e status; Tarefas podem ser filtradas por usuário, status e data de vencimento)
- ***Requisitos Não-Funcionais:*** (Ex: Rápido e responsivo, seguro, fácil de manter e escalar)
- ***Autores:*** Pedro Arthur
- ***Regras de Negócio:*** (Ex: Cada tarefa deve ser atribuída a um único usuário; E-mails de usuários devem ser únicos.)

**2. Configuração do Ambiente**
- Docker e Postgres
- Projeto Python (FastAPI)

**3. Modelagem do Banco de Dados**

**4. Implementação das Rotas da API**
- ***Criar Usuário (POST /users):*** Validação dos dados (e-mail único)
- ***Criar Tarefa (POST /tasks):*** Atribuição da tarefa a um usuário existente.
- ***Listar Tarefas (GET /tasks):*** Filtragem por usuário, status e data de vencimento (opcional).
- ***Atualizar Tarefa (PUT /tasks/{task_id}):*** Alterar título, descrição, data de vencimento e status
- ***Deletar Tarefa*** (DELETE /tasks/{task_id}).

**5. Teste e Ajustes**