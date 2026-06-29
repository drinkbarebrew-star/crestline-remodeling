// Crestline Remodeling - Site JavaScript

document.addEventListener("DOMContentLoaded", function() {

  // ─── Sticky Header ─────────────────────────────────────────
  const header = document.getElementById("siteHeader");
  if (header) {
    window.addEventListener("scroll", function() {
      header.classList.toggle("scrolled", window.scrollY > 20);
    });
  }

  // ─── Mobile Nav Toggle ──────────────────────────────────────
  const toggle = document.getElementById("mobileToggle");
  const nav = document.getElementById("mainNav");
  if (toggle && nav) {
    toggle.addEventListener("click", function() {
      toggle.classList.toggle("active");
      nav.classList.toggle("active");
    });
    // Dropdown toggle on mobile
    nav.querySelectorAll(".has-dropdown > a").forEach(function(link) {
      link.addEventListener("click", function(e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          link.parentElement.classList.toggle("open");
        }
      });
    });
  }

  // ─── Gallery Filters ────────────────────────────────────────
  const filterBtns = document.querySelectorAll(".filter-btn");
  const galleryItems = document.querySelectorAll(".gallery-item");
  filterBtns.forEach(function(btn) {
    btn.addEventListener("click", function() {
      filterBtns.forEach(function(b) { b.classList.remove("active"); });
      btn.classList.add("active");
      var filter = btn.getAttribute("data-filter");
      galleryItems.forEach(function(item) {
        if (filter === "all" || item.getAttribute("data-category") === filter) {
          item.style.display = "";
        } else {
          item.style.display = "none";
        }
      });
    });
  });

  // ─── Lightbox ───────────────────────────────────────────────
  var lightbox = document.getElementById("lightbox");
  var lightboxImg = document.getElementById("lightboxImg");
  var lightboxClose = document.getElementById("lightboxClose");
  var lightboxPrev = document.getElementById("lightboxPrev");
  var lightboxNext = document.getElementById("lightboxNext");
  var currentIndex = 0;
  var visibleItems = [];

  function getVisibleItems() {
    visibleItems = [];
    galleryItems.forEach(function(item) {
      if (item.style.display !== "none") {
        visibleItems.push(item);
      }
    });
  }

  function openLightbox(index) {
    if (!lightbox) return;
    getVisibleItems();
    currentIndex = index;
    var imgEl = visibleItems[currentIndex].querySelector("img");
    lightboxImg.src = imgEl.src.replace("w=800", "w=1200");
    lightboxImg.alt = imgEl.alt;
    lightbox.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove("active");
    document.body.style.overflow = "";
  }

  galleryItems.forEach(function(item, i) {
    item.addEventListener("click", function() {
      getVisibleItems();
      var idx = visibleItems.indexOf(item);
      if (idx !== -1) openLightbox(idx);
    });
  });

  if (lightboxClose) lightboxClose.addEventListener("click", closeLightbox);
  if (lightboxPrev) lightboxPrev.addEventListener("click", function() {
    currentIndex = (currentIndex - 1 + visibleItems.length) % visibleItems.length;
    var imgEl = visibleItems[currentIndex].querySelector("img");
    lightboxImg.src = imgEl.src.replace("w=800", "w=1200");
    lightboxImg.alt = imgEl.alt;
  });
  if (lightboxNext) lightboxNext.addEventListener("click", function() {
    currentIndex = (currentIndex + 1) % visibleItems.length;
    var imgEl = visibleItems[currentIndex].querySelector("img");
    lightboxImg.src = imgEl.src.replace("w=800", "w=1200");
    lightboxImg.alt = imgEl.alt;
  });

  if (lightbox) {
    lightbox.addEventListener("click", function(e) {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", function(e) {
      if (!lightbox.classList.contains("active")) return;
      if (e.key === "Escape") closeLightbox();
      if (e.key === "ArrowLeft" && lightboxPrev) lightboxPrev.click();
      if (e.key === "ArrowRight" && lightboxNext) lightboxNext.click();
    });
  }

  // ─── Form Validation ───────────────────────────────────────
  document.querySelectorAll(".contact-form").forEach(function(form) {
    form.addEventListener("submit", function(e) {
      var valid = true;
      form.querySelectorAll("[required]").forEach(function(input) {
        if (!input.value.trim()) {
          valid = false;
          input.style.borderColor = "#e74c3c";
        } else {
          input.style.borderColor = "";
        }
      });
      var emailInput = form.querySelector("input[type=email]");
      if (emailInput && emailInput.value) {
        var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(emailInput.value)) {
          valid = false;
          emailInput.style.borderColor = "#e74c3c";
        }
      }
      if (!valid) {
        e.preventDefault();
      }
    });
  });

  // ─── Smooth scroll for anchor links ─────────────────────────
  document.querySelectorAll("a[href^=\"#\"]").forEach(function(link) {
    link.addEventListener("click", function(e) {
      var target = document.querySelector(link.getAttribute("href"));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });
});
