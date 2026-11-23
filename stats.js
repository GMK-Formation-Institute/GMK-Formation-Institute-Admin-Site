// Statistiques — données de démonstration + graphiques SVG (courbes avec survol)
(() => {
const PAL = ['#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#e87ba4', '#008300', '#6250d6', '#e34948'];
const MO = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'];
const Y0 = 2023, NOW = (2026 - Y0) * 12 + 10; // nov. 2026
let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const N = NOW + 1, mY = i => Y0 + Math.floor(i / 12), mM = i => i % 12;
const growth = i => Math.pow(1.13, i / 12);
// inscriptions : pics aux rentrées (oct., janv., avr.)
const PEAK = [0.9, .35, .25, .85, .3, .15, .1, .15, .55, 1.25, .35, .4];
const ins = [], ab = [], pay = [];
for (let i = 0; i < N; i++) {
  ins[i] = Math.round(26 * PEAK[mM(i)] * growth(i) * (.85 + rnd() * .3));
  ab[i] = Math.round((2 + rnd() * 3) * growth(i) * (mY(i) >= 2026 ? .8 : 1));
}
for (let i = 0; i < N; i++) { // versements : inscriptions du mois + mensualités des 6 mois précédents
  let s = ins[i] * 85000; for (let k = 1; k <= 6; k++) if (i - k >= 0) s += ins[i - k] * 52000 * (.88 + rnd() * .12);
  pay[i] = Math.round(s / 1000) * 1000;
}
// sources : TikTok monte, Facebook baisse
const SRC = ['TikTok', 'Facebook', 'Bouche à oreille', 'Ancienne élève', 'Instagram', 'Site web', 'Autre'];
const share = i => { const t = i / NOW; const r = [.08 + .30 * t, .38 - .18 * t, .22, .12, .08 + .02 * t, .04 + .06 * t, .08]; const s = r.reduce((a, b) => a + b); return r.map(x => x / s) };
// promotions : 3 par an
const PROMOS = []; for (let i = 0; i < N; i++) if ([0, 3, 9].includes(mM(i))) PROMOS.push({ name: (mM(i) === 9 ? 'Oct. ' : mM(i) === 0 ? 'Janv. ' : 'Avr. ') + mY(i), start: i, size: Math.round(ins[i] + (i > 0 ? ins[i - 1] : 0) * .8) });
PROMOS.forEach(p => {
  let a = p.size, c = 0; p.act = []; p.paid = [];
  const q = .93 + rnd() * .05;
  for (let k = 0; k < 9; k++) { if (p.start + k > NOW) break; if (k) a = Math.round(a * (q + rnd() * .03)); c = Math.min(100, c + (k ? 9 + rnd() * 4 : 22 + rnd() * 6)); p.act.push(a); p.paid.push(Math.round(c)) }
});

const fmtF = v => v >= 1e6 ? (v / 1e6).toFixed(v >= 1e7 ? 0 : 1).replace('.', ',') + ' M' : v >= 1e3 ? Math.round(v / 1e3) + ' k' : '' + v;
const fmtFull = v => Math.round(v).toLocaleString('fr-FR').replace(/ | /g, ' ') + ' F';
const lab = i => MO[mM(i)] + ' ' + String(mY(i)).slice(2);

// ---------- état des filtres ----------
const st = { a: NOW - 11, b: NOW, g: 1, cmp: 'prev', f: 'all', metric: 'act', sel: PROMOS.slice(-5, -1).map(p => p.name) };
const $ = s => document.querySelector(s);
function buckets(a, b, g) {
  const out = []; for (let i = a; i <= b; i++) { const k = g === 12 ? mY(i) : mY(i) * 100 + Math.floor(mM(i) / g); if (!out.length || out[out.length - 1].k !== k) out.push({ k, idx: [] }); out[out.length - 1].idx.push(i) }
  out.forEach(o => { const i = o.idx[0]; o.label = g === 1 ? lab(i) : g === 3 ? 'T' + (Math.floor(mM(i) / 3) + 1) + ' ' + String(mY(i)).slice(2) : g === 6 ? 'S' + (Math.floor(mM(i) / 6) + 1) + ' ' + String(mY(i)).slice(2) : '' + mY(i) });
  return out;
}
const FF = { all: 1, esthetique: .42, coiffure: .38, spe: .2 };
const sum = (arr, idx) => idx.reduce((s, i) => s + (i >= 0 && i < N ? arr[i] : 0), 0) * FF[st.f];
function cmpRange() { const L = st.b - st.a + 1; return st.cmp === 'prev' ? [st.a - L, st.b - L] : st.cmp === 'yoy' ? [st.a - 12, st.b - 12] : null }
function rangeTxt(a, b) { return a === b ? lab(a) : lab(a) + ' → ' + lab(b) }

// ---------- graphique en courbes ----------
function nice(max) { if (max <= 0) return [0, 1]; const e = Math.pow(10, Math.floor(Math.log10(max))); const s = [1, 2, 2.5, 5, 10].map(x => x * e).find(x => max / x <= 5); return [Math.ceil(max / s) * s, s] }
function line(el, { labels, series, fmt, tip }) {
  const W = document.body.classList.contains('printing') ? (el.closest('.g2') ? 330 : 690) : (el.clientWidth || 600), H = el.dataset.h ? +el.dataset.h : 280, pl = 52, pr = W > 520 && series.length <= 4 && series.length > 1 ? 92 : 18, pt = 16, pb = 34;
  const n = labels.length, vals = series.flatMap(s => s.values.filter(v => v != null));
  const [ymax, step] = nice(Math.max(...vals, 1) * 1.08);
  const x = i => pl + (n === 1 ? (W - pl - pr) / 2 : i * (W - pl - pr) / (n - 1)), y = v => pt + (H - pt - pb) * (1 - v / ymax);
  let g = '';
  for (let v = 0; v <= ymax + 1e-9; v += step) g += `<line x1="${pl}" x2="${W - pr}" y1="${y(v)}" y2="${y(v)}" class="gl"/><text x="${pl - 10}" y="${y(v) + 4}" class="ax" text-anchor="end">${fmt(v)}</text>`;
  const every = Math.ceil(n / Math.max(2, Math.floor((W - pl - pr) / 64)));
  labels.forEach((l, i) => { if (i % every === 0 || i === n - 1 && (n - 1) % every > every / 2) g += `<text x="${x(i)}" y="${H - 10}" class="ax" text-anchor="middle">${l}</text>` });
  const ends = [];
  series.forEach(s => {
    const pts = s.values.map((v, i) => v == null ? null : [x(i), y(v)]);
    let d = '', on = false; pts.forEach(p => { if (!p) { on = false; return } d += (on ? 'L' : 'M') + p[0].toFixed(1) + ',' + p[1].toFixed(1); on = true });
    g += `<path d="${d}" fill="none" stroke="${s.color}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"${s.dash ? ' stroke-dasharray="5 5" opacity=".75"' : ''}/>`;
    if (n <= 1 || pts.filter(Boolean).length === 1) pts.forEach(p => p && (g += `<circle cx="${p[0]}" cy="${p[1]}" r="4.5" fill="${s.color}" stroke="#fff" stroke-width="2"/>`));
    const li = s.values.map((v, i) => v == null ? -1 : i).filter(i => i >= 0).pop();
    if (li != null && li >= 0 && pr > 20) ends.push({ y: y(s.values[li]), x: x(li), name: s.short || s.name, color: s.color });
  });
  ends.sort((a, b) => a.y - b.y); for (let i = 1; i < ends.length; i++) if (ends[i].y - ends[i - 1].y < 15) ends[i].y = ends[i - 1].y + 15;
  ends.forEach(e => g += `<circle cx="${e.x}" cy="${e.y}" r="0"/><rect x="${e.x + 8}" y="${e.y - 4}" width="8" height="8" rx="2" fill="${e.color}"/><text x="${e.x + 20}" y="${e.y + 4}" class="dl">${e.name}</text>`);
  el.innerHTML = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img">${g}<line class="xh" y1="${pt}" y2="${H - pb}" x1="-9" x2="-9"/><g class="hv"></g><rect x="${pl}" y="0" width="${W - pl - pr}" height="${H}" fill="transparent" class="hit"/></svg><div class="tt" hidden></div>`;
  const svg = el.querySelector('svg'), tt = el.querySelector('.tt'), xh = el.querySelector('.xh'), hv = el.querySelector('.hv');
  const move = ev => {
    const r = svg.getBoundingClientRect(), mx = (ev.touches ? ev.touches[0].clientX : ev.clientX) - r.left;
    const i = Math.max(0, Math.min(n - 1, Math.round((mx - pl) / ((W - pl - pr) / Math.max(1, n - 1)))));
    xh.setAttribute('x1', x(i)); xh.setAttribute('x2', x(i));
    hv.innerHTML = series.map(s => s.values[i] == null ? '' : `<circle cx="${x(i)}" cy="${y(s.values[i])}" r="5" fill="${s.color}" stroke="#fff" stroke-width="2"/>`).join('');
    tt.hidden = false;
    tt.innerHTML = (tip ? tip(i) : `<b>${labels[i]}</b>`) + series.filter(s => s.values[i] != null).map(s => `<div><i style="background:${s.color}${s.dash ? ';opacity:.6' : ''}"></i>${s.tipName ? s.tipName(i) : s.name}<span>${s.fmtTip ? s.fmtTip(s.values[i]) : fmt(s.values[i])}</span></div>`).join('');
    const tw = tt.offsetWidth; tt.style.left = Math.min(W - tw - 4, Math.max(4, x(i) + 14 > W - tw ? x(i) - tw - 14 : x(i) + 14)) + 'px'; tt.style.top = '8px';
  };
  const leave = () => { tt.hidden = true; hv.innerHTML = ''; xh.setAttribute('x1', -9); xh.setAttribute('x2', -9) };
  svg.addEventListener('mousemove', move); svg.addEventListener('touchmove', move, { passive: true }); svg.addEventListener('mouseleave', leave);
}
function legend(el, items) { el.innerHTML = items.map(s => `<span><i style="background:${s.color}${s.dash ? ';opacity:.55' : ''}" class="${s.dash ? 'd' : ''}"></i>${s.name}</span>`).join('') }

// ---------- rendu ----------
function kpi(id, cur, prev, fmt, inv) {
  const el = $(id); el.querySelector('b').innerHTML = fmt(cur);
  const em = el.querySelector('em');
  if (prev == null || !prev) { em.textContent = 'Pas de comparaison'; em.className = ''; return }
  const d = (cur - prev) / prev * 100, good = inv ? d < 0 : d > 0;
  em.innerHTML = `${d > 0 ? '▲' : '▼'} ${Math.abs(d).toFixed(0)} % <small>vs ${fmt(prev).replace(/<[^>]+>/g, '')}</small>`; em.className = Math.abs(d) < .5 ? '' : good ? 'up' : 'down';
}
function render() {
  const B = buckets(st.a, st.b, st.g), cr = cmpRange();
  const CB = cr ? B.map(o => ({ idx: o.idx.map(i => i - (st.a - cr[0])) })) : null;
  const fs = document.querySelector('.fsum b'); if (fs) fs.textContent = (document.querySelector('#pre .on')?.textContent || rangeTxt(st.a, st.b)) + ' · ' + document.querySelector('#gran .on').textContent + (cr ? ' · vs ' + (st.cmp === 'prev' ? 'préc.' : 'N-1') : '') + (st.f !== 'all' ? ' · ' + document.querySelector('#ff').selectedOptions[0].text : '');
  const cn = st.cmp === 'prev' ? 'Période précédente' : 'Même période N-1';
  $('#rng').textContent = rangeTxt(st.a, st.b) + (cr ? ' · comparé à ' + rangeTxt(cr[0], cr[1]) : '');
  const allI = []; for (let i = st.a; i <= st.b; i++) allI.push(i); const allC = cr ? allI.map(i => i - (st.a - cr[0])) : null;
  // KPI
  const P = sum(pay, allI), I = sum(ins, allI), A = sum(ab, allI);
  kpi('#k1', P, cr && sum(pay, allC), v => fmtF(v) + ' <small>FCFA</small>');
  kpi('#k2', I, cr && sum(ins, allC), v => '' + Math.round(v));
  const tr = I ? A / I * 100 : 0, trc = cr ? sum(ab, allC) / Math.max(1, sum(ins, allC)) * 100 : null;
  kpi('#k3', tr, trc, v => v.toFixed(1).replace('.', ',') + ' %', true);
  const sh = allI.reduce((a, i) => share(i).map((x, k) => a[k] + x * ins[i]), SRC.map(() => 0)), tk = sh[0] / sh.reduce((a, b) => a + b) * 100;
  const shc = cr ? allC.reduce((a, i) => i < 0 ? a : share(i).map((x, k) => a[k] + x * ins[i]), SRC.map(() => 0)) : null;
  kpi('#k4', tk, shc && shc.reduce((a, b) => a + b) ? shc[0] / shc.reduce((a, b) => a + b) * 100 : null, v => v.toFixed(0) + ' %');
  // 1. versements
  const s1 = [{ name: 'Encaissé', short: 'Période', color: PAL[0], values: B.map(o => sum(pay, o.idx)), fmtTip: fmtFull }];
  if (CB) s1.push({ name: cn, short: st.cmp === 'prev' ? 'Préc.' : 'N-1', color: PAL[0], dash: 1, values: CB.map(o => o.idx.some(i => i >= 0) ? sum(pay, o.idx) : null), fmtTip: fmtFull, tipName: i => cn + ' · ' + buckets(CB[i].idx[0], CB[i].idx[CB[i].idx.length - 1], st.g)[0]?.label });
  line($('#c1'), { labels: B.map(o => o.label), series: s1, fmt: fmtF }); legend($('#l1'), s1);
  // 2. inscriptions / abandons
  const s2 = [{ name: 'Inscriptions', color: PAL[0], values: B.map(o => sum(ins, o.idx)) }, { name: 'Abandons', color: PAL[1], values: B.map(o => sum(ab, o.idx)) }];
  if (CB) { s2.push({ name: 'Inscriptions · ' + cn.toLowerCase(), short: 'Inscr. préc.', color: PAL[0], dash: 1, values: CB.map(o => o.idx.some(i => i >= 0) ? sum(ins, o.idx) : null) }); s2.push({ name: 'Abandons · ' + cn.toLowerCase(), short: 'Aband. préc.', color: PAL[1], dash: 1, values: CB.map(o => o.idx.some(i => i >= 0) ? sum(ab, o.idx) : null) }) }
  line($('#c2'), { labels: B.map(o => o.label), series: s2, fmt: v => '' + Math.round(v) }); legend($('#l2'), s2);
  // 3. sources (courbes par source, 4 principales)
  const s3 = SRC.slice(0, 4).map((nm, k) => ({ name: nm, color: PAL[k], values: B.map(o => Math.round(o.idx.reduce((a, i) => a + share(i)[k] * ins[i], 0) * FF[st.f])) }));
  line($('#c3'), { labels: B.map(o => o.label), series: s3, fmt: v => '' + Math.round(v) }); legend($('#l3'), s3);
  // barres sources période vs comparaison
  const tot = sh.reduce((a, b) => a + b), totc = shc ? shc.reduce((a, b) => a + b) : 0;
  $('#src').innerHTML = SRC.map((nm, k) => { const p = sh[k] / tot * 100, pc = shc && totc ? shc[k] / totc * 100 : null, d = pc != null ? p - pc : null;
    return `<div class="sb"><span>${nm}</span><div class="bar"><i style="width:${p}%"></i>${pc != null ? `<u style="left:${pc}%" title="${cn} : ${pc.toFixed(0)} %"></u>` : ''}</div><b>${Math.round(sh[k] * FF[st.f])}</b><em class="${d == null || Math.abs(d) < 1 ? '' : d > 0 ? 'up' : 'down'}">${p.toFixed(0)} %${d != null && Math.abs(d) >= 1 ? ` <small>${d > 0 ? '+' : ''}${d.toFixed(0)} pt</small>` : ''}</em></div>` }).join('');
  $('#srcl').innerHTML = cr ? `<span><i class="bx"></i>Période</span><span><i class="tk"></i>${cn}</span>` : '';
  // 4. promotions
  renderPromo();
  // à retenir
  const best = SRC[sh.indexOf(Math.max(...sh))], dP = cr ? (P - sum(pay, allC)) / Math.max(1, sum(pay, allC)) * 100 : null;
  const tkc = shc && totc ? shc[0] / totc * 100 : null, fbc = shc && totc ? shc[1] / totc * 100 : null;
  const pr = PROMOS.filter(p => p.act.length >= 6), ret = pr.map(p => ({ n: p.name, r: p.act[5] / p.act[0] * 100 })).sort((a, b) => b.r - a.r);
  $('#ins').innerHTML = [
    dP != null ? `Les encaissements sont <b>${dP >= 0 ? 'en hausse' : 'en baisse'} de ${Math.abs(dP).toFixed(0)} %</b> par rapport à ${st.cmp === 'prev' ? 'la période précédente' : "l'an dernier"}.` : '',
    `<b>${best}</b> est la première source d'inscriptions sur la période (${(Math.max(...sh) / tot * 100).toFixed(0)} %).` + (tkc != null ? ` TikTok passe de ${tkc.toFixed(0)} % à ${(sh[0] / tot * 100).toFixed(0)} %, Facebook de ${fbc.toFixed(0)} % à ${(sh[1] / tot * 100).toFixed(0)} %.` : ''),
    ret.length ? `Meilleure rétention à 6 mois : <b>promotion ${ret[0].n}</b> (${ret[0].r.toFixed(0)} % encore présentes) ; la plus faible : ${ret[ret.length - 1].n} (${ret[ret.length - 1].r.toFixed(0)} %).` : '',
    `Les rentrées d'<b>octobre</b> concentrent le plus d'inscriptions : c'est le moment où concentrer le budget publicitaire.`
  ].filter(Boolean).map(t => `<li>${t}</li>`).join('');
  // tableau
  $('#tbl').innerHTML = `<table><thead><tr><th>Période</th><th>Encaissé</th><th>Inscriptions</th><th>Abandons</th>${CB ? '<th>Encaissé (comparaison)</th>' : ''}</tr></thead><tbody>` + B.map((o, i) => `<tr><td>${o.label}</td><td>${fmtFull(sum(pay, o.idx))}</td><td>${Math.round(sum(ins, o.idx))}</td><td>${Math.round(sum(ab, o.idx))}</td>${CB ? `<td>${CB[i].idx.some(j => j >= 0) ? fmtFull(sum(pay, CB[i].idx)) : '—'}</td>` : ''}</tr>`).join('') + '</tbody></table>';
}
const promoColor = {}; // couleur attachée à la promotion, pas au rang
function renderPromo() {
  Object.keys(promoColor).forEach(k => { if (!st.sel.includes(k)) delete promoColor[k] });
  st.sel.forEach(k => { if (!promoColor[k]) promoColor[k] = PAL.find(c => !Object.values(promoColor).includes(c)) });
  $('#pchips').innerHTML = PROMOS.slice().reverse().map(p => { const on = st.sel.includes(p.name); return `<button class="pc${on ? ' on' : ''}" data-p="${p.name}"${!on && st.sel.length >= 6 ? ' disabled title="6 promotions maximum"' : ''}>${on ? `<i style="background:${promoColor[p.name]}"></i>` : ''}${p.name}<small>${p.size}</small></button>` }).join('');
  const sel = PROMOS.filter(p => st.sel.includes(p.name)), m = st.metric;
  const s = sel.map(p => ({ name: 'Promotion ' + p.name, short: p.name, color: promoColor[p.name], values: Array.from({ length: 9 }, (_, k) => (m === 'act' ? p.act : m === 'paid' ? p.paid : p.act.map(v => v / p.act[0] * 100))[k] ?? null) }));
  const f = m === 'act' ? v => '' + Math.round(v) : v => Math.round(v) + ' %';
  line($('#c4'), { labels: Array.from({ length: 9 }, (_, k) => 'Mois ' + (k + 1)), series: s, fmt: f, tip: i => `<b>Mois ${i + 1} après la rentrée</b>` });
  legend($('#l4'), s);
}

// ---------- contrôles ----------
const presets = { m3: [NOW - 2, NOW, 1], ytd: [NOW - 10, NOW, 1], sy: [NOW - 13, NOW - 2, 1], m12: [NOW - 11, NOW, 1], y3: [NOW - 35, NOW, 3], all: [0, NOW, 6] };
const toVal = i => mY(i) + '-' + String(mM(i) + 1).padStart(2, '0'), fromVal = v => { const [y, m] = v.split('-').map(Number); return Math.max(0, Math.min(NOW, (y - Y0) * 12 + m - 1)) };
function syncInputs() { $('#da').value = toVal(st.a); $('#db').value = toVal(st.b); document.querySelectorAll('#gran button').forEach(b => b.classList.toggle('on', +b.dataset.g === st.g)) }
document.querySelectorAll('#pre button').forEach(b => b.onclick = () => { document.querySelectorAll('#pre button').forEach(x => x.classList.toggle('on', x === b)); [st.a, st.b, st.g] = presets[b.dataset.p]; syncInputs(); render() });
['#da', '#db'].forEach(s => $(s).onchange = () => { st.a = fromVal($('#da').value); st.b = Math.max(st.a, fromVal($('#db').value)); document.querySelectorAll('#pre button').forEach(x => x.classList.remove('on')); const L = st.b - st.a + 1; if (L > 24 && st.g === 1) st.g = 3; syncInputs(); render() });
document.querySelectorAll('#gran button').forEach(b => b.onclick = () => { st.g = +b.dataset.g; syncInputs(); render() });
$('#cmp').onchange = e => { st.cmp = e.target.value; render() };
$('#ff').onchange = e => { st.f = e.target.value; render() };
document.querySelectorAll('#met button').forEach(b => b.onclick = () => { st.metric = b.dataset.m; document.querySelectorAll('#met button').forEach(x => x.classList.toggle('on', x === b)); renderPromo() });
$('#pchips').onclick = e => { const b = e.target.closest('[data-p]'); if (!b || b.disabled) return; const k = b.dataset.p; st.sel = st.sel.includes(k) ? st.sel.filter(x => x !== k) : [...st.sel, k]; renderPromo() };
$('#tv').onclick = () => { const t = $('#tbl'); t.hidden = !t.hidden; $('#tv').textContent = t.hidden ? 'Voir en tableau' : 'Masquer le tableau' };
let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(render, 150) });
syncInputs(); render();
setTimeout(render);
})();
(() => { const f = document.querySelector('.filt'); const s = document.createElement('div'); f.before(s);
  new IntersectionObserver(([e]) => f.classList.toggle('stuck', !e.isIntersecting), { rootMargin: '-85px 0px 0px 0px' }).observe(s); })();

