// Pré-inscriptions reçues depuis le formulaire du site (démo, en mémoire)
(() => {
document.querySelectorAll('.drw,.dbg,.toast').forEach(x => document.body.appendChild(x));
const $ = s => document.querySelector(s), esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const NOW = new Date('2026-11-22T16:30:00');
const ST = { new: ['Nouvelle', 'vi'], called: ['Contactée', 'warn'], visit: ['Visite prévue', 'ok'], conv: ['Inscrite', 'ok'], lost: ['Sans suite', 'gr'] };
const h = n => new Date(NOW - n * 3600e3);
let n = 70;
const P = (prenom, nom, form, rent, tel, commune, age, niv, src, contact, moment, hAgo, st = 'new', x = {}) => ({ ref: 'PRE-2611-' + String(n--).padStart(4, '0'), prenom, nom, form, rent, tel, commune, age, niv, src, contact, moment, at: h(hAgo), st, notes: [], hist: [{ t: h(hAgo), m: 'Pré-inscription reçue via le site' }], ...x });
const L = [
  P('Aya Marie', 'Konan', 'Esthétique', 'Janvier 2027', '07 07 12 34 56', 'Yopougon', '18 – 25 ans', 'Débutante', 'TikTok', 'WhatsApp', 'Matin', 0.5),
  P('Fatoumata', 'Diallo', 'Coiffure', 'Janvier 2027', '05 44 21 09 87', 'Abobo', '18 – 25 ans', "J'ai quelques bases", 'TikTok', 'Appel téléphonique', 'Après-midi', 2),
  P('Mariam', 'Ouattara', 'Onglerie', 'Janvier 2027', '01 23 45 67 89', 'Cocody', '26 – 35 ans', 'Je travaille déjà dans la beauté', 'Instagram', 'WhatsApp', 'Peu importe', 5),
  P('Prisca', 'Yao', 'Maquillage', 'Je ne sais pas encore', '07 88 10 20 30', 'Marcory', '18 – 25 ans', 'Débutante', 'Facebook', 'WhatsApp', 'Après-midi', 9),
  P('Raïssa', 'Bamba', 'Esthétique', 'Avril 2027', '05 01 02 03 04', 'Yopougon', 'Moins de 18 ans', 'Débutante', 'Une ancienne élève', 'Appel téléphonique', 'Matin', 27),
  P('Clarisse', 'Aké', 'Coiffure', 'Janvier 2027', '07 55 66 77 88', 'Songon', '26 – 35 ans', "J'ai quelques bases", 'TikTok', 'WhatsApp', 'Matin', 31),
  P('Linda', 'Kouamé', 'Esthétique', 'Janvier 2027', '01 98 76 54 32', 'Attécoubé', '18 – 25 ans', 'Débutante', 'Bouche à oreille', 'WhatsApp', 'Peu importe', 20, 'called', { notes: [{ t: h(18), a: 'Mlle Gnamien', m: "Intéressée, attend l'accord de sa mère pour le paiement. Rappeler lundi." }] }),
  P('Sandrine', 'Gbagbo', 'Massage', 'Janvier 2027', '07 31 41 59 26', 'Treichville', 'Plus de 35 ans', 'Je travaille déjà dans la beauté', 'Facebook', 'Appel téléphonique', 'Après-midi', 46, 'visit', { visite: 'Mardi 24 nov. · 10 h', notes: [{ t: h(40), a: 'Mlle Gnamien', m: 'Visite fixée mardi 10 h. Viendra avec CNI et photos.' }] }),
  P('Awa', 'Touré', 'Coiffure', 'Janvier 2027', '05 27 18 28 18', 'Yopougon', '18 – 25 ans', 'Débutante', 'TikTok', 'WhatsApp', 'Matin', 70, 'visit', { visite: 'Lundi 23 nov. · 9 h' }),
  P('Nadège', 'Soro', 'Maquillage', 'Janvier 2027', '07 14 15 92 65', 'Adjamé', '26 – 35 ans', "J'ai quelques bases", 'Instagram', 'WhatsApp', 'Peu importe', 96, 'conv', { mat: 'IGMK-26-040' }),
  P('Corinne', 'Aka', 'Esthétique', 'Janvier 2027', '01 41 42 13 56', 'Yopougon', '18 – 25 ans', 'Débutante', 'TikTok', 'Appel téléphonique', 'Matin', 140, 'conv', { mat: 'IGMK-27-001' }),
  P('Josiane', 'Tanoh', 'Décoration', 'Avril 2027', '07 62 83 18 53', 'Bingerville', 'Plus de 35 ans', 'Débutante', 'Facebook', 'WhatsApp', 'Après-midi', 160, 'lost', { notes: [{ t: h(120), a: 'M. Gboze', m: 'Pas joignable après 3 relances.' }] }),
];
L.forEach(p => { if (p.st !== 'new') p.hist.push({ t: new Date(+p.at + 3 * 3600e3), m: 'Statut : ' + ST[p.st][0] }) });
const ago = d => { const m = Math.round((NOW - d) / 60000); return m < 60 ? `il y a ${m} min` : m < 1440 ? `il y a ${Math.round(m / 60)} h` : `il y a ${Math.round(m / 1440)} j` };
const fdt = d => d.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' }) + ' · ' + d.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
const late = p => p.st === 'new' && NOW - p.at > 24 * 3600e3;
const sla = p => { if (p.st !== 'new') return ''; const left = 24 - (NOW - p.at) / 3600e3; return left < 0 ? `<span class="sla bad">En retard de ${Math.round(-left)} h</span>` : `<span class="sla ${left < 6 ? 'warn' : ''}">À rappeler sous ${Math.max(1, Math.round(left))} h</span>` };
const wa = p => 'https://wa.me/225' + p.tel.replace(/\D/g, '') + '?text=' + encodeURIComponent(`Bonjour ${p.prenom.split(' ')[0]}, ici IGMK Formation. Merci pour votre pré-inscription en ${p.form} (dossier ${p.ref}). Quand pouvez-vous passer à l'école ?`);
let flt = 'todo', q = '', ff = '', cur = null;

function render() {
  const c = { todo: 0, all: L.length }; Object.keys(ST).forEach(k => c[k] = 0);
  L.forEach(p => { c[p.st]++; if (p.st === 'new' || p.st === 'called') c.todo++ });
  document.querySelectorAll('#pf .chip').forEach(b => { b.querySelector('em').textContent = c[b.dataset.f]; b.classList.toggle('on', b.dataset.f === flt) });
  $('#k1 b').textContent = c.new; $('#k2 b').textContent = L.filter(late).length;
  const conv = L.filter(p => p.st === 'conv').length; $('#k3 b').innerHTML = Math.round(conv / L.length * 100) + ' <small>%</small>';
  document.querySelectorAll('.side a[href="preinscriptions.html"] .n').forEach(x => x.textContent = c.new);
  const list = L.filter(p => (flt === 'all' || (flt === 'todo' ? p.st === 'new' || p.st === 'called' : p.st === flt)) && (!ff || p.form === ff) && (!q || (p.prenom + ' ' + p.nom + ' ' + p.tel + ' ' + p.ref).toLowerCase().includes(q)))
    .sort((a, b) => (late(b) - late(a)) || (b.at - a.at));
  $('#plist').innerHTML = list.length ? list.map(p => `<tr data-ref="${p.ref}" class="${late(p) ? 'late' : ''}${p.st === 'new' ? ' nw' : ''}" tabindex="0">
    <td><b class="nm">${esc(p.prenom)} ${esc(p.nom.toUpperCase())}</b><small class="mono">${p.ref}</small></td>
    <td><b>${p.form}</b><small>${p.rent}</small></td>
    <td><span class="tel">${p.tel}</span><small>${p.contact === 'WhatsApp' ? 'WhatsApp' : 'Appel'} · ${p.moment.toLowerCase()}</small></td>
    <td>${p.commune}<small>${p.src}</small></td>
    <td>${ago(p.at)}${sla(p) ? '<br>' + sla(p) : ''}</td>
    <td><span class="bd ${ST[p.st][1]}">${ST[p.st][0]}</span>${p.visite ? `<small>${p.visite}</small>` : p.mat ? `<small class="mono">${p.mat}</small>` : ''}</td>
    <td class="act"><a class="ib wa" href="${wa(p)}" target="_blank" title="Écrire sur WhatsApp" data-stop><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/></svg></a><a class="ib" href="tel:+225${p.tel.replace(/\D/g, '')}" title="Appeler" data-stop><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg></a></td></tr>`).join('')
    : `<tr><td colspan="7" class="empty">Aucune pré-inscription ${flt === 'todo' ? 'à traiter' : 'dans cette catégorie'}.</td></tr>`;
}
document.querySelectorAll('#pf .chip').forEach(b => b.onclick = () => { flt = b.dataset.f; render() });
$('#pq').oninput = e => { q = e.target.value.trim().toLowerCase(); render() };
$('#pform').onchange = e => { ff = e.target.value; render() };
$('#plist').addEventListener('click', e => { if (e.target.closest('[data-stop]')) { const p = L.find(x => x.ref === e.target.closest('tr').dataset.ref); log(p, e.target.closest('.wa') ? 'Message WhatsApp envoyé' : 'Appel passé'); return } const r = e.target.closest('tr[data-ref]'); if (r) open(r.dataset.ref) });
$('#plist').addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.dataset.ref) open(e.target.dataset.ref) });
function log(p, m) { p.hist.push({ t: new Date(), m }); if (p.st === 'new') { p.st = 'called'; p.hist.push({ t: new Date(), m: 'Statut : Contactée' }) } render(); if (cur === p) drawer() }

