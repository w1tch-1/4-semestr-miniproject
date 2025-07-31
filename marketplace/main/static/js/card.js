const rotateAmplitude = 15;
const scaleOnHover = 1.1;

document.querySelectorAll('.tilted-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -rotateAmplitude;
      const rotateY = ((x - centerX) / centerX) * rotateAmplitude;

      card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(${scaleOnHover})`;
});

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
  });
});