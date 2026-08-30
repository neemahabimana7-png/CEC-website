document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-slider]').forEach((slider, sliderIndex) => {
    const slides = [...slider.querySelectorAll('.project-slides img')];
    let current = 0;
    let timer;

    const showSlide = (index) => {
      current = (index + slides.length) % slides.length;
      slides.forEach((slide, slideIndex) => slide.classList.toggle('is-active', slideIndex === current));
    };

    const startSlider = () => {
      window.clearInterval(timer);
      timer = window.setInterval(() => showSlide(current + 1), 3000 + (sliderIndex * 300));
    };

    startSlider();
  });

  const items = document.querySelectorAll('.marine-service .reveal-item');

  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    items.forEach((item) => item.classList.add('is-visible'));
    return;
  }

  document.querySelectorAll('.marine-intro .reveal-item').forEach((item, index) => {
    item.style.transitionDelay = `${index * 80}ms`;
  });

  document.querySelectorAll('.capability-wrap.reveal-item').forEach((item, index) => {
    item.style.transitionDelay = `${index * 55}ms`;
  });

  document.querySelectorAll('.project-photo.reveal-item').forEach((item, index) => {
    item.style.transitionDelay = `${120 + (index * 100)}ms`;
  });

  const observer = new IntersectionObserver((entries, currentObserver) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      currentObserver.unobserve(entry.target);
    });
  }, { threshold: 0.12 });

  items.forEach((item) => observer.observe(item));
});
