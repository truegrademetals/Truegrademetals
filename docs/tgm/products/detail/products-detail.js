(function(doc, win) {
  'use strict';

  /* ---------- Screen size class ---------- */
  let screenWidth = 0, size = 'M';
  if (win.screen && win.screen.width) {
    screenWidth = win.screen.width;
    if (screenWidth > 1920) {
      size = 'L';
    } else if (screenWidth < 1000) {
      size = 'Sm';
    }
  }
  doc.documentElement.className = size;
  win.SIZE = size;
})(document, window);

/* ---------- Upgrade scope ---------- */
document.body.classList.add('tgm-v2');
var tgmHtml = document.documentElement;

/* ---------- Hide empty chemical bars ---------- */
(function() {
  var elementsContent = document.querySelectorAll(".chemicalc > div");
  var elements = document.querySelectorAll(".chemicalc > div > div");
  for (var i = 0; i < elements.length; i++) {
    if (elements[i].offsetWidth == 0 && elementsContent[i]) {
      elementsContent[i].style.display = "none";
    }
  }
})();

/* ---------- Hero photo carousel (only when 5 images exist) ---------- */
(function() {
  var mainPhoto1 = document.querySelectorAll("#main-photo > img");
  var mainPhoto2 = document.querySelectorAll("#main-photo-2 > img");

  function setup(photos, offsets) {
    if (photos.length !== 5) return;
    for (var i = 0; i < photos.length; i++) {
      (function(i) {
        photos[i].addEventListener("click", function() {
          photos[(i + offsets[0]) % 5].style.transform = "translate(-45vw, 1.8vw) scale(0.6, 0.6)";
          photos[(i + offsets[0]) % 5].style.opacity = "0.5";
          photos[(i + offsets[0]) % 5].style.zIndex = "0";
          photos[(i + offsets[0]) % 5].style.boxShadow = "0 0 0 #666";
          photos[(i + offsets[1]) % 5].style.transform = "translate(-25vw, 1vw) scale(0.8, 0.8)";
          photos[(i + offsets[1]) % 5].style.opacity = "1";
          photos[(i + offsets[1]) % 5].style.zIndex = "1";
          photos[(i + offsets[1]) % 5].style.boxShadow = ".5vw .5vw 1vw #666";
          photos[i].style.transform = "translate(0, 0) scale(1, 1)";
          photos[i].style.opacity = "1";
          photos[i].style.zIndex = "2";
          photos[i].style.boxShadow = "1vw 1vw 2vw #666";
          photos[(i + offsets[2]) % 5].style.transform = "translate(25vw, 1vw) scale(0.8, 0.8)";
          photos[(i + offsets[2]) % 5].style.opacity = "1";
          photos[(i + offsets[2]) % 5].style.zIndex = "1";
          photos[(i + offsets[2]) % 5].style.boxShadow = ".5vw .5vw 1vw #666";
          photos[(i + offsets[3]) % 5].style.transform = "translate(45vw, 1.8vw) scale(0.6, 0.6)";
          photos[(i + offsets[3]) % 5].style.opacity = "0.5";
          photos[(i + offsets[3]) % 5].style.zIndex = "0";
          photos[(i + offsets[3]) % 5].style.boxShadow = "0 0 0 #666";
        });
      })(i);
    }
  }

  setup(mainPhoto1, [3, 4, 6, 7]);
  setup(mainPhoto2, [4, 6, 7, 3]);
})();

/* ---------- Chemical bar layout ---------- */
(function() {
  var chemical = document.querySelectorAll(".chemical");
  if (!chemical.length) return;

  function maximum(arr) {
    var max = 0;
    for (var i = 0; i < arr.length; i++) {
      if (arr[i] > max) max = arr[i];
    }
    return max;
  }

  function rank() {
    var elementWidth = [];
    var elementWidthReverse = [];
    var elementWidthMax = [];
    for (var i = 0; i < chemical.length; i++) {
      var element = chemical[i].querySelectorAll(".element");
      for (var j = 0; j < element.length; j++) {
        var cp = element[j].querySelector(".chemeicalp");
        if (cp) cp.style.color = "#fff";
      }
    }
    for (var i = 0; i < chemical.length; i++) {
      elementWidth.push([]);
      var element = chemical[i].querySelectorAll(".element");
      for (var j = 0; j < element.length; j++) {
        elementWidth[i].push(element[j].offsetWidth);
        if (element[j].offsetWidth == 0) {
          var cp = element[j].querySelector(".chemeicalp");
          if (cp) cp.style.color = "transparent";
        }
      }
    }
    for (var i = 0; i < elementWidth.length; i++) {
      for (var j = 0; j < elementWidth[i].length; j++) {
        if (i == 0) elementWidthReverse.push([]);
        elementWidthReverse[j].push(elementWidth[i][j]);
      }
    }
    for (var i = 0; i < elementWidthReverse.length; i++) {
      elementWidthMax.push(maximum(elementWidthReverse[i]));
    }
    for (var i = 0; i < chemical.length; i++) {
      var bar = chemical[i].querySelectorAll(".ele-frame");
      for (var j = 0; j < bar.length; j++) {
        bar[j].style.display = elementWidthMax[j] == 0 ? "none" : "block";
      }
    }
  }
  rank();
})();

