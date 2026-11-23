// Fiche élève : onglets, envoi du relevé, résolution d'une contestation (démo)
(() => {
document.querySelectorAll('.mbg,.toast').forEach(x => document.body.appendChild(x));
const $ = s => document.querySelector(s);
const tabs = document.querySelectorAll('.etabs a');
const go = k => { tabs.forEach(a => a.classList.toggle('on', a.dataset.t === k)); document.querySelectorAll('.et').forEach(s => s.hidden = s.id !== 'e-' + k) };
tabs.forEach(a => a.onclick = e => { e.preventDefault(); if (!document.getElementById('e-' + a.dataset.t)) return toast('Onglet non inclus dans cette maquette.'); go(a.dataset.t); history.replaceState(0, '', '#' + a.dataset.t) });
document.querySelectorAll('[data-gopay]').forEach(a => a.onclick = e => { e.preventDefault(); go('pay'); history.replaceState(0, '', '#pay') });
if (location.hash === '#pay') go('pay');
const S = $('#msend'), lbl = { wa: 'Envoyer sur WhatsApp', mail: 'Envoyer par e-mail', pdf: 'Télécharger le PDF' };
document.querySelectorAll('[data-send]').forEach(b => b.onclick = e => { e.preventDefault(); S.classList.add('on') });
S.querySelectorAll('[data-close]').forEach(b => b.onclick = () => S.classList.remove('on'));
S.onclick = e => { if (e.target === S) S.classList.remove('on') };
document.addEventListener('keydown', e => e.key === 'Escape' && S.classList.remove('on'));
$('#sch').onchange = () => { const v = S.querySelector('[name=ch]:checked').value; $('#sgo').textContent = lbl[v]; $('#sto').hidden = $('#smsg').hidden = v === 'pdf';
  $('#sto select').innerHTML = v === 'mail' ? '<option>awa.kone04@gmail.com</option><option>Mme Koné (mère) · kone.mariam@yahoo.fr</option>' : '<option>Awa Koné · +225 07 10 20 40 00</option><option>Mme Koné (mère) · +225 05 55 31 22 90</option><option>Les deux</option>' };
$('#sgo').onclick = () => { const v = S.querySelector('[name=ch]:checked').value;
  if (v === 'pdf') { document.body.classList.add('print-rlv'); setTimeout(() => { print(); document.body.classList.remove('print-rlv') }, 100); S.classList.remove('on'); return }
  S.classList.remove('on'); toast(v === 'wa' ? 'Relevé envoyé sur WhatsApp à Awa Koné. Vous serez notifié dès qu\'elle répond.' : 'Relevé envoyé par e-mail.') };
addEventListener('afterprint', () => document.body.classList.remove('print-rlv'));
let tt; function toast(m) { const t = $('#toast'); t.innerHTML = '<span>✓</span>' + m; t.classList.add('on'); clearTimeout(tt); tt = setTimeout(() => t.classList.remove('on'), 5000) }
})();
