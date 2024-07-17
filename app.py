from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey' 

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_priority = request.form['task_priority']
        task_date = request.form['task_date']
        task_hour = request.form['task_hour']
        created_at = datetime.now().isoformat()

        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (task_name, task_priority, task_date, task_hour, created_at) VALUES (?, ?, ?, ?, ?)',
                     (task_name, task_priority, task_date, task_hour, created_at))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', rows=rows)


@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE task_id = ?', (task_id,))
    conn.commit()
    conn.close()
    flash('Tarefa deletada com sucesso!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
