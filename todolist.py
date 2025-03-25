from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

#rota para listar tarefas    

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})



@app.route('/tasks', methods=['POST'])
def add_task():
    # Receber os dados da requisição
    task_data = request.get_json()  # Alterei de 'tasks' para 'task_data'
    
    # Validar se os dados estão corretos
    if not task_data or 'title' not in task_data:
        return jsonify({'error': 'task é invalida'}), 400

    # Criar uma nova tarefa
    new_task = {
        'id': len(tasks) + 1,  # IDs incrementais
        'title': task_data['title'],
        'done': False
    }
    
    # Adicionar à lista global de tarefas
    tasks.append(new_task)

    return jsonify(new_task), 200


#rota para atualizar tarefas
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        return jsonify({'error': 'task não encontrada'}), 400

    task[0]['title'] = request.get_json().get('title', task[0]['title'])
    task[0]['done'] = request.get_json().get('done', task[0]['done'])
    return jsonify(task[0]), 200

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        return jsonify({'error': 'tarefa não encontrada'}), 400

    tasks.remove(task[0])
    return jsonify({'result': True}), 200

if __name__ == '__main__':  
    app.run(debug=True)
