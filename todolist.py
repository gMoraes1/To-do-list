from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

#rota para listar tarefas    

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

#rota para adicionar tarefas    

@app.route('/tasks', methods=['POST'])

def add_task():
    tasks = request.get_json()
    if not tasks or 'title' not in tasks:
        return jsonify({'error': 'task é invalida'}), 400

    new_task = {
        'id': len(tasks) + 1,
        'title': tasks['title'],
        'done': False
    } 
    tasks.append(new_task)

    return jsonify(new_task), 200


#rota para atualizar tarefas

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(tasks_id):
    task = [task for task in tasks if task['id'] == tasks_id]   
    if len(task) == 0:
        return jsonify({'error': 'task não encontrada'}), 400
    
    task['title'] = request.get_json().get('title', task['title'])
    task['done'] = request.get_json().get('done', task['done'])

    return jsonify(task), 200


#rota para deletar tarefas      

@app.route('/tasks/<int:id>', methods=['DELETE'])

def delete_task(tasks_id):
    task = [task for task in tasks in tasks if task['id'] == tasks_id]
    if len(task) == 0:
        return jsonify({'error': 'tarefa nao encontrada'}), 400
    
    tasks.remove(task[0])   
    return jsonify({'result': True}), 200       

if __name__ == '__main__':  
    app.rum(debug=True)
