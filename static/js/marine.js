document.addEventListener('DOMContentLoaded', () => {
  const CEC_STATIC_IMAGES = (document.body && document.body.dataset.staticImages) || '';
  const resolveCecImage = (src) => src.startsWith('../images/') ? CEC_STATIC_IMAGES + src.slice('../images/'.length) : src;
  const cecSlugForFile = (file) => (
    { 'civil&engineering.html': 'civil-structural', 'building.html': 'building', 'powertransmission.html': 'power-transmission', 'MPEP.html': 'mep', 'water.html': 'water', 'marine.html': 'marine' }[file] || 'marine'
  );
  // One circular service sequence shared by every service detail page.
  const services = [
    { file: 'civil&engineering.html', name: 'Civil & Structural Engineering', image: '../images/cec-about-reference.png' },
    { file: 'building.html', name: 'Building & Infrastructure Development', image: 'https://static.wixstatic.com/media/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg/v1/fill/w_1200,h_650,al_c,q_90,enc_avif,quality_auto/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg' },
    { file: 'powertransmission.html', name: 'Power Transmission & Distribution', image: '../images/B58A4353.jpg' },
    { file: 'MPEP.html', name: 'Electromechanical / MEP Engineering', image: '../images/B58A4353.jpg' },
    { file: 'water.html', name: 'Water Supply & Sanitation', image: '../images/keya-hpp.jpg' },
    { file: 'marine.html', name: 'Marine & Civil Works', image: '../images/rubavu port.jpg' }
  ];
  const currentFile = (document.body && document.body.dataset.serviceFile) || decodeURIComponent(window.location.pathname.split('/').pop());
  const currentService = services.findIndex((service) => service.file === currentFile);
  const footer = document.querySelector('.cec-footer');

  if (currentService !== -1 && footer) {
    const navigation = document.createElement('nav');
    navigation.className = 'service-navigation';
    navigation.setAttribute('aria-label', 'Previous and next services');
    const container = document.createElement('div');
    container.className = 'container service-navigation-inner';

    [-1, 1].forEach((offset) => {
      const service = services[(currentService + offset + services.length) % services.length];
      const direction = offset === -1 ? 'previous' : 'next';
      const link = document.createElement('a');
      link.className = `service-navigation-link service-navigation-${direction}`;
      link.href = `/services/${cecSlugForFile(service.file)}/`;
      const thumbnail = document.createElement('span');
      thumbnail.className = 'service-navigation-thumbnail';
      const image = document.createElement('img');
      image.src = resolveCecImage(service.image);
      image.alt = '';
      image.width = 90;
      image.height = 90;
      image.loading = 'lazy';
      thumbnail.append(image);
      const copy = document.createElement('span');
      copy.className = 'service-navigation-copy';
      const label = document.createElement('span');
      label.className = 'service-navigation-label';
      label.textContent = direction.toUpperCase();
      const title = document.createElement('span');
      title.className = 'service-navigation-title';
      title.textContent = service.name;
      copy.append(label, title);
      link.append(...(offset === -1 ? [thumbnail, copy] : [copy, thumbnail]));
      container.append(link);
    });

    navigation.append(container);
    footer.before(navigation);
  }

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
