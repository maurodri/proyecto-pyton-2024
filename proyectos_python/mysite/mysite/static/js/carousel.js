
var scrollToTopIcon = document.getElementById('scroll-to-top');

// Función para desplazarse rápidamente hacia arriba
function scrollToTop() {
    var scrollInterval = setInterval(function(){
        if ( window.scrollY != 0 ) {
            window.scrollBy( 0, -55 );
        }
        else clearInterval(scrollInterval); 
    },0.15);
}

// Ocultar el icono cuando se llega a la parte superior de la página
window.addEventListener('scroll', function() {
    if (window.pageYOffset === 0) {
        scrollToTopIcon.style.display = 'none';
    } else {
        scrollToTopIcon.style.display = 'block';
    }
});

// Desplazarse hacia arriba cuando se hace clic en el icono
scrollToTopIcon.addEventListener('click', function() {
    window.scrollTo(0, 0);
});