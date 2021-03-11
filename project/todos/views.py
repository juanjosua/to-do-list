from flask import render_template, request, redirect, Blueprint
from project.models import Todo
from project import db

todos_blueprint = Blueprint(
    'todos',
    __name__,
    template_folder='templates'
)


@todos_blueprint.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('todos/index.html', tasks=tasks)


@todos_blueprint.route('/delete/<int:id>')
def delete(id):
    tasK_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(tasK_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task.'


@todos_blueprint.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('todos/update.html', task=task)
