# Importa a classe principal do FastAPI e o módulo de roteamento de usuários
from fastapi import FastAPI
from infra.api.routers import user_routers

# Instancia o aplicativo FastAPI
app = FastAPI()

# Inclui o roteador de usuários na aplicação principal, registrando todos os endpoints definidos
app.include_router(user_routers.router)
