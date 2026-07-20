

document.body.classList.add('tgm-v2');

let floatLogo = document.querySelector("#floatlogo");


let descriptionCatalogue3 = document.querySelector("#description-catalogue-3");
if (descriptionCatalogue3 && floatLogo) {
  let top6 = descriptionCatalogue3.offsetTop;
  document.addEventListener("scroll", function(){
    let scrTop = html.scrollTop;
    if(scrTop >= top6){
      if (window.SIZE == 'Sm'){
        floatButton.style.width = "10.5vw";
        floatLogo.style.transform = "translate(0, 0)";
      }else{
        floatButton.style.width = "3.5vw";
        floatLogo.style.transform = "translate(0, 0)";
      }
    }
  });
}


let fold = document.querySelector("#fold");
let fold2 = document.querySelector("#fold2");
let technicalSheet = document.querySelector("#technical-sheet-1");
let faqFold = document.querySelector("#FAQ-fold");
let faqFold1 = document.querySelectorAll(".FAQ-fold-1");

if (fold) fold.addEventListener("click", function(){
  technicalSheet.className = "fold2";
  fold.style.opacity = "0";
  fold.style.pointerEvents = "none";
});
if (fold2) fold2.addEventListener("click", function(){
  technicalSheet.className = "fold2";
  fold2.style.opacity = "0";
  fold2.style.pointerEvents = "none";
});
if (faqFold) faqFold.addEventListener("click", function(){
  for (let i = 0; i < faqFold1.length; i++) {
    faqFold1[i].className = "FAQ-fold-2";
  }
  faqFold.style.opacity = "0";
  faqFold.style.pointerEvents = "none";
});



let mainPhoto1 = document.querySelectorAll("#main-photo > img");
let mainPhoto2 = document.querySelectorAll("#main-photo-2 > img");

if (mainPhoto1.length === 5) {
  for (let i = 0; i < mainPhoto1.length; i++) {
    mainPhoto1[i].addEventListener("click", function(){
      mainPhoto1[(i+3)%5].style.transform = "translate(-45vw, 1.8vw) scale(0.6, 0.6)";
      mainPhoto1[(i+3)%5].style.opacity = "0.5";
      mainPhoto1[(i+3)%5].style.zIndex = "0";
      mainPhoto1[(i+3)%5].style.boxShadow = "0 0 0 #666";
      mainPhoto1[(i+4)%5].style.transform = "translate(-25vw, 1vw) scale(0.8, 0.8)";
      mainPhoto1[(i+4)%5].style.opacity = "1";
      mainPhoto1[(i+4)%5].style.zIndex = "1";
      mainPhoto1[(i+4)%5].style.boxShadow = ".5vw .5vw 1vw #666";
      mainPhoto1[i].style.transform = "translate(0, 0) scale(1, 1)";
      mainPhoto1[i].style.opacity = "1";
      mainPhoto1[i].style.zIndex = "2";
      mainPhoto1[i].style.boxShadow = "1vw 1vw 2vw #666";
      mainPhoto1[(i+6)%5].style.transform = "translate(25vw, 1vw) scale(0.8, 0.8)";
      mainPhoto1[(i+6)%5].style.opacity = "1";
      mainPhoto1[(i+6)%5].style.zIndex = "1";
      mainPhoto1[(i+6)%5].style.boxShadow = ".5vw .5vw 1vw #666";
      mainPhoto1[(i+7)%5].style.transform = "translate(45vw, 1.8vw) scale(0.6, 0.6)";
      mainPhoto1[(i+7)%5].style.opacity = "0.5";
      mainPhoto1[(i+7)%5].style.zIndex = "0";
      mainPhoto1[(i+7)%5].style.boxShadow = "0 0 0 #666";
    })
  }
}
if (mainPhoto2.length === 5) {
  for (let i = 0; i < mainPhoto2.length; i++) {
    mainPhoto2[i].addEventListener("click", function(){
      mainPhoto2[(i+4)%5].style.transform = "translate(-20vw, 1.8vw) scale(0.9, 0.9)";
      mainPhoto2[(i+4)%5].style.opacity = "0.5";
      mainPhoto2[(i+4)%5].style.zIndex = "0";
      mainPhoto2[(i+4)%5].style.boxShadow = "0 0 0 #666";
      mainPhoto2[i].style.transform = "translate(-10vw, 1vw) scale(1, 1)";
      mainPhoto2[i].style.opacity = "1";
      mainPhoto2[i].style.zIndex = "1";
      mainPhoto2[i].style.boxShadow = ".5vw .5vw 1vw #666";
      mainPhoto2[(i+6)%5].style.transform = "translate(0, 0) scale(1.1, 1.1)";
      mainPhoto2[(i+6)%5].style.opacity = "1";
      mainPhoto2[(i+6)%5].style.zIndex = "2";
      mainPhoto2[(i+6)%5].style.boxShadow = "1vw 1vw 2vw #666";
      mainPhoto2[(i+7)%5].style.transform = "translate(10vw, 1vw) scale(1, 1)";
      mainPhoto2[(i+7)%5].style.opacity = "1";
      mainPhoto2[(i+7)%5].style.zIndex = "1";
      mainPhoto2[(i+7)%5].style.boxShadow = ".5vw .5vw 1vw #666";
      mainPhoto2[(i+3)%5].style.transform = "translate(20vw, 1.8vw) scale(0.9, 0.9)";
      mainPhoto2[(i+3)%5].style.opacity = "0.5";
      mainPhoto2[(i+3)%5].style.zIndex = "0";
      mainPhoto2[(i+3)%5].style.boxShadow = "0 0 0 #666";
    })
  }
}

