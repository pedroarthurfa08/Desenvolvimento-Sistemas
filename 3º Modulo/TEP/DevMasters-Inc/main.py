from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List, Literal
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI()

# 🧠 Banco de dados em memória
banco_projetos = {}

# 📦 Modelos Pydantic
class ProjetoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    prioridade: Literal[1, 2, 3]
    status: Literal["Planejado", "Em Andamento", "Concluído", "Cancelado"]

class ProjetoCriacao(ProjetoBase):
    pass

class ProjetoResposta(ProjetoBase):
    id: UUID
    criado_em: datetime

class ProjetoAtualizacao(ProjetoBase):
    pass

# ✅ Criar novo projeto
@app.post("/projetos", response_model=ProjetoResposta, status_code=201)
def criar_projeto(projeto: ProjetoCriacao):
    id_novo = uuid4()
    criado_em = datetime.now()
    novo_projeto = ProjetoResposta(id=id_novo, criado_em=criado_em, **projeto.dict())
    banco_projetos[id_novo] = novo_projeto
    return novo_projeto

# 📃 Listar projetos com filtro e paginação
@app.get("/projetos", response_model=List[ProjetoResposta])
def listar_projetos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    status: Optional[Literal["Planejado", "Em Andamento", "Concluído", "Cancelado"]] = None,
    prioridade: Optional[Literal[1, 2, 3]] = None
):
    lista = list(banco_projetos.values())
    if status:
        lista = [p for p in lista if p.status == status]
    if prioridade:
        lista = [p for p in lista if p.prioridade == prioridade]
    return lista[skip : skip + limit]

# 🔍 Detalhar um projeto
@app.get("/projetos/{projeto_id}", response_model=ProjetoResposta)
def obter_projeto(projeto_id: UUID):
    projeto = banco_projetos.get(projeto_id)
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado.")
    return projeto

# ✏️ Atualizar projeto
@app.put("/projetos/{projeto_id}", response_model=ProjetoResposta)
def atualizar_projeto(projeto_id: UUID, dados: ProjetoAtualizacao):
    projeto_existente = banco_projetos.get(projeto_id)
    if not projeto_existente:
        raise HTTPException(status_code=404, detail="Projeto não encontrado.")
    projeto_atualizado = projeto_existente.copy(update=dados.dict())
    banco_projetos[projeto_id] = projeto_atualizado
    return projeto_atualizado

# ❌ Deletar projeto
@app.delete("/projetos/{projeto_id}", status_code=204)
def deletar_projeto(projeto_id: UUID):
    if projeto_id not in banco_projetos:
        raise HTTPException(status_code=404, detail="Projeto não encontrado.")
    del banco_projetos[projeto_id]
