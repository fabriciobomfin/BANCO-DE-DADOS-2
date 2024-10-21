from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Criando um usuário.
    service.criar_usuario("Marta", "marta@gmail.com", "123")

    # Listando todos os usuarios.
    print("\nListando todos os usuarios.")
    lista_usuarios = service. listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} -{usuario.senha}")

if __name__ == "_main_":
    main() # Chamada para função.