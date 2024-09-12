document.addEventListener('DOMContentLoaded', function() {
    var passwordInput = document.getElementById('password');
    var passwordConfirmInput = document.getElementById('password2');
    var form = document.getElementById('registrationForm');
    var errorMessage = document.getElementById('error-message');

    form.onsubmit = function(event) {
        // 重置错误信息
        errorMessage.style.display = 'none';

        // 检查密码是否一致
        if (passwordInput.value !== passwordConfirmInput.value) {
            event.preventDefault(); // 阻止表单提交
            errorMessage.style.display = 'block'; // 显示错误信息
        }
    };
});