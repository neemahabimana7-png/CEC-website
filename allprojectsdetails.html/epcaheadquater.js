const revealItems = document.querySelectorAll('.reveal');

if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  revealItems.forEach((item) => item.classList.add('is-visible'));
} else {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12 });

  revealItems.forEach((item, index) => {
    item.style.transitionDelay = `${Math.min(index % 6, 5) * 70}ms`;
    observer.observe(item);
  });
}
const galleryLightbox = document.querySelector('.gallery-lightbox');
const galleryLightboxImage = galleryLightbox?.querySelector('img');
const galleryLightboxClose = galleryLightbox?.querySelector('.gallery-lightbox-close');
const galleryImages = document.querySelectorAll('.gallery-track img');

function openGalleryImage(image) {
  if (!galleryLightbox || !galleryLightboxImage) return;
  galleryLightboxImage.src = image.currentSrc || image.src;
  galleryLightboxImage.alt = image.alt || 'EPCA Group Headquarters project image';
  galleryLightbox.hidden = false;
  document.body.classList.add('lightbox-open');
  galleryLightboxClose?.focus();
}

function closeGalleryImage() {
  if (!galleryLightbox || !galleryLightboxImage) return;
  galleryLightbox.hidden = true;
  galleryLightboxImage.src = '';
  document.body.classList.remove('lightbox-open');
}

galleryImages.forEach((image) => {
  image.addEventListener('click', () => openGalleryImage(image));
  image.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      openGalleryImage(image);
    }
  });
});

galleryLightboxClose?.addEventListener('click', closeGalleryImage);
galleryLightbox?.addEventListener('click', (event) => {
  if (event.target === galleryLightbox) closeGalleryImage();
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && galleryLightbox && !galleryLightbox.hidden) closeGalleryImage();
});