processButton = document.querySelectorAll(".process-button");
processChoose = document.querySelectorAll(".process-choose");
for (let i = 0; i < processButton.length; i++) {
  processButton[i].addEventListener("click", function(){
    for (let j = 0; j < processButton.length; j++) {
      processButton[j].style = "opacity: .5;"
      processChoose[j].style = "opacity: 0; pointer-events: none;"
    }    
    processButton[i].style = "opacity: 1;"
    processChoose[i].style = "opacity: 1; pointer-events: inherit;"
  });
}



let mainAdvantage = document.querySelectorAll("#main-advantage > div");

for (let i = 0; i < mainAdvantage.length; i++) {
  mainAdvantage[i].addEventListener("click", () => {
    floatcontact.className = (floatcontact.className == "floatcontact1")?"floatcontact2":"floatcontact1";
  });
  
}




let rightButton = document.querySelector("#rightbutton1");
let leftButton = document.querySelector("#leftbutton1");
let alloyPage = document.querySelector("#alloypage");
let se = document.querySelectorAll(".s-e-1, .s-e-2");
let floatcontact = document.querySelector(".floatcontact1");
let position = 0;
let gradeFrame = document.querySelectorAll(".gradeframe1").length;

if (rightButton) rightButton.addEventListener("click", function(){
  if (position > -84*(gradeFrame-1)+1) {
    position -= 84;
    alloypage.style.transform = "translate(" + position + "vw, 0)";
  }
});
if (leftButton) leftButton.addEventListener("click", function(){
  if (position < 0) {
    position += 84;
    alloypage.style.transform = "translate(" + position + "vw, 0)";
  }
});



let learnButton2 = document.querySelectorAll("#learn-button-2 > div");


function getPageTop(){  
  let pageTop = [];
  let section = document.querySelectorAll("main > section");
  for (let i = 0; i < section.length; i++) {
    pageTop.push(section[i].offsetTop);
  }
  pageTop.splice(0, 1);
  return pageTop;
}

let navTimer;
function pageScroll(btn, page, num=0) {
  btn.addEventListener("click", function(){
    let navTime = 0.02;
    navTimer = setInterval(function(){
      html.scrollTop += (getPageTop()[page] - html.scrollTop + num)*navTime;
      navTime += 0.01;
      if (html.scrollTop >= getPageTop()[page] + num - 1 & html.scrollTop <= getPageTop()[page] + num + 1) {
        clearInterval(navTimer);
      }
    }, 10);
  });
}

for (let i = 0; i < learnButton2.length; i++) {
  pageScroll(learnButton2[i], i, -10);
}

document.addEventListener("mousewheel", function(){
  clearInterval(navTimer);
});

//自动填充

function tagDel(x) {
  y = x.innerHTML.replace(/from China/g, '').replace(/<[^<]+>/g, '').replace(/\s+/g, ' ').replace(/(\r\n|\n|\r)/gm, "").trim();
  return y;
}

