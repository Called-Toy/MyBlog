function toggleBlock() {
        const newBlock = document.getElementById('newBlock');
        if (newBlock.style.display === 'none' || newBlock.style.display === '') {
            newBlock.style.display = 'block';
        } else {
            newBlock.style.display = 'none';
        }
    }

    var passwordInput = document.getElementById('password');
        var passwordConfirmInput = document.getElementById('password2');
        var form = document.getElementById('passwordForm');
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

