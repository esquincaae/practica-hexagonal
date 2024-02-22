from flask import Blueprint, request, jsonify
from dependencies.dependency_container import task_service

task_blueprint = Blueprint('task_blueprint', __name__)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = task_service.add_task(title=data['title'])
    # Asegúrate de convertir el objeto Task a un diccionario antes de jsonify
    return jsonify(task.to_dict()), 201

@task_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_service.get_task(task_id)
    if task:
        # Convierte el objeto Task a un diccionario antes de enviarlo
        return jsonify(task.to_dict()), 200
    return jsonify({'message': 'Task not found'}), 404

@task_blueprint.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = task_service.get_all_tasks()
    # Convierte cada objeto Task en la lista a un diccionario
    tasks_dict = [task.to_dict() for task in tasks]
    return jsonify(tasks_dict), 200

@task_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = task_service.update_task(task_id, title=data.get('title'), completed=data.get('completed'))
    if task:
        # Convierte el objeto Task actualizado a un diccionario antes de enviarlo
        return jsonify(task.to_dict()), 200
    return jsonify({'message': 'Task not found'}), 404

@task_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_service.delete_task(task_id):
        return jsonify({}), 204
    return jsonify({'message': 'Task not found'}), 404