let bigContactBtn = document.querySelector("#contactbutton");
let smallContactBtn = document.querySelectorAll("#main-advantage > div");
let mainTitle = document.querySelector("#main-text > h1");
let asideSubject = document.querySelector("#aside-subject");

if (bigContactBtn) {
  bigContactBtn.addEventListener("click", () => {
    if (asideSubject) asideSubject.value = tagDel(mainTitle);
  });
}

if (smallContactBtn !== null) {
  for (let i = 0; i < smallContactBtn.length; i++) {
    smallContactBtn[i].addEventListener("click", () => {
      if (asideSubject) asideSubject.value = tagDel(mainTitle);
    });
  }
}

let footerSubject = document.querySelector("#footer-subject");
if (footerSubject) footerSubject.value = tagDel(mainTitle);


let rightPopular = document.querySelector("#popular-products-right");
let leftPopular = document.querySelector("#popular-products-left");
let popularProductsPart = document.querySelector("#popular-products-part");
let position2 = 6.5;

if (rightPopular) rightPopular.addEventListener("click", function(){
  if (position2 > -283.5) {
    position2 -= 29;
    popularProductsPart.style.transform = "translate(" + position2 + "vw, 0)";
  }
  if (leftPopular) leftPopular.style.pointerEvents = "inherit";
  if (leftPopular) leftPopular.style.opacity = 1;
  if (rightPopular) rightPopular.style.pointerEvents = "inherit";
  if (rightPopular) rightPopular.style.opacity = 1;
  if (position2 == -283.5) {
    if (rightPopular) rightPopular.style.pointerEvents = "none";
    if (rightPopular) rightPopular.style.opacity = 0;
  }
  if (position2 == 6.5) {
    if (leftPopular) leftPopular.style.pointerEvents = "none";
    if (leftPopular) leftPopular.style.opacity = 0;
  }
});
if (leftPopular) leftPopular.addEventListener("click", function(){
  if (position2 < 6.5) {
    position2 += 29;
    popularProductsPart.style.transform = "translate(" + position2 + "vw, 0)";
  }
  if (leftPopular) leftPopular.style.pointerEvents = "inherit";
  if (leftPopular) leftPopular.style.opacity = 1;
  if (rightPopular) rightPopular.style.pointerEvents = "inherit";
  if (rightPopular) rightPopular.style.opacity = 1;
  if (position2 == -283.5) {
    if (rightPopular) rightPopular.style.pointerEvents = "none";
    if (rightPopular) rightPopular.style.opacity = 0;
  }
  if (position2 == 6.5) {
    if (leftPopular) leftPopular.style.pointerEvents = "none";
    if (leftPopular) leftPopular.style.opacity = 0;
  }
});

/* =========================================================
   Conversion upgrades — applied to all product pages
   ========================================================= */
