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

  // ─── Form Validation + AJAX Submission ──────────────────────
  document.querySelectorAll(".contact-form").forEach(function(form) {
    form.addEventListener("submit", function(e) {
      e.preventDefault();

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
        return;
      }

      var formData = new FormData(form);
      var data = {};
      formData.forEach(function(value, key) { data[key] = value; });

      // Telegram notification (fires immediately for speed-to-lead)
      fetch('https://api.telegram.org/bot8735044985:AAGPjuQD8t_FCgRCY_KcIm64BKs980WUQYo/sendMessage', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          chat_id: '7046304764',
          text: '🔔 NEW LEAD - Crestline Remodeling\n\nName: ' + (data.name || '') + '\nPhone: ' + (data.phone || '') + '\nEmail: ' + (data.email || '') + '\nService: ' + (data.service || 'Not specified') + '\nMessage: ' + (data.message || '')
        })
      }).catch(function () {});

      var submitBtn = form.querySelector("button[type=submit], input[type=submit]");
      var originalText = submitBtn ? submitBtn.textContent : "";
      if (submitBtn) { submitBtn.textContent = "Sending..."; submitBtn.disabled = true; }

      function showSuccess() {
        var existing = form.querySelector(".form-message");
        if (existing) existing.remove();
        var div = document.createElement("div");
        div.className = "form-message";
        div.style.cssText = "background:#E8F5E9;color:#2E7D32;border:1px solid #A5D6A7;padding:14px 20px;border-radius:6px;margin-top:16px;font-weight:500;";
        div.innerHTML = "<strong>Thank you!</strong> Your request has been sent. We'll get back to you within one business day.";
        form.appendChild(div);
        form.reset();
        div.scrollIntoView({ behavior: "smooth", block: "center" });
        if (submitBtn) { submitBtn.textContent = originalText; submitBtn.disabled = false; }
      }

      // Submit to Formspree (backup / email record)
      fetch(form.action, {
        method: "POST",
        body: formData,
        headers: { "Accept": "application/json" }
      }).then(function () {
        showSuccess();
      }).catch(function () {
        showSuccess();
      });
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
