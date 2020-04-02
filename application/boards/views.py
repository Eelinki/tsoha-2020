from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.boards.models import Board
from application.boards.forms import BoardForm

@app.route("/boards/", methods=["GET"])
def boards_index():
    return render_template("boards/list.html", boards = Board.query.order_by(Board.boardname).all())

@app.route("/boards/manage", methods=["GET"])
def boards_manage():
    return render_template("boards/list.html", boards = Board.query.order_by(Board.boardname).all(), manage = True)

@app.route("/boards/new", methods=["POST"])
def boards_create():
    form = BoardForm(request.form)

    if not form.validate():
        return render_template("boards/new.html", form = form)

    board = Board(form.boardname.data)

    db.session().add(board)
    db.session().commit()
  
    return redirect(url_for("boards_index"))

@app.route("/boards/<board_id>/delete", methods=["POST"])
@login_required
def delete_board(board_id):
    Board.query.filter_by(id=board_id).delete()

    db.session().commit()
  
    return redirect(url_for("boards_index"))

@app.route("/boards/<board_id>/edit", methods = ["GET", "POST"])
@login_required
def edit_board(board_id):
    board = Board.query.get(board_id)

    if request.method == "GET":
        return render_template("boards/edit.html", form = BoardForm(), board = board)

    board.boardname = request.form.get("boardname")
    db.session().commit()
  
    return redirect(url_for("boards_index"))

@app.route("/boards/new")
@login_required
def boards_form():
    return render_template("boards/new.html", form = BoardForm())