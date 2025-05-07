document.addEventListener('DOMContentLoaded', function() {
    // Валидация паролей при регистрации
    const password1 = document.getElementById('id_password1');
    const password2 = document.getElementById('id_password2');
    
    if (password1 && password2) {
        function validatePassword() {
            if (password1.value !== password2.value) {
                password2.setCustomValidity('Пароли не совпадают');
            } else {
                password2.setCustomValidity('');
            }
        }
        
        password1.onchange = validatePassword;
        password2.onkeyup = validatePassword;
    }
    
    // Маска для телефона
    const phoneField = document.getElementById('id_phone');
    if (phoneField) {
        phoneField.addEventListener('input', function(e) {
            let x = e.target.value.replace(/\D/g, '').match(/(\d{0,1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
            e.target.value = !x[2] ? x[1] : x[1] + ' (' + x[2] + ') ' + x[3] + '-' + x[4] + (x[5] ? '-' + x[5] : '');
        });
    }
});