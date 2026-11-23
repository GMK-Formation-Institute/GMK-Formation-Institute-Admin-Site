# Maquettes de l'espace de gestion IGMK (données fictives)
import pathlib, random
R = pathlib.Path(__file__).parent
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Manrope:wght@400;500;600&display=swap" rel="stylesheet">'
I = {  # icônes (traits)
 "dash":'<path d="M3 3h7v9H3zM14 3h7v5h-7zM14 12h7v9h-7zM3 16h7v5H3z"/>',
 "users":'<circle cx="9" cy="8" r="4"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6M16 4a4 4 0 0 1 0 8M22 21c0-3-2-5-4-6"/>',
 "add":'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6M19 14v6M16 17h6"/>',
 "pay":'<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
 "stage":'<path d="M3 21h18M5 21V8l7-5 7 5v13M9 21v-6h6v6"/>',
 "class":'<path d="M4 4h16v12H4zM8 20h8M12 16v4"/>',
 "staff":'<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',
 "cal":'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "cert":'<circle cx="12" cy="9" r="6"/><path d="M8 14l-2 7 6-3 6 3-2-7"/>',
 "news":'<path d="M4 5h13v14H6a2 2 0 0 1-2-2zM17 9h3v8a2 2 0 0 1-2 2M8 9h5M8 13h5"/>',
 "set":'<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-2.9 1.2V21a2 2 0 1 1-4 0v-.1A1.7 1.7 0 0 0 7 19.4a1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1A1.7 1.7 0 0 0 1.2 14H1a2 2 0 1 1 0-4h.1A1.7 1.7 0 0 0 4.6 7a1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1A1.7 1.7 0 0 0 10 1.2V1a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 2.9 1.2l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1A1.7 1.7 0 0 0 19.4 9"/>',
 "bell":'<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21a2 2 0 0 0 4 0"/>',
 "search":'<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>',
 "plus":'<path d="M12 5v14M5 12h14"/>',
 "dl":'<path d="M12 3v12M7 10l5 5 5-5M4 21h16"/>',
 "alert":'<path d="M12 3l10 18H2zM12 10v5M12 18v.5"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "menu":'<path d="M3 6h18M3 12h18M3 18h18"/>',
 "edit":'<path d="M4 20h4L19 9l-4-4L4 16zM14 6l4 4"/>',
 "wa":'<path d="M4 20l1.5-4A8 8 0 1 1 9 19z"/>',
}
I["chart"] = '<path d="M3 3v18h18"/><path d="M7 15l4-5 3 3 5-7"/>'
def ic(n): return f'<svg viewBox="0 0 24 24">{I[n]}</svg>'
MENU = [("Pilotage",[("dashboard.html","dash","Tableau de bord",""),("eleves.html","users","Élèves","248"),("preinscriptions.html","news","Pré-inscriptions","6"),("inscriptions.html","add","Inscriptions","12"),("paiements.html","pay","Paiements",""),("stages.html","stage","Stages",""),("stats.html","chart","Statistiques","")]),
        ("École",[("classes.html","class","Classes & formations",""),("emploi.html","cal","Emploi du temps",""),("personnel.html","staff","Personnel",""),("certificats.html","cert","Certificats","11")]),
        ("Site public",[("site.html","edit","Contenu du site",""),("actualites.html","news","Actualités","")]),
        ("Compte",[("journal.html","clock","Journal d'activité",""),("parametres.html","set","Paramètres","")])]

def shell(fn, title, body, active):
    nav = "".join(f'<h6>{g}</h6><nav>' + "".join(f'<a href="{h}"{" class=on" if h==active else ""}>{ic(i)}{t}{f"<span class=n>{n}</span>" if n else ""}</a>' for h,i,t,n in items) + '</nav>' for g,items in MENU)
    (R/fn).write_text(f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — Espace IGMK</title>{FONTS}<link rel="stylesheet" href="style.css?v=37"><script src="palette.js?v=3"></script></head>
<body><div class="app"><aside class="side"><a class="brand" href="dashboard.html"><span class="mk"><img src="img/cosmetique.jpg" alt=""></span><div><b>IGMK</b><small>Espace de gestion</small></div></a>{nav}
<div class="me"><img src="img/about/BATIYE.jpg" alt=""><div><b>K. N'Si Batiye</b><span>Directeur général</span></div></div></aside>
<div class="main"><header class="top"><button class="burger" onclick="document.body.classList.toggle('nav')">{ic("menu").replace("<svg","<svg width=22 stroke=#170A1C fill=none stroke-width=1.8")}</button>
<label class="search">{ic("search").replace("<svg","<svg width=18 stroke=currentColor fill=none stroke-width=1.8")}<input placeholder="Rechercher un élève, un membre du personnel, un reçu…"><kbd>⌘K</kbd></label><span class="sp"></span>
<a class="ic h" href="#" title="Agenda">{ic("cal")}</a><a class="ic" href="#" title="Notifications">{ic("bell")}<i></i></a></header>
<main class="page">{body}</main></div></div>{DEMO(fn)}
<script>document.addEventListener('click',e=>{{if(document.body.classList.contains('nav')&&!e.target.closest('.side,.burger'))document.body.classList.remove('nav')}})</script></body></html>''')

def DEMO(fn):
    return '<div class="demo">' + "".join(f'<a href="{h}"{" class=on" if h==fn else ""}>{t}</a>' for h,t in [("index.html","Connexion"),("dashboard.html","Tableau de bord"),("eleves.html","Élèves"),("eleve.html","Fiche élève"),("preinscriptions.html","Pré-inscriptions"),("inscriptions.html","Inscriptions"),("paiements.html","Paiements"),("stats.html","Statistiques"),("stages.html","Stages"),("classes.html","Classes"),("emploi.html","Emploi du temps"),("certificats.html","Certificats"),("actualites.html","Actualités"),("site.html","Contenu du site"),("personnel.html","Personnel"),("membre.html","Fiche membre"),("journal.html","Journal"),("parametres.html","Paramètres")]) + '</div>'

def ini(n, c=""):
    p = n.replace(".","").split(); return f'<span class="ini"{f" style={c}" if c else ""}>{p[0][0]}{p[-1][0]}</span>'

# ---------------- CONNEXION ----------------
(R/"index.html").write_text(f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Connexion — Espace IGMK</title>{FONTS}<link rel="stylesheet" href="style.css?v=37"><script src="palette.js?v=3"></script></head><body>
<div class="login"><div class="pic"><img src="img/formations/esthetique/7.jpg" alt=""><a class="brand" href="#"><span class="mk"><img src="img/cosmetique.jpg" alt=""></span><div><b>IGMK</b><small>Espace de gestion</small></div></a>
<div class="q"><p>« L'excellence s'apprend à la main — et se pilote avec rigueur. »</p><small>Institut GMK Formation · depuis 2012</small></div></div>
<div class="f"><small style="font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--v);font-weight:600">Espace réservé</small><h1 style="margin-top:10px">Bon retour<br><i>parmi nous.</i></h1>
<p>Connectez-vous pour accéder à la gestion des élèves, des paiements, des stages et du personnel.</p>
<div class="roles"><span>Direction</span><span>Secrétariat</span><span>Formateurs</span><span>Comptabilité</span></div>
<form onsubmit="location.href='dashboard.html';return false"><div class="fld"><label>Identifiant ou e-mail</label><input placeholder="prenom.nom@igmk-formation.net"></div>
<div class="fld"><label>Mot de passe</label><input type="password" placeholder="••••••••••"></div>
<div class="opts"><label><input type="checkbox" checked> Rester connecté</label><a href="#">Mot de passe oublié ?</a></div>
<button class="btn p">Se connecter →</button></form>
<div class="foot"><span>© 2026 Institut GMK Formation</span><a href="../site-v2/index.html">← Retour au site public</a></div></div></div>{DEMO("index.html")}</body></html>''')

# ---------------- TABLEAU DE BORD ----------------
months = [("Juin",6.2,5.1),("Juil",5.4,4.8),("Août",3.1,3.4),("Sept",9.8,8.2),("Oct",8.6,7.9),("Nov",7.4,6.6)]
mx = 10
bars = "".join(f'<div class="{"now" if i==len(months)-1 else ""}"><div style="display:flex;gap:4px;align-items:flex-end;height:100%;width:100%;justify-content:center"><i class="prev" style="height:{p/mx*100}%" data-v="{p} M (2025)"></i><i style="height:{v/mx*100}%" data-v="{v} M FCFA"></i></div><span>{m}</span></div>' for i,(m,v,p) in enumerate(months))
seg = [("Esthétique",96,"#9B5BB0"),("Coiffure",88,"#3A1548"),("Spécialisations",46,"#D4AEE0"),("Stage en cours",18,"#7A4A2E")]
tot = sum(s[1] for s in seg); off = 0; arcs = ""
for n,v,c in seg:
    L = v/tot*100; arcs += f'<circle r="15.9" cx="21" cy="21" fill="none" stroke="{c}" stroke-width="5" stroke-dasharray="{L-0.6} {100-L+0.6}" stroke-dashoffset="{-off+25}"/>'; off += L
donut = f'<div class="donut"><svg viewBox="0 0 42 42">{arcs}<text x="21" y="21" text-anchor="middle" font-family="Cormorant Garamond" font-size="9">{tot}</text><text x="21" y="27" text-anchor="middle" font-size="2.6" fill="#6E6068" font-family="Manrope">ÉLÈVES</text></svg><ul>' + "".join(f'<li><i style="background:{c}"></i>{n}<b>{v}</b></li>' for n,v,c in seg) + '</ul></div>'
retards = [("Awa Koné","Esthétique · Promo Juil. 26","85 000","12 j"),("Fatoumata Diallo","Coiffure · Promo Juil. 26","60 000","9 j"),("Mariam Ouattara","Onglerie","45 000","6 j"),("Prisca Yao","Esthétique · Promo Jan. 26","85 000","3 j")]
dash = f'''<div class="ph"><div><small>Samedi 22 novembre 2026</small><h1>Bonjour, <i>M. Batiye.</i></h1><p>Voici l'essentiel de l'activité de l'école aujourd'hui.</p></div><div class="row"><a class="btn" href="#">{ic("dl")}Rapport mensuel</a><a class="btn p" href="inscriptions.html#nouvelle">{ic("plus")}Nouvelle inscription</a></div></div>
<div class="grid g4">
<div class="card kpi dark"><span>Élèves actifs</span><b>248</b><em style="color:var(--vl)">▲ +18 vs. nov. 2025</em><div class="ico">{ic("users")}</div></div>
<div class="card kpi"><span>Encaissé en novembre</span><b>7,4 <small>M FCFA</small></b><em class="up">▲ 12 % vs. nov. 2025</em><div class="ico">{ic("pay")}</div></div>
<div class="card kpi"><span>Impayés en retard</span><b>1,9 <small>M FCFA</small></b><em class="down">23 élèves concernés</em><div class="ico">{ic("alert")}</div></div>
<div class="card kpi"><span>Stagiaires sur le terrain</span><b>18</b><em class="up">14 instituts partenaires</em><div class="ico">{ic("stage")}</div></div></div>
<div class="grid g21" style="margin-top:18px">
<div class="card"><div class="hd"><h3>Encaissements</h3><select class="sel"><option>6 derniers mois</option><option>Année 2026</option></select></div><div class="bars">{bars}</div><div class="legend"><span><i style="background:var(--v)"></i>2026</span><span><i style="background:#eadff0"></i>2025</span><span style="margin-left:auto">Total semestre : <b style="color:var(--ink)">40,5 M FCFA</b></span></div></div>
<div class="card cd"><small>Prochaine rentrée</small><h3 style="font-size:30px;margin-top:8px">Janvier 2027</h3><div class="nums"><div><b>51</b><span>jours</span></div><div><b>34</b><span>inscrites</span></div><div><b>6</b><span>places</span></div></div>
<p>Capacité : 40 places (2 salles). Taux de remplissage : 85 %.</p><div class="prog" style="margin-top:12px;background:#ffffff1a"><i style="width:85%;background:var(--vl)"></i></div>
<a class="btn" style="margin-top:20px;width:100%;justify-content:center" href="#">Voir les inscriptions</a></div></div>
<div class="grid g3" style="margin-top:18px">
<div class="card"><div class="hd"><h3>Répartition</h3><a href="eleves.html">Détail →</a></div>{donut}</div>
<div class="card"><div class="hd"><h3>Paiements en retard</h3><a href="#">Tout voir →</a></div>''' + "".join(f'<div class="li">{ini(n)}<div class="who"><div><b>{n}</b><small>{f}</small></div></div><div class="r"><b>{m} F</b><small class="down">Retard {d}</small></div></div>' for n,f,m,d in retards) + f'''<a class="btn" style="width:100%;justify-content:center;margin-top:10px" href="#">{ic("wa")}Relancer par WhatsApp</a></div>
<div class="card"><div class="hd"><h3>À traiter</h3><span class="bd vi">5</span></div>
<div class="al bad">{ic("alert")}<div><b>3 dossiers incomplets</b><p>Pièce d'identité manquante — rentrée de janvier.</p></div></div>
<div class="al warn">{ic("clock")}<div><b>Évaluations de stage</b><p>4 fiches à recevoir avant le 30 novembre.</p></div></div>
<div class="al vi">{ic("cert")}<div><b>Certificats à signer</b><p>11 certificats — promo juillet 2026.</p></div></div>
<div class="al vi">{ic("staff")}<div><b>Absence formateur</b><p>Mme Kouassi absente lundi — remplacement à prévoir.</p></div></div></div></div>
<div class="grid g2" style="margin-top:18px">
<div class="card"><div class="hd"><h3>Dernières inscriptions</h3><a href="eleves.html">Tous les élèves →</a></div>''' + "".join(f'<div class="li">{ini(n)}<div class="who"><div><b>{n}</b><small>{f}</small></div></div><div class="r"><span class="bd {c}">{s}</span><small style="display:block;margin-top:4px">{d}</small></div></div>' for n,f,s,c,d in [("Grâce Amani","Esthétique · Janvier 2027","Acompte versé","ok","Aujourd'hui"),("Ruth Ouédraogo","Coiffure · Janvier 2027","Dossier incomplet","warn","Hier"),("Nadège Soro","Spécialisation Maquillage","Soldé","ok","20 nov."),("Christelle N'Guessan","Esthétique · Janvier 2027","En attente","gr","19 nov.")]) + '''</div>
<div class="card"><div class="hd"><h3>Aujourd'hui à l'école</h3><a href="#">Emploi du temps →</a></div>''' + "".join(f'<div class="li"><div style="width:56px;font-weight:600">{h}</div><div class="who"><div><b>{c}</b><small>{s}</small></div></div><div class="r"><span class="bd {b}">{st}</span></div></div>' for h,c,s,b,st in [("08:00","Soins du visage — Esthé. A","Salle 1 · Mme Kouassi","ok","En cours"),("08:00","Tresses & nattes — Coiffure B","Salle 2 · M. Bamba","ok","En cours"),("13:00","Cosmétologie (théorie)","Salle 3 · Dr Adegoke","gr","À venir"),("14:30","Nail art — Spécialisation","Salle 4 · Mme Yao","gr","À venir")]) + '</div></div>'
shell("dashboard.html","Tableau de bord",dash,"dashboard.html")

# ---------------- ÉLÈVES ----------------
E = [("Awa Koné","IGMK-26-014","Esthétique","Juil. 2026","Stage","vi",62,"bad","Retard"),
 ("Fatoumata Diallo","IGMK-26-021","Coiffure","Juil. 2026","En formation","ok",70,"bad","Retard"),
 ("Grâce Amani","IGMK-27-002","Esthétique","Jan. 2027","Inscrite","gr",20,"ok","À jour"),
 ("Mariam Ouattara","IGMK-26-033","Onglerie","Nov. 2026","En formation","ok",50,"warn","Échéance proche"),
 ("Prisca Yao","IGMK-26-004","Esthétique","Jan. 2026","Stage","vi",88,"bad","Retard"),
 ("Nadège Soro","IGMK-26-040","Maquillage","Nov. 2026","En formation","ok",100,"ok","Soldé"),
 ("Christelle N'Guessan","IGMK-27-005","Esthétique","Jan. 2027","Dossier incomplet","warn",0,"gr","Non commencé"),
 ("Aïcha Konaté","IGMK-26-018","Coiffure","Juil. 2026","En formation","ok",83,"ok","À jour"),
 ("Ruth Ouédraogo","IGMK-27-007","Coiffure","Jan. 2027","Dossier incomplet","warn",10,"ok","À jour"),
 ("Sandrine Kouadio","IGMK-25-061","Esthétique","Jan. 2026","Diplômée","gr",100,"ok","Soldé")]
