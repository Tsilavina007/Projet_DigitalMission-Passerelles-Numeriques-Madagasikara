document.addEventListener("DOMContentLoaded", function() {
    const menuItems = document.querySelectorAll(".dropdown-menu li a");

    menuItems.forEach(function(item) {
      item.addEventListener("click", function(event) {
        event.stopPropagation(); // Empêche la propagation du clic vers le parent
      });
    });
  });

