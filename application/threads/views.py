from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.threads.models import Thread
from application.threads.forms import ThreadForm

@app.route("/threads/", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())

@app.route("/threads/new", methods=["POST"])
@login_required
def threads_create():
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/new.html", form = form)

    thread = Thread(form.title.data)
    thread.user_id = current_user.id
    thread.board_id = 1

    db.session().add(thread)
    db.session().commit()
  
    return redirect(url_for("threads_index"))

@app.route("/threads/new")
@login_required
def threads_form():
    return render_template("threads/new.html", form = ThreadForm())