pc = {"ok":"ok","bad":"bad","warn":"warn","gr":""}
rows = "".join(f'<tr onclick="location.href=\'eleve.html\'" style="cursor:pointer"><td><input type="checkbox" onclick="event.stopPropagation()"></td><td><div class="who">{ini(n)}<div><b>{n}</b><small>+225 07 {10+i} {20+i*3} {40+i} {11*i%90:02d}</small></div></div></td><td><span class="mono">{m}</span></td><td>{f}</td><td>{p}</td><td><span class="bd {sc}">{s}</span></td><td><div style="display:flex;align-items:center;gap:10px"><div class="prog {pc[pcl]}" style="flex:1"><i style="width:{pr}%"></i></div><small style="width:34px">{pr}%</small></div><small style="color:var(--{ {"ok":"ok","bad":"bad","warn":"warn","gr":"mute"}[pcl]})">{pl}</small></td><td><button class="dots" onclick="event.stopPropagation()">⋯</button></td></tr>' for i,(n,m,f,p,s,sc,pr,pcl,pl) in enumerate(E))
el = f'''<div class="ph"><div><small>Pilotage</small><h1>Élèves <i>· 248</i></h1><p>Dossiers, statuts et suivi des paiements de toutes les apprenantes.</p></div><div class="row"><a class="btn" href="#">{ic("dl")}Exporter (Excel)</a><a class="btn p" href="inscriptions.html#nouvelle">{ic("plus")}Nouvelle inscription</a></div></div>
<div class="grid g4" style="margin-bottom:22px">
<div class="card kpi"><span>En formation</span><b>184</b><div class="ico">{ic("class")}</div></div>
<div class="card kpi"><span>En stage</span><b>18</b><div class="ico">{ic("stage")}</div></div>
<div class="card kpi"><span>Inscrites janvier</span><b>34</b><div class="ico">{ic("add")}</div></div>
<div class="card kpi"><span>Paiements en retard</span><b style="color:var(--bad)">23</b><div class="ico">{ic("alert")}</div></div></div>
<div class="tools"><button class="chip on">Toutes <em>248</em></button><button class="chip">En formation <em>184</em></button><button class="chip">En stage <em>18</em></button><button class="chip">Inscrites <em>34</em></button><button class="chip">Diplômées <em>512</em></button>
<span style="flex:1"></span><select class="sel"><option>Toutes les formations</option><option>Esthétique</option><option>Coiffure</option><option>Spécialisations</option></select><select class="sel"><option>Toutes les promotions</option><option>Janvier 2027</option><option>Juillet 2026</option></select><select class="sel"><option>Paiement : tous</option><option>En retard</option><option>À jour</option><option>Soldé</option></select></div>
<div class="tw"><table><thead><tr><th style="width:30px"><input type="checkbox"></th><th>Élève</th><th>Matricule</th><th>Formation</th><th>Promotion</th><th>Statut</th><th style="width:220px">Paiement</th><th></th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="pager"><span>Affichage 1 – 10 sur 248</span><div class="row"><button>‹</button><button class="on">1</button><button>2</button><button>3</button><button>…</button><button>25</button><button>›</button></div></div>'''
shell("eleves.html","Élèves",el,"eleves.html")

# ---------------- FICHE ÉLÈVE ----------------
ech = [("Frais d'inscription","05/07/2026","50 000","Payé","ok"),("Mensualité 1","05/08/2026","85 000","Payé","ok"),("Mensualité 2","05/09/2026","85 000","Payé","ok"),("Mensualité 3","05/10/2026","85 000","Payé","ok"),("Mensualité 4","05/11/2026","85 000","Partiel · 35 000 F en retard","bad"),("Mensualité 5","05/12/2026","85 000","À venir","gr"),("Mensualité 6","05/01/2027","85 000","À venir","gr")]
notes = [("Soins du visage","Pratique",16.5),("Épilation","Pratique",15),("Manucure & pédicure","Pratique",17),("Massage","Pratique",14.5),("Cosmétologie","Théorie",13),("Dermatologie esthétique","Théorie",12.5)]
fiche = f'''<a href="eleves.html" style="color:var(--mute);font-size:13px;font-weight:600">← Retour aux élèves</a>
<div class="hero" style="margin-top:18px"><img class="big" src="img/formations/esthetique/8.jpg" alt=""><div style="flex:1;min-width:260px"><div class="row"><span class="bd vi">En stage</span><span class="bd bad">Paiement en retard</span></div><h1 style="margin-top:8px">Awa Koné</h1>
<div class="meta"><span>Matricule <b>IGMK-26-014</b></span><span>Formation <b>Esthétique</b></span><span>Promotion <b>Juillet 2026</b></span><span>Née le <b>14/03/2004</b></span></div></div>
<div class="row"><a class="btn" href="#">{ic("wa")}WhatsApp</a><a class="btn" href="#">{ic("edit")}Modifier</a><a class="btn" href="#" data-send>Envoyer le relevé</a><a class="btn v" href="paiements.html">{ic("pay")}Encaisser</a></div></div>
<div class="tabs etabs"><a class="on" href="#ov" data-t="ov">Vue d'ensemble</a><a href="#info" data-t="info">Informations</a><a href="#pay" data-t="pay">Paiements</a><a href="#notes" data-t="notes">Notes & évaluations</a><a href="#pres" data-t="pres">Présences</a><a href="#stage" data-t="stage">Stage</a><a href="#docs" data-t="docs">Documents</a></div>
<section class="et" id="e-ov"><div class="grid g4">
<div class="card kpi"><span>Moyenne générale</span><b>15,2 <small>/20</small></b><em class="up">Pratique 15,8 · Théorie 12,8</em></div>
<div class="card kpi"><span>Assiduité</span><b>94 <small>%</small></b><em>6 absences sur 104 jours</em></div>
<div class="card kpi"><span>Payé</span><b>355 000 <small>F</small></b><em>sur 560 000 F</em></div>
<div class="card kpi"><span>Reste à payer</span><b style="color:var(--bad)">205 000 <small>F</small></b><em class="down">dont 35 000 F en retard</em></div></div>
<div class="grid g21" style="margin-top:18px">
<div class="card"><div class="hd"><h3>Échéancier</h3><a href="#pay" data-gopay>Historique des paiements →</a></div><div class="tw" style="border:0"><table style="min-width:520px"><thead><tr><th>Échéance</th><th>Date</th><th>Montant</th><th>Statut</th></tr></thead><tbody>''' + "".join(f'<tr><td><b style="font-weight:600">{a}</b></td><td>{d}</td><td>{m} F</td><td><span class="bd {c}">{s}</span></td></tr>' for a,d,m,s,c in ech) + f'''</tbody></table></div></div>
<div class="card"><div class="hd"><h3>Parcours</h3></div><div class="ring" style="--p:72"><div><div><b>72%</b><small>du cursus</small></div></div></div>
<div class="tl" style="margin-top:24px"><div class="done"><b>Inscription</b><small>05 juillet 2026</small></div><div class="done"><b>Formation à l'école</b><small>Juil. → déc. 2026 · 6 mois</small></div><div class="done"><b>Début du stage</b><small>02 novembre 2026</small></div><div><b>Fin du stage</b><small>02 février 2027</small></div><div><b>Certificat</b><small>Février 2027</small></div></div></div></div>
<div class="grid g3" style="margin-top:18px">
<div class="card"><div class="hd"><h3>Notes</h3><a href="#">Bulletin PDF →</a></div>''' + "".join(f'<div class="note"><div><b style="font-weight:600">{m}</b><small style="display:block;color:var(--mute);font-size:12px">{t}</small></div><div class="n">{str(n).replace(".",",")}<small>/20</small></div></div>' for m,t,n in notes) + f'''</div>
<div class="card"><div class="hd"><h3>Stage en cours</h3><span class="bd vi">Semaine 3 / 13</span></div>
<div class="li"><span class="ini" style="border-radius:10px">SR</span><div class="who"><div><b>Spa Riviera</b><small>Cocody Riviera 3 · Institut partenaire</small></div></div></div>
<div class="kv" style="margin-top:14px"><div><span>Maître de stage</span>Mme Laure Achi</div><div><span>Contact</span>07 48 22 10 05</div><div><span>Horaires</span>Lun – Sam · 9h – 18h</div><div><span>Prochaine visite</span>28 novembre</div></div>
<div class="prog" style="margin-top:18px"><i style="width:23%"></i></div></div>
<div class="card"><div class="hd"><h3>Contacts & documents</h3></div>
<div class="kv"><div><span>Téléphone</span>+225 07 10 20 40 00</div><div><span>Quartier</span>Yopougon Niangon</div><div><span>Personne à prévenir</span>Mme Koné (mère)</div><div><span>Téléphone</span>05 55 31 22 90</div></div>
<div style="margin-top:18px">''' + "".join(f'<div class="li" style="padding:9px 0"><span class="bd {c}" style="min-width:86px">{s}</span><span>{d}</span></div>' for d,s,c in [("Pièce d'identité","Reçu","ok"),("Photo d'identité","Reçue","ok"),("Convention de stage","Signée","ok"),("Attestation de stage","Attendue","warn")]) + '</div></div></div></section>' + (R/"_src/eleve_pay.html").read_text()
shell("eleve.html","Awa Koné",fiche,"eleves.html")

# ---------------- PERSONNEL ----------------
S = [("img/about/BATIYE.jpg","K. N'Si Batiye","Directeur général","Direction","CDI"),("img/about/ADEGOKE.jpg","Dr Adegoke Moucaïla","Directeur des études","Direction","CDI"),("img/about/GBOZE.jpg","Dr Gboze Jean-Claude","Directeur commercial","Direction","CDI"),
     ("img/instructor/002.jpg","Mme Kouassi Hortense","Formatrice Esthétique","Formation","CDI"),("img/instructor/010.jpg","M. Bamba Ismaël","Formateur Coiffure","Formation","CDI"),("img/about/KOUAKOU.jpg","Mme Kouakou Ange","Formatrice Maquillage","Formation","Vacataire"),
     ("img/instructor/decoration1.jpg","M. Traoré Salif","Formateur Décoration","Formation","Vacataire"),("","Mme Yao Bernadette","Formatrice Onglerie","Formation","Vacataire"),("","Mlle Gnamien Esther","Secrétaire — Accueil","Administration","CDI"),("","M. Coulibaly Moussa","Comptable","Administration","CDD")]
cards = "".join(f'<div class="card staff">{f"<img src={p} alt=>" if p else ini(n)}<h4>{n}</h4><p>{r}</p><div class="row"><span class="bd {"vi" if d=="Direction" else "ok" if d=="Formation" else "gr"}">{d}</span><span class="bd gr">{c}</span></div><div class="st"><div><b>{[0,0,0,62,58,24,12,20,0,0][i] or "—"}</b><small>Élèves</small></div><div><b>{[0,0,0,24,22,8,6,8,0,0][i] or "—"}</b><small>H / sem.</small></div><div><b>{["97","100","95","92","98","100","90","96","99","100"][i]}%</b><small>Présence</small></div></div></div>' for i,(p,n,r,d,c) in enumerate(S))
week = '<div class="week"><div></div>' + "".join(f'<div class="h">{d}</div>' for d in ["Lun 24","Mar 25","Mer 26","Jeu 27","Ven 28"])
slots = {"08:00":[("Soins visage","Kouassi · S1",""),("Tresses","Bamba · S2","c"),("Épilation","Kouassi · S1",""),("Tissage","Bamba · S2","c"),("Évaluation pratique","Kouassi · S1","")],
         "10:30":[("Maquillage mariée","Kouakou · S4","m"),("Manucure","Yao · S4",""),("Perruques","Bamba · S2","c"),("Contouring","Kouakou · S4","m"),("Coiffure moderne","Bamba · S2","c")],
         "13:00":[("Cosmétologie","Adegoke · S3",""),("Nail art","Yao · S4",""),("Dermatologie","Adegoke · S3",""),("Déco de salle","Traoré · S5","m"),("Réunion pédagogique","Tous · Salle prof","m")]}
for t,ss in slots.items(): week += f'<div class="t">{t}</div>' + "".join(f'<div class="s {c}"><b>{a}</b><small>{b}</small></div>' for a,b,c in ss)
week += '</div>'
pay = "".join(f'<tr><td><div class="who">{ini(n)}<div><b>{n}</b><small>{r}</small></div></div></td><td>{c}</td><td>{h}</td><td>{m} F</td><td><span class="bd {sc}">{s}</span></td></tr>' for n,r,c,h,m,s,sc in [("Mme Kouassi Hortense","Formatrice Esthétique","CDI","96 h","350 000","Payé le 05/11","ok"),("M. Bamba Ismaël","Formateur Coiffure","CDI","88 h","320 000","Payé le 05/11","ok"),("Mme Kouakou Ange","Maquillage","Vacataire · 6 000 F/h","32 h","192 000","À valider","warn"),("M. Traoré Salif","Décoration","Vacataire · 6 000 F/h","24 h","144 000","À valider","warn"),("Mme Yao Bernadette","Onglerie","Vacataire · 6 000 F/h","32 h","192 000","À valider","warn")])
pers = f'''<div class="ph"><div><small>École</small><h1>Personnel <i id="scount">· 10</i></h1><p>Équipe de direction, formateurs et administration.</p></div><div class="row"><a class="btn" href="#">{ic("cal")}Planning</a><a class="btn p" href="#" id="addm">{ic("plus")}Ajouter un membre</a></div></div>
<div class="grid g4" style="margin-bottom:22px">
<div class="card kpi"><span>Formateurs</span><b>5</b><em>2 CDI · 3 vacataires</em><div class="ico">{ic("class")}</div></div>
<div class="card kpi"><span>Heures de cours / semaine</span><b>68</b><em class="up">Toutes les salles couvertes</em><div class="ico">{ic("clock")}</div></div>
<div class="card kpi"><span>Absences ce mois</span><b>3</b><em class="down">1 non remplacée</em><div class="ico">{ic("alert")}</div></div>
<div class="card kpi"><span>Masse salariale nov.</span><b>2,6 <small>M FCFA</small></b><em>3 vacations à valider</em><div class="ico">{ic("pay")}</div></div></div>
<div class="tools" id="sf"><button class="chip on" data-f="all">Tous <em></em></button><button class="chip" data-f="Direction">Direction <em></em></button><button class="chip" data-f="Formation">Formateurs <em></em></button><button class="chip" data-f="Administration">Administration <em></em></button><button class="chip" data-f="off">Inactifs <em></em></button></div>
<div class="grid" id="staff" style="grid-template-columns:repeat(auto-fill,minmax(220px,1fr))"></div>
<div class="grid g12" style="margin-top:18px"><div class="card"><div class="hd"><h3>Vacations & salaires</h3><a href="#">Novembre ▾</a></div><div class="tw" style="border:0"><table style="min-width:560px"><thead><tr><th>Membre</th><th>Contrat</th><th>Heures</th><th>Montant</th><th>Statut</th></tr></thead><tbody>{pay}</tbody></table></div></div>
<div class="card" style="grid-column:auto"><div class="hd"><h3>Planning de la semaine</h3><a href="#">Semaine 48 ▾</a></div><div style="overflow-x:auto">{week}</div></div></div>'''
# planning en pleine largeur, salaires dessous
pers = pers.replace('<div class="grid g12" style="margin-top:18px"><div class="card"><div class="hd"><h3>Vacations', '<div class="grid" style="margin-top:18px;grid-template-columns:1fr"><div class="card"><div class="hd"><h3>Vacations')
pers += (R/"_src/pform.html").read_text()
shell("personnel.html","Personnel",pers,"personnel.html")

# ---------------- INSCRIPTIONS ----------------
COLS=[("Demandes","gr",[("Christelle N'Guessan","Esthétique","Via WhatsApp · 21 nov."),("Inès Bléhoué","Spé. Onglerie","Via le site · 21 nov."),("Josiane Tanoh","Coiffure","Visite à l'école · 20 nov."),("Laetitia Gnaoré","Esthétique","Via WhatsApp · 19 nov.")]),
 ("Dossier en cours","warn",[("Ruth Ouédraogo","Coiffure","Manque : pièce d'identité"),("Bintou Sangaré","Esthétique","Manque : photo, acte de naissance"),("Esther Kra","Coiffure","Manque : pièce d'identité")]),
 ("Acompte versé","vi",[("Grâce Amani","Esthétique","50 000 F · 22 nov."),("Sarah Brou","Esthétique","50 000 F · 18 nov."),("Mireille Assi","Coiffure","50 000 F · 15 nov.")]),
 ("Inscrites","ok",[("Nadège Soro","Spé. Maquillage","Soldé · Matricule IGMK-26-040"),("Corinne Aka","Esthétique","IGMK-27-001"),("Rokia Cissé","Coiffure","IGMK-27-003")])]
