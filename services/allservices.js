const serviceRevealItems = document.querySelectorAll('[data-service-reveal]');

if ('IntersectionObserver' in window && serviceRevealItems.length) {
  const serviceObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12 });

  serviceRevealItems.forEach((item) => serviceObserver.observe(item));
} else {
  serviceRevealItems.forEach((item) => item.classList.add('is-visible'));
}
