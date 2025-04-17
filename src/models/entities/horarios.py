from utils.DateFormat import DateFormat

class Horarios():

    def __init__(self, id=None, seccion=None, hora_inicio=None, hora_fin=None, estado=None, fecha_creacion=None, fecha_modificacion=None) -> None:
        self.id = id
        self.seccion = seccion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion

    def to_JSON(self):
        return {
            'id': self.id,
            'seccion': self.seccion,
            'hora_inicio': self.hora_inicio.strftime('%H:%M:%S') if self.hora_inicio else None,
            'hora_fin': self.hora_fin.strftime('%H:%M:%S') if self.hora_fin else None,
            'estado': self.estado,
            'fecha_creacion': DateFormat.convert_date(self.fecha_creacion),
            'fecha_modificacion': DateFormat.convert_date(self.fecha_modificacion)
        }
