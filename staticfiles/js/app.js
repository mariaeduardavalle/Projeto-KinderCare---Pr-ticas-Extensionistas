document.addEventListener('DOMContentLoaded', function () {

    // Auto-hide alerts after 3.5s
    document.querySelectorAll('.alert').forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = 'opacity .4s';
            alert.style.opacity = '0';
        }, 3500);
    });

    // Sidebar active link — longest-match wins para evitar falsos positivos
    // ex: /agenda/ e /agenda/atendimentos/ não ficam ambos ativos
    var currentPath = window.location.pathname;
    var bestMatch = null;
    var bestLength = 0;

    document.querySelectorAll('.sidebar a').forEach(function (link) {
        try {
            var linkPath = new URL(link.href).pathname;
            var isMatch = linkPath === '/'
                ? currentPath === '/'
                : currentPath === linkPath || currentPath.startsWith(linkPath + '/');
            if (isMatch && linkPath.length > bestLength) {
                bestMatch = link;
                bestLength = linkPath.length;
            }
        } catch (e) {}
    });

    if (bestMatch) bestMatch.classList.add('active');

});
