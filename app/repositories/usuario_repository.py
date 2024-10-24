from models.usuario import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__ (self, session: Session) -> None:
        self.session = session 

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh()

    def pesquisar_usuario(self, email: str):
        return self.session.query(Usuario).selter_by(email = email).filter_by(email = email)
    
    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh()

    def listar_todos_usuario(self):
        return self.session.query(Usuario).all()
