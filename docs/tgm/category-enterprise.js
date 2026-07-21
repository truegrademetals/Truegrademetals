/**
 * TrueGrade Metals — Enterprise Category Page Behaviour
 * Requires tgm-core.js for shared float form / email copy behaviour.
 * Adds category-specific interactions: grade carousel, form validation, FAQ accordion.
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
  var faqItems = document.querySelectorAll('#cat-faq details');
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
})();