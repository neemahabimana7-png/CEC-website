const newsArticles = [
  {
    title: 'A First for Rwandan Engineering',
    slug: 'a-first-for-rwandan-engineering',
    category: 'events',
    categoryLabel: 'Engineering Milestone',
    image: '../images/B58A4353.jpg',
    imageAlt: 'CEC engineer working on power transmission infrastructure',
    excerpt: 'CEC Ltd made history by becoming the first Rwandan company to successfully build a 220kV transmission line, constructing a portion of the Shango–Birembo Line interconnecting Rwanda and DRC.',
    date: null,
    body: [
      'Century Engineering Contractors (CEC) achieved an important milestone in Rwanda’s engineering sector by becoming the first Rwandan company to successfully construct a 220kV transmission line.',
      'CEC contributed to the construction of a portion of the Shango–Birembo transmission line, an important high-voltage infrastructure project connecting Rwanda and the Democratic Republic of Congo (DRC).',
      'The works included civil works for the transmission-line infrastructure, including tower pegging, excavation and construction of tower foundations, followed by tower erection and conductor stringing.',
      'This achievement demonstrates the growing capacity of Rwandan engineering companies to undertake complex high-voltage infrastructure projects and contribute to the development of reliable regional power networks.',
      'For CEC, the project represents an important engineering milestone and reflects the company’s experience in power transmission and distribution infrastructure.'
    ]
  },
  {
    title: 'EPCA Group Headquarters Officially Completed',
    slug: 'epca-group-headquarters-officially-completed',
    category: 'projects',
    categoryLabel: 'Project Update',
    image: 'https://static.wixstatic.com/media/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg/v1/fill/w_1200,h_650,al_c,q_90,enc_avif,quality_auto/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg',
    imageAlt: 'Completed EPCA Group Headquarters building in Kigali',
    excerpt: 'The EPCA Group Headquarters in Gacuriro, Kigali, has been completed with structural construction and comprehensive MEP installations.',
    date: null,
    body: [
      'Century Engineering Contractors constructed the two-storey building that serves as the headquarters of EPC Africa Group in Gacuriro, Kigali.',
      'The works included substructure and superstructure construction together with comprehensive mechanical, electrical and plumbing installations.',
      'The completed building provides modern and functional office space designed to support the group’s operations and future growth.'
    ]
  },
  {
    title: 'Rubavu Port Construction Progress Update',
    slug: 'rubavu-port-construction-progress-update',
    category: 'projects',
    categoryLabel: 'Project Update',
    image: '../images/Capture.PNG',
    imageAlt: 'Aerial view of Rubavu Port on Lake Kivu',
    excerpt: 'Construction of Rubavu Port has delivered key quay and port infrastructure to support passenger, cargo and marine operations.',
    date: null,
    body: [
      'Century Engineering Contractors carried out the design, procurement and construction works for the development of the Port of Rubavu.',
      'The project included offshore and in-water quay construction together with cargo storage, passenger terminal and utility infrastructure required to support port operations.',
      'The development strengthens Rwanda’s marine transport infrastructure on Lake Kivu.'
    ]
  },
  {
    title: 'Rusizi Port Development Continues',
    slug: 'rusizi-port-development-continues',
    category: 'projects',
    categoryLabel: 'Project Update',
    image: '../images/Rusizi port.jpg',
    imageAlt: 'Aerial view of Rusizi Port development',
    excerpt: 'Works at Rusizi Port support the development of marine transport infrastructure, trade and connectivity on Lake Kivu.',
    date: null,
    body: [
      'Century Engineering Contractors is delivering works associated with the development of Rusizi Port.',
      'The project brings together marine and civil engineering works required for safe and efficient port operations.',
      'The development contributes to improved transport infrastructure, trade and regional connectivity.'
    ]
  }
];

const galleryItems = [
  { image: '../images/B58A4353.jpg', name: 'Shango–Birembo Transmission Line', category: 'Power & Energy' },
  { image: 'https://static.wixstatic.com/media/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg/v1/fill/w_1200,h_650,al_c,q_90,enc_avif,quality_auto/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg', name: 'EPCA Group Headquarters', category: 'Buildings' },
  { image: '../images/Capture.PNG', name: 'Rubavu Port', category: 'Marine & Civil Works' },
  { image: '../images/Rusizi port.jpg', name: 'Rusizi Port', category: 'Marine & Civil Works' },
  { image: '../images/luxury-apartments-blocks.jpg', name: 'Luxury Apartments – Kagarama', category: 'Buildings' },
  { image: '../images/akagera-game-lodge.jpg', name: 'Akagera Game Lodge', category: 'Buildings' },
  { image: '../images/residential-house-kimihurura.jpg', name: 'Kimihurura Residential House', category: 'Buildings' },
  { image: '../images/keya-hpp.jpg', name: 'Keya Hydropower Plant', category: 'Power & Energy' },
  { image: '../images/rubavu3.PNG', name: 'Rubavu Port Infrastructure', category: 'Marine & Civil Works' }
];

const escapeHtml = (value) => String(value).replace(/[&<>'"]/g, character => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', "'":'&#39;', '"':'&quot;' })[character]);

