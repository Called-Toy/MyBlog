function toggleBlock() {
        const newBlock = document.getElementById('newBlock');
        if (newBlock.style.display === 'none' || newBlock.style.display === '') {
            newBlock.style.display = 'block';
        } else {
            newBlock.style.display = 'none';
        }
    }
