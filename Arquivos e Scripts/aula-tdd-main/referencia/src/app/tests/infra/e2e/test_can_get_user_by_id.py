from fastapi.testclient import TestClient
from infra.api.main import app
from uuid import UUID


# Inicializa o cliente de teste para enviar requisições à aplicação FastAPI
client = TestClient(app)


def test_can_get_user_by_id():
    # Cria um novo usuário enviando uma requisição POST para o endpoint "/users/"
    created_user_response = client.post(
        "/users/",
        json={"name": "João"},
    )

    # Extrai os dados JSON da resposta da criação do usuário
    created_user_data = created_user_response.json()

    # Envia uma requisição GET para obter o usuário criado pelo ID gerado
    finded_user_response = client.get(f"/users/{created_user_data['id']}")

    # Verifica se a resposta ao buscar o usuário foi bem-sucedida (código 200)
    assert finded_user_response.status_code == 200
    # Verifica se o ID do usuário criado é uma instância válida de UUID
    assert isinstance(UUID(created_user_data["id"]), UUID) == True
    # Verifica se o nome do usuário criado corresponde ao nome fornecido ("João")
    assert created_user_data["name"] == "João"
