// alert("holaaaaa.")

document.addEventListener("DOMContentLoaded", function () {
    const maxStock = ( product.stok );
    let currentStock = maxStock;

    const decreaseButton = document.getElementById("decrease");
    const increaseButton = document.getElementById("increase");
    const stockDisplay = document.getElementById("current-stock");

    decreaseButton.addEventListener("click", function () {
        if (currentStock > 0) {
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
        decreaseButton.disabled = currentStock <= 0;
        increaseButton.disabled = currentStock >= maxStock;
    }

    updateButtons();  // Asegura que los botones estén correctamente deshabilitados al cargar la página
});
