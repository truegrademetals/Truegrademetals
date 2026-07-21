/**
 * TrueGrade Metals — Enterprise Product Page Behaviour
 * Requires tgm-core.js for shared float form / email copy behaviour.
 * Adds product-specific interactions: grade carousel, form validation, FAQ accordion, gallery, table wrappers.
 */
(function () {
  'use strict';

  // Grade carousel scroll
  var alloyPage = document.getElementById('alloypage');
  var leftBtn = document.getElementById('leftbutton1');
  var rightBtn = document.getElementById('rightbutton1');

  function scrollGrades(direction) {
    if (!alloyPage) return;
    var frame = alloyPage.querySelector('.gradeframe1');
    var gap = 24;
    var step = frame ? frame.offsetWidth + gap : alloyPage.clientWidth * 0.84;
    alloyPage.scrollBy({ left: direction * step, behavior: 'smooth' });
  }

  if (leftBtn) leftBtn.addEventListener('click', function () { scrollGrades(-1); });
  if (rightBtn) rightBtn.addEventListener('click', function () { scrollGrades(1); });

  // Float form email validation
  var floatForm = document.getElementById('floatform');
  var asideEmail = document.getElementById('aside-email');
  var errorMessage2 = document.getElementById('errorMessage2');
  var emailRegex = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.]){1,2}[A-Za-z\d]{2,5}$/;

  if (floatForm) {
    floatForm.addEventListener('submit', function (e) {
      if (!asideEmail) return;
      var val = asideEmail.value.trim();
      if (!val || val === 'info@truegrademetals.com') {
        if (errorMessage2) errorMessage2.textContent = 'Please input your E-mail';
        e.preventDefault();
      } else if (!emailRegex.test(val)) {
        if (errorMessage2) errorMessage2.textContent = 'Please input the right E-mail';
        e.preventDefault();
      } else if (errorMessage2) {
        errorMessage2.innerHTML = '&emsp;';
      }
    });
  }

  // FAQ accordion: close others on open
  var faqItems = document.querySelectorAll('#cat-faq details, #prod-faq details');
  for (var f = 0; f < faqItems.length; f++) {
    (function(item) {
      item.addEventListener('toggle', function() {
        if (item.open) {
          for (var g = 0; g < faqItems.length; g++) {
            if (faqItems[g] !== item) faqItems[g].open = false;
          }
        }
      });
    })(faqItems[f]);
  }

  // Wrap large technical tables in a scroll container and mark if scrollable
  var tableSelectors = ['.tolerence-table', '.delivery-table'];
  tableSelectors.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (table) {
      var parent = table.parentNode;
      if (parent && parent.classList.contains('table-container2')) return;
      var wrapper = document.createElement('div');
      wrapper.className = 'table-container2';
      parent.insertBefore(wrapper, table);
      wrapper.appendChild(table);
      if (table.scrollWidth > wrapper.clientWidth) {
        wrapper.classList.add('is-scrollable');
      }
    });
  });
})();

/* Product page gallery thumbnail switcher */
(function () {
  'use strict';
  var slides = document.querySelectorAll('.prod-gallery-main .prod-gallery-slide');
  var thumbs = document.querySelectorAll('.prod-gallery-thumbs button');
  if (!slides.length || !thumbs.length) return;

  function show(idx) {
    idx = parseInt(idx, 10) - 1;
    if (idx < 0 || idx >= slides.length) return;
    slides.forEach(function (s) { s.classList.remove('active'); });
    thumbs.forEach(function (t) { t.classList.remove('active'); });
    slides[idx].classList.add('active');
    thumbs[idx].classList.add('active');
  }

  thumbs.forEach(function (btn) {
    btn.addEventListener('click', function () {
      show(btn.getAttribute('data-index'));
    });
  });

  show('1');
})();