kan='<div class="kan">'+"".join(f'<div class="kc"><div class="kh"><span class="bd {c}">{t}</span><b>{[12,7,9,34][i]}</b></div>'+"".join(f'<div class="kcard">{ini(n)}<div><b>{n}</b><small>{f}</small><em>{d}</em></div></div>' for n,f,d in items)+f'<a class="kmore" href="#">+ {[8,4,6,31][i]} autres</a></div>' for i,(t,c,items) in enumerate(COLS))+'</div>'
form=f'''<div class="card" id="nouvelle"><div class="hd"><h3>Nouvelle inscription</h3><span class="bd vi">Étape 2 / 4</span></div>
<div class="steps4"><span class="done">1 · Identité</span><span class="on">2 · Formation</span><span>3 · Documents</span><span>4 · Paiement</span></div>
<div class="kv" style="margin-top:22px"><div class="fld"><label>Formation</label><select class="inp"><option>Esthétique — formation longue (6 + 3 mois)</option><option>Coiffure — formation longue</option><option>Spécialisation Maquillage (2 sem.)</option></select></div>
<div class="fld"><label>Promotion</label><select class="inp"><option>Janvier 2027 · 6 places restantes</option><option>Juillet 2027</option></select></div>
<div class="fld"><label>Horaires</label><select class="inp"><option>Journée · 8h – 17h</option></select></div>
<div class="fld"><label>Source</label><select class="inp"><option>WhatsApp</option><option>Site internet</option><option>Bouche-à-oreille</option><option>Facebook / TikTok</option></select></div></div>
<div class="sum"><div><span>Frais d'inscription</span><b>50 000 F</b></div><div><span>Scolarité</span><b>510 000 F</b></div><div><span>Mode</span><b>6 × 85 000 F</b></div><div class="t"><span>Total</span><b>560 000 F</b></div></div>
<div class="row" style="justify-content:space-between;margin-top:20px"><a class="btn" href="#">← Identité</a><a class="btn p" href="#">Continuer : documents →</a></div></div>'''
ins=f'''<div class="ph"><div><small>Pilotage</small><h1>Inscriptions <i>· Janvier 2027</i></h1><p>Du premier contact à l'inscription définitive.</p></div><div class="row"><select class="sel"><option>Rentrée janvier 2027</option><option>Rentrée juillet 2027</option></select><a class="btn p" href="#nouvelle">{ic("plus")}Nouvelle inscription</a></div></div>
<div class="grid g4" style="margin-bottom:22px">
<div class="card kpi dark"><span>Places remplies</span><b>34 <small style="color:var(--vl)">/ 40</small></b><div class="prog" style="background:#ffffff1a;margin-top:8px"><i style="width:85%;background:var(--vl)"></i></div><div class="ico">{ic("users")}</div></div>
<div class="card kpi"><span>Nouvelles demandes (7 j)</span><b>12</b><em class="up">▲ +5 vs. semaine passée</em><div class="ico">{ic("add")}</div></div>
<div class="card kpi"><span>Taux de conversion</span><b>64 <small>%</small></b><em>demande → inscrite</em><div class="ico">{ic("dash")}</div></div>
<div class="card kpi"><span>Acomptes encaissés</span><b>2,1 <small>M FCFA</small></b><em>pour janvier 2027</em><div class="ico">{ic("pay")}</div></div></div>
<a class="al vi pbanner" href="preinscriptions.html"><svg viewBox="0 0 24 24"><path d="M4 4h16v12H5.2L4 17.2z"/></svg><div><b>6 nouvelles pré-inscriptions en ligne</b><p>Dont 2 en attente depuis plus de 24 h. Convertissez-les en un clic : leurs informations sont déjà remplies.</p></div><span>Traiter →</span></a>
<div class="card" style="margin-bottom:18px"><div class="hd"><h3>Suivi des candidates</h3><div class="row"><button class="chip on">Toutes</button><button class="chip">Esthétique</button><button class="chip">Coiffure</button><button class="chip">Spécialisations</button></div></div>{kan}</div>
<div class="grid g21">{form}<div class="card"><div class="hd"><h3>Remplissage</h3></div>'''+"".join(f'<div style="margin-bottom:18px"><div class="row" style="justify-content:space-between;margin-bottom:8px"><b style="font-weight:600">{n}</b><small style="color:var(--mute)">{a} / {b}</small></div><div class="prog {c}"><i style="width:{a/b*100:.0f}%"></i></div></div>' for n,a,b,c in [("Esthétique — Salle A",18,20,""),("Coiffure — Salle B",14,20,""),("Spé. Maquillage (déc.)",10,10,"ok"),("Spé. Onglerie (déc.)",4,10,"warn")])+'''<div class="al vi" style="margin-top:20px"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg><div><b>Clôture des inscriptions</b><p>Le 5 janvier 2027 · dans 44 jours</p></div></div>
<div class="al bad"><svg viewBox="0 0 24 24"><path d="M12 3l10 18H2zM12 10v5M12 18v.5"/></svg><div><b>7 dossiers incomplets</b><p>Relance automatique WhatsApp prévue demain 9h.</p></div></div></div></div>'''
shell("inscriptions.html","Inscriptions",ins,"inscriptions.html")

# ---------------- PAIEMENTS ----------------
J=[("Grâce Amani","Acompte inscription","50 000","Mobile Money · Orange","R-26-1182","22/11 · 10:14"),("Aïcha Konaté","Mensualité 5","85 000","Espèces","R-26-1181","22/11 · 09:40"),("Mariam Ouattara","Spé. Onglerie — solde","45 000","Wave","R-26-1180","21/11 · 16:22"),("Sarah Brou","Acompte inscription","50 000","Mobile Money · MTN","R-26-1179","21/11 · 11:05"),("Nadège Soro","Spé. Maquillage — solde","60 000","Espèces","R-26-1178","20/11 · 15:30"),("Fatou Bamba","Mensualité 4","85 000","Virement bancaire","R-26-1177","20/11 · 09:12")]
mc={"Espèces":"gr","Wave":"vi","Virement bancaire":"gr"}
jr="".join(f'<tr><td><span class="mono">{r}</span></td><td><div class="who">{ini(n)}<div><b>{n}</b><small>{o}</small></div></div></td><td><span class="bd {mc.get(m,"warn")}">{m}</span></td><td><b style="font-weight:600">{a} F</b></td><td>{d}</td><td><a class="btn" style="height:32px;padding:0 12px" href="#">Reçu</a></td></tr>' for n,o,a,m,r,d in J)
rt="".join(f'<tr><td><div class="who">{ini(n)}<div><b>{n}</b><small>{f}</small></div></div></td><td>{e}</td><td><b style="font-weight:600;color:var(--bad)">{a} F</b></td><td><span class="bd {"bad" if int(j)>7 else "warn"}">{j} jours</span></td><td>{l}</td><td><div class="row"><a class="btn" style="height:32px;padding:0 12px" href="#">Relancer</a></div></td></tr>' for n,f,e,a,j,l in [("Awa Koné","Esthétique · Juil. 26","Mensualité 4 · 05/11","85 000","17","WhatsApp · 15/11"),("Fatoumata Diallo","Coiffure · Juil. 26","Mensualité 4 · 05/11","60 000","17","Appel · 18/11"),("Mariam Ouattara","Onglerie","Solde · 10/11","45 000","12","—"),("Prisca Yao","Esthétique · Jan. 26","Mensualité 6 · 15/11","85 000","7","WhatsApp · 20/11"),("Kadi Touré","Coiffure · Juil. 26","Mensualité 4 · 15/11","85 000","7","—")])
modes=[("Mobile Money",46,"#9B5BB0"),("Wave",22,"#D4AEE0"),("Espèces",24,"#3A1548"),("Virement",8,"#7A4A2E")]
recu=f'''<div class="recu"><div class="rh"><span class="mk" style="width:46px;height:46px;border-radius:50%;overflow:hidden;background:#fff;box-shadow:0 0 0 1px var(--vl)"><img src="img/cosmetique.jpg" style="width:100%;height:100%;object-fit:cover;object-position:28% 48%;transform:scale(1.25)" alt=""></span><div><b>Institut GMK Formation</b><small>Yopougon – Millionnaire · 07 07 58 90 81</small></div><span class="rn">REÇU<br><b>R-26-1182</b></span></div>
<div class="rl"><span>Élève</span><b>Grâce Amani · IGMK-27-002</b></div><div class="rl"><span>Objet</span><b>Acompte — Esthétique janv. 2027</b></div><div class="rl"><span>Mode</span><b>Orange Money · Réf. MP261122.1014</b></div><div class="rl"><span>Date</span><b>22/11/2026 à 10:14</b></div>
<div class="ra"><span>Montant reçu</span><b>50 000 FCFA</b></div><div class="rl"><span>Reste à payer</span><b>510 000 FCFA</b></div><div class="rs">Encaissé par Mlle Gnamien Esther · Secrétariat</div></div>'''
pay=f'''<div class="ph"><div><small>Pilotage</small><h1>Paiements <i>· Novembre</i></h1><p>Encaissements, reçus, échéances et relances.</p></div><div class="row"><a class="btn" href="#">{ic("dl")}Export comptable</a><a class="btn v" href="#" onclick="openPay();return false">{ic("pay")}Encaisser un paiement</a></div></div>
<div class="grid g4" style="margin-bottom:22px">
<div class="card kpi dark"><span>Encaissé ce mois</span><b>7,4 <small style="color:var(--vl)">M FCFA</small></b><em style="color:var(--vl)">Objectif 9 M · 82 %</em><div class="ico">{ic("pay")}</div></div>
<div class="card kpi"><span>Attendu d'ici fin nov.</span><b>1,6 <small>M FCFA</small></b><em>19 échéances</em><div class="ico">{ic("cal")}</div></div>
<div class="card kpi"><span>En retard</span><b style="color:var(--bad)">1,9 <small>M FCFA</small></b><em class="down">23 élèves</em><div class="ico">{ic("alert")}</div></div>
<div class="card kpi"><span>Taux de recouvrement</span><b>91 <small>%</small></b><em class="up">▲ 3 pts vs. octobre</em><div class="ico">{ic("dash")}</div></div></div>
<div class="grid g21"><div class="card"><div class="hd"><h3>Journal des encaissements</h3><div class="row"><select class="sel"><option>Tous les modes</option><option>Mobile Money</option><option>Wave</option><option>Espèces</option></select><select class="sel"><option>Cette semaine</option><option>Ce mois</option></select></div></div>
<div class="tw" style="border:0"><table style="min-width:640px"><thead><tr><th>Reçu</th><th>Élève</th><th>Mode</th><th>Montant</th><th>Date</th><th></th></tr></thead><tbody>{jr}</tbody></table></div></div>
<div class="card"><div class="hd"><h3>Liens de paiement envoyés</h3><span class="bd warn">3 en attente</span></div>
<p style="font-size:12.5px;color:var(--mute);margin:-6px 0 12px">Mis à jour automatiquement dès que l'élève paie.</p>
<div class="li"><span class="ini">KT</span><div class="who"><div><b>Kadi Touré</b><small>Mensualité 4 · Wave</small></div></div><div class="r"><b>85 000 F</b><span class="bd warn">Envoyé il y a 2 h</span></div></div>
<div class="li"><span class="ini">PY</span><div class="who"><div><b>Prisca Yao</b><small>Mensualité 6 · Orange Money</small></div></div><div class="r"><b>85 000 F</b><span class="bd warn">Ouvert, non payé</span></div></div>
<div class="li"><span class="ini">AK</span><div class="who"><div><b>Aïcha Konaté</b><small>Mensualité 5 · MTN</small></div></div><div class="r"><b>85 000 F</b><span class="bd ok">Payé à 09:40 ✓</span></div></div>
<a class="btn v" style="width:100%;justify-content:center;margin-top:14px" href="#" onclick="openPay();return false">Encaisser un paiement</a></div></div>
<div class="grid g21" style="margin-top:18px"><div class="card"><div class="hd"><h3>Retards de paiement</h3><a class="btn" href="#">{ic("wa")}Relancer tout le monde</a></div><div class="tw" style="border:0"><table style="min-width:680px"><thead><tr><th>Élève</th><th>Échéance</th><th>Montant</th><th>Retard</th><th>Dernière relance</th><th></th></tr></thead><tbody>{rt}</tbody></table></div></div>
<div class="grid" style="align-content:start"><div class="card"><div class="hd"><h3>Aperçu du reçu</h3><a href="#">Imprimer →</a></div>{recu}</div>
<div class="card"><div class="hd"><h3>Modes de paiement</h3><small style="color:var(--mute)">Novembre</small></div>'''+"".join(f'<div style="margin-bottom:14px"><div class="row" style="justify-content:space-between;margin-bottom:6px"><span>{n}</span><b style="font-weight:600">{v} %</b></div><div class="prog"><i style="width:{v*2}%;background:{c}"></i></div></div>' for n,v,c in modes)+'</div></div></div>'

MODAL = r'''<div class="mbg" id="pay" onclick="if(event.target===this)closePay()"><div class="modal">
<div class="mh"><div><small>Paiements</small><h3>Encaisser un paiement</h3></div><button class="x" onclick="closePay()">×</button></div>
<div class="mb">
<div class="fld"><label>Élève</label><div class="ac"><input class="inp" id="q" placeholder="Tapez un nom ou un matricule…" value="Grâce" oninput="sug(this.value)" autocomplete="off"><div class="sugg" id="sugg"></div></div></div>
<div class="pick" id="pick"><span class="ini">GA</span><div><b>Grâce Amani</b><small>IGMK-27-002 · Esthétique janv. 2027</small></div><a href="#" onclick="document.getElementById('q').focus();return false">Changer</a></div>
<div class="fld"><label>Échéance <em class="auto">proposée automatiquement</em></label><div class="ech"><label class="on"><input type="radio" name="e" checked><b>Acompte inscription</b><span>Dû le 25/11</span><i>50 000 F</i></label><label><input type="radio" name="e"><b>Mensualité 1</b><span>Dû le 05/01</span><i>85 000 F</i></label></div></div>
<div class="fld"><label>Mode de paiement</label><div class="modes" id="modes"><span data-m="link" class="on">Lien de paiement</span><span data-m="sms">Mobile Money déjà reçu</span><span data-m="cash">Espèces</span><span data-m="bank">Virement</span></div></div>
<div class="mpanel on" data-p="link"><div class="info ok"><b>Recommandé — zéro saisie.</b> L'élève reçoit un lien sur WhatsApp et paie avec Orange Money, MTN, Moov ou Wave. Le paiement, la référence et le reçu sont enregistrés automatiquement.</div>
<div class="kv" style="margin-top:14px"><div><span>Envoyé au</span>+225 07 10 20 40 00</div><div><span>Montant</span>50 000 F</div></div></div>
<div class="mpanel" data-p="sms"><label class="lab">Collez le SMS de confirmation reçu par l'école</label>
<textarea class="inp ta" id="sms" oninput="parse()">Vous avez reçu 50000 FCFA de GRACE AMANI (0710204000). Ref: MP261122.1014. Nouveau solde: 1 254 300 FCFA.</textarea>
<div class="det" id="det"></div><p class="hint">…ou <a href="#">importer une capture d'écran</a> : la référence est lue automatiquement.</p></div>
<div class="mpanel" data-p="cash"><div class="info"><b>Aucune référence à saisir.</b> Le numéro de reçu est généré automatiquement : <span class="mono">R-26-1183</span>.</div>
<div class="fld" style="margin-top:14px"><label>Montant reçu (FCFA)</label><input class="inp big" value="50 000"></div><div class="rendu">Rendu monnaie : <b>0 F</b></div></div>
<div class="mpanel" data-p="bank"><div class="info">Le virement apparaîtra dans le <b>rapprochement bancaire</b> : il suffira de valider la ligne correspondante, sans rien taper.</div></div>
</div>
<div class="mf"><label class="ck"><input type="checkbox" checked> Envoyer le reçu par WhatsApp</label><div class="row"><button class="btn" onclick="closePay()">Annuler</button><button class="btn p" id="go">Envoyer le lien</button></div></div>
</div></div>
<script>
const P=document.getElementById('pay'),G=document.getElementById('go'),LB={link:'Envoyer le lien',sms:'Valider et générer le reçu',cash:'Encaisser et imprimer le reçu',bank:'Ouvrir le rapprochement'};
function openPay(){P.classList.add('on');parse()}function closePay(){P.classList.remove('on')}
document.addEventListener('keydown',e=>e.key==='Escape'&&closePay());
document.getElementById('modes').onclick=e=>{const s=e.target.closest('span');if(!s)return;document.querySelectorAll('#modes span').forEach(x=>x.classList.toggle('on',x===s));document.querySelectorAll('.mpanel').forEach(x=>x.classList.toggle('on',x.dataset.p===s.dataset.m));G.textContent=LB[s.dataset.m]};
document.querySelectorAll('.ech label').forEach(l=>l.onclick=()=>{document.querySelectorAll('.ech label').forEach(x=>x.classList.toggle('on',x===l))});
const ST=[['Grâce Amani','IGMK-27-002'],['Awa Koné','IGMK-26-014'],['Aïcha Konaté','IGMK-26-018'],['Fatoumata Diallo','IGMK-26-021'],['Mariam Ouattara','IGMK-26-033']];
function sug(v){const b=document.getElementById('sugg');v=v.toLowerCase();b.innerHTML=v?ST.filter(s=>(s[0]+s[1]).toLowerCase().includes(v)).map(s=>`<a href="#" onclick="choose('${s[0]}','${s[1]}');return false"><b>${s[0]}</b><small>${s[1]}</small></a>`).join(''):'';}
function choose(n,m){document.getElementById('q').value=n;document.getElementById('sugg').innerHTML='';const p=document.getElementById('pick');p.querySelector('b').textContent=n;p.querySelector('small').textContent=m;p.querySelector('.ini').textContent=n.split(' ').map(w=>w[0]).join('')}
function parse(){const t=document.getElementById('sms').value,d=document.getElementById('det');
const ref=(t.match(/r[ée]f(?:[ée]rence)?\.?\s*:?\s*([A-Z0-9][A-Z0-9.\-]{4,}[A-Z0-9])/i)||[])[1],amt=(t.match(/(\d[\d\s]{2,})\s*F(?:CFA)?/i)||[])[1],tel=(t.match(/\(?(0\d{9})\)?/)||[])[1];
const ok=a=>a?'<i class="y">✓</i>':'<i class="n">?</i>';
d.innerHTML=`<div>${ok(ref)}<span>Référence</span><b>${ref||'non trouvée'}</b></div><div>${ok(amt)}<span>Montant</span><b>${amt?amt.replace(/\s/g,'').replace(/\B(?=(\d{3})+$)/g,' ')+' F':'—'}</b></div><div>${ok(tel)}<span>Numéro</span><b>${tel||'—'}</b></div>`+(amt&&+amt.replace(/\s/g,'')===50000?'<p class="match">✓ Le montant correspond à l’échéance sélectionnée.</p>':'')}
</script>'''
shell("paiements.html","Paiements",pay+MODAL,"paiements.html")

