from application import app, db, login_required, login_manager
from flask import redirect, render_template, request, url_for
from flask_login import  current_user
from application.threads.models import Thread
from application.threads.forms import ThreadForm
from application.posts.models import Post
from application.posts.forms import PostForm

@app.route("/threads/", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())

@app.route("/threads/<thread_id>/", methods = ["GET"])
def view_thread(thread_id):
    thread = Thread.query.get(thread_id)

    posts = Post.query.filter_by(thread_id = thread_id)

    return render_template("threads/thread.html", thread = thread, posts = posts, form = PostForm())

@app.route("/threads/<thread_id>/delete", methods=["GET"])
@login_required
def delete_thread(thread_id):
    thread = Thread.query.get(thread_id)

    print(current_user.roles())

    if not(thread.user_id == current_user.id or "ADMIN" in current_user.roles()):
        return login_manager.unauthorized()

    Thread.query.filter_by(id=thread_id).delete()

    db.session().commit()
  
    return redirect(url_for("boards_index"))

@app.route("/threads/<thread_id>/edit", methods = ["GET", "POST"])
@login_required
def edit_thread(thread_id):
    thread = Thread.query.get(thread_id)

    if not(thread.user_id == current_user.id or "ADMIN" in current_user.roles()):
        return login_manager.unauthorized()

    if request.method == "GET":
        return render_template("threads/edit.html", form = ThreadForm(), thread = thread)

    thread.title = request.form.get("title")
    db.session().commit()
  
    return redirect(url_for("view_thread", thread_id = thread_id))

@app.route("/threads/<thread_id>/reply", methods = ["POST"])
@login_required
def thread_reply(thread_id):
    thread = Thread.query.get(thread_id)

    form = PostForm(request.form)

    if not form.validate():
        return redirect(url_for("view_thread", thread_id = thread_id, form = form))

    post = Post(form.message.data)
    post.user_id = current_user.id
    post.thread_id = thread.id

    db.session().add(post)
    db.session().commit()
  
    return redirect(url_for("view_thread", thread_id = thread_id, form = ThreadForm()))