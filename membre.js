// Fiche d'un membre du personnel : présence calculée à partir de l'emploi du temps et des absences (démo)
(() => {
document.querySelectorAll('.mbg,.toast').forEach(x => document.body.appendChild(x));
const $ = s => document.querySelector(s), esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
// emploi du temps type de Mme Kouassi (jour de semaine 1 = lundi)
const EDT = { 1: [['08:00', '10:00', 'Soins visage', 'Esth. A'], ['13:00', '15:00', 'Cosmétologie', 'Esth. B']], 2: [['08:00', '12:00', 'Épilation', 'Esth. A']], 3: [['08:00', '10:00', 'Soins visage', 'Esth. B'], ['10:30', '12:30', 'Soins corps', 'Esth. A']], 4: [['08:00', '12:00', 'Manucure', 'Esth. A']], 5: [['08:00', '10:00', 'Évaluation pratique', 'Esth. A'], ['13:00', '15:00', 'Atelier libre', 'Esth. B']] };
const dur = ([a, b]) => { const m = s => +s.slice(0, 2) * 60 + +s.slice(3); return (m(b) - m(a)) / 60 };
const MON = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
const TYPES = { just: ['Justifiée', 'ok'], nonj: ['Non justifiée', 'bad'], remp: ['Remplacée', 'warn'] };
const key = d => d.toISOString().slice(0, 10);
// absences connues (date, index des créneaux, type, motif, remplaçant, justificatif)
const ABS = [
  { d: '2026-11-04', s: [0, 1], t: 'just', m: 'Maladie', r: '', j: 'certificat-medical.pdf' },
  { d: '2026-11-12', s: [0], t: 'nonj', m: 'Retard non prévenu — cours non assuré', r: '', j: '' },
  { d: '2026-11-17', s: [0, 1], t: 'remp', m: 'Rendez-vous administratif', r: 'M. Bamba Ismaël', j: '' },
  { d: '2026-10-08', s: [0, 1], t: 'just', m: 'Formation externe (L\'Oréal)', r: '', j: 'attestation.pdf' },
  { d: '2026-10-21', s: [0], t: 'nonj', m: 'Absence non signalée', r: '', j: '' },
];
let Y = 2026, M = 10; // novembre (0-index)
const TODAY = new Date('2026-11-22');

function stats(y, m) {
  let prevu = 0, just = 0, nonj = 0, remp = 0; const days = [];
  const last = new Date(y, m + 1, 0).getDate();
  for (let d = 1; d <= last; d++) {
    const dt = new Date(Date.UTC(y, m, d)), wd = dt.getUTCDay(), sl = EDT[wd] || [], k = key(dt), past = dt <= TODAY;
    const a = ABS.find(x => x.d === k); let st = sl.length ? (past ? 'ok' : 'fut') : 'off', h = 0;
    sl.forEach((s, i) => { if (!past) return; prevu += dur(s); if (a && a.s.includes(i)) { h += dur(s); if (a.t === 'just') just += dur(s); else if (a.t === 'nonj') nonj += dur(s); else remp += dur(s) } });
    if (a) st = past ? a.t : 'plan';
    days.push({ d, wd, st, k, h, sl });
  }
  const base = prevu - just, eff = base - nonj - remp;
  return { prevu, just, nonj, remp, base, eff, taux: base ? eff / base * 100 : 100, days };
}
const f1 = v => (Math.round(v * 10) / 10).toString().replace('.', ',');

function render() {
  const s = stats(Y, M);
  $('#pmon').textContent = MON[M] + ' ' + Y;
  $('#kp1').textContent = f1(s.prevu) + ' h'; $('#kp2').textContent = f1(s.just) + ' h'; $('#kp3').textContent = f1(s.nonj + s.remp) + ' h'; $('#kp4').textContent = Math.round(s.taux) + ' %';
  $('#kp4').closest('.kpi').querySelector('em').className = s.taux >= 95 ? 'up' : s.taux >= 90 ? '' : 'down';
  $('#kp4').closest('.kpi').querySelector('em').textContent = s.taux >= 95 ? 'Très bon' : s.taux >= 90 ? 'Correct' : 'À surveiller';
  $('#hero-pres').textContent = Math.round(s.taux) + '%'; if (Y === 2026 && M === 10) { document.querySelector('.pr-mini').textContent = Math.round(s.taux) + ' %'; document.querySelector('.ab-mini').textContent = ABS.filter(a => a.d.startsWith('2026-11')).length; document.querySelector('.rp-mini').textContent = ABS.filter(a => a.d.startsWith('2026-11') && a.t === 'remp').length }
  $('#formula').innerHTML = `<div class="fx"><span><b>${f1(s.prevu)} h</b><small>prévues</small></span><i>−</i><span><b>${f1(s.just)} h</b><small>justifiées</small></span><i>=</i><span class="base"><b>${f1(s.base)} h</b><small>base de calcul</small></span></div>
   <div class="fx"><span class="base"><b>${f1(s.base)} h</b><small>base</small></span><i>−</i><span><b>${f1(s.nonj)} h</b><small>non justifiées</small></span><i>−</i><span><b>${f1(s.remp)} h</b><small>remplacées</small></span><i>=</i><span><b>${f1(s.eff)} h</b><small>effectuées</small></span></div>
   <div class="fx res"><span><b>${f1(s.eff)} ÷ ${f1(s.base)}</b></span><i>=</i><span class="tot"><b>${Math.round(s.taux)} %</b><small>de présence</small></span></div>`;
  // calendrier
  const first = (new Date(Date.UTC(Y, M, 1)).getUTCDay() + 6) % 7;
  $('#cal').innerHTML = ['L', 'M', 'M', 'J', 'V', 'S', 'D'].map(x => `<b>${x}</b>`).join('') + '<span></span>'.repeat(first) + s.days.map(x => `<span class="c ${x.st}" title="${x.sl.length ? x.sl.length + ' cours · ' + f1(x.sl.reduce((a, b) => a + dur(b), 0)) + ' h' : 'Pas de cours'}${x.h ? ' — ' + f1(x.h) + ' h d\'absence' : ''}">${x.d}</span>`).join('');
  // liste
  const list = ABS.filter(a => a.d.startsWith(`${Y}-${String(M + 1).padStart(2, '0')}`)).sort((a, b) => b.d.localeCompare(a.d));
  $('#alist').innerHTML = list.length ? list.map(a => { const dt = new Date(a.d + 'T00:00:00Z'), sl = EDT[dt.getUTCDay()] || [], h = a.s.reduce((t, i) => t + (sl[i] ? dur(sl[i]) : 0), 0);
    return `<tr><td><b>${dt.toLocaleDateString('fr-FR', { weekday: 'short', day: 'numeric', month: 'short', timeZone: 'UTC' })}</b><small>${a.s.map(i => sl[i] ? sl[i][0] + '–' + sl[i][1] + ' · ' + sl[i][2] : '').join('<br>')}</small></td><td>${f1(h)} h</td><td><span class="bd ${TYPES[a.t][1]}">${TYPES[a.t][0]}</span></td><td>${esc(a.m)}${a.r ? `<small>Remplacée par ${esc(a.r)}</small>` : ''}</td><td>${a.j ? `<a href="#">${esc(a.j)}</a>` : a.t === 'nonj' ? '<a href="#" class="muted">+ Ajouter</a>' : '—'}</td></tr>` }).join('')
    : '<tr><td colspan="5" class="empty">Aucune absence ce mois-ci.</td></tr>';
  // tendance 6 mois
  const tr = []; for (let k = 5; k >= 0; k--) { const d = new Date(2026, 10 - k, 1); tr.push({ l: MON[d.getMonth()].slice(0, 4) + '.', v: stats(d.getFullYear(), d.getMonth()).taux }) }
  $('#trend').innerHTML = tr.map(t => `<div class="tb${t.l.startsWith(MON[M].slice(0, 4)) ? ' on' : ''}"><em>${Math.round(t.v)}%</em><i style="height:${Math.max(4, (t.v - 70) / 30 * 100)}%"></i><small>${t.l}</small></div>`).join('');
}
$('#pprev').onclick = () => { M--; if (M < 0) { M = 11; Y-- } render() };
$('#pnext').onclick = () => { if (Y === 2026 && M === 10) return; M++; if (M > 11) { M = 0; Y++ } render() };

// ---------- onglets ----------
const go = k => { document.querySelectorAll('.mtabs a').forEach(a => a.classList.toggle('on', a.dataset.t === k)); document.querySelectorAll('.mt').forEach(s => s.hidden = s.id !== 't-' + k) };
document.querySelectorAll('.mtabs a').forEach(a => a.onclick = e => { e.preventDefault(); go(a.dataset.t); history.replaceState(0, '', '#' + a.dataset.t) });
if (location.hash) go(location.hash.slice(1));
document.querySelectorAll('[data-go]').forEach(a => a.onclick = e => { e.preventDefault(); go(a.dataset.go); scrollTo({ top: 0, behavior: 'smooth' }) });

// ---------- déclarer une absence ----------
const A = $('#mabs'), af = A.querySelector('form');
const slots = () => { const d = new Date(af.elements.date.value + 'T00:00:00Z'), sl = EDT[d.getUTCDay()] || [];
  $('#aslots').innerHTML = sl.length ? sl.map((s, i) => `<label class="slot"><input type="checkbox" name="s" value="${i}" checked><span><b>${s[0]} – ${s[1]}</b> ${s[2]} <small>${s[3]} · ${f1(dur(s))} h</small></span></label>`).join('') : '<p class="hint" style="margin:0">Aucun cours prévu ce jour-là dans l\'emploi du temps.</p>'; hrs() };
const hrs = () => { const d = new Date(af.elements.date.value + 'T00:00:00Z'), sl = EDT[d.getUTCDay()] || []; const h = [...af.querySelectorAll('[name=s]:checked')].reduce((t, c) => t + dur(sl[c.value]), 0); $('#ahrs').textContent = f1(h) + ' h de cours concernées'; $('#arep').hidden = af.elements.t.value !== 'remp'; $('#ajus').hidden = af.elements.t.value !== 'just' };
af.addEventListener('change', e => { if (e.target.name === 'date') slots(); else hrs() });
document.querySelectorAll('[data-abs]').forEach(b => b.onclick = e => { e.preventDefault(); af.reset(); af.elements.date.value = '2026-11-23'; slots(); A.classList.add('on') });
A.querySelectorAll('[data-close]').forEach(b => b.onclick = () => A.classList.remove('on'));
A.onclick = e => { if (e.target === A) A.classList.remove('on') };
af.onsubmit = e => { e.preventDefault(); const s = [...af.querySelectorAll('[name=s]:checked')].map(c => +c.value); if (!s.length) return toast('Sélectionnez au moins un cours.');
  const d = af.elements.date.value; ABS.push({ d, s, t: af.elements.t.value, m: af.elements.m.value || 'Non précisé', r: af.elements.t.value === 'remp' ? af.elements.r.value : '', j: af.elements.j.files[0]?.name || '' });
  A.classList.remove('on'); const dt = new Date(d); Y = dt.getFullYear(); M = dt.getMonth(); go('pres'); render();
  toast(new Date(d) > TODAY ? 'Absence planifiée. Elle sera comptée le jour venu ; les élèves seront prévenus par WhatsApp.' : 'Absence enregistrée. Le taux de présence a été recalculé.') };

let tt; function toast(m) { const t = $('#toast'); t.innerHTML = '<span>✓</span>' + esc(m); t.classList.add('on'); clearTimeout(tt); tt = setTimeout(() => t.classList.remove('on'), 4500) }
render();
})();