# ---------------- STAGES ----------------
SG=[("Awa Koné","Esthétique","Spa Riviera","Cocody",3,"28/11","ok","Bon démarrage"),("Prisca Yao","Esthétique","Institut Belle Ivoire","Plateau",11,"25/11","ok","Très bien"),("Aïcha Konaté","Coiffure","Salon Prestige Hair","Yopougon",6,"02/12","warn","Retards signalés"),
 ("Kadi Touré","Coiffure","Nappy Queen","Marcory",8,"—","bad","Visite en retard"),("Sandrine Kouadio","Esthétique","Zen Spa Angré","Cocody Angré",12,"30/11","ok","Proposition d'embauche"),("Fatou Bamba","Onglerie","Nails Factory","Treichville",4,"05/12","ok","RAS")]
st="".join(f'<tr><td><div class="who">{ini(n)}<div><b>{n}</b><small>{f}</small></div></div></td><td><div class="who"><span class="ini" style="border-radius:10px;background:#f6efe9;color:var(--brown)">{i[0]}{i.split()[-1][0]}</span><div><b>{i}</b><small>{q}</small></div></div></td><td><div style="display:flex;align-items:center;gap:10px;min-width:150px"><div class="prog" style="flex:1"><i style="width:{w/13*100:.0f}%"></i></div><small>S{w}/13</small></div></td><td>{v}</td><td><span class="bd {c}">{e}</span></td><td><button class="dots">⋯</button></td></tr>' for n,f,i,q,w,v,c,e in SG)
PART=[("Spa Riviera","Cocody · Esthétique",3,4),("Salon Prestige Hair","Yopougon · Coiffure",4,4),("Institut Belle Ivoire","Plateau · Esthétique",2,3),("Nappy Queen","Marcory · Coiffure",1,3),("Zen Spa Angré","Cocody Angré · Esthétique",2,2),("Nails Factory","Treichville · Onglerie",1,2)]
stg=f'''<div class="ph"><div><small>Pilotage</small><h1>Stages <i>· 3 mois sur le terrain</i></h1><p>Affectations, suivi hebdomadaire, visites et évaluations.</p></div><div class="row"><a class="btn" href="#">{ic("dl")}Conventions</a><a class="btn p" href="#">{ic("plus")}Affecter un stage</a></div></div>
<div class="grid g4" style="margin-bottom:22px">
<div class="card kpi dark"><span>Stagiaires sur le terrain</span><b>18</b><em style="color:var(--vl)">14 instituts</em><div class="ico">{ic("stage")}</div></div>
<div class="card kpi"><span>À affecter (janv.)</span><b style="color:var(--warn)">11</b><em>Fin des cours le 20/12</em><div class="ico">{ic("users")}</div></div>
<div class="card kpi"><span>Visites cette semaine</span><b>5</b><em class="down">1 en retard</em><div class="ico">{ic("cal")}</div></div>
<div class="card kpi"><span>Embauches après stage</span><b>41 <small>%</small></b><em class="up">Promo 2025</em><div class="ico">{ic("cert")}</div></div></div>
<div class="tools"><button class="chip on">En cours <em>18</em></button><button class="chip">À affecter <em>11</em></button><button class="chip">Terminés <em>64</em></button><span style="flex:1"></span><select class="sel"><option>Toutes les formations</option></select><select class="sel"><option>Tous les quartiers</option></select></div>
<div class="tw"><table><thead><tr><th>Stagiaire</th><th>Institut</th><th>Avancement</th><th>Prochaine visite</th><th>Suivi</th><th></th></tr></thead><tbody>{st}</tbody></table></div>
<div class="grid g21" style="margin-top:18px">
<div class="card"><div class="hd"><h3>À affecter — fin de cours 20 déc.</h3><span class="bd warn">11 élèves</span></div><p style="font-size:12.5px;color:var(--mute);margin:-6px 0 10px">Suggestions selon la formation, le quartier de l'élève et les places libres.</p>'''+"".join(f'<div class="li">{ini(n)}<div class="who"><div><b>{n}</b><small>{f} · habite {q}</small></div></div><div class="r" style="display:flex;align-items:center;gap:10px"><div style="text-align:right"><small>Suggestion</small><b>{i}</b></div><a class="btn v" style="height:34px;padding:0 12px" href="#">Affecter</a></div></div>' for n,f,q,i in [("Grâce Amani","Esthétique","Yopougon","Spa Riviera"),("Fatoumata Diallo","Coiffure","Abobo","Nappy Queen"),("Mariam Ouattara","Onglerie","Treichville","Nails Factory"),("Josiane Tanoh","Esthétique","Plateau","Institut Belle Ivoire")])+'''</div>
<div class="card"><div class="hd"><h3>Instituts partenaires</h3><a href="#">Tous (42) →</a></div>'''+"".join(f'<div style="padding:10px 0;border-bottom:1px solid var(--line)"><div class="row" style="justify-content:space-between"><div><b style="font-weight:600">{n}</b><small style="display:block;color:var(--mute);font-size:12px">{q}</small></div><small style="color:var(--{"bad" if a==b else "mute"});font-weight:600">{a} / {b} places</small></div><div class="prog {"bad" if a==b else ""}" style="margin-top:8px"><i style="width:{a/b*100:.0f}%"></i></div></div>' for n,q,a,b in PART)+'''</div></div>
<div class="grid g2" style="margin-top:18px"><div class="card"><div class="hd"><h3>Dernière évaluation reçue</h3><span class="bd ok">Prisca Yao · S10</span></div>'''+"".join(f'<div class="note"><div><b style="font-weight:600">{c}</b></div><div class="stars">{"★"*n}<span>{"★"*(5-n)}</span></div></div>' for c,n in [("Maîtrise technique",5),("Ponctualité",4),("Relation clientèle",5),("Hygiène & tenue",5),("Autonomie",4)])+'''<p style="margin-top:14px;font:300 italic 19px/1.4 var(--serif)">« Très professionnelle, les clientes la demandent déjà. Nous souhaitons la garder après le stage. »</p><small style="color:var(--mute)">Mme Diabaté — Institut Belle Ivoire · rempli via le lien WhatsApp</small></div>
<div class="card"><div class="hd"><h3>Visites de la semaine</h3><a href="#">Agenda →</a></div>'''+"".join(f'<div class="li"><div style="width:62px"><b style="font:400 24px var(--serif);display:block">{d}</b><small style="color:var(--mute)">{m}</small></div><div class="who"><div><b>{n}</b><small>{i} · {h}</small></div></div><div class="r"><span class="bd {c}">{s}</span></div></div>' for d,m,n,i,h,c,s in [("25","nov.","Prisca Yao","Belle Ivoire","10h","ok","Confirmée"),("27","nov.","Kadi Touré","Nappy Queen","14h","bad","À replanifier"),("28","nov.","Awa Koné","Spa Riviera","11h","ok","Confirmée"),("30","nov.","Sandrine Kouadio","Zen Spa Angré","9h","gr","À confirmer")])+'</div></div>'

# ---- annuaire complet des instituts (fictif) ----
INST=[("Spa Riviera","Cocody","Riviera 3","Esthétique",3,4,"Laure Achi"),("Zen Spa Angré","Cocody","Angré 8e tranche","Esthétique",2,2,"Awa Diabaté"),("Institut Les Perles","Cocody","II Plateaux Vallon","Esthétique",1,3,"Nadia Bah"),("Salon Élégance","Cocody","Saint-Jean","Coiffure",0,2,"Paul Gnagne"),("Nails Studio Riviera","Cocody","Riviera Palmeraie","Onglerie",1,2,"Sonia Yéo"),
("Salon Prestige Hair","Yopougon","Millionnaire","Coiffure",4,4,"Rose Aké"),("Beauté Divine","Yopougon","Niangon","Esthétique",1,3,"Odile Kassi"),("Afro Style Yop","Yopougon","Selmer","Coiffure",2,3,"Ali Sylla"),("Institut Maya","Yopougon","Siporex","Esthétique",0,2,"Maya Kouamé"),("Glam Nails","Yopougon","Toits Rouges","Onglerie",1,2,"Linda Gbê"),
("Institut Belle Ivoire","Plateau","Avenue Chardy","Esthétique",2,3,"Mme Diabaté"),("Spa du Plateau","Plateau","Rue du Commerce","Massage",1,2,"Ines Touré"),
("Nappy Queen","Marcory","Zone 4","Coiffure",1,3,"Fanta Koné"),("Beauty Lounge Zone 4","Marcory","Zone 4C","Esthétique",2,3,"Chloé Adou"),("Maquillage Pro Studio","Marcory","Biétry","Maquillage",1,2,"Eva N'Dri"),("Salon Anoumabo","Marcory","Anoumabo","Coiffure",0,2,"Joël Brou"),
("Nails Factory","Treichville","Avenue 16","Onglerie",1,2,"Grace Koffi"),("Salon Arras","Treichville","Arras","Coiffure",2,3,"Moussa Bamba"),("Institut Soleil","Treichville","Belleville","Esthétique",0,2,"Aimée Tano"),
("Coiffure Abobo Gare","Abobo","Abobo Gare","Coiffure",2,3,"Kader Ouédraogo"),("Institut Grâce","Abobo","Avocatier","Esthétique",1,2,"Grâce Djédjé"),("Salon N'Dotré","Abobo","N'Dotré","Coiffure",1,2,"Salif Diarra"),
("Beauté Adjamé","Adjamé","220 Logements","Esthétique",1,2,"Rita Kouassi"),("Salon Williamsville","Adjamé","Williamsville","Coiffure",0,2,"Yao Kan"),
("Institut Remblais","Koumassi","Remblais","Esthétique",1,2,"Pascale Amon"),("Koumassi Hair","Koumassi","Sicogi","Coiffure",2,3,"Issa Coulibaly"),("Spa Prodomo","Koumassi","Prodomo","Massage",0,2,"Mariette Ehui"),
("Salon Gonzagueville","Port-Bouët","Gonzagueville","Coiffure",1,2,"Hervé Assi"),("Institut Vridi","Port-Bouët","Vridi Cité","Esthétique",0,2,"Clarisse Lago"),
("Salon Locodjro","Attécoubé","Locodjro","Coiffure",1,2,"Bintou Traoré"),
("Bingerville Beauté","Bingerville","Centre","Esthétique",1,2,"Hélène Yapo"),("Déco & Events Binger","Bingerville","Santai","Décoration",1,2,"Firmin Aka"),("Salon Féh Kessé","Bingerville","Féh Kessé","Coiffure",0,2,"Ange Kra"),
("Institut Anyama","Anyama","Centre","Esthétique",0,2,"Odette Bi"),("Salon Anyama Belle","Anyama","Ebimpé","Coiffure",1,2,"Karim Fofana"),
("Songon Spa","Songon","Songon Agban","Massage",0,2,"Lucie Mel"),("Event Déco Cocody","Cocody","Danga","Décoration",0,2,"Serge Loukou"),
("Institut Ivoire Glow","Yopougon","Ananeraie","Esthétique",1,2,"Estelle Gogoua"),("Salon Bel Air","Yopougon","Sideci","Coiffure",1,3,"Mamadou Konaté"),
("Ongles d'Or","Plateau","Indénié","Onglerie",0,2,"Viviane Achy"),("Salon Port-Bouët Centre","Port-Bouët","Centre","Coiffure",0,2,"Alain Kipré"),("Beauté Koumassi Campement","Koumassi","Campement","Esthétique",1,2,"Nina Gba")]
from collections import Counter
CC=Counter(c for _,c,*_ in INST)
SPC={"Esthétique":"vi","Coiffure":"","Onglerie":"ok","Massage":"warn","Maquillage":"vi","Décoration":"gr"}
arows="".join(f'<tr data-c="{c}" data-q="{(n+" "+c+" "+q+" "+sp).lower()}"><td><div class="who"><span class="ini" style="border-radius:10px;background:#f6efe9;color:var(--brown)">{n.replace("’","").split()[0][0]}{n.split()[-1][0]}</span><div><b>{n}</b><small>{m}</small></div></div></td><td><b style="font-weight:600">{c}</b><small style="display:block;color:var(--mute)">{q}</small></td><td><span class="bd {SPC[sp]}">{sp}</span></td><td><div style="display:flex;align-items:center;gap:10px;min-width:120px"><div class="prog {"bad" if a==b else "ok" if a==0 else ""}" style="flex:1"><i style="width:{max(a/b*100,4):.0f}%"></i></div><small>{a}/{b}</small></div></td><td>{"<span class=\'bd bad\'>Complet</span>" if a==b else f"<span class=\'bd ok\'>{b-a} place{"s" if b-a>1 else ""}</span>"}</td><td><a class="btn" style="height:32px;padding:0 12px" href="#">Voir</a></td></tr>' for n,c,q,sp,a,b,m in sorted(INST,key=lambda x:(x[1],x[0])))
ANNUAIRE=f'''<div class="card" id="annuaire" style="margin-top:18px"><div class="hd"><div><h3>Annuaire des instituts partenaires</h3><small style="color:var(--mute)">{len(INST)} instituts · {len(CC)} communes · {sum(b-a for *_,a,b,_ in INST)} places libres</small></div><div class="row"><label class="search" style="height:38px;max-width:260px">{ic("search").replace("<svg","<svg width=16 stroke=currentColor fill=none stroke-width=1.8")}<input id="aq" placeholder="Rechercher un institut…"></label><a class="btn p" href="#">{ic("plus")}Ajouter un institut</a></div></div>
<div class="tools" id="acom"><button class="chip on" data-c="">Toutes <em>{len(INST)}</em></button>'''+"".join(f'<button class="chip" data-c="{c}">{c} <em>{n}</em></button>' for c,n in sorted(CC.items(),key=lambda x:-x[1]))+f'''</div>
<div class="tw" style="border:0"><table style="min-width:760px"><thead><tr><th>Institut</th><th>Commune</th><th>Spécialité</th><th>Stagiaires</th><th>Disponibilité</th><th></th></tr></thead><tbody id="atb">{arows}</tbody></table></div>
<p id="anone" style="display:none;text-align:center;padding:30px;color:var(--mute)">Aucun institut ne correspond.</p><div class="pager"><span id="acnt"></span><span>Trié par commune</span></div></div>
<script>(()=>{{let c='';const q=document.getElementById('aq'),R=[...document.querySelectorAll('#atb tr')];
function f(){{const v=q.value.toLowerCase();let n=0;R.forEach(r=>{{const ok=(!c||r.dataset.c===c)&&(!v||r.dataset.q.includes(v));r.style.display=ok?'':'none';n+=ok}});document.getElementById('acnt').textContent=n+' institut'+(n>1?'s':'')+' affiché'+(n>1?'s':'');document.getElementById('anone').style.display=n?'none':'block'}}
document.getElementById('acom').onclick=e=>{{const b=e.target.closest('button');if(!b)return;c=b.dataset.c;document.querySelectorAll('#acom .chip').forEach(x=>x.classList.toggle('on',x===b));f()}};q.oninput=f;f()}})();</script>'''
stg=stg.replace('<a href="#">Tous (42) →</a>','<a href="#annuaire">Tous ('+str(len(INST))+') →</a>')
shell("stages.html","Stages",stg+ANNUAIRE,"stages.html")