(() => { const f = document.querySelector('.filt'), b = document.createElement('button'); b.className = 'fsum'; b.type = 'button'; b.innerHTML = '<span>Filtres</span><b></b><i>▾</i>'; f.prepend(b);
  b.onclick = () => f.classList.toggle('open'); document.addEventListener('click', e => { if (!e.target.closest('.filt')) f.classList.remove('open') }); })();
// ---------- export ----------
(() => {
  const b = document.getElementById('expb'), m = document.getElementById('expm');
  b.onclick = e => { e.stopPropagation(); m.hidden = !m.hidden };
  document.addEventListener('click', e => { if (!e.target.closest('.exp')) m.hidden = true });
  const meta = () => {
    const sel = s => document.querySelector(s);
    document.getElementById('prp').textContent = sel('#rng').textContent;
    document.getElementById('prf').textContent = 'Regroupé par ' + sel('#gran .on').textContent.toLowerCase() + ' · ' + sel('#cmp').selectedOptions[0].text + ' · Formation : ' + sel('#ff').selectedOptions[0].text;
    document.getElementById('prd').textContent = new Date().toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' }) + ' par K. N\'Si Batiye';
  };
  // graphiques redessinés à la largeur de la page A4 avant impression
  const redraw = () => window.dispatchEvent(new Event('resize'));
  const tb = document.getElementById('tbl'), tbHome = tb.nextElementSibling; const toEnd = () => document.querySelector('.page').appendChild(tb), back = () => tbHome.before(tb);
  addEventListener('beforeprint', () => { meta(); toEnd(); document.body.classList.add('printing'); redraw() });
  addEventListener('afterprint', () => { back(); document.body.classList.remove('printing'); redraw() });
  m.onclick = e => {
    const x = e.target.closest('[data-x]'); if (!x) return; m.hidden = true;
    if (x.dataset.x === 'pdf') { meta(); toEnd(); document.body.classList.add('printing'); redraw(); setTimeout(() => { document.title = 'IGMK - Statistiques ' + document.getElementById('rng').textContent.split(' · ')[0]; print() }, 250) }
    else {
      const rows = [...document.querySelectorAll('#tbl tr')].map(r => [...r.children].map(c => '"' + c.textContent.replace(/"/g, '""') + '"').join(';'));
      const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob(['﻿' + rows.join('\n')], { type: 'text/csv' })); a.download = 'igmk-statistiques.csv'; a.click();
    }
  };
})();
