$(document).ready(function() {
    // Mostrar formulario vacío para agregar un nuevo horario
    $('#mostrarFormBtn').click(function() {
        $('#horarioForm').show();
        $('#id').val('');
        $('#seccion').val('');
        $('#hora_inicio').val('');
        $('#hora_fin').val('');
        $('#estado').val('true'); // Opción por defecto seleccionada como "Activo"
        $('#fecha_creacion').val('');
        $('#fecha_modificacion').val('');
    });

    // Función para editar horario
    window.editarHorario = function(id) {
        $.ajax({
            url: `/api/horarios/${id}`,
            method: 'GET',
            success: function(data) {
                $('#horarioForm').show();
                $('#id').val(data.id);
                $('#seccion').val(data.seccion);
                $('#hora_inicio').val(data.hora_inicio);
                $('#hora_fin').val(data.hora_fin);
                $('#estado').val(data.estado === 't' ? 'true' : 'false');
                $('#fecha_creacion').val(data.fecha_creacion);
                $('#fecha_modificacion').val(data.fecha_modificacion);
            },
            error: function(error) {
                console.log('Error al obtener el horario:', error);
            }
        });
    };

    // Función para mostrar todos los horarios
    function mostrarHorarios() {
        $.ajax({
            url: '/api/horarios',
            method: 'GET',
            cache: false,
            success: function(data) {
                if (!Array.isArray(data)) {
                    console.error('Formato de datos incorrecto:', data);
                    return;
                }

                let horariosHtml = '';
                data.forEach(horario => {
                    const estadoTexto = horario.estado === 't' ? "Encendido" : "Apagado";
                    horariosHtml += `
                        <div class="card mb-2">
                            <div class="card-body">
                                <h5 class="card-title">Sección: ${horario.seccion}</h5>
                                <p class="card-text">Hora: ${horario.hora_inicio} - ${horario.hora_fin}</p>
                                <p class="card-text">Estado: ${estadoTexto}</p>
                                <button class="btn btn-warning" onclick="editarHorario(${horario.id})">Editar</button>
                                <button class="btn btn-danger" onclick="eliminarHorario(${horario.id})">Eliminar</button>
                            </div>
                        </div>
                    `;
                });

                $('#horariosList').html(horariosHtml);
            },
            error: function(error) {
                console.error('Error al obtener los horarios:', error);
                $('#horariosList').html('<div class="alert alert-danger">No se pudieron cargar los horarios.</div>');
            }
        });
    }

    // Filtro por sección
    $('#obtenerDatosBtn').click(function () {
        const filtro = $('#filtroSeccion').val();

        $.ajax({
            url: '/api/horarios',
            method: 'GET',
            success: function (data) {
                let horariosFiltrados = data;

                if (filtro !== 'todos') {
                    horariosFiltrados = data.filter(h => h.seccion === filtro);
                }

                let horariosHtml = '';
                horariosFiltrados.forEach(horario => {
                    const estadoTexto = horario.estado === 't' ? "Encendido" : "Apagado";

                    horariosHtml += `
                        <div class="card mb-2">
                            <div class="card-body">
                                <h5 class="card-title">${horario.seccion}</h5>
                                <p class="card-text">Hora: ${horario.hora_inicio} - ${horario.hora_fin}</p>
                                <p class="card-text">Estado: ${estadoTexto}</p>
                                <button class="btn btn-warning" onclick="editarHorario(${horario.id})">Editar</button>
                                <button class="btn btn-danger" onclick="eliminarHorario(${horario.id})">Eliminar</button>
                            </div>
                        </div>
                    `;
                });

                $('#horariosList').html(horariosHtml);
            },
            error: function (error) {
                console.log('Error al filtrar horarios:', error);
            }
        });
    });

    // Mostrar horarios al cargar la página
    mostrarHorarios();

    // Envío del formulario para agregar o editar horario
    $('#horarioForm').submit(function(e) {
        e.preventDefault();

        const id = $('#id').val();
        const seccion = $('#seccion').val();
        const hora_inicio = $('#hora_inicio').val();
        const hora_fin = $('#hora_fin').val();
        const estado = $('#estado').val() === 'true' ? 't' : 'f'; // Usar .val() por ser <select>
        const fecha_creacion = $('#fecha_creacion').val();
        const fecha_modificacion = $('#fecha_modificacion').val();

        const data = {
            seccion,
            hora_inicio,
            hora_fin,
            estado,
            fecha_creacion,
            fecha_modificacion
        };

        let esDuplicado = false;

        $.ajax({
            url: '/api/horarios',
            method: 'GET',
            async: false, // ⚠️ importante para esperar la respuesta antes de continuar
            success: function(horarios) {
                esDuplicado = horarios.some(h =>
                    h.seccion === seccion &&
                    h.hora_inicio === hora_inicio &&
                    h.hora_fin === hora_fin &&
                    h.id != id // permite editar sin bloquearse a sí mismo
                );
            }
        });

        if (esDuplicado) {
            console.log('Horario duplicado:');
            alert('Ya existe un horario con la misma sección, hora de inicio y hora de fin.');
            return; // ⛔ no se envía el formulario si es duplicado
        }

        let url = '/api/horarios/add';
        let method = 'POST';

        if (id) {
            url = `/api/horarios/update/${id}`;
            method = 'PUT';
           

        }
        

        $.ajax({
            url: url,
            method: method,
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function() {
                $('#horarioForm').hide();
                mostrarHorarios();
            },
            error: function(error) {
                console.log('Error al guardar el horario:', error);
                
            }
        });
        
    });
    // Eliminar horario
    window.eliminarHorario = function(id) {
        if(!confirm('¿Estas seguro de que deseas eliminar este horario?')) return;
        $.ajax({
            url: `/api/horarios/delete/${id}`,
            method: 'DELETE',
            success: function() {
                alert('Horario eliminado correctamente');
                mostrarHorarios();
            },
            error: function(error) {
                console.log('Error al eliminar el horario:', error);
                alert('Error al eliminar el horario');
            }
        });
    };
});
