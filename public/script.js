/* Crestline Remodeling — shared JS: mobile menu, FAQ accordion, scroll animations, contact form */
(function () {
  'use strict';

  // Mobile menu toggle
  var toggle = document.querySelector('.menu-toggle');
  var links = document.querySelector('.nav__links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
      var expanded = links.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
  }

  // Mobile dropdown (Services / Areas) expand on tap
  document.querySelectorAll('.nav__item--has-menu > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 760) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  // FAQ accordion
  document.querySelectorAll('.faq__q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq__item');
      var isOpen = item.classList.contains('open');
      // close siblings within the same .faq group
      var group = item.closest('.faq');
      if (group) {
        group.querySelectorAll('.faq__item.open').forEach(function (other) {
          if (other !== item) other.classList.remove('open');
        });
      }
      item.classList.toggle('open', !isOpen);
      btn.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
    });
  });

  // Scroll reveal animations
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { obs.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('visible'); });
  }

  // Contact form (client-side handling; no backend yet)
  var form = document.querySelector('#contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var success = document.querySelector('.form-success');
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      if (success) {
        success.classList.add('show');
        success.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      form.reset();
    });
  }

  // Current year in footer
  document.querySelectorAll('.js-year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
