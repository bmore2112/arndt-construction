  // year
  document.getElementById('yr').textContent = new Date().getFullYear();

  // sticky nav state
  const nav = document.getElementById('nav');
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 12);
  onScroll(); window.addEventListener('scroll', onScroll, {passive:true});

  // reveal-on-scroll
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }
  }, {threshold: 0.12, rootMargin: '0px 0px -40px 0px'});
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  // only one FAQ open at a time
  const faqs = document.querySelectorAll('.faq');
  faqs.forEach(f => f.addEventListener('toggle', () => {
    if (f.open) faqs.forEach(o => { if (o !== f) o.open = false; });
  }));

  // mobile menu
  const menuBtn = document.querySelector('.menu-btn');
  const navLinks = document.querySelector('.nav-links');
  function setMenu(open){
    if (!navLinks || !menuBtn) return;
    navLinks.classList.toggle('open', open);
    menuBtn.classList.toggle('open', open);
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  }
  menuBtn?.addEventListener('click', () => setMenu(!navLinks.classList.contains('open')));
  navLinks?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  // close menu on resize up to desktop
  window.addEventListener('resize', () => { if (window.innerWidth > 880) setMenu(false); });

  // review modal
  const reviewModal = document.getElementById('reviewModal');
  function setReview(open){
    if (!reviewModal) return;
    reviewModal.classList.toggle('open', open);
    reviewModal.setAttribute('aria-hidden', open ? 'false' : 'true');
    document.body.style.overflow = open ? 'hidden' : '';
  }
  document.querySelectorAll('[data-open-review]').forEach(b => b.addEventListener('click', () => setReview(true)));
  document.querySelectorAll('[data-close-review]').forEach(b => b.addEventListener('click', () => setReview(false)));
  reviewModal?.addEventListener('click', (e) => { if (e.target === reviewModal) setReview(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && reviewModal?.classList.contains('open')) setReview(false); });

  // nav dropdown (click-to-toggle, also responds to hover via CSS)
  const dropdowns = document.querySelectorAll('.nav-dropdown');
  dropdowns.forEach((dd) => {
    const toggle = dd.querySelector('.nav-dropdown-toggle');
    if (!toggle) return;
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const willOpen = !dd.classList.contains('open');
      // close any other open dropdowns
      dropdowns.forEach((other) => {
        if (other !== dd) {
          other.classList.remove('open');
          other.querySelector('.nav-dropdown-toggle')?.setAttribute('aria-expanded', 'false');
        }
      });
      dd.classList.toggle('open', willOpen);
      toggle.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
    });
  });
  // close on click outside
  document.addEventListener('click', (e) => {
    dropdowns.forEach((dd) => {
      if (!dd.contains(e.target)) {
        dd.classList.remove('open');
        dd.querySelector('.nav-dropdown-toggle')?.setAttribute('aria-expanded', 'false');
      }
    });
  });
  // close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      dropdowns.forEach((dd) => {
        dd.classList.remove('open');
        dd.querySelector('.nav-dropdown-toggle')?.setAttribute('aria-expanded', 'false');
      });
    }
  });
