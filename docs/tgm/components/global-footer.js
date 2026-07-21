/**
 * TrueGrade Metals — Global Footer Loader
 * Fetches and injects the global footer component into any page.
 *
 * Usage:
 *   <div id="global-footer"></div>
 *   <script src="/tgm/components/global-footer.js"></script>
 */
(function () {
  'use strict';

  var container = document.getElementById('global-footer');
  if (!container) return;

  var url = '/tgm/components/global-footer.html';

  fetch(url)
    .then(function (response) {
      if (!response.ok) throw new Error('Footer load failed: ' + response.status);
      return response.text();
    })
    .then(function (html) {
      container.innerHTML = html;

      var scripts = container.querySelectorAll('script');
      scripts.forEach(function (oldScript) {
        var newScript = document.createElement('script');
        if (oldScript.src) {
          newScript.src = oldScript.src;
        } else {
          newScript.textContent = oldScript.textContent;
        }
        document.body.appendChild(newScript);
        newScript.remove();
      });
    })
    .catch(function (err) {
      console.warn('Global footer could not load:', err);
    });
})();
