from application import app, db, login_required, login_manager
from flask import redirect, render_template, request, url_for
from flask_login import  current_user
from application.groups.models import Group
from application.groups.forms import GroupForm
from application.auth.models import User

@app.route("/groups/", methods=["GET"])
def list_groups():
    return render_template("groups/list.html", groups = Group.query.all())

@app.route("/groups/new")
@login_required(role="ADMIN")
def group_form():
    return render_template("groups/new.html", form = GroupForm())

@app.route("/groups/new", methods=["POST"])
@login_required(role="ADMIN")
def groups_create():
    form = GroupForm(request.form)

    if not form.validate():
        return render_template("groups/new.html", form = form)

    group = Group(form.groupname.data)

    db.session().add(group)
    db.session().commit()
  
    return redirect(url_for("list_groups"))

@app.route("/groups/<group_id>/join")
@login_required
def join_group(group_id):
    group = Group.query.get(group_id)

    user = User.query.get(current_user.id)

    user.groups.append(group)
    db.session().commit()

    return redirect(url_for('list_groups'))

@app.route("/groups/<group_id>/leave")
@login_required
def leave_group(group_id):
    group = Group.query.get(group_id)

    user = User.query.get(current_user.id)

    user.groups.remove(group)
    db.session().commit()

    return redirect(url_for('list_groups'))