// ---------- panneau de détail ----------
function open(ref) { cur = L.find(p => p.ref === ref); drawer(); $('.drw').classList.add('on'); $('.dbg').classList.add('on') }
function shut() { $('.drw').classList.remove('on'); $('.dbg').classList.remove('on'); cur = null }
function drawer() {
  const p = cur;
  $('.drw').innerHTML = `<div class="dh"><div><small class="mono">${p.ref}</small><h3>${esc(p.prenom)} ${esc(p.nom)}</h3><span class="bd ${ST[p.st][1]}">${ST[p.st][0]}</span> ${sla(p)}</div><button class="x" data-x>×</button></div>
  <div class="db">
   <div class="qa"><a class="btn wa" href="${wa(p)}" target="_blank" data-log="Message WhatsApp envoyé"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/></svg> WhatsApp</a><a class="btn" href="tel:+225${p.tel.replace(/\D/g, '')}" data-log="Appel passé"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg> Appeler</a></div>
   <dl class="dkv"><dt>Formation</dt><dd><b>${p.form}</b></dd><dt>Rentrée</dt><dd>${p.rent}</dd><dt>WhatsApp</dt><dd>+225 ${p.tel}</dd><dt>Préfère</dt><dd>${p.contact} · ${p.moment}</dd><dt>Commune</dt><dd>${p.commune}</dd><dt>Âge</dt><dd>${p.age}</dd><dt>Expérience</dt><dd>${p.niv}</dd><dt>Source</dt><dd>${p.src}</dd><dt>Reçue le</dt><dd>${fdt(p.at)}</dd>${p.visite ? `<dt>Visite</dt><dd><b>${p.visite}</b></dd>` : ''}${p.mat ? `<dt>Matricule</dt><dd class="mono">${p.mat}</dd>` : ''}</dl>
   <h5 class="fs">Statut</h5><div class="stb">${Object.entries(ST).filter(([k]) => k !== 'conv').map(([k, [t]]) => `<button data-st="${k}" class="${p.st === k ? 'on' : ''}"${p.st === 'conv' ? ' disabled' : ''}>${t}</button>`).join('')}</div>
   <div id="vis" ${p.st === 'visit' && !p.visite ? '' : 'hidden'} class="vis"><input type="datetime-local" class="inp" id="vdt" value="2026-11-24T10:00"><button class="btn sm" id="vok">Fixer la visite</button><small class="hint">Un rappel WhatsApp est envoyé la veille.</small></div>
   <h5 class="fs">Notes</h5><div class="notes">${p.notes.map(n => `<div class="note"><b>${esc(n.a)}</b><small>${fdt(n.t)}</small><p>${esc(n.m)}</p></div>`).join('') || '<p class="hint" style="margin:0 0 10px">Aucune note pour le moment.</p>'}</div>
   <div class="nadd"><textarea class="inp" id="nt" rows="2" placeholder="Ajouter une note (ex. rappeler lundi, a des questions sur le prix…)"></textarea><button class="btn sm" id="nok">Ajouter</button></div>
   <h5 class="fs">Historique</h5><ol class="hist">${p.hist.slice().reverse().map(x => `<li><small>${fdt(x.t)}</small>${esc(x.m)}</li>`).join('')}</ol>
  </div>
  <div class="df">${p.st === 'conv' ? `<span class="hint" style="margin:0">Inscription créée · <b class="mono">${p.mat}</b></span><a class="btn" href="inscriptions.html">Voir le dossier →</a>` : `<button class="btn lost" data-st="lost"${p.st === 'lost' ? ' disabled' : ''}>Sans suite</button><button class="btn p" id="conv">Convertir en inscription →</button>`}</div>`;
  const D = $('.drw');
  D.querySelector('[data-x]').onclick = shut;
  D.querySelectorAll('[data-log]').forEach(a => a.onclick = () => log(p, a.dataset.log));
  D.querySelectorAll('[data-st]').forEach(b => b.onclick = () => { if (b.dataset.st === 'visit') { setSt(p, 'visit'); $('#vis').hidden = false; return } setSt(p, b.dataset.st) });
  D.querySelector('#vok').onclick = () => { const d = new Date($('#vdt').value); p.visite = d.toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'short' }) + ' · ' + d.getHours() + ' h'; p.hist.push({ t: new Date(), m: 'Visite fixée : ' + p.visite }); render(); drawer(); toast('Visite fixée. Rappel WhatsApp programmé la veille.') };
  D.querySelector('#nok').onclick = () => { const v = $('#nt').value.trim(); if (!v) return $('#nt').focus(); p.notes.push({ t: new Date(), a: "K. N'Si Batiye", m: v }); drawer(); toast('Note ajoutée.') };
  const cv = D.querySelector('#conv'); if (cv) cv.onclick = () => { p.st = 'conv'; p.mat = 'IGMK-27-0' + (10 + Math.floor(Math.random() * 80)); p.hist.push({ t: new Date(), m: 'Convertie en inscription · ' + p.mat }); render(); drawer(); toast(`${p.prenom.split(' ')[0]} est passée dans Inscriptions (étape « Dossier en cours »). Ses informations sont déjà remplies.`) };
}
function setSt(p, s) { if (p.st === s) return; p.st = s; if (s !== 'visit') delete p.visite; p.hist.push({ t: new Date(), m: 'Statut : ' + ST[s][0] }); render(); drawer() }
$('.dbg').onclick = shut; document.addEventListener('keydown', e => e.key === 'Escape' && shut());

let tt; function toast(m) { const t = $('#toast'); t.innerHTML = '<span>✓</span>' + esc(m); t.classList.add('on'); clearTimeout(tt); tt = setTimeout(() => t.classList.remove('on'), 4500) }
render();
})();
