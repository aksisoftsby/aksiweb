/* Aksisoft redesign: navigasi tetap langsung; animasi hanya mendukung keterbacaan. */
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');

if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

document.querySelectorAll('.nav-item.dropdown').forEach((dropdown) => {
  const btn = dropdown.querySelector('.dropdown-toggle');
  if (!btn) return;
  btn.addEventListener('click', (event) => {
    if (window.innerWidth <= 760) {
      event.preventDefault();
      dropdown.classList.toggle('active');
      btn.setAttribute('aria-expanded', dropdown.classList.contains('active') ? 'true' : 'false');
    }
  });
});

const initReveal = () => {
  const revealItems = document.querySelectorAll('.reveal-section, .site-main > *');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver((entries, activeObserver) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          activeObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -20px 0px' });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initReveal);
} else {
  initReveal();
}

