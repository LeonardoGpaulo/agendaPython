
from models.database import Database
from typing import Optional, Self, Any
from sqlite3 import Cursor

class Tarefa:
    """
        Classe para representar uma tarefa, com métodos para salvar, obter, excluir tarefas em um banco de dados usando a classe `Database`.
    """
    def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str]= None, id_tarefa: Optional[int] = None, concluida: Optional[int] = 0) -> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.id_tarefa: Optional[int] = id_tarefa
        self.concluida: Optional[int] = concluida


        #Tarefa(titulo_tarefa='Nova tarefa')
        #Tarefa(titulo-tarefa="Outra tarefa", data_conclusao="2026-02-03")
        #Tarefa(id_tarefa=1)

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, concluida FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)
            #resultado = [["titulo_tarefa, data_conclusao"]]

            #desempacotamento de coleção
            [[titulo,data, concluida]] = resultado

        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data, concluida=concluida)
        
        #Simulando o conceito de sobrecarga
        #Tarefa('título da Tarefa')  
        #Tarefa('Título da Tarefa', '2026-02-03')
        #Tarefa(id_tarefa=1)


    def salvar_tarefa(self: Self) -> None:
        with Database () as db:
            query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao, concluida)VALUES (?,?,?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.concluida)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, id, concluida FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            tarefas: list[Self] = [cls(titulo, data, id, concluida) for titulo, data, id, concluida in resultados]
            return tarefas
        
    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params:tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
        
    def completar_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE tarefas SET concluida = 1 WHERE id = ?;'
            params:tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
        
    def atualizar_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ?, concluida = 0 WHERE id = ?;'
            params:tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado