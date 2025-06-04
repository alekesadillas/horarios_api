from flask import Blueprint, jsonify, request
from datetime import datetime
from services.arduino_cloud_service import actualizar_status_en_arduino_cloud
import requests

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
        fecha_creacion = datetime.strptime(request.json['fecha_creacion'], "%Y-%m-%d").date()
        fecha_modificacion = datetime.strptime(request.json['fecha_modificacion'], "%Y-%m-%d").date()


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

            actualizar_status_en_arduino_cloud(estado)

            return jsonify({'id': new_id})
            # Después de insertar en la base de datos

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

        # Convertir 't'/'f' a un booleano
        estado_raw = request.json['estado']
        estado = 't' if estado_raw == 't' or estado_raw is True else 'f'

        # Cambiar el formato de fecha a '%Y-%m-%d'
        fecha_creacion = datetime.strptime(request.json['fecha_creacion'], "%Y-%m-%d").date()
        fecha_modificacion = datetime.strptime(request.json['fecha_modificacion'], "%Y-%m-%d").date()

        # Crear el objeto Horarios
        horario = Horarios(
            id=id,
            seccion=seccion,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            estado=estado,
            fecha_creacion=fecha_creacion,
            fecha_modificacion=fecha_modificacion
        )

        # Actualizar en la base de datos
        affected_rows = horarios_model.update_horario(horario)

        if affected_rows == 1:
            actualizar_status_en_arduino_cloud(estado)
            return jsonify(id)
        else:
            return jsonify({'message': 'Failed to update Horario'}), 404

    except Exception as ex:
        # Imprimir el error completo en los logs
        print(f"Error al actualizar el horario: {str(ex)}")
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