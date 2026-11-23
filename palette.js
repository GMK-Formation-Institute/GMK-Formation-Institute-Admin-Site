// Palettes de couleurs de l'espace de gestion (maquette) : même choix que pour le site public.
// La palette vient de ?palette=N, sinon du dernier choix mémorisé dans le navigateur.
(function () {
  var P = {
    '3': { n: 'Rose poudré', ink: '#2A1622', ink2: '#36202D', v: '#A63D6B', vl: '#F2B8C6', vxl: '#FBEAF0', paper: '#FCF8F8', mute: '#6A5560' },
    '4': { n: 'Lavande et pêche', ink: '#241430', ink2: '#30203D', v: '#6B3A8E', vl: '#D9C9E8', vxl: '#EEE8F4', paper: '#FAF8FC', mute: '#5E5068', acc: '#E3A587' },
    '5': { n: 'Terracotta et sable', ink: '#2B1A14', ink2: '#3A251D', v: '#A4512B', vl: '#E8A07A', vxl: '#F6ECE2', paper: '#FBF7F2', mute: '#6B5A50' }
  };
  var K = 'igmk-admin-palette', q = new URLSearchParams(location.search).get('palette'), cur = null;
  try { if (q !== null) localStorage.setItem(K, q); cur = q !== null ? q : localStorage.getItem(K); } catch (e) { cur = q; }
  if (!P[cur]) cur = 'a';
  var mix = function (c, pct) { return 'color-mix(in srgb,' + c + ' ' + pct + '%,transparent)'; };
  if (cur !== 'a') {
    var p = P[cur], st = document.createElement('style');
    st.textContent = ':root{--ink:' + p.ink + ';--ink2:' + p.ink2 + ';--plum:' + p.ink + ';--v:' + p.v + ';--vl:' + p.vl + ';--vxl:' + p.vxl + ';--paper:' + p.paper + ';--mute:' + p.mute + ';--line:' + mix(p.ink, 8) + '}'
      + '.side nav a.on{background:linear-gradient(90deg,' + mix(p.v, 30) + ',' + mix(p.v, 8) + ')}'
      + '.side .brand .mk,.brand .mk{box-shadow:0 0 0 1px ' + p.vl + '}'
      + '.fld input:focus,.inp:focus{border-color:var(--v);box-shadow:0 0 0 4px ' + mix(p.v, 14) + '}'
      + '.mbg{background:' + mix(p.ink, 60) + '}.dbg{background:' + mix(p.ink, 40) + '}.tt,.spv{background:' + p.ink + '}'
      + (p.acc ? '.sla.warn,.bd.warn{background:' + mix(p.acc, 25) + '}' : '');
    document.head.appendChild(st);
  }
  var bar = document.createElement('div'); bar.className = 'palbar';
  bar.innerHTML = '<span>Palette</span>' + [['a', 'Actuelle']].concat(Object.keys(P).map(function (k) { return [k, k + ' · ' + P[k].n]; }))
    .map(function (it) { return '<a href="?palette=' + it[0] + location.hash + '"' + (it[0] === cur ? ' class="on"' : '') + '>' + it[1] + '</a>'; }).join('');
  var s2 = document.createElement('style');
  s2.textContent = '.palbar{position:fixed;right:16px;bottom:64px;z-index:120;display:flex;align-items:center;gap:3px;background:#fff;border:1px solid #0000001a;padding:4px;border-radius:24px;box-shadow:0 10px 30px #0002;max-width:calc(100vw - 32px);overflow-x:auto;scrollbar-width:none}'
    + '.palbar::-webkit-scrollbar{display:none}.palbar span{font:600 10px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#888;padding:0 8px}'
    + '.palbar a{font:600 11.5px/1 Manrope,sans-serif;color:#444;padding:8px 11px;border-radius:18px;white-space:nowrap}.palbar a:hover{background:#f2f2f2}.palbar a.on{background:var(--ink);color:#fff}'
    + '.demo{max-width:calc(100vw - 32px);overflow-x:auto;scrollbar-width:none}'
    + '@media(max-width:600px){.palbar{right:12px;left:12px;bottom:12px}}';
  document.head.appendChild(s2);
  function mount() { document.body.appendChild(bar); var o = bar.querySelector('.on'); if (o) bar.scrollLeft = o.offsetLeft - (bar.clientWidth - o.offsetWidth) / 2; }
  if (document.body) mount(); else document.addEventListener('DOMContentLoaded', mount);
})();
