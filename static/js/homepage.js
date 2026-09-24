// Shared Projects navigation, also loaded on pages without homepage effects.
(() => {
  document.querySelectorAll('.cec-projects-nav').forEach((item) => {
    if (item.dataset.initialized) return;
    item.dataset.initialized = 'true';
    const toggle = item.querySelector('.cec-projects-toggle');
    const menu = item.querySelector('.cec-projects-menu');
    const desktop = window.matchMedia('(min-width: 992px)');
    const setOpen = (open) => {
      menu.hidden = !open;
      item.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
    };
    item.addEventListener('pointerenter', (event) => {
      if (desktop.matches && event.pointerType === 'mouse') setOpen(true);
    });
    item.addEventListener('pointerleave', () => {
      if (desktop.matches && !item.contains(document.activeElement)) setOpen(false);
    });
    item.addEventListener('focusin', (event) => {
      if (desktop.matches && event.target !== toggle) setOpen(true);
    });
    item.addEventListener('focusout', (event) => {
      if (!item.contains(event.relatedTarget)) setOpen(false);
    });
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    item.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        event.preventDefault();
        event.stopPropagation();
        toggle.focus();
        setOpen(false);
      } else if (event.key === 'ArrowDown' && !menu.contains(event.target)) {
        event.preventDefault();
        setOpen(true);
        menu.querySelector('a').focus();
      }
    });
    document.addEventListener('click', (event) => {
      if (!item.contains(event.target)) setOpen(false);
    });
    item.closest('.offcanvas')?.addEventListener('hidden.bs.offcanvas', () => setOpen(false));
    desktop.addEventListener('change', () => setOpen(false));
    const updateActive = () => {
      const current = new URL(window.location.href);
      const selected = current.searchParams.get('category') || 'all';
      menu.querySelectorAll('a').forEach((link) => {
        const destination = new URL(link.href, current);
        const active = destination.pathname === current.pathname && link.dataset.projectCategory === selected;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'page');
        else link.removeAttribute('aria-current');
      });
    };
    window.addEventListener('cec:project-filter', updateActive);
    window.addEventListener('popstate', updateActive);
    updateActive();
  });
})();

(() => {
if (document.currentScript?.hasAttribute('data-navbar-only')) return;
const navbar = document.querySelector('.navbar');
const revealItems = document.querySelectorAll('.reveal-up');
const projectSlides = document.querySelectorAll('.project-slide');
const projectPrev = document.getElementById('projectPrev');
const projectNext = document.getElementById('projectNext');
const aboutImage = document.querySelector('.about-image');
let currentSlide = 0;

let scrollFramePending = false;

function updateScrollEffects() {
  scrollFramePending = false;
  navbar?.classList.toggle('scrolled', window.scrollY > 30);
  if (aboutImage && window.innerWidth > 992 && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const rect = aboutImage.getBoundingClientRect();
    const offset = Math.min(20, Math.max(-20, (window.innerHeight / 2 - rect.top) * 0.025));
    aboutImage.style.transform = `translate3d(0, ${offset}px, 0) scale(1.06)`;
  }
}

window.addEventListener('scroll', () => {
  if (!scrollFramePending) {
    scrollFramePending = true;
    requestAnimationFrame(updateScrollEffects);
  }
}, { passive: true });
window.addEventListener('resize', updateScrollEffects, { passive: true });
updateScrollEffects();

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
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

// Start when the hero is visible; unrelated maps and images must not delay playback.
const heroVideo = document.querySelector('.hero-video');
const connection = navigator.connection;
const canLoadHeroVideo = heroVideo && !connection?.saveData
  && !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (canLoadHeroVideo) {
  let heroVisible = false;
  let pageReady = false;
  const updateHeroPlayback = () => {
    if (heroVideo.tagName === 'IFRAME') {
      if (!pageReady || !heroVisible || document.hidden) {
        if (heroVideo.hasAttribute('src')) heroVideo.removeAttribute('src');
      } else if (!heroVideo.hasAttribute('src')) {
        heroVideo.src = heroVideo.dataset.src;
      }
      return;
    }
    if (!pageReady || !heroVisible || document.hidden) {
      heroVideo.pause();
      return;
    }
    const source = heroVideo.querySelector('source[data-src]');
    if (source) {
      source.src = source.dataset.src;
      source.removeAttribute('data-src');
      heroVideo.load();
    }
    heroVideo.play().catch(() => {});
  };
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(([entry]) => {
      heroVisible = entry.isIntersecting;
      updateHeroPlayback();
    }).observe(heroVideo.closest('.hero-section') || heroVideo);
  } else {
    heroVisible = true;
  }
  document.addEventListener('visibilitychange', updateHeroPlayback);
  const scheduleVideo = () => {
    const ready = () => {
      pageReady = true;
      updateHeroPlayback();
    };
    if ('requestIdleCallback' in window) requestIdleCallback(ready, { timeout: 1500 });
    else setTimeout(ready, 400);
  };
  scheduleVideo();
}

})();