# ---------------- CLASSES ----------------
CL=[("Esthétique A","Juil. 2026","Mme Kouassi","Salle 1",18,20,78,"Massage"),("Coiffure B","Juil. 2026","M. Bamba","Salle 2",16,20,72,"Perruques & lace"),("Esthétique C","Jan. 2026","Mme Kouassi","Stage",17,20,100,"En stage"),
    ("Spé. Maquillage","Nov. 2026","Mme Kouakou","Salle 4",10,10,60,"Maquillage mariée"),("Spé. Onglerie","Nov. 2026","Mme Yao","Salle 4",8,10,45,"Gel & résine"),("Esthétique A","Jan. 2027","—","Salle 1",18,20,0,"Démarre le 12/01")]
cards="".join(f'<div class="card ccl{" sel" if i==0 else ""}"><div class="row" style="justify-content:space-between"><span class="bd {"vi" if p<100 and p>0 else "ok" if p==100 else "gr"}">{pr}</span><button class="dots">⋯</button></div><h3 style="margin:12px 0 4px">{n}</h3><small style="color:var(--mute)">{f} · {s}</small><div class="row" style="justify-content:space-between;margin:16px 0 8px"><small style="color:var(--mute)">Programme</small><b style="font-weight:600">{p} %</b></div><div class="prog"><i style="width:{p}%"></i></div><div class="cft"><span><b>{e}</b>/{c} élèves</span><span>▸ {m}</span></div></div>' for i,(n,pr,f,s,e,c,p,m) in enumerate(CL))
MODS=[("Soins du visage","done"),("Soins du corps","done"),("Épilation","done"),("Manucure","done"),("Pédicure","done"),("Massage","now"),("Maquillage",""),("Cosmétique",""),("Dermatologie esthétique",""),("Biologie esthétique",""),("Insertion professionnelle","")]
APPEL=[("Awa Koné","p"),("Aminata Fofana","p"),("Bintou Sangaré","r"),("Christelle Ehui","p"),("Diane Koffi","a"),("Estelle Yapi","p"),("Fanta Camara","p"),("Hélène Djè","p")]
appel="".join(f'<div class="li">{ini(n)}<div class="who"><div><b>{n}</b></div></div><div class="r"><div class="pa" data-v="{v}"><button data-k="p" title="Présente">P</button><button data-k="r" title="Retard">R</button><button data-k="a" title="Absente">A</button></div></div></div>' for n,v in APPEL)
cls=f'''<div class="ph"><div><small>École</small><h1>Classes <i>& formations</i></h1><p>Groupes, programmes, appel et progression.</p></div><div class="row"><a class="btn" href="#">{ic("cal")}Emploi du temps</a><a class="btn p" href="#">{ic("plus")}Créer une classe</a></div></div>
<div class="grid g4" style="margin-bottom:22px">
<div class="card kpi dark"><span>Classes actives</span><b>5</b><em style="color:var(--vl)">+1 en janvier</em><div class="ico">{ic("class")}</div></div>
<div class="card kpi"><span>Présence aujourd'hui</span><b>92 <small>%</small></b><em>5 absentes · 2 retards</em><div class="ico">{ic("users")}</div></div>
<div class="card kpi"><span>Évaluations à saisir</span><b style="color:var(--warn)">3</b><em>Massage, Perruques, Gel</em><div class="ico">{ic("edit")}</div></div>
<div class="card kpi"><span>Salles occupées</span><b>4 <small>/ 5</small></b><em>Salle 3 libre à 14h</em><div class="ico">{ic("dash")}</div></div></div>
<div class="grid g3">{cards}</div>
<div class="grid g21" style="margin-top:18px">
<div class="card"><div class="hd"><div><h3>Esthétique A · Juillet 2026</h3><small style="color:var(--mute)">Mme Kouassi · Salle 1 · 18 élèves</small></div><div class="row"><a class="btn" href="#">Notes</a><a class="btn" href="#">Élèves</a></div></div>
<div class="mods">'''+"".join(f'<div class="mo {c}"><i>{"✓" if c=="done" else k+1}</i><b>{m}</b><small>{"Terminé" if c=="done" else "En cours · sem. 2/3" if c=="now" else "À venir"}</small></div>' for k,(m,c) in enumerate(MODS))+f'''</div>
<div class="grid g2" style="margin-top:20px"><div><h4 class="h4">Moyennes par module</h4>'''+"".join(f'<div style="margin-bottom:12px"><div class="row" style="justify-content:space-between;margin-bottom:6px"><span>{m}</span><b style="font-weight:600">{str(n).replace(".",",")}</b></div><div class="prog {"ok" if n>=14 else "warn"}"><i style="width:{n*5}%"></i></div></div>' for m,n in [("Soins du visage",15.2),("Soins du corps",14.6),("Épilation",13.1),("Manucure",15.8),("Pédicure",14.9)])+f'''</div>
<div><h4 class="h4">Élèves à accompagner</h4><div class="al warn"><svg viewBox="0 0 24 24"><path d="M12 3l10 18H2zM12 10v5M12 18v.5"/></svg><div><b>Diane Koffi</b><p>4 absences ce mois · moyenne 10,5</p></div></div><div class="al warn"><svg viewBox="0 0 24 24"><path d="M12 3l10 18H2zM12 10v5M12 18v.5"/></svg><div><b>Bintou Sangaré</b><p>Retards répétés (6)</p></div></div><div class="al vi"><svg viewBox="0 0 24 24"><circle cx="12" cy="9" r="6"/><path d="M8 14l-2 7 6-3 6 3-2-7"/></svg><div><b>Awa Koné · Fanta Camara</b><p>Meilleures moyennes · candidates « major de promo »</p></div></div></div></div></div>
<div class="card"><div class="hd"><div><h3>Appel du jour</h3><small style="color:var(--mute)">Soins du corps · 08:00</small></div><span class="bd ok" id="cnt"></span></div>{appel}<a class="btn p" style="width:100%;justify-content:center;margin-top:14px" href="#">Valider l'appel</a><p style="font-size:12px;color:var(--mute);text-align:center;margin-top:8px">Les parents des absentes sont prévenus par WhatsApp.</p></div></div>
<script>function cnt(){{const a=[...document.querySelectorAll('.pa')];document.getElementById('cnt').textContent=a.filter(x=>x.dataset.v!='a').length+' / '+a.length+' présentes'}}
document.querySelectorAll('.pa').forEach(g=>g.onclick=e=>{{const b=e.target.closest('button');if(b){{g.dataset.v=b.dataset.k;cnt()}}}});cnt();</script>'''
shell("classes.html","Classes",cls,"classes.html")

# ---------------- EMPLOI DU TEMPS ----------------
H0,PX=8,64
def fh(h): return f"{int(h)}h{int(round((h%1)*60)):02d}".replace("h00","h")
days=["Lun 24","Mar 25","Mer 26","Jeu 27","Ven 28"]
hours="".join(f'<span style="top:{(h-H0)*PX}px">{h}h</span>' for h in range(8,18))
def cal(EV, key, lines, conflict_keys):
    cols=""
    for d in range(5):
        evs=[e for e in EV if e["d"]==d]; html=""
        for e in evs:
            ov=[x for x in evs if x["s"]<e["e"] and e["s"]<x["e"]]; k=ov.index(e); n=len(ov)
            conf=any(x is not e and any(x.get(c) and x.get(c)==e.get(c) for c in conflict_keys) for x in ov)
            html+=f'<div class="ev {e["t"]}{" conf" if conf else ""}" data-k="{e[key]}" style="top:{(e["s"]-H0)*PX}px;height:{(e["e"]-e["s"])*PX-4}px;left:calc({k}*100%/{n} + 3px);width:calc(100%/{n} - 6px)"><b>{e["ti"]}</b><small>{fh(e["s"])} – {fh(e["e"])}</small>'+"".join(f"<small>{l(e)}</small>" for l in lines[:-1])+f'<em>{lines[-1](e)}</em>{"<i title=Conflit>!</i>" if conf else ""}</div>'
        cols+=f'<div class="dc{" today" if d==0 else ""}"><div class="dh">{days[d]}</div><div class="db" style="height:{9*PX}px">{html}{"<span class=nowline style=top:"+str(int((10.4-H0)*PX))+"px></span>" if d==0 else ""}</div></div>'
    return f'<div class="cal"><div class="hc"><div class="dh"></div><div class="hb" style="height:{9*PX}px">{hours}</div></div>{cols}</div>'
def E(d,s,e,ti,t,**k): return dict(d=d,s=s,e=e,ti=ti,t=t,**k)

# --- élèves : uniquement les cours et évaluations ---
ES=[E(0,8,12,"Soins du visage","e",cl="Esthétique A",f="Mme Kouassi",r="Salle 1"),E(0,8,12,"Tresses & nattes","c",cl="Coiffure B",f="M. Bamba",r="Salle 2"),E(0,13,15,"Cosmétologie","t",cl="Esthétique A",f="Dr Adegoke",r="Salle 3"),E(0,13,16.5,"Maquillage mariée","s",cl="Spé. Maquillage",f="Mme Kouakou",r="Salle 4"),E(0,13,15,"Coiffure moderne","c",cl="Coiffure B",f="M. Bamba",r="Salle 2"),
E(1,8,12,"Soins du corps","e",cl="Esthétique A",f="Mme Kouassi",r="Salle 1"),E(1,8,10.5,"Coiffure moderne","c",cl="Coiffure B",f="M. Bamba",r="Salle 2"),E(1,10.5,12,"Biologie capillaire","t",cl="Coiffure B",f="Dr Adegoke",r="Salle 3"),E(1,13,16,"Gel & résine","s",cl="Spé. Onglerie",f="Mme Yao",r="Salle 4"),E(1,13,15,"Tissage","c",cl="Coiffure B",f="M. Bamba",r="Salle 2"),
E(2,8,12,"Épilation","e",cl="Esthétique A",f="Mme Kouassi",r="Salle 1"),E(2,8,12,"Perruques & lace","c",cl="Coiffure B",f="M. Bamba",r="Salle 2"),E(2,13,15,"Dermatologie","t",cl="Esthétique A",f="Dr Adegoke",r="Salle 3"),E(2,13,16.5,"Contouring","s",cl="Spé. Maquillage",f="Mme Kouakou",r="Salle 4"),
E(3,8,12,"Massage","e",cl="Esthétique A",f="Mme Kouassi",r="Salle 1"),E(3,8,12,"Tissage (suite)","c",cl="Coiffure B",f="M. Bamba",r="Salle 2"),E(3,13,16,"Nail art","s",cl="Spé. Onglerie",f="Mme Yao",r="Salle 4"),E(3,13,16,"Déco de salle","s",cl="Spé. Décoration",f="M. Traoré",r="Salle 5"),E(3,14,16,"Insertion pro","t",cl="Coiffure B",f="M. Coulibaly",r="Salle 4"),
E(4,8,11,"Évaluation pratique","x",cl="Esthétique A",f="Mme Kouassi",r="Salle 1"),E(4,8,11,"Évaluation pratique","x",cl="Coiffure B",f="M. Bamba",r="Salle 2"),E(4,11,12,"Bilan de semaine","t",cl="Toutes",f="Direction",r="Salle 3")]
calS=cal(ES,"cl",[lambda e:f'{e["cl"]} · {e["r"]}',lambda e:e["f"]],["r"])
# --- personnel : cours donnés + réunions, permanences, visites, congés… ---
EP=[E(0,8,12,"Cours · Soins du visage","k",p="Mme Kouassi",w="Salle 1"),E(0,8,12,"Cours · Tresses","k",p="M. Bamba",w="Salle 2"),E(0,8,12,"Accueil & inscriptions","p",p="Mlle Gnamien",w="Accueil"),E(0,9,10,"Point direction","r",p="Direction",w="Bureau DG"),E(0,13,15,"Cours · Cosmétologie","k",p="Dr Adegoke",w="Salle 3"),E(0,13,17,"Congé","a",p="Mme Yao",w="—"),E(0,14,15.5,"Rendez-vous candidates","d",p="Mlle Gnamien",w="Accueil"),
E(1,8,12,"Cours · Soins du corps","k",p="Mme Kouassi",w="Salle 1"),E(1,9,11,"Visite de stage · Prisca Y.","v",p="Dr Gboze",w="Institut Belle Ivoire"),E(1,10.5,12,"Cours · Biologie capillaire","k",p="Dr Adegoke",w="Salle 3"),E(1,13,16,"Cours · Gel & résine","k",p="Mme Yao",w="Salle 4"),E(1,14,16,"Clôture de caisse","p",p="M. Coulibaly",w="Comptabilité"),
E(2,8,12,"Cours · Épilation","k",p="Mme Kouassi",w="Salle 1"),E(2,8,10,"Formation interne · Hygiène","f",p="Formateurs",w="Salle prof"),E(2,8,12,"Cours · Perruques","k",p="M. Bamba",w="Salle 2"),E(2,13,15,"Cours · Dermatologie","k",p="Dr Adegoke",w="Salle 3"),E(2,14,16,"Visite de stage · Kadi T.","v",p="Dr Gboze",w="Nappy Queen"),
E(3,8,12,"Cours · Massage","k",p="Mme Kouassi",w="Salle 1"),E(3,9,10,"Point direction","r",p="Direction",w="Bureau DG"),E(3,11,12,"Visite de stage · Awa K.","v",p="Dr Gboze",w="Spa Riviera"),E(3,13,16,"Cours · Nail art","k",p="Mme Yao",w="Salle 4"),E(3,14,16,"Cours · Insertion pro","k",p="M. Coulibaly",w="Salle 4"),E(3,13,17,"Absence (maladie)","a",p="M. Traoré",w="—"),
E(4,8,11,"Jury évaluation pratique","k",p="Mme Kouassi",w="Salle 1"),E(4,8,11,"Jury évaluation pratique","k",p="M. Bamba",w="Salle 2"),E(4,11,12,"Bilan de semaine","r",p="Direction",w="Salle 3"),E(4,14,16,"Réunion pédagogique","r",p="Formateurs",w="Salle prof"),E(4,15,17,"Paie des vacataires","p",p="M. Coulibaly",w="Comptabilité")]
calP=cal(EP,"p",[lambda e:e["w"],lambda e:e["p"]],["w"])
legS="".join(f'<span><i class="lg {c}"></i>{t}</span>' for c,t in [("e","Esthétique"),("c","Coiffure"),("s","Spécialisations"),("t","Théorie"),("x","Évaluation")])
legP="".join(f'<span><i class="lg {c}"></i>{t}</span>' for c,t in [("k","Cours donné"),("r","Réunion"),("v","Visite de stage"),("p","Permanence / admin"),("d","Rendez-vous"),("f","Formation interne"),("a","Congé / absence")])
nav=f'''<div class="row"><button class="btn" style="height:38px;width:38px;padding:0;justify-content:center">‹</button><button class="btn" style="height:38px">Aujourd'hui</button><button class="btn" style="height:38px;width:38px;padding:0;justify-content:center">›</button></div>'''
edt=f'''<div class="ph"><div><small>École</small><h1>Emploi du temps <i>· Semaine 48</i></h1><p>Du lundi 24 au vendredi 28 novembre 2026.</p></div><div class="row"><a class="btn" href="#">{ic("dl")}Imprimer / PDF</a><a class="btn p" href="#">{ic("plus")}Ajouter un événement</a></div></div>
<div class="vtabs" id="vt"><button class="on" data-v="el">{ic("users")}<span><b>Emploi du temps élèves</b><small>Cours et évaluations, par classe</small></span></button><button data-v="pe">{ic("staff")}<span><b>Emploi du temps personnel</b><small>Cours donnés, réunions, visites, congés…</small></span></button></div>

<div class="view on" data-v="el">
<div class="tools"><div class="seg"><button>Jour</button><button class="on">Semaine</button><button>Mois</button></div>{nav}<span style="flex:1"></span>
<select class="sel flt"><option value="">Toutes les classes</option><option>Esthétique A</option><option>Coiffure B</option><option>Spé. Maquillage</option><option>Spé. Onglerie</option><option>Spé. Décoration</option></select><a class="btn" style="height:38px" href="#">{ic("wa")}Envoyer aux élèves</a></div>
<div class="card" style="padding:0;overflow:hidden">{calS}<div class="legend" style="padding:14px 20px;border-top:1px solid var(--line);flex-wrap:wrap">{legS}</div></div>
<div class="grid g3" style="margin-top:18px;align-items:start">
<div class="card"><div class="hd"><h3>Conflit de salle</h3><span class="bd bad">1</span></div><div class="al bad"><svg viewBox="0 0 24 24"><path d="M12 3l10 18H2zM12 10v5M12 18v.5"/></svg><div><b>Jeudi 14h – 16h · Salle 4</b><p>« Nail art » et « Insertion pro » dans la même salle.</p></div></div><a class="btn" style="width:100%;justify-content:center" href="#">Proposer une salle libre</a></div>
<div class="card"><div class="hd"><h3>Évaluations à venir</h3></div>'''+"".join(f'<div class="li"><div style="width:56px"><b style="font:400 24px var(--serif);display:block">{d}</b><small style="color:var(--mute)">{m}</small></div><div class="who"><div><b>{t}</b><small>{c}</small></div></div></div>' for d,m,t,c in [("28","nov.","Évaluation pratique","Esthétique A · Coiffure B"),("05","déc.","Examen Maquillage","Spé. Maquillage"),("12","déc.","Examen final théorie","Esthétique A")])+'''</div>
<div class="card"><div class="hd"><h3>Occupation des salles</h3></div>'''+"".join(f'<div style="margin-bottom:12px"><div class="row" style="justify-content:space-between;margin-bottom:6px"><span>{n}</span><small style="color:var(--mute)">{h} h / 45</small></div><div class="prog"><i style="width:{h/45*100:.0f}%"></i></div></div>' for n,h in [("Salle 1",19),("Salle 2",24),("Salle 3",9),("Salle 4",17),("Salle 5",3)])+f'''</div></div></div>

<div class="view" data-v="pe">
<div class="tools"><div class="seg"><button>Jour</button><button class="on">Semaine</button><button>Mois</button></div>{nav}<span style="flex:1"></span>
<select class="sel flt"><option value="">Tout le personnel</option><option>Direction</option><option>Dr Adegoke</option><option>Dr Gboze</option><option>Mme Kouassi</option><option>M. Bamba</option><option>Mme Yao</option><option>M. Traoré</option><option>M. Coulibaly</option><option>Mlle Gnamien</option><option>Formateurs</option></select><a class="btn" style="height:38px" href="#">{ic("wa")}Envoyer au personnel</a></div>
<div class="card" style="padding:0;overflow:hidden">{calP}<div class="legend" style="padding:14px 20px;border-top:1px solid var(--line);flex-wrap:wrap">{legP}</div></div>
<div class="grid g3" style="margin-top:18px;align-items:start">
<div class="card"><div class="hd"><h3>Absences & congés</h3><span class="bd warn">2</span></div><div class="al warn"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg><div><b>Mme Yao · congé lundi après-midi</b><p>Aucun cours impacté.</p></div></div><div class="al bad"><svg viewBox="0 0 24 24"><path d="M12 3l10 18H2zM12 10v5M12 18v.5"/></svg><div><b>M. Traoré · absent jeudi</b><p>« Déco de salle » (13h–16h) à remplacer.</p></div></div><a class="btn" style="width:100%;justify-content:center" href="#">Trouver un remplaçant</a></div>
<div class="card"><div class="hd"><h3>Visites de stage</h3><a href="stages.html">Stages →</a></div>'''+"".join(f'<div class="li"><span class="ini">JG</span><div class="who"><div><b>{n}</b><small>{d} · {i}</small></div></div></div>' for n,d,i in [("Prisca Yao","Mar. 9h","Belle Ivoire"),("Kadi Touré","Mer. 14h","Nappy Queen"),("Awa Koné","Jeu. 11h","Spa Riviera")])+'''</div>
<div class="card"><div class="hd"><h3>Charge de la semaine</h3></div>'''+"".join(f'<div class="li"><span class="ini">{i}</span><div class="who"><div><b>{n}</b><small>{c}</small></div></div><div class="r"><b>{h} h</b></div></div>' for i,n,c,h in [("HK","Mme Kouassi","19 h de cours",19),("IB","M. Bamba","15 h de cours",15),("AM","Dr Adegoke","9 h cours + 3 h réunions",12),("JG","Dr Gboze","3 visites + réunions",8),("EG","Mlle Gnamien","Accueil · RDV",26)])+'''</div></div></div>
<script>(()=>{const T=document.getElementById('vt'),show=v=>{T.querySelectorAll('button').forEach(b=>b.classList.toggle('on',b.dataset.v===v));document.querySelectorAll('.view').forEach(x=>x.classList.toggle('on',x.dataset.v===v))};
T.onclick=e=>{const b=e.target.closest('button');if(b){show(b.dataset.v);history.replaceState(null,'',b.dataset.v==='pe'?'#personnel':'#eleves')}};if(location.hash==='#personnel')show('pe');
document.querySelectorAll('.view').forEach(v=>{const s=v.querySelector('.flt');s.onchange=()=>v.querySelectorAll('.ev').forEach(e=>e.classList.toggle('dim',s.value&&e.dataset.k!==s.value&&e.dataset.k!=='Toutes'))})})();</script>'''
shell("emploi.html","Emploi du temps",edt,"emploi.html")

