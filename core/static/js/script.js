
    let index = 0;
    const slides = document.querySelector(".slides");
    const totalSlides = slides.querySelectorAll("img").length;

    function showSlide() {
        slides.style.transform = `translateX(-${index * window.innerWidth}px)`;
    }

    function nextSlide() {
        index = (index + 1) % totalSlides;
        showSlide();
    }

    setInterval(nextSlide, 3000);
    window.addEventListener("resize", showSlide);

    const menuToggle = document.querySelector('.menu-toggle');
    menuToggle.addEventListener('click', toggleMenu);
    menuToggle.addEventListener('touchstart', toggleMenu);
    
    function toggleMenu() {
        const navbar = document.getElementById('navbar');
        navbar.classList.toggle('nav-visible');
        navbar.classList.toggle('nav-hidden');
    }

    // Ativando os ícones Lucide no carregamento
    document.addEventListener("DOMContentLoaded", function () {
    lucide.createIcons();
    });
