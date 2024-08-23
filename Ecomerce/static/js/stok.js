document.addEventListener("DOMContentLoaded", function () {
    const maxStock = parseInt(document.getElementById("max-stock").value, 10); // Límite máximo desde el campo oculto
    let currentStock = 1; // Comienza en 1

    const decreaseButton = document.getElementById("decrease");
    const increaseButton = document.getElementById("increase");
    const stockDisplay = document.getElementById("current-stock");

    decreaseButton.addEventListener("click", function () {
        if (currentStock > 1) { // No bajar de 1
            currentStock--;
            stockDisplay.textContent = currentStock;
            updateButtons();
        }
    });

    increaseButton.addEventListener("click", function () {
        if (currentStock < maxStock) {
            currentStock++;
            stockDisplay.textContent = currentStock;
            updateButtons();
        }
    });

    function updateButtons() {
        decreaseButton.disabled = currentStock <= 1; // Deshabilitar si es 1
        increaseButton.disabled = currentStock >= maxStock;
    }

    updateButtons();  // Asegura que los botones estén correctamente deshabilitados al cargar la página
});
