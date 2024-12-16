document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('.header a');
    const currentUrl = window.location.pathname + window.location.hash;

    links.forEach(link => {
           if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });
});