# ---------------- CERTIFICATS ----------------
random.seed(3)
qr="".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for x in range(21) for y in range(21) if (x<7 and y<7) or (x>13 and y<7) or (x<7 and y>13) or random.random()<.45) 
qr=f'<svg viewBox="-1 -1 23 23" class="qr"><rect x="-1" y="-1" width="23" height="23" fill="#fff"/><g fill="#170A1C">{qr}</g>'+"".join(f'<rect x="{a+1}" y="{b+1}" width="5" height="5" fill="#fff"/><rect x="{a+2}" y="{b+2}" width="3" height="3" fill="#170A1C"/>' for a,b in [(0,0),(14,0),(0,14)])+'</svg>'
ELIG=[("Prisca Yao","Esthétique","Jan. 2026",1,1,1,"Très bien","ready"),("Sandrine Kouadio","Esthétique","Jan. 2026",1,1,1,"Bien","ready"),("Nadège Soro","Spé. Maquillage","Nov. 2026",1,None,1,"Bien","ready"),("Aïcha Konaté","Coiffure","Juil. 2026",1,0,1,"—","stage"),
      ("Awa Koné","Esthétique","Juil. 2026",1,0,0,"—","pay"),("Fatou Bamba","Onglerie","Nov. 2026",1,None,0,"—","pay"),("Corinne Aka","Esthétique","Jan. 2026",1,1,1,"Assez bien","signed"),("Rokia Cissé","Coiffure","Jan. 2026",1,1,1,"Bien","sent")]
def ck(v): return '<span class="ck2 na">—</span>' if v is None else f'<span class="ck2 {"y" if v else "n"}">{"✓" if v else "✕"}</span>'
STT={"ready":("bd vi","Prêt à signer"),"stage":("bd warn","Stage en cours"),"pay":("bd bad","Solde impayé"),"signed":("bd ok","Signé · à remettre"),"sent":("bd gr","Remis le 15/11")}
erows="".join(f'<tr><td><input type="checkbox"{" checked" if st=="ready" else ""}{" disabled" if st in ("stage","pay") else ""}></td><td><div class="who">{ini(n)}<div><b>{n}</b><small>{f} · {pr}</small></div></div></td><td style="text-align:center">{ck(a)}</td><td style="text-align:center">{ck(b)}</td><td style="text-align:center">{ck(c)}</td><td>{m}</td><td><span class="{STT[st][0]}">{STT[st][1]}</span></td><td><a class="btn" style="height:32px;padding:0 12px" href="#">Aperçu</a></td></tr>' for n,f,pr,a,b,c,m,st in ELIG)
reg="".join(f'<tr><td><span class="mono">{c}</span></td><td><b style="font-weight:600">{n}</b></td><td>{f}</td><td>{d}</td><td>{v}</td></tr>' for c,n,f,d,v in [("IGMK-C-2026-0187","Rokia Cissé","Coiffure","15/11/2026","3 vérifications"),("IGMK-C-2026-0186","Corinne Aka","Esthétique","14/11/2026","—"),("IGMK-C-2026-0185","Mireille Assi","Spé. Onglerie","02/11/2026","1 vérification"),("IGMK-C-2026-0184","Sarah Brou","Esthétique","20/10/2026","5 vérifications")])
cert=f'''<div class="ph"><div><small>École</small><h1>Certificats <i>· Promo janvier 2026</i></h1><p>Génération, signature, remise et vérification en ligne.</p></div><div class="row"><select class="sel"><option>Promo janvier 2026</option><option>Promo juillet 2026</option><option>Spécialisations nov. 2026</option></select><a class="btn p" href="#">{ic("edit")}Signer la sélection (3)</a></div></div>
<div class="grid g4" style="margin-bottom:22px">
<div class="card kpi dark"><span>Prêts à signer</span><b>11</b><em style="color:var(--vl)">toutes conditions remplies</em><div class="ico">{ic("cert")}</div></div>
<div class="card kpi"><span>Bloqués</span><b style="color:var(--warn)">6</b><em>stage ou solde manquant</em><div class="ico">{ic("alert")}</div></div>
<div class="card kpi"><span>Délivrés en 2026</span><b>187</b><em class="up">▲ +22 vs. 2025</em><div class="ico">{ic("dl")}</div></div>
<div class="card kpi"><span>Vérifications employeurs</span><b>64</b><em>via QR code ce mois</em><div class="ico">{ic("search")}</div></div></div>
<div class="grid g21">
<div class="card"><div class="hd"><div><h3>Éligibilité</h3><small style="color:var(--mute)">Le certificat n'est délivrable que si les 3 conditions sont remplies.</small></div><div class="row"><button class="chip on">Tous</button><button class="chip">Prêts</button><button class="chip">Bloqués</button></div></div>
<div class="tw" style="border:0"><table style="min-width:600px"><thead><tr><th style="width:30px"></th><th>Élève</th><th style="text-align:center">Formation<br>validée</th><th style="text-align:center">Stage<br>validé</th><th style="text-align:center">Solde<br>payé</th><th>Mention</th><th>Statut</th><th></th></tr></thead><tbody>{erows}</tbody></table></div>
<div class="row" style="margin-top:14px;justify-content:space-between"><small style="color:var(--mute)">3 sélectionnés · signature électronique du Directeur général</small><div class="row"><a class="btn" href="#">{ic("wa")}Relancer les soldes impayés</a><a class="btn v" href="#">Générer & signer</a></div></div></div>
<div class="card"><div class="hd"><h3>Aperçu</h3><a href="#">PDF →</a></div>
<div class="cert"><div class="ci"><img class="clogo" src="img/cosmetique.jpg" alt=""><small class="ck">Institut GMK Formation · Abidjan</small><h2>Certificat <i>de formation</i></h2><p class="cp">Le Directeur général atteste que</p>
<div class="cn">Prisca Yao</div><p class="cp">a suivi avec succès la formation professionnelle en</p><div class="cf">Esthétique</div><p class="cp">6 mois de formation pratique et théorique · 3 mois de stage en institut<br>Mention <b>Très bien</b> · Promotion janvier 2026</p>
<div class="cs"><div><span class="sig">Batiye</span><small>K. N'Si Batiye<br>Directeur général</small></div><div class="seal2">IGMK<br><small>2012</small></div><div style="text-align:right">{qr}<small>N° IGMK-C-2026-0188<br>Vérifier : igmk.ci/v</small></div></div></div></div>
<p style="font-size:12px;color:var(--mute);margin-top:12px;line-height:1.6">Le QR code permet à un employeur de vérifier en ligne l'authenticité du certificat : impossible à falsifier.</p></div></div>
<div class="grid g2" style="margin-top:18px"><div class="card"><div class="hd"><h3>Registre des certificats</h3><a href="#">Tout le registre →</a></div><div class="tw" style="border:0"><table style="min-width:560px"><thead><tr><th>Numéro</th><th>Titulaire</th><th>Formation</th><th>Délivré le</th><th>Vérifié</th></tr></thead><tbody>{reg}</tbody></table></div></div>
<div class="card"><div class="hd"><h3>Remise des certificats</h3><span class="bd vi">Cérémonie</span></div><div class="cd card" style="margin-bottom:16px"><small>Prochaine cérémonie</small><h3 style="font-size:28px;margin-top:6px">Samedi 13 décembre · 10h</h3><p style="margin-top:6px">Salle polyvalente · 48 diplômées · familles invitées</p></div>
<div class="li"><span class="ini">✓</span><div class="who"><div><b>Invitations envoyées</b><small>41 / 48 confirmées par WhatsApp</small></div></div></div><div class="li"><span class="ini">⎙</span><div class="who"><div><b>Impression sur papier sécurisé</b><small>Prévue le 10 décembre</small></div></div></div><div class="li"><span class="ini">★</span><div class="who"><div><b>Majors de promo</b><small>Prisca Yao (Esthétique) · Rokia Cissé (Coiffure)</small></div></div></div></div></div>'''
shell("certificats.html","Certificats",cert,"certificats.html")

# ---------------- ACTUALITÉS DU SITE ----------------
F2="img/formations/"
A=[("esthetique/1.jpg","Rentrée","Rentrée de janvier 2027 : inscriptions ouvertes","Publié","ok","1 nov.","1 284",1,"12/01/2027","Formations"),
   ("onglerie/10.jpg","Promotion","−15 % sur les spécialisations","Publié","ok","15 nov.","932",1,"15/12/2026","Spécialisations"),
   ("maquillage/57.jpg","Événement","Journée portes ouvertes","Publié","ok","10 nov.","611",1,"06/12/2026","Contact"),
   ("coiffure/7.jpg","Stage","Début des stages, promo 2026","Publié","ok","2 nov.","402",1,"","Le stage"),
   ("coiffure/18.jpg","Diplômées","Cérémonie de remise des certificats","Programmé","vi","13 déc. 10h","—",0,"","Diplômées"),
   ("massage/4.jpg","Vie de l'école","Un nouvel espace massage & spa","Brouillon","gr","—","—",0,"","L'école"),
   ("esthetique/6.jpg","Stage","Trois nouveaux instituts partenaires","Archivé","gr","18 sept.","356",0,"","Le stage")]
rows="".join(f'<tr><td><div class="who"><img src="{F2}{im}" alt="" style="width:64px;height:46px;border-radius:8px;object-fit:cover"><div><b>{t}</b><small>{c} · lien → {lk}</small></div></div></td><td>{"<span class=\'bd vi\'>À la une</span>" if u else "—"}</td><td>{""+cd if cd else "—"}</td><td><span class="bd {sc}">{st}</span></td><td>{d}</td><td>{v}</td><td><button class="dots">⋯</button></td></tr>' for im,c,t,st,sc,d,v,u,cd,lk in A)
une="".join(f'<div class="une"><span class="hdl">⋮⋮</span><b>{i+1}</b><img src="{F2}{im}" alt=""><div><b>{t}</b><small>{c}{" · compte à rebours "+cd if cd else ""}</small></div></div>' for i,(im,c,t,st,sc,d,v,u,cd,lk) in enumerate([a for a in A if a[7]]))
act=f'''<div class="ph"><div><small>Site public</small><h1>Actualités <i>du site</i></h1><p>Publiez rentrées, promotions, stages et événements sans toucher au code.</p></div><div class="row"><a class="btn" href="https://gmk-formation-institute.github.io/GMK-Formation-Institute-Web-Site/actualites.html" target="_blank">Voir sur le site ↗</a><a class="btn p" href="#editeur">{ic("plus")}Nouvelle actualité</a></div></div>
<div class="grid g4" style="margin-bottom:22px">
<div class="card kpi dark"><span>Publiées</span><b>4</b><em style="color:var(--vl)">4 dans le carrousel d'accueil</em><div class="ico">{ic("news")}</div></div>
<div class="card kpi"><span>Programmées</span><b>1</b><em>13 déc. à 10h</em><div class="ico">{ic("clock")}</div></div>
<div class="card kpi"><span>Vues ce mois</span><b>3 229</b><em class="up">▲ 38 % vs. octobre</em><div class="ico">{ic("dash")}</div></div>
<div class="card kpi"><span>Clics WhatsApp générés</span><b>146</b><em>depuis les actualités</em><div class="ico">{ic("wa")}</div></div></div>
<div class="grid g21"><div class="card"><div class="hd"><h3>Toutes les actualités</h3><div class="row"><button class="chip on">Toutes <em>7</em></button><button class="chip">Publiées <em>4</em></button><button class="chip">Programmées <em>1</em></button><button class="chip">Brouillons <em>1</em></button></div></div>
<div class="tw" style="border:0"><table style="min-width:640px"><thead><tr><th>Actualité</th><th>Accueil</th><th>Compte à rebours</th><th>Statut</th><th>Publication</th><th>Vues</th><th></th></tr></thead><tbody>{rows}</tbody></table></div></div>
<div class="card"><div class="hd"><div><h3>Carrousel « À la une »</h3><small style="color:var(--mute)">Glissez pour changer l'ordre · défilement toutes les 5 s</small></div></div>{une}<div class="al vi" style="margin-top:14px"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg><div><b>Retrait automatique</b><p>Une actualité quitte le carrousel quand son compte à rebours est terminé.</p></div></div></div></div>

<div class="card" id="editeur" style="margin-top:18px"><div class="hd"><div><h3>Nouvelle actualité</h3><small style="color:var(--mute)">L'aperçu se met à jour pendant que vous écrivez.</small></div><span class="bd gr">Brouillon enregistré</span></div>
<div class="grid" style="grid-template-columns:1fr 1.1fr;gap:28px">
<div>
<div class="fld"><label>Titre</label><input class="inp" id="et" value="Journée portes ouvertes de décembre"></div>
<div class="kv"><div class="fld"><label>Catégorie</label><select class="inp" id="ec"><option>Événement</option><option>Rentrée</option><option>Promotion</option><option>Stage</option><option>Vie de l'école</option><option>Diplômées</option></select></div>
<div class="fld"><label>Le bouton « En savoir plus » mène vers</label><select class="inp"><option>Contact</option><option>Formations</option><option>Spécialisations</option><option>Le stage</option><option>WhatsApp</option></select></div></div>
<div class="fld"><label>Texte court</label><textarea class="inp ta" id="ed">Visitez nos ateliers, rencontrez les formateurs et assistez à des démonstrations en direct.</textarea></div>
<div class="fld"><label>Photo</label><div class="drop"><img src="{F2}maquillage/57.jpg" alt=""><div><b>maquillage-57.jpg</b><small>Glissez une nouvelle photo ou <a href="#">parcourir</a> · recadrage automatique</small></div></div></div>
<div class="kv"><div class="fld"><label>Date de publication</label><select class="inp"><option>Maintenant</option><option>Programmer…</option></select></div>
<div class="fld"><label class="tg"><input type="checkbox" id="ecd" checked> Afficher un compte à rebours</label><input class="inp" id="edate" type="datetime-local" value="2026-12-06T09:00"></div></div>
<div class="fld"><label class="tg"><input type="checkbox" checked> Mettre dans le carrousel « À la une » de l'accueil</label></div>
<div class="row" style="justify-content:flex-end;margin-top:8px"><a class="btn" href="#">Enregistrer le brouillon</a><a class="btn v" href="#">Publier sur le site</a></div></div>
<div><div class="h4">Aperçu sur le site — accueil</div>
<div class="pv"><div class="pvi"><img src="{F2}maquillage/57.jpg" alt=""></div><div class="pvt"><span class="pvtag" id="pc">Événement</span><h3 id="pt"></h3><p id="pd"></p><div class="pvcd" id="pcd"><small>Ouverture des portes dans</small><div><span><b data-u="d">00</b>jours</span><span><b data-u="h">00</b>heures</span><span><b data-u="m">00</b>min</span><span><b data-u="s">00</b>sec</span></div></div><div class="pvw"><span>En savoir plus →</span></div></div></div>
<div class="h4" style="margin-top:22px">Aperçu sur mobile</div><div class="pvm"><div class="pvi" style="height:150px"><img src="{F2}maquillage/57.jpg" alt=""></div><div class="pvt" style="padding:18px"><span class="pvtag" id="pc2">Événement</span><h3 id="pt2" style="font-size:24px"></h3></div></div></div></div></div>
<script>(()=>{{const $=i=>document.getElementById(i);function up(){{$('pt').textContent=$('pt2').textContent=$('et').value;$('pd').textContent=$('ed').value;$('pc').textContent=$('pc2').textContent=$('ec').value;$('pcd').style.display=$('ecd').checked?'':'none'}}
['et','ed','ec','ecd'].forEach(i=>$(i).addEventListener('input',up));$('ecd').onchange=up;up();
function t(){{let x=Math.max(0,(new Date($('edate').value)-new Date())/1000);const v={{d:Math.floor(x/86400),h:Math.floor(x%86400/3600),m:Math.floor(x%3600/60),s:Math.floor(x%60)}};document.querySelectorAll('#pcd b').forEach(b=>b.textContent=String(v[b.dataset.u]).padStart(2,'0'))}}t();setInterval(t,1000)}})();</script>'''
shell("actualites.html","Actualités du site",act,"actualites.html")

