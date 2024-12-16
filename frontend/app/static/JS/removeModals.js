document.querySelectorAll('.alert').forEach((alert) => {
    setTimeout(() => {
        alert.classList.remove('show');
        alert.classList.add('fade');
        setTimeout(() => alert.remove(), 500);
    }, 3000);
});