/**
 * CCEYD - Main JavaScript
 * Handles: loader, header scroll, mobile nav, scroll animations, progress bars
 */

(function () {
  'use strict';

  // ===== LOADER =====
  const loader = document.getElementById('loader');
  if (loader) {
    window.addEventListener('load', () => {
      setTimeout(() => {
        loader.classList.add('hidden');
        setTimeout(() => loader.remove(), 500);
      }, 600);
    });
  }

  // ===== HEADER SCROLL =====
  const header = document.getElementById('header') || document.querySelector('.header');
  if (header) {
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
      const currentScroll = window.scrollY;
      if (currentScroll > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
      lastScroll = currentScroll;
    }, { passive: true });
  }

  // ===== MOBILE NAV =====
  // Support both ID and class selectors for the toggle button
  const mobileToggle = document.getElementById('mobile-menu-toggle') || document.querySelector('.mobile-menu-btn');
  const mobileNav = document.getElementById('mobile-nav');
  const mobileOverlay = document.getElementById('mobile-overlay');
  const mobileClose = document.getElementById('mobile-nav-close');

  function openMobileNav() {
    if (mobileNav) mobileNav.classList.add('active');
    if (mobileOverlay) mobileOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileNav() {
    if (mobileNav) mobileNav.classList.remove('active');
    if (mobileOverlay) mobileOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (mobileToggle) mobileToggle.addEventListener('click', openMobileNav);
  if (mobileClose) mobileClose.addEventListener('click', closeMobileNav);
  if (mobileOverlay) mobileOverlay.addEventListener('click', closeMobileNav);

  // Close mobile nav on link click
  if (mobileNav) {
    mobileNav.querySelectorAll('a:not(.mobile-nav-dropdown-toggle)').forEach((link) => {
      link.addEventListener('click', closeMobileNav);
    });
  }

  // Mobile nav accordion dropdowns
  document.querySelectorAll('.mobile-nav-dropdown-toggle').forEach((toggle) => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      const dropdown = toggle.closest('.mobile-nav-dropdown');
      if (dropdown) {
        dropdown.classList.toggle('open');
      }
    });
  });

  // Close on ESC
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMobileNav();
  });

  // ===== SCROLL ANIMATIONS =====
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -60px 0px',
    threshold: 0.15,
  };

  const animateObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        animateObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.animate-in').forEach((el) => {
    animateObserver.observe(el);
  });

  // ===== PROGRESS BAR ANIMATION =====
  const progressObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const fills = entry.target.querySelectorAll('.progress-bar-fill');
        fills.forEach((fill) => {
          const width = fill.style.width;
          fill.style.width = '0%';
          requestAnimationFrame(() => {
            requestAnimationFrame(() => {
              fill.style.width = width;
            });
          });
        });
        progressObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  const campaignsGrid = document.querySelector('.campaigns-grid');
  if (campaignsGrid) {
    progressObserver.observe(campaignsGrid);
  }

  // ===== SMOOTH SCROLL FOR ANCHOR LINKS =====
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href === '#') return;
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        closeMobileNav();
      }
    });
  });

  // ===== NEWSLETTER FORM =====
  const newsletterForm = document.getElementById('newsletter-form');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = document.getElementById('newsletter-email');
      if (emailInput && emailInput.value) {
        const btn = document.getElementById('newsletter-submit-btn');
        if (btn) {
          const original = btn.textContent;
          btn.textContent = 'Subscribed!';
          btn.style.background = '#22c55e';
          setTimeout(() => {
            btn.textContent = original;
            btn.style.background = '';
            emailInput.value = '';
          }, 2500);
        }
      }
    });
  }

  // ===== DONATE PAGE LOGIC =====
  const freqBtns = document.querySelectorAll('.freq-btn');
  if (freqBtns.length > 0) {
    freqBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        freqBtns.forEach(b => {
          b.classList.remove('btn-primary');
          b.classList.add('btn-outline-pill');
        });
        btn.classList.remove('btn-outline-pill');
        btn.classList.add('btn-primary');
      });
    });
  }

  const amountBtns = document.querySelectorAll('.amount-btn');
  const impactText = document.getElementById('impact-text');
  const otherAmountContainer = document.getElementById('other-amount-container');

  if (amountBtns.length > 0) {
    const impacts = {
      '50': '50 GHS provides health education materials for one family.',
      '100': '100 GHS provides essential school supplies for one child for a year.',
      '250': '250 GHS funds a community workshop on environmental sustainability.',
      '500': '500 GHS supports legal advocacy for a victim of human trafficking.',
      '1000': '1000 GHS helps build a clean water well for a rural community.',
      'other': 'Every contribution helps us empower communities.'
    };

    amountBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Update active classes
        amountBtns.forEach(b => {
          b.classList.remove('btn-primary');
          b.classList.add('btn-outline-pill');
        });
        btn.classList.remove('btn-outline-pill');
        btn.classList.add('btn-primary');
        
        // Handle impact text and "Other Amount" input
        const amount = btn.getAttribute('data-amount');
        if (amount === 'other') {
          otherAmountContainer.style.display = 'block';
        } else {
          otherAmountContainer.style.display = 'none';
        }
        
        if (impactText && impacts[amount]) {
          impactText.innerHTML = `<i class="ri-information-line"></i> ${impacts[amount]}`;
        }
      });
    });
  }

})();
