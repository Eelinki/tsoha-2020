from flask import render_template
from application import app
from application.auth.models import User
from application.boards.models import Board

@app.route("/")
def index():
    return render_template("index.html", new_users=User.users_without_threads(), board_thread_count = Board.board_thread_count())