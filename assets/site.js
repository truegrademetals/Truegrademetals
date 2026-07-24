/* AEETHER shared interactions */
(function(){
  /* header shadow */
  var header = document.getElementById('header');
  if (header){
    var onScroll = function(){ header.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
  }
  /* sticky bottom bar */
  var bar = document.getElementById('stickyBar');
  if (bar){
    var shown = false;
    window.addEventListener('scroll', function(){
      if (sessionStorage.getItem('ae-bar-closed')) return;
      var past = window.scrollY > 700;
      if (past !== shown){ shown = past; bar.classList.toggle('visible', shown); }
    }, {passive:true});
    var close = document.getElementById('stickyClose');
    if (close) close.addEventListener('click', function(){
      bar.classList.remove('visible'); sessionStorage.setItem('ae-bar-closed','1');
    });
  }
  /* reveal + counters */
  function animateCounter(c){
    if (c.dataset.done) return; c.dataset.done = 1;
    var to = +c.dataset.to, t0 = performance.now();
    (function tick(t){
      var p = Math.min((t - t0) / 1100, 1);
      c.textContent = Math.round(to * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  }
  if ('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(en){
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        en.target.querySelectorAll('.counter').forEach(animateCounter);
        io.unobserve(en.target);
      });
    }, {threshold:.12});
    document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });
    var ioC = new IntersectionObserver(function(es){
      es.forEach(function(en){
        if (!en.isIntersecting) return;
        animateCounter(en.target); ioC.unobserve(en.target);
      });
    }, {threshold:.4});
    document.querySelectorAll('.counter').forEach(function(c){ ioC.observe(c); });
  } else {
    document.querySelectorAll('.reveal').forEach(function(el){ el.classList.add('in'); });
  }
})();
