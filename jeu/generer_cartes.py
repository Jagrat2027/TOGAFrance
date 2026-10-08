#!/usr/bin/env python3
"""Génère les cartes du jeu « Le Cycle ».

Entrées : jeu/cartes.yaml (rôles, événements) et tools/fake-data/territoires-fictifs.yaml (territoires).
Sorties : jeu/cartes.md (lisible sur GitHub) et jeu/cartes-a-imprimer.html (format carte 63 × 88 mm, A4).

Usage : python3 jeu/generer_cartes.py
"""
import html
import os

import yaml

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)

TYPES = {
    "crise": ("Crise", "#b4432f", "ϟ"),
    "signal": ("Signal faible", "#b07d12", "◔"),
    "raccourci": ("Raccourci", "#6b4fa0", "↯"),
    "bonne": ("Bonne nouvelle", "#2f7d4f", "✦"),
    "seuil": ("Seuil", "#1f5f8b", "⚑"),
}


def charger():
    c = yaml.safe_load(open(os.path.join(ICI, "cartes.yaml"), encoding="utf-8"))
    t = yaml.safe_load(open(os.path.join(RACINE, "tools", "fake-data", "territoires-fictifs.yaml"), encoding="utf-8"))
    vus, terr = set(), []
    for x in t["territoires"]:
        cle = (tuple(x["priorités"]), tuple(x["contraintes"]), tuple(x["ressources"]))
        if cle not in vus:  # une carte par territoire distinct
            vus.add(cle)
            terr.append(x)
    return c["roles"], c["evenements"], terr


def markdown(roles, evts, terr):
    o = ["<!-- Généré par jeu/generer_cartes.py : modifier jeu/cartes.yaml ou les données factices, puis régénérer. -->",
         "", "# Le Cycle — les cartes", "",
         "Version à imprimer : [cartes-a-imprimer.html](./cartes-a-imprimer.html). Règles : [regles.md](./regles.md).", "",
         f"## Rôles ({len(roles)})", "", "| Rôle | Devise | Pouvoir |", "| --- | --- | --- |"]
    o += [f"| **{r['nom']}** | {r['devise']} | {r['pouvoir']} |" for r in roles]
    o += ["", f"## Événements ({len(evts)})", "", "| Type | Carte | Situation | Effet |", "| --- | --- | --- | --- |"]
    ordre = list(TYPES)
    for e in sorted(evts, key=lambda e: ordre.index(e["type"])):
        o.append(f"| {TYPES[e['type']][0]} | **{e['titre']}** | {e['texte']} | {e['effet']} |")
    o += ["", f"## Territoires ({len(terr)})", "",
          "| Territoire | Profil | Priorités | Contraintes | Ressources |", "| --- | --- | --- | --- | --- |"]
    for t in terr:
        o.append(f"| **{t['nom']}** | {t['statut']}, {t['population']:,} hab.".replace(",", " ")
                 + f" | {' · '.join(t['priorités'])} | {' · '.join(t['contraintes'])} | {' · '.join(t['ressources'])} |")
    return "\n".join(o) + "\n"


def carte(couleur, etiquette, titre, corps):
    e = html.escape
    return (f'<section class="carte" style="--c:{couleur}"><header>{e(etiquette)}</header>'
            f"<h2>{e(titre)}</h2>{corps}<footer>Le Cycle · TOGAFrance</footer></section>")


def page(roles, evts, terr):
    e = html.escape
    cartes = []
    for r in roles:
        cartes.append(carte("#2d2a26", "Rôle", r["nom"],
                            f'<p class="devise">«\u00a0{e(r["devise"])}\u00a0»</p><div class="symbole">{e(r.get("symbole", ""))}</div>'
                            f'<p class="effet">{e(r["pouvoir"])}</p>'))
    for t in terr:
        liste = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)
        cartes.append(carte("#7a5a2b", "Territoire", t["nom"],
                            f'<p class="profil">{e(t["statut"])}</p>'
                            f'<h3>Priorités</h3><ul>{liste(t["priorités"])}</ul>'
                            f'<h3>Contraintes</h3><ul>{liste(t["contraintes"])}</ul>'
                            f'<h3>Ressources</h3><ul>{liste(t["ressources"])}</ul>'))
    for v in evts:
        nom, coul, sym = TYPES[v["type"]]
        cartes.append(carte(coul, nom, v["titre"],
                            f'<p class="situation">{e(v["texte"])}</p><div class="symbole">{sym}</div>'
                            f'<p class="effet">{e(v["effet"])}</p>'))
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Le Cycle — cartes à imprimer</title>
<!-- Généré par jeu/generer_cartes.py -->
<style>
  @page {{ size: A4; margin: 8mm; }}
  :root {{ --papier: #fbf8f2; --encre: #24211d; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; padding: 16px; background: #e9e4da; color: var(--encre);
         font: 9.5pt/1.35 "Iowan Old Style", "Palatino Linotype", Georgia, serif; }}
  .intro {{ max-width: 190mm; margin: 0 auto 12px; font-family: system-ui, sans-serif; font-size: 10pt; }}
  .grille {{ display: grid; grid-template-columns: repeat(auto-fill, 63mm); gap: 4mm; justify-content: center; }}
  .carte {{ width: 63mm; height: 88mm; background: var(--papier); border: 1.6mm solid var(--c);
           border-radius: 3mm; padding: 3mm 3.2mm; display: flex; flex-direction: column;
           break-inside: avoid; overflow: hidden; }}
  header {{ font: 600 7pt/1 system-ui, sans-serif; letter-spacing: .12em; text-transform: uppercase;
            color: var(--c); }}
  h2 {{ font-size: 12.5pt; line-height: 1.15; margin: 1.6mm 0 2mm; }}
  h3 {{ font: 600 6.8pt/1 system-ui, sans-serif; text-transform: uppercase; letter-spacing: .08em;
        margin: 1.6mm 0 .6mm; color: var(--c); }}
  ul {{ margin: 0; padding-left: 3.5mm; }}
  p {{ margin: 0 0 1.8mm; }}
  .devise, .situation, .profil {{ font-style: italic; }}
  .symbole {{ flex: 1; display: grid; place-items: center; font-size: 34pt; color: var(--c); opacity: .85; }}
  .effet {{ margin-top: auto; padding-top: 2mm; border-top: .3mm solid color-mix(in srgb, var(--c) 40%, transparent);
            font-family: system-ui, sans-serif; font-size: 8.4pt; }}
  footer {{ font: 6pt/1 system-ui, sans-serif; color: #8a8378; text-align: right; margin-top: 1.5mm; }}
  @media print {{ body {{ background: none; padding: 0; }} .intro {{ display: none; }} }}
</style>
</head>
<body>
<p class="intro"><strong>Le Cycle</strong> — {len(cartes)} cartes. Imprimez en A4, à 100 %, puis découpez.
Règles : <code>jeu/regles.md</code>.</p>
<main class="grille">
{chr(10).join(cartes)}
</main>
</body>
</html>
"""


def main():
    roles, evts, terr = charger()
    open(os.path.join(ICI, "cartes.md"), "w", encoding="utf-8").write(markdown(roles, evts, terr))
    open(os.path.join(ICI, "cartes-a-imprimer.html"), "w", encoding="utf-8").write(page(roles, evts, terr))
    print(f"{len(roles)} rôles, {len(evts)} événements, {len(terr)} territoires générés.")


if __name__ == "__main__":
    main()
