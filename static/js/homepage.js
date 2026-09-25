// One photo layer per banner, retaining the original responsive crop.
(() => {
  const heroes = [...document.querySelectorAll('.about-hero, .services-hero, .projects-hero, .careers-hero, .news-hero, .project-section-banner')]
    .filter(hero => !hero.dataset.scrollPhotoReady);
  if (!heroes.length) return;
  document.body.style.overflowX = 'clip';
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const entries = heroes.map(hero => {
    hero.dataset.scrollPhotoReady = 'true';
    const source = hero.querySelector(':scope > .projects-hero-image, :scope > img');
    const originalBackground = hero.style.backgroundImage;
    const track = document.createElement('div');
    const photo = document.createElement('div');
    track.setAttribute('aria-hidden', 'true');
    track.style.cssText = 'position:absolute;inset:0 0 -100%;pointer-events:none;';
    photo.style.cssText = 'position:sticky;top:0;width:100%;background-repeat:no-repeat;';
    track.append(photo);
    hero.prepend(track);
    hero.style.position = 'relative';
    hero.style.overflow = 'clip';
    const content = hero.querySelector(':scope > .container');
    if (content) { content.style.position = 'relative'; content.style.zIndex = '1'; }
    return {hero, source, photo, originalBackground};
  });
  const sync = () => entries.forEach(({hero, source, photo, originalBackground}) => {
    // Read the original stylesheet at this breakpoint before hiding its duplicate paint.
    if (!source) hero.style.backgroundImage = originalBackground;
    const style = getComputedStyle(source || hero);
    if (source?.tagName === 'IMG') {
      photo.style.backgroundImage = 'url(' + JSON.stringify(source.currentSrc || source.src) + ')';
      photo.style.backgroundSize = style.objectFit;
      photo.style.backgroundPosition = style.objectPosition;
    } else {
      for (const key of ['backgroundImage', 'backgroundPosition', 'backgroundSize', 'backgroundRepeat', 'backgroundOrigin', 'backgroundClip', 'backgroundColor']) photo.style[key] = style[key];
    }
    photo.style.height = hero.clientHeight + 'px';
    photo.style.transform = source ? style.transform : 'none';
    photo.style.position = reduced.matches ? 'relative' : 'sticky';
    if (source) source.style.visibility = 'hidden';
    else hero.style.backgroundImage = 'none';
  });
  sync();
  const observer = new ResizeObserver(sync);
  entries.forEach(({hero, source}) => { observer.observe(hero); source?.addEventListener('load', sync); });
  window.addEventListener('load', sync, {once:true});
  reduced.addEventListener('change', sync);
})();

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
if (heroVideo) {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const connection = navigator.connection;
  const bounds = (heroVideo.closest('.hero-section') || heroVideo).getBoundingClientRect();
  let heroVisible = bounds.bottom > 0 && bounds.top < window.innerHeight;
  heroVideo.muted = true;
  const updateHeroPlayback = () => {
    if (!heroVisible || document.hidden || connection?.saveData || reducedMotion.matches) {
      heroVideo.pause();
      return;
    }
    // Start as soon as media is available; never wait for window load or idle time.
    const source = heroVideo.querySelector('source[data-src]');
    if (source) {
      source.src = source.dataset.src;
      source.removeAttribute('data-src');
      heroVideo.load();
    }
    if (heroVideo.paused) heroVideo.play().catch(() => {});
  };
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(([entry]) => {
      heroVisible = entry.isIntersecting;
      updateHeroPlayback();
    }).observe(heroVideo.closest('.hero-section') || heroVideo);
  }
  document.addEventListener('visibilitychange', updateHeroPlayback);
  reducedMotion.addEventListener('change', updateHeroPlayback);
  updateHeroPlayback();
}

})();