/* ---------- Sticky secondary CTA reveal (legacy, now hidden by CSS) ---------- */
(function() {
  var mainPage = document.querySelector("#main-page");
  var contactbutton2 = document.querySelector("#contactbutton-2");
  if (!mainPage || !contactbutton2) return;
  var screenHeight = mainPage.offsetHeight;
  document.addEventListener("mousewheel", function() {
    if (tgmHtml.scrollTop >= screenHeight) {
      contactbutton2.style.opacity = "1";
      contactbutton2.style.pointerEvents = "inherit";
    } else {
      contactbutton2.style.opacity = "0";
      contactbutton2.style.pointerEvents = "none";
    }
  });
})();

/* ---------- Text clean helper ---------- */
function tagDel(x) {
  if (!x) return '';
  return x.innerHTML.replace(/from China/g, '').replace(/<[^<]+>/g, ' ').replace(/\s+/g, ' ').replace(/(\r\n|\n|\r)/gm, "").trim();
}

function getPageProductName() {
  var mainTitle = document.querySelector("#main-text > h1");
  if (mainTitle) return tagDel(mainTitle);
  return document.title.split(/[-|]/)[0].trim();
}

/* ---------- Primary CTAs + form prefill ---------- */
(function() {
  var bigContactBtn = document.querySelector("#contactbutton");
  var bigContactBtn2 = document.querySelector("#contactbutton-2");
  var smallContactBtn = document.querySelectorAll("#main-advantage > div");
  var mainTitle = document.querySelector("#main-text > h1");
  var asideSubject = document.querySelector("#aside-subject");
  var footerSubject = document.querySelector("#footer-subject");

  var prefill = mainTitle ? tagDel(mainTitle) : document.title.split(/[-|]/)[0].trim();

  function open(e) {
    if (e) { e.preventDefault(); e.stopImmediatePropagation(); }
    tgmOpenQuote(prefill);
  }

  if (bigContactBtn) bigContactBtn.addEventListener("click", open, true);
  if (bigContactBtn2) bigContactBtn2.addEventListener("click", open, true);

  for (var i = 0; i < smallContactBtn.length; i++) {
    smallContactBtn[i].addEventListener("click", open, true);
  }

  var tagDiv = document.querySelectorAll("#tag-div > div");
  for (var i = 0; i < tagDiv.length; i++) {
    tagDiv[i].addEventListener("click", open, true);
  }

  if (asideSubject) asideSubject.value = prefill;
  if (footerSubject) footerSubject.value = prefill;
})();

/* ---------- FAQ accordion (legacy q-frame) ---------- */
(function() {
  var qFrame = document.querySelectorAll(".q-frame");
  var faqFrame = document.querySelectorAll(".faq-frame");
  for (var i = 0; i < qFrame.length; i++) {
    (function(i) {
      if (!faqFrame[i]) return;
      qFrame[i].addEventListener("click", function() {
        faqFrame[i].className = (faqFrame[i].className == "faq-frame faq-v") ? "faq-frame faq-u" : "faq-frame faq-v";
      });
    })(i);
  }
})();

/* ---------- Intro expand ---------- */
(function() {
  var introP = document.querySelector("#intro-page > p");
  var fold = document.querySelector("#fold");
  if (fold && introP) {
    fold.addEventListener("click", function() {
      introP.className = "";
      fold.style.opacity = 0;
      fold.style.display = "none";
    });
  }
})();