# ---------------- CONTENU DU SITE (front-office) ----------------
F2="img/formations/"
SECS=[("Accueil",[("Bandeau principal","hero",1),("Bandeau défilant","marq",1),("Actualités « À la une »","news",1),("Manifeste & chiffres","facts",1),("Méthode 80 / 20","meth",1),("Parcours en 3 étapes","jour",1),("Liste des formations","prog",1),("Le stage","stage",1),("Diplômées","alum",1),("Témoignage","testi",1),("Mot de la direction","lead",1),("Appel final","final",1)]),
      ("L'école",[]),("Formations",[]),("Esthétique",[]),("Coiffure",[]),("Spécialisations",[]),("Le stage",[]),("Diplômées",[]),("Galerie",[]),("Contact",[])]
tree=""
for pg,ss in SECS:
    if ss:
        tree+=f'<div class="tp open"><div class="tph">▾ {pg} <em>{len(ss)} sections</em></div>'+"".join(f'<div class="ts{" on" if k=="hero" else ""}"><span class="hdl">⋮⋮</span>{t}<label class="sw"><input type="checkbox"{" checked" if v else ""}><i></i></label></div>' for t,k,v in ss)+'</div>'
    else: tree+=f'<div class="tp"><div class="tph">▸ {pg}</div></div>'
TABS=[("pages","Pages & sections"),("forma","Formations & tarifs"),("media","Photos & vidéos"),("temo","Témoignages & diplômées"),("equipe","Direction & équipe"),("infos","Coordonnées & réglages")]
tabs='<div class="tabs" id="cmst">'+"".join(f'<a href="#" data-t="{k}"{" class=on" if i==0 else ""}>{t}</a>' for i,(k,t) in enumerate(TABS))+'</div>'
P_pages=f'''<div class="cms"><div class="card" style="padding:16px"><div class="hd" style="margin-bottom:10px"><h3 style="font-size:20px">Pages du site</h3></div><div class="tree">{tree}</div><p class="hint">Glissez pour réordonner · l'interrupteur masque une section sans la supprimer.</p></div>
<div class="card"><div class="hd"><div><small style="color:var(--v);font-weight:600;font-size:11px;letter-spacing:.16em;text-transform:uppercase">Accueil</small><h3>Bandeau principal</h3></div><span class="bd warn">Modifications non publiées</span></div>
<div class="fld"><label>Petit titre</label><input class="inp" id="h1" value="Depuis 2012 · Abidjan"></div>
<div class="fld"><label>Grand titre <em class="auto">la dernière ligne s'affiche en violet italique</em></label><textarea class="inp ta" id="h2" style="height:84px">L'excellence
s'apprend
à la main.</textarea></div>
<div class="fld"><label>Texte d'introduction</label><textarea class="inp ta" id="h3">La grande école ivoirienne de l'esthétique et de la coiffure. Quatre-vingts pour cent de pratique, un stage obligatoire en institut, et un métier pour la vie.</textarea></div>
<div class="kv"><div class="fld"><label>Bouton principal</label><input class="inp" id="h4" value="Découvrir les formations"></div><div class="fld"><label>Mène vers</label><select class="inp"><option>Page Formations</option><option>WhatsApp</option></select></div></div>
<div class="fld"><label>Photo ou vidéo de fond</label><div class="drop"><img id="himg" src="{F2}coiffure/1.jpg" alt=""><div><b>coiffure-atelier.jpg</b><small>Image ou vidéo courte (MP4) · <a href="#" data-t2="media">Choisir dans la médiathèque</a></small></div></div></div>
<div class="kv"><div class="fld"><label>Chiffre mis en avant</label><input class="inp" id="h5" value="500+"></div><div class="fld"><label>Légende</label><input class="inp" id="h6" value="Professionnelles formées"></div></div>
<div class="row" style="justify-content:space-between;margin-top:6px"><a class="btn" href="#">↶ Historique des versions</a><div class="row"><a class="btn" href="#">Enregistrer</a><a class="btn v" href="#">Publier sur le site</a></div></div></div>
<div class="card" style="padding:14px"><div class="hd" style="margin-bottom:10px"><h3 style="font-size:20px">Aperçu</h3><div class="seg"><button class="on">Ordinateur</button><button>Mobile</button></div></div>
<div class="spv"><div class="spn"><span class="mk2"><img src="img/cosmetique.jpg" alt=""></span>IGMK<i></i></div><div class="spt"><small id="p1"></small><h4 id="p2"></h4><p id="p3"></p><span class="spb" id="p4"></span></div><div class="spi"><img id="pimg" src="{F2}coiffure/1.jpg" alt=""><div class="spg"><b id="p5"></b><small id="p6"></small></div></div></div>
<a class="btn" style="width:100%;justify-content:center;margin-top:12px" href="https://gmk-formation-institute.github.io/GMK-Formation-Institute-Web-Site/index.html" target="_blank">Ouvrir le site en prévisualisation ↗</a></div></div>'''
FORM=[("Esthétique","6 mois + 3 mois de stage","11 modules","560 000","esthetique/5.jpg"),("Coiffure","6 mois + 3 mois de stage","6 modules","540 000","coiffure/4.jpg"),("Maquillage","2 semaines","Spécialisation","120 000","maquillage/57.jpg"),("Onglerie","2 semaines","Spécialisation","100 000","onglerie/10.jpg"),("Massage","2 semaines","Spécialisation","100 000","massage/3.jpg"),("Décoration","2 semaines","Spécialisation","90 000","decoration/13.jpg")]
P_forma='<div class="grid g3">'+"".join(f'<div class="card fc"><img src="{F2}{im}" alt=""><div class="row" style="justify-content:space-between;margin-top:14px"><h3>{n}</h3><label class="sw"><input type="checkbox" checked><i></i></label></div><small style="color:var(--mute)">{d} · {m}</small><div class="kv" style="margin-top:14px"><div class="fld"><label>Tarif (FCFA)</label><input class="inp" value="{t}"></div><div class="fld"><label>Paiement</label><select class="inp"><option>{"6 mensualités" if "mois" in d else "1 ou 2 fois"}</option></select></div></div><div class="row"><a class="btn" style="flex:1;justify-content:center" href="#">Modules & programme</a><a class="btn" href="#">{ic("edit")}</a></div></div>' for n,d,m,t,im in FORM)+f'<div class="card fc add"><b>+</b><span>Ajouter une formation</span><small>Elle apparaîtra automatiquement dans le menu, la page Formations et les tarifs.</small></div></div>'
imgs=["esthetique/1.jpg","coiffure/2.jpg","maquillage/5.jpg","onglerie/3.jpg","massage/4.jpg","decoration/14.jpg","esthetique/7.jpg","coiffure/6.jpg","maquillage/9.jpg","onglerie/4.jpg","esthetique/16.jpg","coiffure/15.jpg"]
P_media=f'''<div class="tools"><button class="chip on">Toutes <em>186</em></button><button class="chip">Esthétique</button><button class="chip">Coiffure</button><button class="chip">Maquillage</button><button class="chip">Stages</button><button class="chip">Vidéos <em>4</em></button><span style="flex:1"></span><a class="btn v" href="#">{ic("dl")}Importer des photos</a></div>
<div class="drop big"><b>Glissez vos photos et vidéos ici</b><small>Elles sont automatiquement compressées et redimensionnées pour un site rapide, même en 3G.</small></div>
<div class="mlib">'''+"".join(f'<div class="mi{" sel" if i==1 else ""}"><img src="{F2}{x}" alt=""><span>{x.split("/")[0].capitalize()}</span>{"<em>Galerie · Accueil</em>" if i%3==0 else ""}</div>' for i,x in enumerate(imgs))+'</div>'
P_temo='''<div class="grid g2"><div class="card"><div class="hd"><h3>Témoignages</h3><a class="btn p" href="#">+ Ajouter</a></div>'''+"".join(f'<div class="li"><img class="av" src="{im}" alt=""><div class="who"><div><b>{n}</b><small>« {q} »</small></div></div><div class="r"><label class="sw"><input type="checkbox"{" checked" if v else ""}><i></i></label></div></div>' for im,n,q,v in [("img/feedback/001.jpg","Aïcha K. · Coiffure 2019","Dès mon premier jour de stage, je savais travailler…",1),("img/formations/esthetique/8.jpg","Mariam T. · Esthétique 2022","Embauchée par mon institut de stage…",1),("img/formations/onglerie/10.jpg","Grâce A. · Onglerie 2023","J'ai lancé mon activité en 3 mois…",0)])+'''</div>
<div class="card"><div class="hd"><h3>Diplômées mises en avant</h3><a class="btn p" href="#">+ Ajouter</a></div>'''+"".join(f'<div class="li"><img class="av" src="img/formations/{im}" alt="" style="border-radius:8px"><div class="who"><div><b>{n}</b><small>{d}</small></div></div><div class="r"><span class="bd vi">Promo {y}</span></div></div>' for im,n,d,y in [("coiffure/18.jpg","Aïcha K.","Fondatrice d'Aïcha Hair, Yopougon","2019"),("esthetique/8.jpg","Mariam T.","Esthéticienne au Spa Riviera","2022"),("onglerie/10.jpg","Grâce A.","Prothésiste ongulaire","2023"),("maquillage/57.jpg","Fatou D.","Maquilleuse mariages","2021")])+'<p class="hint">Astuce : une diplômée peut être ajoutée directement depuis sa fiche élève.</p></div></div>'
P_equipe='<div class="grid g3">'+"".join(f'<div class="card"><div class="row" style="gap:14px"><img src="img/about/{im}" alt="" style="width:64px;height:64px;border-radius:50%;object-fit:cover;object-position:top"><div><h3 style="font-size:22px">{n}</h3><small style="color:var(--mute)">{r}</small></div></div><div class="fld" style="margin-top:14px"><label>Citation affichée sur le site</label><textarea class="inp ta">{q}</textarea></div><div class="row"><span class="bd gr">Position {i+1} dans le carrousel</span></div></div>' for i,(im,n,r,q) in enumerate([("BATIYE.jpg","K. N'Si Batiye","Directeur général","Depuis 2012, nous formons des professionnelles prêtes à exercer dès leur sortie."),("ADEGOKE.jpg","Dr Adegoke Moucaïla","Directeur des études","Le savoir ne vaut que confronté au terrain."),("GBOZE.jpg","Dr Gboze Jean-Claude","Directeur commercial","Nos élèves surprennent leurs maîtres de stage.")]))+'</div>'
P_infos=f'''<div class="grid g2"><div class="card"><div class="hd"><h3>Coordonnées</h3></div><div class="kv">
<div class="fld"><label>Numéro WhatsApp (bouton flottant)</label><input class="inp" value="+225 07 07 58 90 81"></div><div class="fld"><label>Message pré-rempli</label><input class="inp" value="Bonjour, je souhaite des informations…"></div>
<div class="fld"><label>Téléphones</label><input class="inp" value="07 07 58 90 81 · 01 02 93 92 21"></div><div class="fld"><label>E-mail</label><input class="inp" value="info@igmk-formation.net"></div>
<div class="fld"><label>Adresse</label><input class="inp" value="Yopougon – Millionnaire, Abidjan"></div><div class="fld"><label>Horaires</label><input class="inp" value="Lun – Ven · 8h – 17h"></div></div></div>
<div class="card"><div class="hd"><h3>Réseaux & référencement</h3></div><div class="kv"><div class="fld"><label>Facebook</label><input class="inp" value="facebook.com/igmkformation"></div><div class="fld"><label>Instagram</label><input class="inp" value="@igmk.formation"></div><div class="fld"><label>TikTok</label><input class="inp" value="@igmkformation"></div><div class="fld"><label>Date de la prochaine rentrée</label><input class="inp" type="date" value="2027-01-12"></div></div>
<div class="fld"><label>Description Google</label><textarea class="inp ta">École d'esthétique et de coiffure à Abidjan : 80 % de pratique, 3 mois de stage obligatoire, certificat reconnu.</textarea></div>
<div class="gp"><small>Aperçu Google</small><b>IGMK Formation — École d'esthétique et de coiffure · Abidjan</b><span>igmk-formation.net</span><p>École d'esthétique et de coiffure à Abidjan : 80 % de pratique, 3 mois de stage obligatoire…</p></div></div></div>
<div class="card" style="margin-top:18px"><div class="hd"><h3>Chiffres clés affichés sur le site</h3><small style="color:var(--mute)">Mis à jour automatiquement depuis la gestion · modifiables</small></div><div class="grid g4">'''+"".join(f'<div class="fld"><label>{l}</label><input class="inp" value="{v}"><small style="color:var(--ok);font-size:11.5px;font-weight:600">{a}</small></div>' for l,v,a in [("Année de fondation","2012",""),("Diplômées","500+","↻ 512 dans la base"),("Part de pratique","80 %",""),("Instituts partenaires","40+","↻ 42 dans l'annuaire")])+'</div></div>'
site=f'''<div class="ph"><div><small>Site public</small><h1>Contenu <i>du site</i></h1><p>Modifiez textes, photos, formations, tarifs et coordonnées — sans toucher au code.</p></div><div class="row"><span class="bd ok">● Site en ligne · publié il y a 2 jours</span><a class="btn v" href="#">Publier les modifications (3)</a></div></div>
{tabs}<div class="cp on" data-t="pages">{P_pages}</div><div class="cp" data-t="forma">{P_forma}</div><div class="cp" data-t="media">{P_media}</div><div class="cp" data-t="temo">{P_temo}</div><div class="cp" data-t="equipe">{P_equipe}</div><div class="cp" data-t="infos">{P_infos}</div>
<script>(()=>{{const $=i=>document.getElementById(i);const show=t=>{{document.querySelectorAll('#cmst a').forEach(a=>a.classList.toggle('on',a.dataset.t===t));document.querySelectorAll('.cp').forEach(c=>c.classList.toggle('on',c.dataset.t===t))}};
document.addEventListener('click',e=>{{const a=e.target.closest('[data-t],[data-t2]');if(!a||a.classList.contains('cp'))return;e.preventDefault();show(a.dataset.t2||a.dataset.t)}});
function up(){{$('p1').textContent=$('h1').value;const L=$('h2').value.split('\\n');$('p2').innerHTML=L.map((l,i)=>i===L.length-1?'<i>'+l+'</i>':l).join('<br>');$('p3').textContent=$('h3').value;$('p4').textContent=$('h4').value;$('p5').textContent=$('h5').value;$('p6').textContent=$('h6').value}}
['h1','h2','h3','h4','h5','h6'].forEach(i=>$(i).addEventListener('input',up));up();
document.querySelectorAll('.mi').forEach(m=>m.onclick=()=>{{document.querySelectorAll('.mi').forEach(x=>x.classList.toggle('sel',x===m));const s=m.querySelector('img').src;$('himg').src=$('pimg').src=s}})}})();</script>'''
shell("site.html","Contenu du site",site,"site.html")

