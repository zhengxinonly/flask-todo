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


@app.route('/add_todo', methods=["POST"])
def add_todo():
    info = request.form.get('info', None)
    if info:
        todo.count += 1
        item = {
            'id': todo.count,
            'info': info,
            'done': False
        }
        todo.todo_list.append(item)

    return redirect('/')


@app.route('/clear_todo')
def clear_todo():
    todo_id = request.args.get('id', None)
    print(todo_id)
    if todo_id and todo_id.isdigit():
        todo_id = int(todo_id)
        current_todo = list(filter(lambda item: item['id'] == todo_id, todo.todo_list))
        if current_todo[0] in todo.todo_list:
            todo.todo_list.remove(current_todo[0])
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
