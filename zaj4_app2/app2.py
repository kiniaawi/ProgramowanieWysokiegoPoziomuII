from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista zadań (przechowywana w pamięci)
tasks = []

@app.route('/')
def home():
    return render_template('todo_home.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks_page():
    if request.method == 'POST':
        task_text = request.form.get('task')
        if task_text:
            tasks.append({'text': task_text, 'done': False, 'id': len(tasks)})
    return render_template('tasks.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('tasks_page'))

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    return redirect(url_for('tasks_page'))

@app.route('/about')
def about_todo():
    return render_template('todo_about.html')

if __name__ == '__main__':
    app.run(debug=True)