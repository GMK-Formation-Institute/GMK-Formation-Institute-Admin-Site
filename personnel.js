// Personnel : liste, ajout, modification, activation / désactivation, suppression (démo, en mémoire)
(() => {
document.querySelectorAll('.mbg,.toast').forEach(x => document.body.appendChild(x));
const $ = s => document.querySelector(s), esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
let id = 0;
const M = (civ, prenom, nom, poste, dep, contrat, photo, x = {}) => ({ id: ++id, civ, prenom, nom, poste, dep, contrat, photo, actif: true, tel: '', email: '', entree: '2019-09-02', taux: 6000, specs: [], acces: false, role: '', eleves: 0, heures: 0, presence: 98, ...x });
const S = [
  M('M.', "K. N'Si", 'Batiye', 'Directeur général', 'Direction', 'CDI', 'img/about/BATIYE.jpg', { tel: '07 07 58 90 81', email: 'direction@igmk-formation.net', entree: '2012-01-09', acces: true, role: 'Administrateur', presence: 97 }),
  M('Dr', 'Moucaïla', 'Adegoke', 'Directeur des études', 'Direction', 'CDI', 'img/about/ADEGOKE.jpg', { tel: '01 02 93 92 21', email: 'etudes@igmk-formation.net', entree: '2014-09-01', acces: true, role: 'Pédagogie', presence: 100 }),
  M('Dr', 'Jean-Claude', 'Gboze', 'Directeur commercial', 'Direction', 'CDI', 'img/about/GBOZE.jpg', { tel: '07 48 22 10 05', entree: '2016-03-01', acces: true, role: 'Inscriptions', presence: 95 }),
  M('Mme', 'Hortense', 'Kouassi', 'Formatrice Esthétique', 'Formation', 'CDI', 'img/instructor/002.jpg', { tel: '05 66 12 30 44', specs: ['Esthétique', 'Soins visage'], eleves: 62, heures: 24, presence: 92 }),
  M('M.', 'Ismaël', 'Bamba', 'Formateur Coiffure', 'Formation', 'CDI', 'img/instructor/010.jpg', { tel: '07 59 01 77 21', specs: ['Coiffure', 'Tresses'], eleves: 58, heures: 22 }),
  M('Mme', 'Ange', 'Kouakou', 'Formatrice Maquillage', 'Formation', 'Vacataire', 'img/about/KOUAKOU.jpg', { tel: '01 40 55 62 18', specs: ['Maquillage'], eleves: 24, heures: 8, presence: 100 }),
  M('M.', 'Salif', 'Traoré', 'Formateur Décoration', 'Formation', 'Vacataire', 'img/instructor/decoration1.jpg', { tel: '07 22 81 09 33', specs: ['Décoration'], eleves: 12, heures: 6, presence: 90 }),
  M('Mme', 'Bernadette', 'Yao', 'Formatrice Onglerie', 'Formation', 'Vacataire', '', { tel: '05 04 77 18 62', specs: ['Onglerie'], eleves: 20, heures: 8, presence: 96 }),
  M('Mlle', 'Esther', 'Gnamien', 'Secrétaire — Accueil', 'Administration', 'CDI', '', { tel: '07 10 33 45 90', acces: true, role: 'Secrétariat', presence: 99 }),
  M('M.', 'Moussa', 'Coulibaly', 'Comptable', 'Administration', 'CDD', '', { tel: '01 71 26 04 58', acces: true, role: 'Comptabilité', presence: 100 }),
  M('Mme', 'Awa', 'Diomandé', 'Formatrice Massage', 'Formation', 'Vacataire', '', { tel: '07 87 14 52 03', specs: ['Massage'], actif: false, entree: '2021-02-01', presence: 0 }),
];
const full = m => `${m.civ} ${m.prenom} ${m.nom}`, ini = m => (m.prenom.replace(/^K\. /, '')[0] + m.nom[0]).toUpperCase();
const DEPC = { Direction: 'vi', Formation: 'ok', Administration: 'gr' };
let flt = 'all';

// ---------- liste ----------
function render() {
  const act = S.filter(m => m.actif), cnt = { all: act.length, Direction: 0, Formation: 0, Administration: 0, off: S.length - act.length };
  act.forEach(m => cnt[m.dep]++);
  document.querySelectorAll('#sf .chip').forEach(c => { c.querySelector('em').textContent = cnt[c.dataset.f]; c.classList.toggle('on', c.dataset.f === flt) });
  $('#scount').textContent = '· ' + act.length;
  const list = S.filter(m => flt === 'off' ? !m.actif : m.actif && (flt === 'all' || m.dep === flt));
  $('#staff').innerHTML = list.length ? list.map(m => `<div class="card staff${m.actif ? '' : ' off'}" data-id="${m.id}">
    <button class="more" aria-label="Actions pour ${esc(full(m))}" data-menu="${m.id}">⋯</button>
    ${m.photo ? `<img src="${esc(m.photo)}" alt="">` : `<span class="ini">${ini(m)}</span>`}
    <h4><a href="membre.html">${esc(full(m))}</a></h4><p>${esc(m.poste)}</p>
    <div class="row"><span class="bd ${DEPC[m.dep]}">${m.dep}</span><span class="bd gr">${m.contrat}</span>${m.actif ? '' : '<span class="bd bad">Inactif</span>'}${m.acces ? `<span class="bd gr" title="Accès à l'espace de gestion : ${esc(m.role)}">Accès : ${esc(m.role)}</span>` : ''}</div>
    <div class="st"><div><b>${m.eleves || '—'}</b><small>Élèves</small></div><div><b>${m.heures || '—'}</b><small>H / sem.</small></div><div><b>${m.actif ? m.presence + '%' : '—'}</b><small>Présence</small></div></div>
    ${m.actif ? '' : `<button class="btn reac" data-act="toggle" data-id="${m.id}">Réactiver</button>`}</div>`).join('')
    : `<div class="empty">${flt === 'off' ? 'Aucun membre inactif.' : 'Aucun membre dans cette catégorie.'}</div>`;
}
document.querySelectorAll('#sf .chip').forEach(c => c.onclick = () => { flt = c.dataset.f; render() });

// ---------- menu d'actions ----------
const menu = document.createElement('div'); menu.className = 'amenu'; menu.hidden = true; document.body.appendChild(menu); addEventListener('scroll', () => menu.hidden = true, true);
document.addEventListener('click', e => {
  const b = e.target.closest('[data-menu]');
  if (b) {
    e.stopPropagation(); const m = S.find(x => x.id == b.dataset.menu), r = b.getBoundingClientRect();
    menu.innerHTML = `<button onclick="location.href='membre.html'">Voir la fiche</button><button data-act="edit" data-id="${m.id}">Modifier les informations</button><button data-act="toggle" data-id="${m.id}">${m.actif ? 'Désactiver' : 'Réactiver'}</button><hr><button class="del" data-act="del" data-id="${m.id}">Supprimer</button>`;
    menu.hidden = false; const below = innerHeight - r.bottom > 170; menu.style.top = (below ? r.bottom + 6 : r.top - 6 - menu.offsetHeight) + 'px'; menu.style.left = Math.max(8, r.right - 230) + 'px'; return;
  }
  const a = e.target.closest('[data-act]');
  menu.hidden = true;
  if (!a) return;
  const m = S.find(x => x.id == a.dataset.id);
  if (a.dataset.act === 'edit') openForm(m);
  if (a.dataset.act === 'toggle') toggle(m);
  if (a.dataset.act === 'del') askDel(m);
});

// ---------- activer / désactiver ----------
function toggle(m) {
  if (m.actif) return confirmBox({ title: 'Désactiver ce membre ?', who: m,
    body: `<p>${esc(full(m))} n'apparaîtra plus dans les plannings ni dans les listes de formateurs${m.acces ? ', et <b>son accès à l\'espace de gestion sera suspendu</b>' : ''}. Son historique (cours, paiements, présences) est conservé.</p>${m.eleves ? `<div class="info warn">${m.eleves} élèves et ${m.heures} h de cours par semaine lui sont attribués : pensez à les réaffecter dans l'emploi du temps.</div>` : ''}
    <div class="fld" style="margin-top:14px"><label>Motif (facultatif)</label><select class="inp"><option>Fin de contrat</option><option>Congé longue durée</option><option>Démission</option><option>Autre</option></select></div>`,
    ok: 'Désactiver', cls: 'warn', run: () => { m.actif = false; render(); toast(`${full(m)} a été désactivé(e).`, () => { m.actif = true; render() }) } });
  m.actif = true; render(); toast(`${full(m)} est de nouveau actif(ve).`);
}

// ---------- suppression ----------
function askDel(m) {
  const linked = m.eleves || m.heures;
  confirmBox({ title: 'Supprimer définitivement ?', who: m,
    body: `<p>La fiche de <b>${esc(full(m))}</b> sera supprimée. Cette action est <b>irréversible</b>.</p>
    ${linked ? `<div class="info warn">Ce membre a un historique (cours, présences${m.contrat === 'Vacataire' ? ', vacations' : ''}). <b>Nous recommandons plutôt de le désactiver</b> : l'historique reste consultable.</div>` : ''}
    <div class="fld" style="margin-top:14px"><label>Pour confirmer, tapez <b>SUPPRIMER</b></label><input class="inp" id="delc" autocomplete="off"></div>`,
    ok: 'Supprimer', cls: 'danger', alt: m.actif && linked ? { t: 'Désactiver à la place', run: () => { m.actif = false; render(); toast(`${full(m)} a été désactivé(e).`) } } : null,
    check: () => $('#delc').value.trim().toUpperCase() === 'SUPPRIMER',
    run: () => { const i = S.indexOf(m); S.splice(i, 1); render(); toast(`La fiche de ${full(m)} a été supprimée.`, () => { S.splice(i, 0, m); render() }) } });
}

// ---------- boîte de confirmation ----------
function confirmBox({ title, who, body, ok, cls, run, check, alt }) {
  $('#cfm').innerHTML = `<div class="modal sm"><div class="mh"><div><small>Personnel</small><h3>${title}</h3></div><button class="x" data-close>×</button></div>
  <div class="mb"><div class="pick">${who.photo ? `<img src="${esc(who.photo)}" alt="">` : `<span class="ini">${ini(who)}</span>`}<div><b>${esc(full(who))}</b><small>${esc(who.poste)} · ${who.contrat}</small></div></div>${body}</div>
  <div class="mf">${alt ? `<button class="btn" data-alt>${alt.t}</button>` : '<span></span>'}<div class="row"><button class="btn" data-close>Annuler</button><button class="btn ${cls}" data-ok${check ? ' disabled' : ''}>${ok}</button></div></div></div>`;
  const box = $('#cfm'), okb = box.querySelector('[data-ok]'); box.classList.add('on');
  if (check) box.querySelector('input').oninput = () => okb.disabled = !check();
  okb.onclick = () => { close(box); run() };
  if (alt) box.querySelector('[data-alt]').onclick = () => { close(box); alt.run() };
  box.querySelectorAll('[data-close]').forEach(b => b.onclick = () => close(box));
  setTimeout(() => (box.querySelector('input') || okb).focus(), 50);
}
const close = b => b.classList.remove('on');
document.querySelectorAll('.mbg').forEach(b => b.addEventListener('click', e => { if (e.target === b) close(b) }));
document.addEventListener('keydown', e => { if (e.key === 'Escape') document.querySelectorAll('.mbg.on').forEach(close) });

// ---------- formulaire ajout / modification ----------
const F = $('#mform'), fm = F.querySelector('form');
let editing = null, photo = '';
function openForm(m) {
  editing = m || null; photo = m ? m.photo : '';
  F.querySelector('.mh small').textContent = m ? 'Modifier' : 'Nouveau membre';
  F.querySelector('.mh h3').textContent = m ? full(m) : 'Ajouter un membre';
  F.querySelector('[type=submit]').textContent = m ? 'Enregistrer les modifications' : 'Ajouter le membre';
  fm.reset(); fm.querySelectorAll('.bad').forEach(x => x.classList.remove('bad'));
  const d = m || { civ: 'Mme', dep: 'Formation', contrat: 'CDI', entree: new Date().toISOString().slice(0, 10), taux: 6000, specs: [], acces: false, role: 'Secrétariat', actif: true };
  ['civ', 'prenom', 'nom', 'poste', 'dep', 'contrat', 'entree', 'tel', 'email', 'taux', 'role'].forEach(k => { if (fm.elements[k]) fm.elements[k].value = d[k] ?? '' });
  fm.elements.acces.checked = !!d.acces; fm.elements.actif.checked = d.actif !== false;
  fm.querySelectorAll('[name=specs]').forEach(c => c.checked = (d.specs || []).includes(c.value));
  setPhoto(); sync(); F.classList.add('on'); setTimeout(() => fm.elements.prenom.focus(), 60);
}
function setPhoto() { const p = $('#fph'); p.innerHTML = photo ? `<img src="${esc(photo)}" alt="">` : '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>'; $('#fphr').hidden = !photo }
$('#fphi').onchange = e => { const f = e.target.files[0]; if (!f) return; const r = new FileReader(); r.onload = () => { photo = r.result; setPhoto() }; r.readAsDataURL(f) };
$('#fphr').onclick = () => { photo = ''; setPhoto() };
function sync() {
  const v = fm.elements.contrat.value === 'Vacataire', f = fm.elements.dep.value === 'Formation', a = fm.elements.acces.checked;
  $('#ftaux').hidden = !v; $('#fspecs').hidden = !f; $('#frole').hidden = !a;
}
fm.addEventListener('change', sync);
fm.elements.tel.addEventListener('input', e => { const d = e.target.value.replace(/\D/g, '').slice(0, 10); e.target.value = d.replace(/(\d{2})(?=\d)/g, '$1 ') });
fm.addEventListener('input', e => { const x = e.target.closest('.fld'); if (x) x.classList.remove('bad') });
fm.onsubmit = e => {
  e.preventDefault(); let ok = true;
  const need = (n, test = v => v.trim()) => { const el = fm.elements[n]; const b = !test(el.value); el.closest('.fld').classList.toggle('bad', b); if (b && ok) { el.focus(); ok = false } };
  need('prenom'); need('nom'); need('poste'); need('tel', v => v.replace(/\D/g, '').length === 10);
  if (fm.elements.email.value) need('email', v => /^\S+@\S+\.\S+$/.test(v));
  if (!ok) return;
  const d = Object.fromEntries(['civ', 'prenom', 'nom', 'poste', 'dep', 'contrat', 'entree', 'tel', 'email', 'role'].map(k => [k, fm.elements[k].value.trim()]));
  d.taux = +fm.elements.taux.value || 0; d.acces = fm.elements.acces.checked; d.actif = fm.elements.actif.checked; d.photo = photo;
  d.specs = [...fm.querySelectorAll('[name=specs]:checked')].map(c => c.value);
  if (editing) { Object.assign(editing, d); toast('Les informations de ' + full(editing) + ' ont été mises à jour.') }
  else { const m = M(d.civ, d.prenom, d.nom, d.poste, d.dep, d.contrat, d.photo, d); S.push(m); flt = m.actif ? 'all' : 'off'; toast(full(m) + ' a été ajouté(e) à l\'équipe.' + (d.acces ? ' Une invitation de connexion lui a été envoyée.' : '')) }
  close(F); render();
  const card = document.querySelector(`[data-id="${editing ? editing.id : S[S.length - 1].id}"].staff`); if (card) { card.scrollIntoView({ behavior: 'smooth', block: 'center' }); card.classList.add('flash') }
};
F.querySelectorAll('[data-close]').forEach(b => b.onclick = () => close(F));
$('#addm').onclick = e => { e.preventDefault(); openForm() };

// ---------- notifications ----------
let tt;
function toast(msg, undo) {
  const t = $('#toast'); t.innerHTML = `<span>✓</span>${esc(msg)}${undo ? '<button>Annuler</button>' : ''}`; t.classList.add('on');
  if (undo) t.querySelector('button').onclick = () => { undo(); t.classList.remove('on'); };
  clearTimeout(tt); tt = setTimeout(() => t.classList.remove('on'), undo ? 6000 : 3500);
}
render();
})();
