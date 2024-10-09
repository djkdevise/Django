$(document).ready(function () {
    $('#task-form').on('submit', function (event) {
        event.preventDefault(); // Previene el envío del formulario

        const taskText = $('#task_input').val().trim();
        const taskIcon = document.getElementById('task_icon').value; // Toma la clase de icono seleccionada

        // Validar si se ingresó una tarea
        if (!taskText) {
            alert('Por favor, ingresa una tarea.');
            return;
        }

        // Validar tareas duplicadas
        let duplicate = false;
        $('#task-pending li').each(function () {
            if ($(this).text().includes(taskText)) {
                duplicate = true;
                return false; // Salir del each
            }
        });

        if (duplicate) {
            alert('La tarea ya existe en la lista.');
            return;
        }

        // Crear un nuevo elemento de tarea
        let taskItem = `
        <li class="list-group-item d-flex justify-content-between align-items-center">
            <div class="d-flex align-items-center"> <!-- Contenedor flex para alinear icono y texto -->
                <span class="fa-3x me-2"> <!-- Espaciado a la derecha del icono -->
                    <i class="fas ${taskIcon}"></i>
                </span>
                <span>${taskText}</span> <!-- Texto alineado a la izquierda -->
            </div>
            <div>
                <button class="btn btn-sm btn-success task-schedule">Agendar</button>
                <button class="btn btn-sm btn-danger task-delete">Eliminar</button>
            </div>
        </li>`;


        // Agregar la tarea a la lista de pendientes
        $('#task-pending').append(taskItem);
        $('#task_input').val(''); // Limpiar el input después de agregar la tarea
    });

    // Manejar el evento de "Agendar"
    $(document).on('click', '.task-schedule', function () {
        const taskElement = $(this).closest('li');
        const taskText = taskElement.find('span').text();
        
        // Mover la tarea a la sección de "Hoy"
        $('#task-today').append(taskElement);
        $(this).text('Terminada').removeClass('task-schedule').addClass('task-complete'); // Cambiar texto y clase
    });

    // Manejar el evento de "Eliminar"
    $(document).on('click', '.task-delete', function () {
        $(this).closest('li').remove(); // Eliminar la tarea
    });

    // Manejar el evento de "Terminada"
    $(document).on('click', '.task-complete', function () {
        const taskElement = $(this).closest('li');
        
        // Mover la tarea a la sección de "Completadas"
        $('#task-completed').append(taskElement);
        $(this).remove(); // Eliminar el botón de "Terminada"
    });

    // Manejar el evento de "Realizada" en el botón dentro de las tarjetas
    $(document).on('click', '.task-complete-btn', function () {
        // Obtener el elemento de la tarjeta
        const cardElement = $(this).closest('.card-body');
        
        // Obtener el nombre de la tarea y el icono
        const taskName = cardElement.find('h5.card-title').text();
        const taskIconClass = cardElement.find('i').attr('class'); // Obtener la clase del icono
        
        // Crear un nuevo elemento para la tarea completada
        const completedItem = `
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <span><i class="${taskIconClass}"></i> ${taskName}</span>
                <div>
                <button class="btn btn-sm btn-danger task-delete">Eliminar</button>
                </div>
            </li>`;

        // Agregar la tarea a la lista de completadas
        $('#task-completed').append(completedItem);
        
        // Opcional: puedes ocultar o deshabilitar el botón después de marcarlo como realizado
        // $(this).prop('disabled', true).text('Completada').removeClass('btn-success').addClass('btn-secondary');
    });
});