/* ---------- Process tabs ---------- */
(function() {
  var processButton = document.querySelectorAll(".process-button");
  var processChoose = document.querySelectorAll(".process-choose");
  if (!processButton.length || !processChoose.length) return;
  for (var i = 0; i < processButton.length; i++) {
    (function(i) {
      processButton[i].addEventListener("click", function() {
        for (var j = 0; j < processButton.length; j++) {
          processButton[j].style.opacity = ".5";
          processChoose[j].style.opacity = "0";
          processChoose[j].style.pointerEvents = "none";
        }
        processButton[i].style.opacity = "1";
        processChoose[i].style.opacity = "1";
        processChoose[i].style.pointerEvents = "inherit";
      });
    })(i);
  }
})();

/* =========================================================
   Conversion upgrades — applied to all product detail pages
   ========================================================= */
(function() {
  'use strict';

  function tgmOpenQuote(prefill) {
    var overlay = document.getElementById('tgm-quote-modal');
    if (!overlay) return;
    overlay.classList.add('open');
    if (prefill) {
      var input = document.getElementById('tgm-quote-product');
      if (input) input.value = prefill;
      var subject = overlay.querySelector('input[name="subject"]');
      if (subject) subject.value = 'Quote Request: ' + prefill;
    }
  }
  window.tgmOpenQuote = tgmOpenQuote;

  var pageTitle = document.title.split(/[-|]/)[0].trim();
  var h1Text = document.querySelector('h1') ? document.querySelector('h1').textContent.trim() : '';
  var productName = getPageProductName() || pageTitle || h1Text || 'Nickel Alloy Product';
  var safeName = productName.replace(/"/g, '&quot;');

  /* Inject modal / bar / FAB once */
  if (!document.getElementById('tgm-quote-modal')) {
    var bar = document.createElement('div');
    bar.id = 'tgm-quote-bar';
    bar.className = 'quote-bar';
    bar.innerHTML = '<div class="quote-bar-text"><strong>Need a quote?</strong>Reply within 24 hours</div><button class="quote-btn" id="tgm-quote-bar-btn" type="button">Get 24h Quote</button>';
    document.body.appendChild(bar);

    var fab = document.createElement('button');
    fab.id = 'tgm-quote-fab';
    fab.className = 'quote-fab';
    fab.setAttribute('aria-label', 'Get a quote');
    fab.setAttribute('type', 'button');
    fab.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>';
    document.body.appendChild(fab);

    var overlay = document.createElement('div');
    overlay.id = 'tgm-quote-modal';
    overlay.className = 'quote-modal-overlay';
    overlay.innerHTML =
      '<div class="quote-modal" role="dialog" aria-modal="true" aria-labelledby="tgm-quote-title">' +
      '<button class="quote-modal-close" id="tgm-quote-modal-close" type="button" aria-label="Close quote form">×</button>' +
      '<h3 id="tgm-quote-title">Get a 24-hour quote</h3>' +
      '<p>Tell us what you need for <strong>' + safeName + '</strong> and we\'ll reply with price, MOQ and data sheet.</p>' +
      '<form action="mailto:info@truegrademetals.com" method="GET" enctype="text/plain">' +
      '<input type="hidden" name="subject" value="Quote Request: ' + safeName + '" />' +
      '<label for="tgm-quote-email">Your Email</label>' +
      '<input id="tgm-quote-email" type="email" name="email" placeholder="your@email.com" required />' +
      '<label for="tgm-quote-product">Product Interest</label>' +
      '<input id="tgm-quote-product" type="text" name="product" value="' + safeName + '" />' +
      '<label for="tgm-quote-qty">Quantity / Size</label>' +
      '<input id="tgm-quote-qty" type="text" name="quantity" placeholder="e.g. 500 kg, 6&quot; SCH40" />' +
      '<label for="tgm-quote-message">Message</label>' +
      '<textarea id="tgm-quote-message" name="body" placeholder="Grade, dimensions, delivery destination, application..."></textarea>' +
      '<button type="submit" class="quote-modal-submit">Send Inquiry</button>' +
      '</form></div>';
    document.body.appendChild(overlay);

    function openModal() { overlay.classList.add('open'); }
    function closeModal() { overlay.classList.remove('open'); }

    document.getElementById('tgm-quote-bar-btn').addEventListener('click', openModal);
    fab.addEventListener('click', openModal);
    document.getElementById('tgm-quote-modal-close').addEventListener('click', closeModal);
    overlay.addEventListener('click', function(e) { if (e.target === overlay) closeModal(); });
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeModal(); });

    var shown = false;
    window.addEventListener('scroll', function() {
      if (window.scrollY > 400 && !shown) {
        bar.classList.add('visible');
        shown = true;
      }
    }, { passive: true });
  }

  /* Trust bar under hero */
  (function initTrustBar() {
    var hero = document.getElementById('main-page');
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
    bar.innerHTML = items.map(function(t) { return '<div class="tgm-trust-item">' + svgCheck + '<span>' + t + '</span></div>'; }).join('');
    hero.appendChild(bar);
  })();

  /* Hero gallery — swap main image from thumbnails */
  (function initHeroGallery() {
    var desk = document.getElementById('main-photo');
    if (!desk) return;
    var imgs = Array.from(desk.querySelectorAll('img.main-photo'));
    if (imgs.length < 2) return;
    imgs.slice(1).forEach(function(thumb) {
      thumb.addEventListener('click', function(e) {
        e.preventDefault();
        var main = imgs[0];
        var tmpSrc = main.src;
        var tmpAlt = main.alt;
        main.src = thumb.src;
        main.alt = thumb.alt;
        thumb.src = tmpSrc;
        thumb.alt = tmpAlt;
        imgs.forEach(function(im) { im.classList.remove('active'); });
        thumb.classList.add('active');
      });
    });
  })();

  /* Quote buttons on popular-product cards */
  (function initPopularQuotes() {
    var cards = document.querySelectorAll('.popular-products-card');
    if (!cards.length) return;
    cards.forEach(function(card) {
      if (card.querySelector('.tgm-card-quote')) return;
      var link = card.querySelector('a');
      var titleText = '';
      if (link) {
        titleText = (link.textContent || '').replace(/\s+/g, ' ').trim();
      }
      if (!titleText) {
        var spans = card.querySelectorAll('span');
        titleText = Array.from(spans).map(function(s) { return s.textContent.trim(); }).filter(Boolean).join(' ');
      }
      var prefill = titleText || pageTitle;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'tgm-card-quote';
      btn.textContent = 'Quote';
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        tgmOpenQuote(prefill);
      });
      card.style.position = 'relative';
      card.appendChild(btn);
    });
  })();

  /* Quote buttons on grade bars */
  (function initGradeQuotes() {
    document.querySelectorAll('.gradebar').forEach(function(bar) {
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
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        tgmOpenQuote(productName || pageTitle);
      });
      bar.appendChild(btn);
    });
  })();

  /* FAQ accordion for Q/A markup */
  (function initFAQ() {
    var faq = document.getElementById('faq');
    if (!faq) return;
    var container = faq.querySelector('div');
    if (!container) return;
    container.querySelectorAll('.FAQ-fold-1').forEach(function(el) { el.classList.remove('FAQ-fold-1'); });
    var qEls = Array.from(container.querySelectorAll('.Q'));
    qEls.forEach(function(q, idx) {
      var a = q.nextElementSibling;
      if (!a || !a.classList.contains('A')) return;
      var wrapper = document.createElement('div');
      wrapper.className = 'tgm-faq-item' + (idx === 0 ? ' open' : '');
      q.parentNode.insertBefore(wrapper, q);
      wrapper.appendChild(q);
      wrapper.appendChild(a);
      q.addEventListener('click', function() { wrapper.classList.toggle('open'); });
    });
    var foldBtn = document.getElementById('FAQ-fold');
    if (foldBtn) foldBtn.style.display = 'none';
  })();

  /* Scroll reveal */
  (function initReveal() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var targets = document.querySelectorAll('section, .popular-products-card, .gradeframe1, #specifications-features-3 > div, .tgm-trust-item');
    targets.forEach(function(el) { el.classList.add('tgm-reveal'); });
    var obs = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('tgm-reveal-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    targets.forEach(function(el) { obs.observe(el); });
  })();

  /* Table horizontal-scroll hint */
  (function initTableScroll() {
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

  /* Desktop sticky side rail */
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
    tab.addEventListener('click', function() { rail.classList.toggle('open'); });
    cta.addEventListener('click', function(e) { e.stopPropagation(); tgmOpenQuote(); close(); });
    rail.addEventListener('mouseenter', open);
    rail.addEventListener('mouseleave', close);
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
