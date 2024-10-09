// Selecciona las imágenes y los inputs de tipo radio
const images = document.querySelectorAll('li img');
const radios = document.querySelectorAll('input[type="radio"]');
const form = document.querySelector('form');
const messageDiv = document.getElementById('message');

// Agrega un evento click a cada imagen para seleccionar la correspondiente opción de radio
images.forEach((image, index) => {
  image.addEventListener('click', () => {
    // Quita la clase 'selected' de todas las imágenes
    images.forEach(img => img.parentElement.classList.remove('selected'));

    // Añade la clase 'selected' a la imagen seleccionada
    image.parentElement.classList.add('selected');

    // Marca el input radio correspondiente
    radios[index].checked = true;
  });
});

// Evento para enviar el formulario
form.addEventListener('submit', function(event) {
  // Verifica si hay una opción seleccionada
  const selectedValue = document.querySelector('input[type="radio"]:checked');
  
  if (!selectedValue) {
    event.preventDefault();  // Previene el envío si no hay selección
    showMessage('Por favor selecciona una imagen.', 'error');
  } else {
    // El formulario se enviará y Django hará la validación en el servidor
  }
});

// Función para mostrar mensajes de éxito o error
function showMessage(message, type) {
  messageDiv.textContent = message;
  messageDiv.className = '';  // Resetea las clases
  messageDiv.classList.add(type);  // Añade la clase de éxito o error
  messageDiv.style.display = 'block';  // Muestra el mensaje
}
