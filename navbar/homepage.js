const navbar = document.querySelector('.navbar');
const revealItems = document.querySelectorAll('.reveal-up');
const projectSlides = document.querySelectorAll('.project-slide');
const projectPrev = document.getElementById('projectPrev');
const projectNext = document.getElementById('projectNext');
const aboutImage = document.querySelector('.about-image');
let currentSlide = 0;

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 30);

  if (aboutImage) {
    const rect = aboutImage.getBoundingClientRect();
    if (window.innerWidth > 992) {
      const offset = Math.min(20, Math.max(-20, (window.scrollY - rect.top) * 0.01));
      aboutImage.style.transform = `translateY(${offset}px) scale(1.06)`;
    } else {
      aboutImage.style.transform = 'translateY(0) scale(1.02)';
    }
  }
});

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.12 });

revealItems.forEach((item) => revealObserver.observe(item));

if (aboutImage) {
  aboutImage.style.transform = 'translateY(0) scale(1.04)';
}

function showSlide(index) {
  if (!projectSlides.length) return;
  currentSlide = (index + projectSlides.length) % projectSlides.length;
  projectSlides.forEach((slide, slideIndex) => {
    slide.classList.toggle('active', slideIndex === currentSlide);
  });
}

projectPrev?.addEventListener('click', () => showSlide(currentSlide - 1));
projectNext?.addEventListener('click', () => showSlide(currentSlide + 1));

showSlide(0);

const counters = document.querySelectorAll('.counter');
const statsObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;

    const counter = entry.target;
    const target = Number(counter.dataset.target || 0);
    const duration = 1600;
    const startTime = performance.now();

    const animate = (time) => {
      const progress = Math.min((time - startTime) / duration, 1);
      const value = Math.floor(progress * target);
      counter.textContent = value + (target === 98 ? '%' : '+');
      if (progress < 1) requestAnimationFrame(animate);
      else counter.textContent = target + (target === 98 ? '%' : '+');
    };

    requestAnimationFrame(animate);
    statsObserver.unobserve(counter);
  });
}, { threshold: 0.5 });

counters.forEach((counter) => statsObserver.observe(counter));

const servicesRevealItems = document.querySelectorAll('.cec-services-reveal');

if ('IntersectionObserver' in window && servicesRevealItems.length) {
  const servicesObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12 });

  servicesRevealItems.forEach((item, index) => {
    item.style.transitionDelay = `${Math.min(index, 6) * 80}ms`;
    servicesObserver.observe(item);
  });
} else {
  servicesRevealItems.forEach((item) => item.classList.add('is-visible'));
}

const projectsRevealItems = document.querySelectorAll('.cec-projects-reveal');

if ('IntersectionObserver' in window && projectsRevealItems.length) {
  const projectsObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12 });

  projectsRevealItems.forEach((item, index) => {
    item.style.transitionDelay = `${Math.min(index, 6) * 80}ms`;
    projectsObserver.observe(item);
  });
} else {
  projectsRevealItems.forEach((item) => item.classList.add('is-visible'));
}

const impactRevealItems = document.querySelectorAll('.cec-impact-reveal');

if ('IntersectionObserver' in window && impactRevealItems.length) {
  const impactObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.15 });

  impactRevealItems.forEach((item, index) => {
    item.style.transitionDelay = `${Math.min(index, 5) * 100}ms`;
    impactObserver.observe(item);
  });
} else {
  impactRevealItems.forEach((item) => item.classList.add('is-visible'));
}

const purposeRevealItems = document.querySelectorAll('.purpose-reveal');

if ('IntersectionObserver' in window && purposeRevealItems.length) {
  const purposeObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.15 });

  purposeRevealItems.forEach((item) => purposeObserver.observe(item));
} else {
  purposeRevealItems.forEach((item) => item.classList.add('is-visible'));
}

const expertiseRevealItems = document.querySelectorAll('.expertise-reveal');

if ('IntersectionObserver' in window && expertiseRevealItems.length) {
  const expertiseObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12 });

  expertiseRevealItems.forEach((item) => expertiseObserver.observe(item));
} else {
  expertiseRevealItems.forEach((item) => item.classList.add('is-visible'));
}

const milestoneRevealItems = document.querySelectorAll('.milestone-reveal');

if ('IntersectionObserver' in window && milestoneRevealItems.length) {
  const milestoneObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.2 });

  milestoneRevealItems.forEach((item) => milestoneObserver.observe(item));
} else {
  milestoneRevealItems.forEach((item) => item.classList.add('is-visible'));
}

const teamRevealItems = document.querySelectorAll('.team-reveal');

if ('IntersectionObserver' in window && teamRevealItems.length) {
  const teamObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12 });

  teamRevealItems.forEach((item) => teamObserver.observe(item));
} else {
  teamRevealItems.forEach((item) => item.classList.add('is-visible'));
}

const groupRevealItems = document.querySelectorAll('.group-reveal, .group-image-reveal');

if ('IntersectionObserver' in window && groupRevealItems.length) {
  const groupObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.15 });

  groupRevealItems.forEach((item) => groupObserver.observe(item));
} else {
  groupRevealItems.forEach((item) => item.classList.add('is-visible'));
}
