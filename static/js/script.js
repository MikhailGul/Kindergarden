// Хранилище пользователей (в реальном приложении - база данных)
let users = JSON.parse(localStorage.getItem('users')) || [];

// Toast-уведомления
function showToast(message, isSuccess = true) {
  const toast = document.createElement('div');
  toast.className = `toast show ${isSuccess ? 'bg-success' : 'bg-danger'}`;
  toast.innerHTML = `
    <div class="toast-body text-white">
      ${message}
      <button class="btn-close btn-close-white float-end" data-bs-dismiss="toast"></button>
    </div>
  `;
  document.querySelector('.toast-container').appendChild(toast);
  setTimeout(() => toast.remove(), 3000);
}

// Регистрация
document.getElementById('registrationForm')?.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  // Визуальная валидация
  if (!name || !email || !password) {
    showToast('Заполните все поля!', false);
    return;
  }

  // Проверка, есть ли пользователь
  const userExists = users.some(user => user.email === email);
  if (userExists) {
    showToast('Пользователь уже существует!', false);
    return;
  }

  // "Регистрация" (сохранение в localStorage)
  users.push({ name, email, password });
  localStorage.setItem('users', JSON.stringify(users));
  showToast('Регистрация прошла успешно!');
  setTimeout(() => window.location.href = 'login.html', 1500);
});

// Вход
document.getElementById('loginForm')?.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  // Поиск пользователя
  const user = users.find(user => user.email === email && user.password === password);
  if (user) {
    showToast('Вход выполнен!');
    localStorage.setItem('currentUser', JSON.stringify(user));
    setTimeout(() => window.location.href = 'dashboard.html', 1500);
  } else {
    showToast('Неверный email или пароль!', false);
  }
});

// Выход
document.getElementById('logoutBtn')?.addEventListener('click', () => {
  localStorage.removeItem('currentUser');
  showToast('Вы вышли из системы.');
  setTimeout(() => window.location.href = 'login.html', 1000);
});
// Общие функции
function showToast(message, isSuccess = true) {
    const toast = document.createElement('div');
    toast.className = `toast show align-items-center ${isSuccess ? 'bg-success' : 'bg-danger'}`;
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    document.querySelector('.toast-container').appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

// Валидация формы регистрации
document.getElementById("registrationForm")?.addEventListener("submit", function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    // Валидация
    if (!formData.get('name') || !formData.get('email') || !formData.get('password')) {
        showToast("Заполните все поля", false);
        return;
    }

    if (formData.get('password') !== formData.get('confirmPassword')) {
        showToast("Пароли не совпадают", false);
        return;
    }

    // Сохранение пользователя и перенаправление
    localStorage.setItem('currentUser', JSON.stringify({
        name: formData.get('name'),
        email: formData.get('email')
    }));
    showToast("Регистрация успешна!");
    setTimeout(() => window.location.href = "dashboard.html", 1500);
});

// Валидация формы входа
document.getElementById("loginForm")?.addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);

    if (!formData.get('email') || !formData.get('password')) {
        showToast("Заполните все поля", false);
        return;
    }

    // Моковая проверка (в реальном приложении - запрос к серверу)
    const user = JSON.parse(localStorage.getItem('currentUser'));
    if (user && user.email === formData.get('email')) {
        showToast("Вход выполнен!");
        setTimeout(() => window.location.href = "dashboard.html", 1500);
    } else {
        showToast("Неверные данные", false);
    }
});

// Проверка авторизации для dashboard
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.includes('dashboard.html')) {
        const user = JSON.parse(localStorage.getItem('currentUser'));
        if (!user) {
            window.location.href = "login.html";
        } else {
            document.getElementById('userName').textContent = user.name;
        }
    }

    // Инициализация toast-контейнера
    if (!document.querySelector('.toast-container')) {
        const container = document.createElement('div');
        container.className = 'toast-container';
        document.body.appendChild(container);
    }
});
// Выход (общий для всех страниц)
function setupLogoutButtons() {
    document.querySelectorAll('.logout-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        localStorage.removeItem('currentUser');
        showToast('Вы вышли из системы.');
        setTimeout(() => window.location.href = 'index.html', 1000);
      });
    });
  }
  
  // Вызов при загрузке
  document.addEventListener('DOMContentLoaded', setupLogoutButtons);
  
  document.addEventListener('DOMContentLoaded', function() {
    // Toast-уведомления
    const toastEl = document.querySelector('.toast');
    if (toastEl) {
        const toast = new bootstrap.Toast(toastEl);
        toast.show();
    }

    // Валидация форм
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
});