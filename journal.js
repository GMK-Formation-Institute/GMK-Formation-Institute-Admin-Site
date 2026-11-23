// Journal d'activité : toutes les actions faites dans l'espace de gestion (démo)
(() => {
const $ = s => document.querySelector(s), esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const U = { bat: ["K. N'Si Batiye", 'Administrateur', 'KB'], ade: ['Dr Adegoke', 'Pédagogie', 'MA'], gbo: ['Dr Gboze', 'Inscriptions', 'JG'], gna: ['Mlle Gnamien', 'Secrétariat', 'EG'], cou: ['M. Coulibaly', 'Comptabilité', 'MC'], kou: ['Mme Kouassi', 'Formateur', 'HK'], bam: ['M. Bamba', 'Formateur', 'IB'], sys: ['Système', 'Automatique', 'SY'] };
const T = { create: ['Création', 'ok', '+'], update: ['Modification', 'vi', '~'], delete: ['Suppression', 'bad', '×'], login: ['Connexion', 'gr', '→'], pay: ['Paiement', 'ok', 'F'], export: ['Export', 'gr', '⤓'], sec: ['Sécurité', 'bad', '!'], send: ['Envoi', 'gr', '↗'] };
const NOW = new Date('2026-11-22T16:30:00');
const t = (d, h, m) => new Date(2026, 10, d, h, m);
let i = 0;
const E = (at, u, ty, mod, txt, obj, x = {}) => ({ id: 'EV-' + String(48210 - i++), at, u, ty, mod, txt, obj, ip: x.ip || '102.67.' + (12 + i % 40) + '.' + (100 + i % 90), dev: x.dev || (u === 'kou' || u === 'bam' ? 'Android · Chrome' : 'Windows · Chrome'), diff: x.diff, ...x });
const L = [
  E(t(22, 16, 12), 'cou', 'pay', 'Paiements', 'a encaissé un paiement de 150 000 F', 'Aya Konan · REC-2611-0417', { diff: [['Mode', '', 'Orange Money'], ['Référence', '', 'MP261122.1612'], ['Solde restant', '410 000 F', '260 000 F']] }),
  E(t(22, 15, 40), 'gna', 'update', 'Pré-inscriptions', 'a changé le statut d\'une pré-inscription', 'Linda Kouamé · PRE-2611-0064', { diff: [['Statut', 'Nouvelle', 'Contactée']] }),
  E(t(22, 15, 2), 'sys', 'send', 'Notifications', 'a envoyé 14 rappels d\'échéance par WhatsApp', 'Mensualité de décembre'),
  E(t(22, 14, 48), 'bat', 'update', 'Personnel', 'a modifié la fiche d\'un membre', 'Mme Hortense Kouassi', { diff: [['Poste', 'Formatrice Esthétique', 'Formatrice principale Esthétique']] }),
  E(t(22, 14, 31), 'bat', 'export', 'Statistiques', 'a exporté le rapport statistique (PDF)', 'déc. 25 → nov. 26'),
  E(t(22, 11, 20), 'gna', 'create', 'Inscriptions', 'a converti une pré-inscription en inscription', 'Corinne Aka · IGMK-27-001'),
  E(t(22, 10, 31), 'cou', 'pay', 'Paiements', 'a encaissé un paiement en espèces de 85 000 F', 'Grâce Amani · R-26-1183'),
  E(t(22, 9, 15), 'bat', 'update', 'Site public', 'a publié une modification du site', 'Accueil · bloc « À la une »', { diff: [['Titre', 'Rentrée de janvier', 'Rentrée de janvier 2027 : inscriptions ouvertes']] }),
  E(t(22, 8, 5), 'gna', 'login', 'Connexion', 's\'est connectée', ''),
  E(t(22, 7, 58), 'kou', 'create', 'Classes', 'a fait l\'appel', 'Esthétique A · 31 présentes / 32'),
  E(t(22, 7, 52), 'kou', 'login', 'Connexion', 's\'est connectée', ''),
  E(t(22, 3, 0), 'sys', 'create', 'Système', 'a effectué la sauvegarde quotidienne', '2,4 Go · OK'),
  E(t(21, 23, 41), 'sys', 'sec', 'Sécurité', '5 tentatives de connexion échouées', 'Compte : m.coulibaly', { ip: '41.202.88.17', dev: 'Linux · inconnu', alert: 1, diff: [['Action', '', 'Compte bloqué 15 min'], ['Alerte', '', 'E-mail envoyé à l\'administrateur']] }),
  E(t(21, 17, 40), 'ade', 'update', 'Emploi du temps', 'a déplacé un cours', 'Tresses · Esth. B', { diff: [['Créneau', 'Jeu. 08:00', 'Ven. 10:30'], ['Salle', 'Salle 2', 'Salle 4']] }),
  E(t(21, 16, 2), 'gbo', 'create', 'Actualités', 'a créé une actualité', '« Journée portes ouvertes »'),
  E(t(21, 15, 4), 'kou', 'update', 'Certificats', 'a saisi 12 notes', 'Évaluation pratique · Esth. A'),
  E(t(21, 11, 12), 'cou', 'delete', 'Paiements', 'a annulé un reçu', 'R-26-1179 · doublon', { diff: [['Montant', '50 000 F', '—'], ['Motif', '', 'Saisi deux fois']] }),
  E(t(21, 10, 0), 'bat', 'update', 'Paramètres', 'a modifié les droits d\'un rôle', 'Rôle Secrétariat', { diff: [['Paiements', 'Non', 'Oui (lecture)']] }),
  E(t(20, 18, 22), 'bat', 'delete', 'Personnel', 'a supprimé une fiche', 'M. Diabaté Karim (stagiaire)'),
  E(t(20, 13, 1), 'kou', 'sec', 'Sécurité', 's\'est connectée depuis un nouvel appareil', 'Android · Yopougon', { dev: 'Android · Chrome' }),
  E(t(20, 9, 47), 'gna', 'create', 'Élèves', 'a ajouté une élève', 'Bintou Sangaré · IGMK-27-008'),
  E(t(19, 16, 30), 'ade', 'update', 'Classes', 'a réaffecté une classe', 'Coiffure B', { diff: [['Formateur', 'M. Traoré', 'M. Bamba']] }),
  E(t(19, 10, 12), 'cou', 'export', 'Paiements', 'a exporté les paiements du mois (Excel)', 'Novembre 2026'),
  E(t(18, 14, 0), 'gbo', 'update', 'Inscriptions', 'a modifié le tarif d\'une formation', 'Onglerie', { diff: [['Scolarité', '110 000 F', '120 000 F']] }),
  E(t(18, 8, 2), 'bam', 'login', 'Connexion', 's\'est connecté', ''),
  E(t(17, 15, 10), 'ade', 'create', 'Personnel', 'a déclaré une absence remplacée', 'Mme Kouassi · remplacée par M. Bamba'),
];
const ago = d => { const m = Math.round((NOW - d) / 60000); return m < 60 ? `il y a ${m} min` : m < 1440 ? `il y a ${Math.round(m / 60)} h` : d.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' }) };
const tm = d => d.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
const day = d => { const k = Math.floor((new Date(2026, 10, 22) - new Date(d.getFullYear(), d.getMonth(), d.getDate())) / 864e5); return k === 0 ? "Aujourd'hui" : k === 1 ? 'Hier' : d.toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' }) };
const st = { u: new URLSearchParams(location.search).get('u') ? 'kou' : '', ty: '', mod: '', q: '', p: '7' };

// options des filtres
$('#fu').innerHTML = '<option value="">Tous les utilisateurs</option>' + Object.entries(U).map(([k, v]) => `<option value="${k}">${v[0]} — ${v[1]}</option>`).join('');
$('#fm').innerHTML = '<option value="">Tous les modules</option>' + [...new Set(L.map(e => e.mod))].sort().map(m => `<option>${m}</option>`).join('');
$('#ft').innerHTML = '<option value="">Toutes les actions</option>' + Object.entries(T).map(([k, v]) => `<option value="${k}">${v[0]}</option>`).join('');
$('#fu').value = st.u;

function filtered() {
  const lim = st.p === '1' ? new Date(2026, 10, 22) : st.p === '7' ? new Date(2026, 10, 15) : new Date(2026, 9, 22);
  return L.filter(e => e.at >= lim && (!st.u || e.u === st.u) && (!st.ty || e.ty === st.ty) && (!st.mod || e.mod === st.mod) && (!st.q || (U[e.u][0] + ' ' + e.txt + ' ' + e.obj + ' ' + e.id).toLowerCase().includes(st.q)));
}
function render() {
  const list = filtered();
  $('#jk1').textContent = list.length; $('#jk2').textContent = new Set(list.map(e => e.u).filter(u => u !== 'sys')).size;
  $('#jk3').textContent = list.filter(e => e.ty === 'delete').length; $('#jk4').textContent = list.filter(e => e.ty === 'sec').length;
  $('#jcount').textContent = list.length + ' événement' + (list.length > 1 ? 's' : '');
  let last = '';
  $('#jlist').innerHTML = list.length ? list.map(e => { const d = day(e.at), h = d !== last ? `<li class="jday">${d}</li>` : ''; last = d;
    return h + `<li class="jev${e.alert ? ' al' : ''}" data-id="${e.id}" tabindex="0"><time>${tm(e.at)}</time><span class="jt ${T[e.ty][1]}" title="${T[e.ty][0]}">${T[e.ty][2]}</span>
    <div class="jb"><p><b>${esc(U[e.u][0])}</b> ${esc(e.txt)}${e.obj ? ` · <em>${esc(e.obj)}</em>` : ''}</p><small><span class="bd gr">${e.mod}</span> ${U[e.u][1]} · ${e.dev} · ${e.ip}</small>
    ${e.diff ? `<div class="jdiff" hidden><table>${e.diff.map(([k, a, b]) => `<tr><td>${k}</td><td class="old">${a ? esc(a) : '—'}</td><td>→</td><td class="new">${esc(b)}</td></tr>`).join('')}</table><small class="mono">${e.id}</small></div>` : ''}</div>
    ${e.diff ? '<button class="jx" aria-label="Voir le détail">▾</button>' : ''}</li>` }).join('') : '<li class="empty">Aucun événement ne correspond à ces filtres.</li>';
}
$('#jlist').addEventListener('click', e => { const li = e.target.closest('.jev'); if (!li) return; const d = li.querySelector('.jdiff'); if (!d) return; d.hidden = !d.hidden; li.classList.toggle('open', !d.hidden) });
$('#jlist').addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.classList.contains('jev')) e.target.click() });
$('#fu').onchange = e => { st.u = e.target.value; render() }; $('#fm').onchange = e => { st.mod = e.target.value; render() }; $('#ft').onchange = e => { st.ty = e.target.value; render() };
$('#fq').oninput = e => { st.q = e.target.value.trim().toLowerCase(); render() };
document.querySelectorAll('#fp button').forEach(b => b.onclick = () => { st.p = b.dataset.p; document.querySelectorAll('#fp button').forEach(x => x.classList.toggle('on', x === b)); render() });
document.querySelectorAll('[data-quick]').forEach(b => b.onclick = () => { st.ty = b.dataset.quick; $('#ft').value = st.ty; st.p = '30'; document.querySelectorAll('#fp button').forEach(x => x.classList.toggle('on', x.dataset.p === '30')); render(); $('#jlist').scrollIntoView({ behavior: 'smooth' }) });
$('#jexp').onclick = () => { const rows = [['Date', 'Heure', 'Utilisateur', 'Rôle', 'Action', 'Module', 'Détail', 'Objet', 'Appareil', 'IP']].concat(filtered().map(e => [e.at.toLocaleDateString('fr-FR'), tm(e.at), U[e.u][0], U[e.u][1], T[e.ty][0], e.mod, e.txt, e.obj, e.dev, e.ip]));
  const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob(['﻿' + rows.map(r => r.map(c => '"' + String(c).replace(/"/g, '""') + '"').join(';')).join('\n')], { type: 'text/csv' })); a.download = 'igmk-journal.csv'; a.click() };
render();
})();
