/**
 * TrueGrade Metals — Global Navigation Loader
 * Fetches and injects the global navigation component into any page.
 *
 * Usage:
 *   <div id="global-nav" style="min-height:122px"></div>
 *   <script src="/tgm/components/global-nav.js"></script>
 */
(function () {
  'use strict';

  var container = document.getElementById('global-nav');
  if (!container) return;

  var url = '/tgm/components/global-nav.html';

  fetch(url)
    .then(function (response) {
      if (!response.ok) throw new Error('Nav load failed: ' + response.status);
      return response.text();
    })
    .then(function (html) {
      container.innerHTML = html;

      // Re-execute any inline scripts from the injected component
      var scripts = container.querySelectorAll('script');
      scripts.forEach(function (oldScript) {
        var newScript = document.createElement('script');
        if (oldScript.src) {
          newScript.src = oldScript.src;
        } else {
          newScript.textContent = oldScript.textContent;
        }
        document.head.appendChild(newScript);
        newScript.remove();
      });

      // Remove placeholder min-height once loaded
      container.style.minHeight = '';
    })
    .catch(function (err) {
      console.warn('Global nav could not load:', err);
      container.style.minHeight = '';
    });
})();
