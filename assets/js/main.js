/* Editorial Burgundy: navigation remains direct; motion only supports reading. */
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');

if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

document.querySelectorAll('.dropdown-toggle').forEach((dropdownToggle) => {
  dropdownToggle.addEventListener('click', (event) => {
    if (window.innerWidth <= 760) {
      event.preventDefault();
      const dropdown = dropdownToggle.closest('.nav-item.dropdown');
      if (dropdown) dropdown.classList.toggle('active');
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

