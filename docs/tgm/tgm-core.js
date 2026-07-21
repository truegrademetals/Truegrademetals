/**
 * TrueGrade Metals — Global Core Behaviours
 * Lightweight shared behaviours used across every page.
 * - Float quote form toggle (if present)
 * - Email copy button (if present)
 * - Escape key closes open float form
 */
(function () {
  'use strict';

  var floatContact = document.getElementById('floatcontact');
  var floatCross = document.getElementById('floatcross');
  var floatBack = document.getElementById('float-back');

  function toggleFloat() {
    if (!floatContact) return;
    floatContact.className = (floatContact.className.indexOf('floatcontact2') !== -1)
      ? 'floatcontact1'
      : 'floatcontact2';
  }

  document.querySelectorAll('.click-event').forEach(function (el) {
    el.addEventListener('click', function (e) {
      var tag = el.tagName.toLowerCase();
      var parentLink = el.closest('a');
      var href = el.getAttribute('href') || (parentLink && parentLink.getAttribute('href'));
      // If it's a real link without a float form, navigate normally
      if ((tag === 'a' || parentLink) && !el.classList.contains('tgm-force-float')) {
        return;
      }
      e.preventDefault();
      e.stopPropagation();
      toggleFloat();
    });
  });

  if (floatCross) floatCross.addEventListener('click', toggleFloat);
  if (floatBack) floatBack.addEventListener('click', toggleFloat);

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && floatContact && floatContact.className.indexOf('floatcontact2') !== -1) {
      floatContact.className = 'floatcontact1';
    }
  });

  // Email copy
  var copyInput = document.querySelector('#input-copy > input');
  var copyButtons = document.querySelectorAll('.copy-button');
  var copyTexts = document.querySelectorAll('.copy-text');
  var emailToCopy = copyInput && copyInput.value ? copyInput.value : 'info@truegrademetals.com';

  function showCopyFeedback(index) {
    if (copyTexts[index]) {
      copyTexts[index].style.opacity = '1';
      setTimeout(function () { copyTexts[index].style.opacity = '0'; }, 2000);
    }
  }

  copyButtons.forEach(function (btn, index) {
    btn.addEventListener('click', function () {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(emailToCopy).then(function () { showCopyFeedback(index); });
      } else if (copyInput) {
        copyInput.select();
        document.execCommand('copy');
        showCopyFeedback(index);
      }
    });
  });
})();
