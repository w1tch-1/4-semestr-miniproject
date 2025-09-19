const sidebar = document.getElementById("filterSidebar");
const toggleBtn = document.getElementById("toggleSidebar");

toggleBtn.addEventListener("click", () => {
if (window.innerWidth > 991) {
  // Desktop → push effect
  sidebar.classList.toggle("closed");
} else {
  // Mobile → overlay effect
  sidebar.classList.toggle("show");
}
});

const priceRange = document.getElementById('priceRange');
const priceValue = document.getElementById('priceValue');

priceRange.addEventListener('input', () => {
    priceValue.textContent = priceRange.value;
});
