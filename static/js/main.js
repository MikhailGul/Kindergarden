// Основной JavaScript файл

document.addEventListener('DOMContentLoaded', function() {
  // Инициализация всплывающих подсказок
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
  });
  
  // Обработка галереи
  const galleryImages = document.querySelectorAll('.gallery-img');
  if (galleryImages.length > 0) {
      galleryImages.forEach(img => {
          img.addEventListener('click', function() {
              // Здесь можно добавить логику для модального окна с увеличенным изображением
              console.log('Изображение кликнуто:', this.src);
          });
      });
  }
  
  // Валидация форм
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
      form.addEventListener('submit', function(e) {
          const password1 = form.querySelector('#id_password1');
          const password2 = form.querySelector('#id_password2');
          
          if (password1 && password2 && password1.value !== password2.value) {
              e.preventDefault();
              alert('Пароли не совпадают!');
          }
      });
  });
});

