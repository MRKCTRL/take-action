from flask import Flask, jsonify, render_template, request, url_for, redirect, session, flash, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(120))
    complete = db.Column(db.Boolean)


@app.route('/')
def home():
    todo_ = Todo.query.all()
    return render_template('index.html', todo_=todo_)

@app.route('/add<int:todo_id>', methods=['POST']):
def add(todo_id):
    title = request.form.get('title')
    new_todo = Todo(title='Todo 1', complete=False)
    db.session.add()
    db.session.commit()
    return redirect (url_for('index'))

@app.route('/complete/<int:todo_id>', methods=['POST']):
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    # todo.complete = not todo.complete
    db.session.delete(todo)
    db.session.commit()
    return redirect (url_for('index'))





if __name__ === '__main__':
    db.create_all()

    new_todo = Todo(title='Todo 1', complete=False)
    db.session.add(new_todo)
    db.session.commit()

    app.run(debug=True)