# ---------------- PARAMETRES ----------------
def F(l,v,t="text"): return f'<div class="fld"><label>{l}</label><input type="{t}" value="{v}"></div>'
def SEL(l,opts): return f'<div class="fld"><label>{l}</label><select>'+"".join(f"<option>{o}</option>" for o in opts)+'</select></div>'
def TG(t,d,v=True): return f'<div class="tgl"><div><b>{t}</b><small>{d}</small></div><label class="sw"><input type="checkbox"{" checked" if v else ""}><i></i></label></div>'
SAVE='<div class="row" style="justify-content:flex-end;margin-top:6px"><button class="btn">Annuler</button><button class="btn p">Enregistrer</button></div>'
ecole=f"""<div class="grid g21"><div class="card"><div class="hd"><h3>Identité de l'école</h3></div><div class="grid g2" style="gap:0 18px">
{F("Nom officiel","IGMK Formation")}{F("Sigle","IGMK")}{F("Agrément ministère","N° 0142/METFP/DEFP")}{F("RCCM","CI-ABJ-2015-B-12345")}
{F("Téléphone","+225 07 07 58 90 81","tel")}{F("WhatsApp (paiements)","+225 07 07 58 90 81","tel")}{F("E-mail","contact@igmk-formation.ci","email")}{F("Site web","www.igmk-formation.ci")}</div>
{F("Adresse","Cocody Angré, 8e tranche — Abidjan")}{SAVE}</div>
<div class="card"><div class="hd"><h3>Logo & documents</h3></div><div class="logo-up"><img src="img/cosmetique.jpg" alt=""><div><b>Logo IGMK</b><small>Utilisé sur les reçus, certificats et cartes d'élève</small><button class="btn">Remplacer</button></div></div>
<div class="fld" style="margin-top:18px"><label>Signature du directeur</label><div class="sig">K. N'Si Batiye</div></div>{TG("Cachet sur les certificats","Ajouter automatiquement le cachet de l'école")}{TG("Mentions légales sur les reçus","Agrément et RCCM en pied de page")}</div></div>"""
RENT="".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td><span class='bd {c}'>{d}</span></td></tr>" for a,b,c,d in [("Rentrée d'octobre","06/10/2025","gr","Passée"),("Rentrée de janvier","12/01/2026","vi","Inscriptions ouvertes"),("Rentrée d'avril","06/04/2026","gr","Planifiée")])
annee=f"""<div class="grid g2"><div class="card"><div class="hd"><h3>Année scolaire</h3><span class="bd ok">En cours</span></div>
{SEL("Année active",["2025 – 2026","2026 – 2027 (préparation)"])}<div class="grid g2" style="gap:0 18px">{F("Début","2025-10-06","date")}{F("Fin","2026-07-31","date")}</div>
<div class="hd" style="margin-top:6px"><h3>Rentrées</h3><a href="#">+ Ajouter</a></div><table><tbody>{RENT}</tbody></table></div>
<div class="card"><div class="hd"><h3>Numérotation</h3></div>{F("Matricule élève","IGMK-{AAAA}-{0000}")}{F("Reçu de paiement","REC-{AA}{MM}-{0000}")}{F("Certificat","CERT-{AAAA}-{000}")}
<p class="hint">Prochain matricule : <b>IGMK-2026-0249</b> · prochain reçu : <b>REC-2611-0418</b></p>{SAVE}</div></div>"""
TAR="".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c} F</td><td>{d} F</td><td>{e}</td><td><a href='#'>Modifier</a></td></tr>" for a,b,c,d,e in [("Esthétique — CAP","12 mois","25 000","450 000","3 tranches"),("Coiffure — CAP","12 mois","25 000","420 000","3 tranches"),("Maquillage professionnel","3 mois","15 000","180 000","2 tranches"),("Onglerie","2 mois","15 000","120 000","2 tranches"),("Décoration événementielle","3 mois","15 000","150 000","2 tranches")])
tarifs=f"""<div class="card"><div class="hd"><h3>Frais & échéanciers</h3><a href="#">+ Nouveau tarif</a></div><div class="tw" style="border:0"><table style="min-width:640px"><thead><tr><th>Formation</th><th>Durée</th><th>Inscription</th><th>Scolarité</th><th>Échéances</th><th></th></tr></thead><tbody>{TAR}</tbody></table></div></div>
<div class="grid g2" style="margin-top:18px"><div class="card"><div class="hd"><h3>Modes de paiement acceptés</h3></div>{TG("Espèces","Encaissement au secrétariat")}{TG("Wave","Lien de paiement envoyé par WhatsApp")}{TG("Orange Money","Référence récupérée automatiquement")}{TG("MTN MoMo","Référence récupérée automatiquement")}{TG("Virement bancaire","SGCI · RIB sur le reçu",False)}</div>
<div class="card"><div class="hd"><h3>Règles</h3></div>{F("Pénalité de retard","5 %")}{F("Délai de grâce (jours)","7","number")}{TG("Bloquer le certificat si solde impayé","Le certificat ne peut pas être délivré tant que la scolarité n'est pas soldée")}{SAVE}</div></div>"""
U=[("K. N'Si Batiye","Directeur général","Administrateur","vi","Aujourd'hui, 09:12"),("Dr Adegoke Moucaïla","Directeur des études","Pédagogie","ok","Hier, 17:40"),("Dr Gboze Jean-Claude","Directeur commercial","Inscriptions","ok","Il y a 3 j"),("Mlle Gnamien Esther","Secrétaire — Accueil","Secrétariat","gr","Aujourd'hui, 08:05"),("M. Coulibaly Moussa","Comptable","Comptabilité","warn","Aujourd'hui, 10:31")]
FA=['<span class="bd ok">Activée</span>','<span class="bd warn">Non</span>']
UR="".join(f"<tr><td><div class='who'>{ini(n)}<div><b>{n}</b><small>{f}</small></div></div></td><td><span class='bd {c}'>{r}</span></td><td>{d}</td><td>{FA[0] if i<3 else FA[1]}</td><td><a href='#'>Gérer</a></td></tr>" for i,(n,f,r,c,d) in enumerate(U))
RO=["Élèves","Inscriptions","Paiements","Stages","Emploi du temps","Certificats","Site public","Paramètres"]
M={"Administrateur":"11111111","Pédagogie":"10011100","Inscriptions":"11000010","Secrétariat":"11101100","Comptabilité":"10100000"}
PR="".join(f"<tr><td><b>{k}</b></td>"+"".join(f"<td><label class='sw'><input type='checkbox'{' checked' if b=='1' else ''}{' disabled' if k=='Administrateur' else ''}><i></i></label></td>" for b in v)+"</tr>" for k,v in M.items())
acces=f"""<div class="card"><div class="hd"><h3>Utilisateurs · 5</h3><a class="btn p" href="#">{ic("plus")}Inviter</a></div><div class="tw" style="border:0"><table style="min-width:620px"><thead><tr><th>Utilisateur</th><th>Rôle</th><th>Dernière connexion</th><th>2FA</th><th></th></tr></thead><tbody>{UR}</tbody></table></div></div>
<div class="card" style="margin-top:18px"><div class="hd"><h3>Droits par rôle</h3><a href="#">+ Créer un rôle</a></div><div class="tw" style="border:0"><table class="perm" style="min-width:720px"><thead><tr><th>Rôle</th>{"".join(f"<th>{x}</th>" for x in RO)}</tr></thead><tbody>{PR}</tbody></table></div></div>"""
notif=f"""<div class="grid g2"><div class="card"><div class="hd"><h3>Messages automatiques aux élèves</h3></div>{TG("Confirmation d'inscription","WhatsApp + SMS dès la validation du dossier")}{TG("Rappel d'échéance","3 jours avant chaque tranche")}{TG("Reçu de paiement","Envoyé en PDF sur WhatsApp")}{TG("Absence signalée","Message au parent / tuteur",False)}{TG("Certificat disponible","Quand le certificat est signé")}</div>
<div class="card"><div class="hd"><h3>Alertes pour l'équipe</h3></div>{TG("Nouvelle pré-inscription en ligne","Notification + e-mail au secrétariat")}{TG("Paiement reçu","Au comptable")}{TG("Formateur absent","À la direction des études")}{TG("Résumé hebdomadaire","Chaque lundi à 8 h, à la direction")}
<div class="fld" style="margin-top:14px"><label>Expéditeur SMS</label><input value="IGMK"></div>{SAVE}</div></div>"""
LOG="".join(f"<tr><td><b>{a}</b><br><small style='color:var(--mute)'>{b}</small></td><td style='text-align:right;color:var(--mute)'>{c}</td></tr>" for a,b,c in [("M. Coulibaly","a encaissé 150 000 F — REC-2611-0417","10:31"),("Mlle Gnamien","a validé l'inscription de Aya Konan","09:47"),("K. N'Si Batiye","a publié une actualité sur le site","09:15"),("Dr Adegoke","a modifié l'emploi du temps — S2","Hier")])
secu=f"""<div class="grid g2"><div class="card"><div class="hd"><h3>Sécurité</h3></div>{TG("Double authentification obligatoire","Pour les rôles Administrateur et Comptabilité")}{TG("Déconnexion automatique","Après 30 min d'inactivité")}{TG("Connexion depuis un nouvel appareil","Alerte e-mail à l'administrateur")}{SAVE}</div>
<div class="card"><div class="hd"><h3>Sauvegardes</h3><span class="bd ok">OK</span></div><p class="hint" style="margin-top:0">Dernière sauvegarde : <b>aujourd'hui à 03:00</b> · quotidienne, conservée 30 jours</p><div class="row"><button class="btn">Exporter les données (Excel)</button><button class="btn">Restaurer…</button></div>
<div class="hd" style="margin-top:22px"><h3>Journal d'activité</h3><a href="journal.html">Tout voir →</a></div><table><tbody>{LOG}</tbody></table></div></div>"""
T=[("ecole","École",ecole),("annee","Année scolaire",annee),("tarifs","Tarifs & paiements",tarifs),("acces","Utilisateurs & accès",acces),("notif","Notifications",notif),("secu","Sécurité & données",secu)]
TABS="".join(f'<a href="#{k}"{" class=on" if i==0 else ""} data-t="{k}">{t}</a>' for i,(k,t,_) in enumerate(T))
SECS="".join(f'<section class="pt" id="t-{k}"{"" if i==0 else " hidden"}>{b}</section>' for i,(k,t,b) in enumerate(T))
JS="<script>(()=>{const go=k=>{document.querySelectorAll('.ptabs a').forEach(a=>a.classList.toggle('on',a.dataset.t===k));document.querySelectorAll('.pt').forEach(s=>s.hidden=s.id!=='t-'+k)};document.querySelectorAll('.ptabs a').forEach(a=>a.onclick=e=>{e.preventDefault();go(a.dataset.t);history.replaceState(0,'','#'+a.dataset.t)});if(location.hash)go(location.hash.slice(1))})()</script>"
par=f'<div class="ph"><div><small>Compte</small><h1>Paramètres</h1><p>Configuration de l\'école, des tarifs, des accès et des notifications.</p></div></div><div class="tabs ptabs" style="margin-top:8px">{TABS}</div>{SECS}{JS}'
shell("parametres.html","Paramètres",par,"parametres.html")

# ---------------- STATISTIQUES ----------------
SEG = lambda i, items, on: f'<div class="seg" id="{i}">' + "".join(f'<button data-{k}="{v}"{" class=on" if v==on else ""}>{t}</button>' for k,v,t in items) + '</div>'
KP = lambda i,t: f'<div class="card kpi" id="{i}"><span>{t}</span><b>—</b><em></em></div>'
stats = f'''<div class="ph"><div><small>Pilotage</small><h1>Statistiques</h1><p id="rng">—</p></div><div class="row"><button class="btn" id="tv">Voir en tableau</button><div class="exp"><button class="btn" id="expb">{ic("dl")}Exporter ▾</button><div class="expm" id="expm" hidden><button data-x="pdf"><b>Rapport PDF</b><small>Graphiques, chiffres clés et conclusions</small></button><button data-x="csv"><b>Données (Excel)</b><small>Tableau des valeurs, fichier .csv</small></button></div></div></div></div>
<div class="prh"><img src="img/cosmetique.jpg" alt=""><div><b>IGMK Formation</b><small>Rapport statistique</small></div><dl><dt>Période</dt><dd id="prp">—</dd><dt>Filtres</dt><dd id="prf">—</dd><dt>Généré le</dt><dd id="prd">—</dd></dl></div>
<div class="card filt"><div class="fg"><label>Période</label>{SEG("pre",[("p","m3","3 mois"),("p","ytd","Cette année"),("p","sy","Année scolaire 25-26"),("p","m12","12 mois"),("p","y3","3 ans"),("p","all","Tout")],"m12")}</div>
<div class="fg"><label>Du — au</label><div class="dr"><input type="month" id="da" min="2023-01" max="2026-11"><span>→</span><input type="month" id="db" min="2023-01" max="2026-11"></div></div>
<div class="fg"><label>Regrouper par</label>{SEG("gran",[("g","1","Mois"),("g","3","Trimestre"),("g","6","Semestre"),("g","12","Année")],"1")}</div>
<div class="fg"><label>Comparer à</label><select id="cmp"><option value="prev">Période précédente</option><option value="yoy">Même période N-1</option><option value="none">Aucune comparaison</option></select></div>
<div class="fg"><label>Formation</label><select id="ff"><option value="all">Toutes</option><option value="esthetique">Esthétique</option><option value="coiffure">Coiffure</option><option value="spe">Spécialisations</option></select></div></div>
<div class="grid g4" style="margin:18px 0">{KP("k1","Encaissé")}{KP("k2","Nouvelles inscriptions")}{KP("k3","Taux d'abandon")}{KP("k4","Part TikTok")}</div>
<div id="tbl" class="card tw" hidden style="margin-bottom:18px"></div>
<div class="card"><div class="hd"><h3>Versements encaissés</h3><div class="clg" id="l1"></div></div><div class="ch" id="c1" data-h="300"></div></div>
<div class="card" style="margin-top:18px"><div class="hd"><h3>Promotions comparées</h3>{SEG("met",[("m","act","Élèves présentes"),("m","ret","Rétention %"),("m","paid","Scolarité payée %")],"act")}</div>
<p class="sub">Chaque courbe suit une promotion depuis sa rentrée : on compare les promotions à la même étape, quelle que soit leur date. Choisissez jusqu'à 6 promotions.</p>
<div class="pchips" id="pchips"></div><div class="ch" id="c4" data-h="300"></div><div class="clg" id="l4" style="margin-top:10px"></div></div>
<div class="grid g2" style="margin-top:18px"><div class="card"><div class="hd"><h3>Inscriptions & abandons</h3></div><div class="ch" id="c2" data-h="240"></div><div class="clg" id="l2"></div></div>
<div class="card"><div class="hd"><h3>Inscriptions par source</h3></div><div class="ch" id="c3" data-h="240"></div><div class="clg" id="l3"></div></div></div>
<div class="grid g21" style="margin-top:18px"><div class="card"><div class="hd"><h3>D'où viennent les élèves ?</h3><div class="clg" id="srcl"></div></div><div id="src"></div></div>
<div class="card insight"><div class="hd"><h3>À retenir</h3></div><ul id="ins"></ul><p class="sub" style="margin:14px 0 0">Calculé automatiquement selon la période choisie.</p></div></div>
<script src="stats.js?v=5"></script>'''
shell("stats.html","Statistiques",stats,"stats.html")

shell("preinscriptions.html","Pré-inscriptions",(R/"_src/preinsc.html").read_text(),"preinscriptions.html")
shell("membre.html","Mme Hortense Kouassi",(R/"_src/membre.html").read_text(),"personnel.html")
shell("journal.html","Journal d'activité",(R/"_src/journal.html").read_text(),"journal.html")
print("Maquettes admin générées.")