document.addEventListener('DOMContentLoaded', function () {
  // Avoid double-injection
  if (document.getElementById('tgm-quote-bar')) return;

  const pageTitle = document.title.split(/[-|]/)[0].trim();
  const h1Text = document.querySelector('h1') ? document.querySelector('h1').textContent.trim() : '';
  const productName = pageTitle || h1Text || 'Nickel Alloy Product';
  const safeName = productName.replace(/"/g, '&quot;');

  // Mobile sticky quote bar
  const bar = document.createElement('div');
  bar.id = 'tgm-quote-bar';
  bar.className = 'quote-bar';
  bar.innerHTML = `
    <div class="quote-bar-text">
      <strong>Need a quote?</strong>
      Reply within 24 hours
    </div>
    <button class="quote-btn" id="tgm-quote-bar-btn" type="button">Get 24h Quote</button>
  `;
  document.body.appendChild(bar);

  // Desktop floating action button
  const fab = document.createElement('button');
  fab.id = 'tgm-quote-fab';
  fab.className = 'quote-fab';
  fab.setAttribute('aria-label', 'Get a quote');
  fab.setAttribute('type', 'button');
  fab.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>';
  document.body.appendChild(fab);

  // Modal
  const overlay = document.createElement('div');
  overlay.id = 'tgm-quote-modal';
  overlay.className = 'quote-modal-overlay';
  overlay.innerHTML = `
    <div class="quote-modal" role="dialog" aria-modal="true" aria-labelledby="tgm-quote-title">
      <button class="quote-modal-close" id="tgm-quote-modal-close" type="button" aria-label="Close quote form">×</button>
      <h3 id="tgm-quote-title">Get a 24-hour quote</h3>
      <p>Tell us what you need for <strong>${safeName}</strong> and we'll reply with price, MOQ and data sheet.</p>
      <form action="mailto:info@truegrademetals.com" method="GET" enctype="text/plain">
        <input type="hidden" name="subject" value="Quote Request: ${safeName}" />
        <label for="tgm-quote-email">Your Email</label>
        <input id="tgm-quote-email" type="email" name="email" placeholder="your@email.com" required />
        <label for="tgm-quote-product">Product Interest</label>
        <input id="tgm-quote-product" type="text" name="product" value="${safeName}" />
        <label for="tgm-quote-qty">Quantity / Size</label>
        <input id="tgm-quote-qty" type="text" name="quantity" placeholder="e.g. 500 kg, 6\" SCH40" />
        <label for="tgm-quote-message">Message</label>
        <textarea id="tgm-quote-message" name="body" placeholder="Grade, dimensions, delivery destination, application..."></textarea>
        <button type="submit" class="quote-modal-submit">Send Inquiry</button>
      </form>
    </div>
  `;
  document.body.appendChild(overlay);

  function openModal() { overlay.classList.add('open'); }
  function closeModal() { overlay.classList.remove('open'); }

  document.getElementById('tgm-quote-bar-btn').addEventListener('click', openModal);
  fab.addEventListener('click', openModal);
  document.getElementById('tgm-quote-modal-close').addEventListener('click', closeModal);
  overlay.addEventListener('click', function (e) { if (e.target === overlay) closeModal(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeModal(); });

  // Show mobile bar after scrolling past hero
  let shown = false;
  window.addEventListener('scroll', function () {
    if (window.scrollY > 400 && !shown) {
      bar.classList.add('visible');
      shown = true;
    }
  }, { passive: true });

  // Wire existing contact button to modal too
  const existingBtn = document.getElementById('contactbutton');
  if (existingBtn) {
    existingBtn.addEventListener('click', function (e) {
      e.preventDefault ? e.preventDefault() : (e.returnValue = false);
      openModal();
    });
  }
});


/* =========================================================
   Product pages — major conversion overhaul JS (v2)
   ========================================================= */
(function () {
  'use strict';

  function tgmOpenQuote(prefill) {
    const overlay = document.getElementById('tgm-quote-modal');
    if (!overlay) return;
    overlay.classList.add('open');
    if (prefill) {
      const input = document.getElementById('tgm-quote-product');
      if (input) input.value = prefill;
      const subject = overlay.querySelector('input[name="subject"]');
      if (subject) subject.value = 'Quote Request: ' + prefill;
    }
  }

  // Hero gallery — swap main image from thumbnails
  (function initHeroGallery() {
    const desk = document.getElementById('main-photo');
    const mob = document.getElementById('main-photo-2');
    const container = desk || mob;
    if (!container) return;
    const imgs = Array.from(container.querySelectorAll('img.main-photo'));
    if (imgs.length < 2 || container.id !== 'main-photo') return;
    imgs.slice(1).forEach(function (thumb) {
      thumb.addEventListener('click', function (e) {
        e.preventDefault();
        const main = imgs[0];
        const tmpSrc = main.src;
        const tmpAlt = main.alt;
        main.src = thumb.src;
        main.alt = thumb.alt;
        thumb.src = tmpSrc;
        thumb.alt = tmpAlt;
        imgs.forEach(function (im) { im.classList.remove('active'); });
        thumb.classList.add('active');
      });
    });
  })();

  // Trust bar under hero
  (function initTrustBar() {
    const hero = document.getElementById('main-page');
    if (!hero || hero.querySelector('.tgm-trust-bar')) return;
    var items = [
      'Quotation with Data Sheet',
      'MTC per EN 10204/3.1',
      'Reply within 24 Hours',
      'Custom sizes available'
    ];
    var svgCheck = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';
    var bar = document.createElement('div');
    bar.className = 'tgm-trust-bar';
    bar.innerHTML = items.map(function (t) { return '<div class="tgm-trust-item">' + svgCheck + '<span>' + t + '</span></div>'; }).join('');
    hero.appendChild(bar);
  })();

  // Quote buttons on popular-product cards
  (function initPopularQuotes() {
    var cards = document.querySelectorAll('.popular-products-card');
    var pageTitle = document.title.split(/[-|]/)[0].trim();
    cards.forEach(function (card) {
      if (card.querySelector('.tgm-card-quote')) return;
      var link = card.querySelector('a');
      var prefill = '';
      if (link) {
        prefill = link.textContent.replace(/\s+/g, ' ').trim();
      }
      if (!prefill) {
        var spans = Array.from(card.querySelectorAll('span'));
        var parts = [];
        spans.forEach(function (s) {
          var t = s.textContent.trim();
          if (t && parts.indexOf(t) === -1) parts.push(t);
        });
        prefill = parts.join(' ');
      }
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'tgm-card-quote';
      btn.textContent = 'Quote';
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        tgmOpenQuote(prefill || pageTitle);
      });
      card.style.position = 'relative';
      card.appendChild(btn);
    });
  })();

  // Quote buttons on grade bars
  (function initGradeQuotes() {
    var pageTitle = document.title.split(/[-|]/)[0].trim();
    document.querySelectorAll('.gradebar').forEach(function (bar) {
      if (bar.querySelector('.tgm-grade-quote')) return;
      var nameEl = bar.querySelector('.gradename, .gradename2, .gradename3');
      var grade = nameEl ? nameEl.textContent.trim() : '';
      var frame = bar.closest('.gradeframe1');
      var familyEl = frame ? frame.querySelector('.grade-class h3') : null;
      var family = familyEl ? familyEl.textContent.trim() : '';
      var productName = [family, grade].filter(Boolean).join(' ');
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'tgm-grade-quote';
      btn.textContent = 'Quote';
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        tgmOpenQuote(productName || pageTitle);
      });
      bar.appendChild(btn);
    });
  })();

  // FAQ accordion
  (function initFAQ() {
    var faq = document.getElementById('faq');
    if (!faq) return;
    var container = faq.querySelector('div');
    if (!container) return;
    container.querySelectorAll('.FAQ-fold-1').forEach(function (el) { el.classList.remove('FAQ-fold-1'); });
    var qEls = Array.from(container.querySelectorAll('.Q'));
    qEls.forEach(function (q, idx) {
      var a = q.nextElementSibling;
      if (!a || !a.classList.contains('A')) return;
      var wrapper = document.createElement('div');
      wrapper.className = 'tgm-faq-item' + (idx === 0 ? ' open' : '');
      q.parentNode.insertBefore(wrapper, q);
      wrapper.appendChild(q);
      wrapper.appendChild(a);
      q.addEventListener('click', function () { wrapper.classList.toggle('open'); });
    });
    var foldBtn = document.getElementById('FAQ-fold');
    if (foldBtn) foldBtn.style.display = 'none';
  })();

  // Scroll reveal
  (function initReveal() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var targets = document.querySelectorAll('section, .popular-products-card, .gradeframe1, #specifications-features-3 > div, .tgm-trust-item');
    targets.forEach(function (el) { el.classList.add('tgm-reveal'); });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('tgm-reveal-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    targets.forEach(function (el) { obs.observe(el); });
  })();

  // Table horizontal-scroll hint
  (function initTableScroll() {
    document.querySelectorAll('.table-container2').forEach(function (container) {
      function update() {
        var canScroll = container.scrollWidth > container.clientWidth + 2;
        container.classList.toggle('tgm-can-scroll', canScroll);
      }
      update();
      container.addEventListener('scroll', function () {
        var nearEnd = container.scrollLeft + container.clientWidth >= container.scrollWidth - 10;
        if (nearEnd) container.classList.remove('tgm-can-scroll');
      });
      window.addEventListener('resize', update, { passive: true });
    });
  })();

  // Desktop sticky side rail
  (function initSideRail() {
    if (document.getElementById('tgm-side-rail')) return;
    var rail = document.createElement('div');
    rail.id = 'tgm-side-rail';
    rail.innerHTML = '<div class="tgm-rail-panel"><h4>Get a 24h quote</h4><ul><li>Price + MOQ in 24h</li><li>MTC 3.1 included</li><li>Custom sizes welcome</li></ul><button type="button" class="tgm-rail-cta">Get Quote</button></div><div class="tgm-rail-tab" aria-label="Open quote panel">QUOTE</div>';
    document.body.appendChild(rail);
    var tab = rail.querySelector('.tgm-rail-tab');
    var cta = rail.querySelector('.tgm-rail-cta');
    function open() { rail.classList.add('open'); }
    function close() { rail.classList.remove('open'); }
    tab.addEventListener('click', function () { rail.classList.toggle('open'); });
    cta.addEventListener('click', function (e) { e.stopPropagation(); tgmOpenQuote(); close(); });
    rail.addEventListener('mouseenter', open);
    rail.addEventListener('mouseleave', close);
  })();



  // Ensure the primary hero CTA opens our modal, not the legacy floatcontact overlay
  (function wirePrimaryCTA() {
    var pageTitle = document.title.split(/[-|]/)[0].trim();
    var cta = document.getElementById('contactbutton');
    if (cta) {
      cta.addEventListener('click', function (e) {
        e.stopPropagation();
        e.preventDefault ? e.preventDefault() : (e.returnValue = false);
        tgmOpenQuote(pageTitle);
      }, true);
    }
    // Prevent legacy advantage cards from toggling the full-screen floatcontact overlay
    document.querySelectorAll('#main-advantage > div').forEach(function (card) {
      card.addEventListener('click', function (e) {
        e.stopPropagation();
      }, true);
    });
  })();

  /* =========================================================
     Data-sheet / technical-sheet table upgrades
     ========================================================= */
  (function initDataSheetUpgrades() {
    var pageTitle = document.title.split(/[-|]/)[0].trim();
    var productName = (function() {
      var h1 = document.querySelector('h1');
      if (h1) return h1.textContent.replace(/\s+/g, ' ').trim();
      return pageTitle;
    })() || 'Nickel Alloy Product';

    /* Wrap bare tables in a responsive container and enhance headers */
    (function initTables() {
      var containers = document.querySelectorAll('#technical-sheet-1, #data-sheet, #m-p, #p-p');
      containers.forEach(function(container) {
        var tables = container.querySelectorAll('table');
        tables.forEach(function(table) {
          var parent = table.parentNode;
          if (!parent || !parent.classList || parent.classList.contains('table-container2')) return;
          var wrapper = document.createElement('div');
          wrapper.className = 'table-container2';
          parent.insertBefore(wrapper, table);
          wrapper.appendChild(table);
        });
      });

      document.querySelectorAll('.table-container2 > table').forEach(function(table) {
        var rows = Array.from(table.querySelectorAll('tr'));
        if (!rows.length) return;

        /* Mark simple header rows */
        rows.forEach(function(row) {
          var cells = Array.from(row.children);
          if (!cells.length) return;
          var isHeaderRow = cells.every(function(cell) { return cell.tagName === 'TH'; });
          var isSimple = cells.every(function(cell) {
            return cell.tagName === 'TH' && (!cell.getAttribute('colspan') || cell.getAttribute('colspan') === '1') && (!cell.getAttribute('rowspan') || cell.getAttribute('rowspan') === '1');
          });
          if (isHeaderRow && isSimple) {
            row.classList.add('head-tr');
          }
        });

        /* Determine data rows: rows that are not header rows and contain td */
        var dataRows = rows.filter(function(row) {
          return !row.classList.contains('head-tr') && row.querySelector('td');
        });
        if (!dataRows.length) return;

        /* Only enable sorting if data rows are uniform and free of rowspans/colspans */
        var colCount = 0;
        dataRows.forEach(function(row) {
          colCount = Math.max(colCount, row.cells.length);
        });
        var hasSpan = dataRows.some(function(row) {
          return Array.from(row.cells).some(function(cell) {
            return cell.getAttribute('rowspan') || cell.getAttribute('colspan');
          });
        });
        var isUniform = dataRows.every(function(row) { return row.cells.length === colCount; });
        if (!isUniform || hasSpan || colCount === 0) return;

        /* Add sortable listeners to eligible headers */
        var headerRows = rows.filter(function(row) { return row.classList.contains('head-tr'); });
        headerRows.forEach(function(hRow) {
          Array.from(hRow.children).forEach(function(th, idx) {
            if (th.tagName !== 'TH') return;
            if (th.getAttribute('colspan') && th.getAttribute('colspan') !== '1') return;
            if (th.getAttribute('rowspan') && th.getAttribute('rowspan') !== '1') return;
            th.classList.add('tgm-sortable');
            th.setAttribute('title', 'Sort column');
            th.addEventListener('click', function(e) {
              e.stopPropagation();
              var dir = th.classList.contains('tgm-sort-asc') ? 'desc' : 'asc';
              /* Reset other headers */
              headerRows.forEach(function(r) {
                Array.from(r.children).forEach(function(other) {
                  other.classList.remove('tgm-sort-asc', 'tgm-sort-desc');
                });
              });
              th.classList.add(dir === 'asc' ? 'tgm-sort-asc' : 'tgm-sort-desc');

              /* Sort data rows */
              var sorted = dataRows.slice().sort(function(a, b) {
                var av = (a.cells[idx] ? a.cells[idx].textContent : '').trim();
                var bv = (b.cells[idx] ? b.cells[idx].textContent : '').trim();
                var an = parseFloat(av.replace(/,/g, ''));
                var bn = parseFloat(bv.replace(/,/g, ''));
                var aIsNum = !isNaN(an) && av !== '' && av !== '...';
                var bIsNum = !isNaN(bn) && bv !== '' && bv !== '...';
                if (aIsNum && bIsNum) {
                  return dir === 'asc' ? an - bn : bn - an;
                }
                if (av === '' || av === '...') return dir === 'asc' ? 1 : -1;
                if (bv === '' || bv === '...') return dir === 'asc' ? -1 : 1;
                return dir === 'asc' ? av.localeCompare(bv) : bv.localeCompare(av);
              });

              var tbody = table.querySelector('tbody') || table;
              sorted.forEach(function(row) { tbody.appendChild(row); });
            });
          });
        });

        /* Tap-to-highlight rows */
        dataRows.forEach(function(row) {
          row.addEventListener('click', function() {
            dataRows.forEach(function(r) { r.classList.remove('tgm-row-active'); });
            row.classList.add('tgm-row-active');
          });
        });
      });

      /* Recompute scroll hints */
      document.querySelectorAll('.table-container2').forEach(function(container) {
        function update() {
          var canScroll = container.scrollWidth > container.clientWidth + 2;
          container.classList.toggle('tgm-can-scroll', canScroll);
        }
        update();
        container.addEventListener('scroll', function() {
          var nearEnd = container.scrollLeft + container.clientWidth >= container.scrollWidth - 10;
          if (nearEnd) container.classList.remove('tgm-can-scroll');
        });
        window.addEventListener('resize', update, { passive: true });
      });
    })();

    /* Standards chips pulled from the standards section */
    (function initStandardsChips() {
      var standardsWrap = document.getElementById('standard-page-2');
      var trustBar = document.querySelector('.tgm-trust-bar');
      if (!standardsWrap || !trustBar) return;
      var standards = [];
      standardsWrap.querySelectorAll('div').forEach(function(el) {
        var text = el.textContent.trim();
        if (text && standards.indexOf(text) === -1) standards.push(text);
      });
      if (!standards.length) return;
      var chip = document.createElement('div');
      chip.className = 'tgm-trust-item tgm-standards-chip';
      chip.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg><span>Standards: ' + standards.slice(0, 4).join(', ') + (standards.length > 4 ? ' +' + (standards.length - 4) : '') + '</span>';
      trustBar.appendChild(chip);
    })();

    /* Repeated CTA after the technical data section */
    (function initDataCTA() {
      if (document.getElementById('tgm-data-cta')) return;
      var target = document.getElementById('data-sheet') || document.getElementById('technical-sheet-1');
      if (!target) return;
      var safeName = productName.replace(/"/g, '&quot;');
      var cta = document.createElement('div');
      cta.id = 'tgm-data-cta';
      cta.className = 'tgm-data-cta';
      cta.innerHTML = '<div class="tgm-data-cta-text"><strong>Need ' + safeName + '?</strong><span>Get price, MOQ & MTC 3.1 within 24 hours.</span></div><button type="button" class="tgm-data-cta-btn">Get 24h Quote</button>';
      target.appendChild(cta);
      cta.querySelector('button').addEventListener('click', function() { tgmOpenQuote(productName); });
    })();
  })();
})();
