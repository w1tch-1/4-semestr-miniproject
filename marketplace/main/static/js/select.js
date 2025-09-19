const categorySelect = document.getElementById("id_category");
const subCategorySelect = document.getElementById("id_sub_category");
const typesSelect = document.getElementById("id_types");

categorySelect.addEventListener("change", function() {
    const categoryId = this.value;
    fetch(`/ajax/load-subcategories/?category=${categoryId}`)
        .then(response => response.json())
        .then(data => {
            subCategorySelect.innerHTML = '<option value="">---------</option>';
            typesSelect.innerHTML = '<option value="">---------</option>';
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.id;
                option.textContent = item.name;
                subCategorySelect.appendChild(option);
            });
        });
});

subCategorySelect.addEventListener("change", function() {
    const subCategoryId = this.value;
    fetch(`/ajax/load-types/?sub_category=${subCategoryId}`)
        .then(response => response.json())
        .then(data => {
            typesSelect.innerHTML = '<option value="">---------</option>';
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item.id;
                option.textContent = item.name;
                typesSelect.appendChild(option);
            });
        });
});