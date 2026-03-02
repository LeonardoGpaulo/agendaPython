from flask import Flask, render_template, request, redirect, url_for
from models.tarefa import Tarefa
from models.database import init_db

app = Flask(__name__)

init_db()


@app.route("/", methods=["GET", "POST"])
def agenda():
    tarefas = None

    if request.method == "POST":
        titulo_tarefa = request.form["titulo-tarefa"]
        data_conclusao = request.form["data-conclusao"]
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()

    tarefas = Tarefa.obter_tarefas()
    return render_template("agenda.html", titulo="Agenda", tarefas=tarefas)


@app.route("/delete/<int:idTarefa>")
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for("agenda"))


@app.route("/complete/<int:idTarefa>")
def complete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.completar_tarefa()
    return redirect(url_for("agenda"))


@app.route("/reabrir/<int:idTarefa>")
def reabrir(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.reabrir_tarefa()
    return redirect(url_for("agenda"))


@app.route("/uptade/<int:idTarefa>", methods=["GET", "POST"])
def uptade(idTarefa):
    if request.method == "POST":
        titulo = request.form["titulo-tarefa"]
        data = request.form["data-conclusao"]
        tarefa = Tarefa(titulo, data, idTarefa)
        tarefa.atualizar_tarefa()
        return redirect(url_for("agenda"))

    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)

    return render_template(
        "agenda.html",
        titulo=f"Editando a tarefa ID: {idTarefa}",
        tarefas=tarefas,
        tarefa_selecionada=tarefa_selecionada,
    )
