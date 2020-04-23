from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.threads.models import Thread

@app.route("/threads/", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())