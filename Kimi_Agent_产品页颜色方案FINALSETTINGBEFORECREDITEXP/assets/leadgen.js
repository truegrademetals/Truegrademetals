/* ═══════════════════════════════════════════════════════════════
   TrueGrade Metals — Lead Generation
   · Datasheet unlock modal (exit-intent + 45% scroll, once/7 days)
   · Captures to localStorage (CRM-ready via LEAD_WEBHOOK_URL)
   · Site owner export: add ?leads=export to any URL → CSV download
   ═══════════════════════════════════════════════════════════════ */
(function(){
  var LEAD_WEBHOOK_URL = ''; /* ← point at your CRM/Formspree/Zapier endpoint to go live */
  var STORE_KEY = 'tg_leads';
  var SUPPRESS_KEY = 'tg_lead_modal_until';
  var PDF = 'assets/grade-selection-guide.pdf';

  function store(lead){
    try{
      var arr = JSON.parse(localStorage.getItem(STORE_KEY) || '[]');
      lead.ts = new Date().toISOString();
      lead.page = location.pathname.split('/').pop() || 'index.html';
      arr.push(lead);
      localStorage.setItem(STORE_KEY, JSON.stringify(arr));
    }catch(e){}
  }
  function send(lead){
    store(lead);
    if (LEAD_WEBHOOK_URL){
      try{ fetch(LEAD_WEBHOOK_URL, {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(lead)}); }catch(e){}
    }
    /* notify sales by email (opens owner's mailbox only when THEY export; for the visitor we just confirm) */
  }

  /* ── owner export: ?leads=export downloads CSV ── */
  if (/[?&]leads=export/.test(location.search)){
    var arr = [];
    try{ arr = JSON.parse(localStorage.getItem(STORE_KEY) || '[]'); }catch(e){}
    var csv = 'timestamp,page,type,name,email,company,interest\n' + arr.map(function(l){
      return [l.ts, l.page, l.type, l.name, l.email, l.company, l.interest].map(function(x){ return '"' + String(x||'').replace(/"/g,'""') + '"'; }).join(',');
    }).join('\n');
    var a = document.createElement('a');
    a.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
    a.download = 'truegrade-leads.csv';
    document.body.appendChild(a); a.click(); a.remove();
  }

  /* ── modal markup ── */
  function buildModal(){
    if (document.getElementById('tgLeadModal')) return;
    var wrap = document.createElement('div');
    wrap.id = 'tgLeadModal';
    wrap.innerHTML =
      '<div class="tglm-backdrop" id="tglmBackdrop"></div>' +
      '<div class="tglm-card" role="dialog" aria-modal="true" aria-label="Free engineering guide">' +
        '<button class="tglm-close" id="tglmClose" aria-label="Close">✕</button>' +
        '<div class="tglm-tag">FREE ENGINEERING GUIDE</div>' +
        '<h3>Nickel Alloy Grade Selection Guide</h3>' +
        '<p>Grade selection matrix · environment shortcuts · forms &amp; ASTM standards · the 5-line RFQ spec. Used by 900+ procurement teams.</p>' +
        '<form id="tglmForm">' +
          '<input id="tglmName" placeholder="Your name" required>' +
          '<input id="tglmEmail" type="email" placeholder="Work email" required>' +
          '<input id="tglmCompany" placeholder="Company (optional)">' +
          '<button type="submit" class="btn btn-primary" style="width:100%;justify-content:center">Send me the free guide →</button>' +
        '</form>' +
        '<div class="tglm-done" id="tglmDone" style="display:none">' +
          '<div class="tglm-check">✔</div>' +
          '<strong>Your guide is downloading.</strong>' +
          '<span>A copy request has been logged — our engineer follows up within 24 h if you have questions.</span>' +
        '</div>' +
        '<small>No spam. One follow-up from a real metallurgist, that\'s it.</small>' +
      '</div>';
    document.body.appendChild(wrap);

    var hide = function(){
      wrap.classList.remove('show');
      try{ localStorage.setItem(SUPPRESS_KEY, String(Date.now() + 7*24*3600*1000)); }catch(e){}
    };
    document.getElementById('tglmBackdrop').addEventListener('click', hide);
    document.getElementById('tglmClose').addEventListener('click', hide);
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape') hide(); });

    document.getElementById('tglmForm').addEventListener('submit', function(e){
      e.preventDefault();
      var lead = {
        type: 'guide-download',
        name: document.getElementById('tglmName').value.trim(),
        email: document.getElementById('tglmEmail').value.trim(),
        company: document.getElementById('tglmCompany').value.trim(),
        interest: 'Grade Selection Guide'
      };
      if (!lead.name || !lead.email) return;
      send(lead);
      this.style.display = 'none';
      document.getElementById('tglmDone').style.display = 'flex';
      var a = document.createElement('a');
      a.href = PDF; a.download = 'TrueGrade-Nickel-Alloy-Grade-Selection-Guide.pdf';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(hide, 5000);
    });
    return wrap;
  }

  function showModal(){
    try{
      var until = +localStorage.getItem(SUPPRESS_KEY) || 0;
      if (Date.now() < until) return;
    }catch(e){}
    var wrap = document.getElementById('tgLeadModal') || buildModal();
    if (!wrap.classList.contains('shown-once')){
      wrap.classList.add('show', 'shown-once');
    }
  }

  /* triggers: 45% scroll OR exit-intent (desktop), min 12 s on page */
  var armedAt = Date.now() + 12000, fired = false;
  function maybeFire(){ if (!fired && Date.now() > armedAt){ fired = true; showModal(); } }
  window.addEventListener('scroll', function(){
    var p = (window.scrollY + innerHeight) / document.documentElement.scrollHeight;
    if (p > 0.45) maybeFire();
  }, {passive:true});
  document.addEventListener('mouseout', function(e){
    if (!e.relatedTarget && e.clientY < 8) maybeFire();
  });

  /* ── inline capture blocks: any element with data-leadform renders a compact capture ── */
  document.querySelectorAll('[data-leadform]').forEach(function(slot){
    slot.innerHTML =
      '<div class="tgl-inline">' +
        '<div class="tgl-inline-text"><strong>Get the free Grade Selection Guide</strong><span>PDF · grade matrix · standards · RFQ spec template</span></div>' +
        '<form class="tgl-inline-form">' +
          '<input type="text" placeholder="Name" required>' +
          '<input type="email" placeholder="Work email" required>' +
          '<button type="submit" class="btn btn-primary btn-sm">Get guide →</button>' +
        '</form>' +
        '<div class="tgl-inline-done" style="display:none">✔ Guide downloading — check your downloads folder.</div>' +
      '</div>';
    var form = slot.querySelector('form');
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var inputs = form.querySelectorAll('input');
      send({type:'inline-guide', name:inputs[0].value.trim(), email:inputs[1].value.trim(), company:'', interest:'Grade Selection Guide'});
      form.style.display = 'none';
      slot.querySelector('.tgl-inline-done').style.display = 'block';
      var a = document.createElement('a');
      a.href = PDF; a.download = 'TrueGrade-Nickel-Alloy-Grade-Selection-Guide.pdf';
      document.body.appendChild(a); a.click(); a.remove();
    });
  });

  /* ── RFQ forms also become leads: hook any form with data-lead ── */
  document.querySelectorAll('form[data-lead]').forEach(function(f){
    f.addEventListener('submit', function(){
      var data = {type:'rfq'};
      f.querySelectorAll('input,select,textarea').forEach(function(el){
        if (el.id) data[el.id] = el.value;
      });
      var flat = {type:'rfq', name:data.fName||data.cName||'', email:data.fEmail||data.cEmail||'',
        company:data.fCompany||data.cCompany||'', interest:(data.fGrade||'')+' '+(data.fForm||'')};
      if (flat.email) send(flat);
    });
  });
})();
