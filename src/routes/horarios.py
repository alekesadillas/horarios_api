from flask import Blueprint, jsonify, request
from datetime import datetime

#Entities
from models.entities.horarios import Horarios
#Modelos
from models.horarios_model import horarios_model

main = Blueprint('horarios_blueprint', __name__)

@main.route('/')
def get_horarios():
    try:
        horarios= horarios_model.get_horarios()
        return jsonify(horarios)
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<int:id>')
def get_horario_by_id(id):
    try:
        horario = horarios_model.get_id(id)
        if horario is not None:
            return jsonify(horario)
        else:
            return jsonify({'message': 'Horario not found'}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<seccion>')
def get_horarios_by_seccion(seccion):
    try:
        horarios= horarios_model.get_horarios_by_seccion(seccion)
        return jsonify(horarios)
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
    
@main.route('/add', methods=['POST'])
def add_horario():
    try:
        seccion = request.json['seccion']
        hora_inicio = request.json['hora_inicio']
        hora_fin = request.json['hora_fin']
        estado = request.json['estado']
        fecha_creacion = datetime.strptime(request.json['fecha_creacion'], "%d/%m/%Y").date()
        fecha_modificacion = datetime.strptime(request.json['fecha_modificacion'], "%d/%m/%Y").date()


        # No pasamos el ID porque la base lo genera
        horario = Horarios(
            seccion=seccion,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            estado=estado,
            fecha_creacion=fecha_creacion,
            fecha_modificacion=fecha_modificacion
        )

        new_id = horarios_model.add_horario(horario)

        if new_id:
            return jsonify({'id': new_id})
        else:
            return jsonify({'message': 'Failed to insert new Horario'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500



@main.route('/update/<int:id>', methods=['PUT'])
def update_horario(id):
    try:
        seccion = request.json['seccion']
        hora_inicio = request.json['hora_inicio']
        hora_fin = request.json['hora_fin']
        estado = request.json['estado']
        fecha_creacion = datetime.strptime(request.json['fecha_creacion'], "%d/%m/%Y").date()
        fecha_modificacion = datetime.strptime(request.json['fecha_modificacion'], "%d/%m/%Y").date()

        # Crear el objeto Horarios con los datos actualizados
        horario = Horarios(
            id=id,
            seccion=seccion,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            estado=estado,
            fecha_creacion=fecha_creacion,
            fecha_modificacion=fecha_modificacion
        )

        affected_rows = horarios_model.update_horario(horario)

        if affected_rows == 1:
            return jsonify(id)
        else:
            return jsonify({'message': 'Failed to update Horario'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500




@main.route('/delete/<int:id>', methods=['DELETE'])
def delete_horario(id):
    try:
        
        affected_rows = horarios_model.delete_horario(id)
        
        if affected_rows == 1:
            return jsonify(id)
        else:
            return jsonify({'message': 'Failed to delete Horario'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