function renderNewsPage() {
  const results = document.querySelector('#news-results');
  if (!results) return;
  const filters = [...document.querySelectorAll('.news-filter')];
  const search = document.querySelector('#news-search');
  const empty = document.querySelector('#news-empty');
  const gallery = document.querySelector('#news-gallery');
  let activeFilter = 'all';

  const render = () => {
    const term = search.value.trim().toLowerCase();
    if (activeFilter === 'gallery') {
      results.hidden = true; empty.hidden = true; gallery.hidden = false;
      gallery.innerHTML = galleryItems.map((item, index) => `<figure class="gallery-item" tabindex="0" data-gallery-index="${index}"><img src="${escapeHtml(item.image)}" alt="${escapeHtml(item.name)}" loading="lazy"><figcaption class="gallery-caption"><strong>${escapeHtml(item.name)}</strong><span>${escapeHtml(item.category)}</span></figcaption></figure>`).join('');
      bindGalleryItems();
      return;
    }
    gallery.hidden = true; results.hidden = false;
    const matches = newsArticles.filter(article => (activeFilter === 'all' || article.category === activeFilter) && `${article.title} ${article.categoryLabel} ${article.excerpt}`.toLowerCase().includes(term));
    results.innerHTML = matches.map(article => `<article class="news-card"><a class="news-card-image" href="./news-article.html?slug=${encodeURIComponent(article.slug)}"><img src="${escapeHtml(article.image)}" alt="${escapeHtml(article.imageAlt)}" loading="lazy"></a><div class="news-card-body"><div class="news-card-meta"><span class="news-card-category">${escapeHtml(article.categoryLabel)}</span>${article.date ? `<time class="news-card-date"><i class="bi bi-calendar3"></i>${escapeHtml(article.date)}</time>` : ''}</div><h2>${escapeHtml(article.title)}</h2><p>${escapeHtml(article.excerpt)}</p><a class="news-card-link" href="./news-article.html?slug=${encodeURIComponent(article.slug)}">Read More →</a></div></article>`).join('');
    empty.hidden = matches.length > 0;
    if (!matches.length && activeFilter === 'company' && !term) empty.querySelector('p').textContent = 'Company news will appear here when verified updates are available.';
    else empty.querySelector('p').textContent = 'Try another search or choose a different category.';
  };

  filters.forEach(button => button.addEventListener('click', () => {
    activeFilter = button.dataset.filter;
    filters.forEach(item => { const selected = item === button; item.classList.toggle('active', selected); item.setAttribute('aria-selected', String(selected)); });
    search.disabled = activeFilter === 'gallery'; render();
  }));
  search.addEventListener('input', render);
  render();
}

let currentGalleryIndex = 0;
let previousFocus = null;
function bindGalleryItems() {
  document.querySelectorAll('.gallery-item').forEach(item => {
    const open = () => openLightbox(Number(item.dataset.galleryIndex));
    item.addEventListener('click', open);
    item.addEventListener('keydown', event => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); open(); } });
  });
}
function openLightbox(index) {
  const lightbox = document.querySelector('#news-lightbox'); if (!lightbox) return;
  previousFocus = document.activeElement; currentGalleryIndex = (index + galleryItems.length) % galleryItems.length;
  const item = galleryItems[currentGalleryIndex]; const image = lightbox.querySelector('img');
  image.src = item.image; image.alt = item.name; lightbox.querySelector('strong').textContent = item.name; lightbox.querySelector('figcaption span').textContent = item.category;
  lightbox.hidden = false; document.body.classList.add('lightbox-open'); lightbox.querySelector('.lightbox-close').focus();
}
function closeLightbox() { const lightbox = document.querySelector('#news-lightbox'); if (!lightbox) return; lightbox.hidden = true; lightbox.querySelector('img').src = ''; document.body.classList.remove('lightbox-open'); previousFocus?.focus(); }
function setupLightbox() {
  const lightbox = document.querySelector('#news-lightbox'); if (!lightbox) return;
  lightbox.querySelector('.lightbox-close').addEventListener('click', closeLightbox);
  lightbox.querySelector('.lightbox-prev').addEventListener('click', () => openLightbox(currentGalleryIndex - 1));
  lightbox.querySelector('.lightbox-next').addEventListener('click', () => openLightbox(currentGalleryIndex + 1));
  lightbox.addEventListener('click', event => { if (event.target === lightbox) closeLightbox(); });
  document.addEventListener('keydown', event => { if (lightbox.hidden) return; if (event.key === 'Escape') closeLightbox(); if (event.key === 'ArrowLeft') openLightbox(currentGalleryIndex - 1); if (event.key === 'ArrowRight') openLightbox(currentGalleryIndex + 1); });
}

function renderArticlePage() {
  const page = document.querySelector('#news-article'); if (!page) return;
  const slug = new URLSearchParams(location.search).get('slug') || newsArticles[0].slug;
  const article = newsArticles.find(item => item.slug === slug) || newsArticles[0];
  document.title = `${article.title} | CEC News`;
  document.querySelector('#article-breadcrumb-title').textContent = article.title;
  document.querySelector('#article-category').textContent = article.categoryLabel;
  document.querySelector('#article-title').textContent = article.title;
  const date = document.querySelector('#article-date'); if (article.date) { date.querySelector('span').textContent = article.date; date.hidden = false; }
  const image = document.querySelector('#article-image'); image.src = article.image; image.alt = article.imageAlt;
  document.querySelector('#article-body').innerHTML = article.body.map(paragraph => `<p>${escapeHtml(paragraph)}</p>`).join('');
}

renderNewsPage(); setupLightbox(); renderArticlePage();
