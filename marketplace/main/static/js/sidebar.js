document.body.addEventListener("input", (e) => {
    if (e.target.id === "priceRange") {
        document.getElementById("priceValue").textContent = e.target.value;
    }
});
