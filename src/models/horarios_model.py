from database.db import get_connection
from .entities.horarios import Horarios


class horarios_model():

    # Metodos GET

    @classmethod
    def get_horarios(self):
        try:

            connection = get_connection()
            horarios = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, seccion, hora_inicio, hora_fin, estado, fecha_creacion, fecha_modificacion FROM horario_v2")
                resultset = cursor.fetchall()

                for row in resultset:
                    horario = Horarios(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    horarios.append(horario.to_JSON())

            connection.close()
            return horarios

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_id(self, id):
        try:

            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, seccion, hora_inicio, hora_fin, estado, fecha_creacion, fecha_modificacion FROM horario_v2 WHERE id = %s", (id,))
                row = cursor.fetchone()

                horario = None
                if row is not None:
                    horario = Horarios(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    horario = horario.to_JSON()
                    
            connection.close()
            return horario

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_horarios_by_seccion(self, seccion):
        try:

            connection = get_connection()
            horarios = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, seccion, hora_inicio, hora_fin, estado, fecha_creacion, fecha_modificacion FROM horario_v2 WHERE seccion = %s", (seccion,))
                resultset = cursor.fetchall()

                for row in resultset:
                    horario = Horarios(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    horarios.append(horario.to_JSON())

            connection.close()
            return horarios

        except Exception as ex:
            raise Exception(ex)


    # Metodos POST

    @classmethod
    def add_horario(self, horario):
        try:

            connection = get_connection()


            with connection.cursor() as cursor:
                #Validar duplicado exacto de seccion, hora_inicio y hora_fin
                cursor.execute("""
                    SELECT COUNT(*) FROM horario_v2 
                    WHERE seccion = %s AND hora_inicio = %s AND hora_fin = %s
                """, (horario.seccion, horario.hora_inicio, horario.hora_fin))

                count = cursor.fetchone()[0]
                if count > 0:
                    raise Exception("Ya existe un horario con la misma seccion, hora_inicio y hora_fin")

                # Si no existe, insertamos el nuevo horario
                cursor.execute("""
                    INSERT INTO horario_v2 (seccion, hora_inicio, hora_fin, estado, fecha_creacion, fecha_modificacion)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING id
                """, (horario.seccion, horario.hora_inicio, horario.hora_fin, horario.estado, horario.fecha_creacion, horario.fecha_modificacion))

                new_id = cursor.fetchone()[0]
                connection.commit()
                return new_id
                                
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def update_horario(self, horario):
        try:

            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE horario_v2
                    SET seccion = %s, hora_inicio = %s, hora_fin = %s, estado = %s, fecha_modificacion = %s
                    WHERE id = %s
                """, (horario.seccion, horario.hora_inicio, horario.hora_fin, horario.estado, horario.fecha_modificacion, horario.id))

                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)


        
    @classmethod
    def delete_horario(self, id):
        try:

            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM horario_v2 WHERE id = %s", (id,))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
