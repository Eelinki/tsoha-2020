from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.boards.models import Board
from application.boards.forms import BoardForm, ThreadForm
from application.threads.models import Thread

@app.route("/boards/", methods=["GET"])
def boards_index():
    return render_template("boards/list.html", boards = Board.query.order_by(Board.boardname).all())

@app.route("/boards/manage", methods=["GET"])
@login_required(role="ADMIN")
def boards_manage():
    return render_template("boards/list.html", boards = Board.query.order_by(Board.boardname).all(), manage = True)

@app.route("/boards/new", methods=["POST"])
@login_required(role="ADMIN")
def boards_create():
    form = BoardForm(request.form)

    if not form.validate():
        return render_template("boards/new.html", form = form)

    board = Board(form.boardname.data)

    db.session().add(board)
    db.session().commit()
  
    return redirect(url_for("boards_index"))

@app.route("/boards/<board_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def delete_board(board_id):
    board = Board.query.get(board_id)

    db.session.delete(board)
    db.session().commit()
  
    return redirect(url_for("boards_index"))

@app.route("/boards/<board_id>/edit", methods = ["GET", "POST"])
@login_required(role="ADMIN")
def edit_board(board_id):
    board = Board.query.get(board_id)

    if request.method == "GET":
        return render_template("boards/edit.html", form = BoardForm(), board = board)

    board.boardname = request.form.get("boardname")
    db.session().commit()
  
    return redirect(url_for("boards_index"))

@app.route("/boards/new")
@login_required(role="ADMIN")
def boards_form():
    return render_template("boards/new.html", form = BoardForm())

@app.route("/board/<board_id>/", methods = ["GET"])
def view_board(board_id):
    board = Board.query.get(board_id)
    threads = Thread.query.filter_by(board_id = board_id)

    return render_template("boards/board.html", board = board, threads = threads)

@app.route("/board/<board_id>/threads/new", methods = ["GET", "POST"])
@login_required
def boards_post_thread(board_id):
    board = Board.query.get(board_id)
    
    if request.method == "GET":
        return render_template("boards/new-thread.html", form = ThreadForm(), board = board)

    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("boards/new-thread.html", form = form, board = board)

    thread = Thread(form.title.data)
    thread.user_id = current_user.id
    thread.board_id = board.id

    db.session().add(thread)
    db.session().commit()
  
    return redirect(url_for("boards_index"))