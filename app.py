from flask import Flask, render_template, request, redirect

from models import todo

app = Flask(__name__)


@app.route('/')
def hello_world():
    key = request.args.get('key', 'all')

    todo_list = []
    if key == 'undone':
        todo_list = todo.undone_list
    elif key == 'done':
        todo_list = todo.done_list
    elif key == 'all':
        todo_list = todo.todo_list

    return render_template('todos.html',
                           todo_list=todo_list,
                           key=key,
                           undone_count=len(todo.undone_list))


@app.route('/clear_done')
def clear_done():
    for item in todo.done_list:
        todo.todo_list.remove(item)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
