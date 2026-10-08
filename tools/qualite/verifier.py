#!/usr/bin/env python3
"""Contrôle qualité du dépôt TOGAFrance.

Trois vérifications :
  1. Liens   — chaque lien interne d'un fichier Markdown pointe vers un fichier existant (erreur sinon).
  2. Traçabilité — pour chaque `tracabilite.yaml` d'un projet pilote, la chaîne
     besoin → exigence → indicateur → seuil de réversibilité est complète et cohérente
     avec les tableaux des livrables 7 et 13 (erreur sinon).
  3. Lisibilité — « défi des 10 ans » : score de Kandel et Moles (adaptation française
     de l'indice de Flesch) pour chaque livrable en français (avertissement sous le seuil).

Usage :
    python3 tools/qualite/verifier.py            # code 1 si erreur
    python3 tools/qualite/verifier.py --strict   # les avertissements deviennent bloquants
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys
import unicodedata
import urllib.parse

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEUIL_LISIBILITE = 40  # Kandel-Moles : 60-70 = standard, 50-60 = assez difficile, < 40 = difficile

LIEN = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")


def fichiers_md():
    for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if os.path.isfile(f) and "/.git/" not in f:
            yield f


def rel(f):
    return os.path.relpath(f, ROOT)


# --------------------------------------------------------------------------- liens
def verifier_liens(err):
    n = 0
    for f in fichiers_md():
        texte = open(f, encoding="utf-8").read()
        texte = re.sub(r"```.*?```", "", texte, flags=re.S)
        for m in LIEN.finditer(texte):
            cible = m.group(1).split("#")[0]
            if not cible or cible == "..." or re.match(r"^[a-z]+:", cible):
                continue
            n += 1
            chemin = os.path.normpath(os.path.join(os.path.dirname(f), urllib.parse.unquote(cible)))
            if not os.path.exists(chemin) and not os.path.exists(unicodedata.normalize("NFD", chemin)) \
                    and not os.path.exists(unicodedata.normalize("NFC", chemin)):
                err.append(f"[lien] {rel(f)} → {cible}")
    return n


# --------------------------------------------------------------------------- traçabilité
def ids_tableau(fichier, prefixe):
    if not os.path.exists(fichier):
        return set()
    return set(re.findall(rf"^\|\s*({prefixe}-\d+)\s*\|", open(fichier, encoding="utf-8").read(), re.M))


def codes_catalogue():
    f = os.path.join(ROOT, "documentation", "11-indicateurs-humains-FR.md")
    return set(re.findall(r"^\|\s*(H-\d+)\s*\|", open(f, encoding="utf-8").read(), re.M)) if os.path.exists(f) else set()


def verifier_tracabilite(err, warn):
    catalogue = codes_catalogue()
    projets = glob.glob(os.path.join(ROOT, "pilots-territories", "**", "tracabilite.yaml"), recursive=True)
    for t in projets:
        base = os.path.dirname(t)
        nom = rel(base)
        d = yaml.safe_load(open(t, encoding="utf-8"))
        besoins = {b["id"] for b in d.get("besoins", [])}
        exig = {e["id"]: e for e in d.get("exigences", [])}
        ind = {i["id"]: i for i in d.get("indicateurs", [])}
        rev = {r["id"]: r for r in d.get("reversibilite", [])}
        hors = set(d.get("verifications_hors_indicateur", []))

        tab_ex = ids_tableau(os.path.join(base, "livrables", "FR", "07_specification_exigences.md"), "EX")
        tab_rev = ids_tableau(os.path.join(base, "livrables", "FR", "13_fiches_de_reversibilite.md"), "REV")
        for manquant in sorted(tab_ex - set(exig)):
            err.append(f"[traçabilité] {nom} : {manquant} figure au livrable 7 mais pas dans tracabilite.yaml.")
        for manquant in sorted(set(exig) - tab_ex):
            err.append(f"[traçabilité] {nom} : {manquant} est dans tracabilite.yaml mais pas au livrable 7.")
        for manquant in sorted(tab_rev ^ set(rev)):
            err.append(f"[traçabilité] {nom} : {manquant} n'est pas à la fois au livrable 13 et dans tracabilite.yaml.")

        for b in d.get("besoins", []):
            if b.get("source") and not os.path.exists(os.path.join(base, b["source"])):
                err.append(f"[traçabilité] {nom} : source introuvable pour {b['id']} ({b['source']}).")
        utilises = set()
        for e in exig.values():
            if e.get("besoin") not in besoins:
                err.append(f"[traçabilité] {nom} : {e['id']} n'est rattachée à aucun besoin connu.")
            verifs = e.get("verifiee_par") or []
            for v in verifs:
                if v not in ind and v not in hors:
                    err.append(f"[traçabilité] {nom} : {e['id']} vérifiée par {v}, inconnu.")
                utilises.add(v)
            if not verifs:
                msg = f"[traçabilité] {nom} : {e['id']} ({e.get('priorite')}) n'a aucun moyen de vérification."
                (err if e.get("priorite") == "obligatoire" else warn).append(msg)
        for r in rev.values():
            if r.get("indicateur") not in ind:
                err.append(f"[réversibilité] {nom} : {r['id']} repose sur un indicateur inconnu ({r.get('indicateur')}).")
            if not r.get("seuil"):
                err.append(f"[réversibilité] {nom} : {r['id']} sans seuil de déclenchement.")
            utilises.add(r.get("indicateur"))
        for i in ind.values():
            if i["id"] not in utilises:
                warn.append(f"[indicateur] {nom} : {i['id']} n'est relié à aucune exigence ni seuil.")
            if i.get("catalogue") and i["catalogue"] not in catalogue:
                err.append(f"[indicateur] {nom} : {i['id']} renvoie au code {i['catalogue']}, absent du catalogue.")
        for b in besoins:
            if not any(e.get("besoin") == b for e in exig.values()):
                warn.append(f"[traçabilité] {nom} : le besoin {b} n'a aucune exigence.")
    return len(projets)


# --------------------------------------------------------------------------- lisibilité
VOYELLES = re.compile(r"[aeiouyàâäéèêëîïôöùûüœæ]+", re.I)


def syllabes(mot):
    mot = mot.lower()
    n = len(VOYELLES.findall(mot))
    if len(mot) > 3 and re.search(r"[^aeiouy]es?$", mot):  # e muet final
        n -= 1
    return max(1, n)


def prose(texte):
    texte = re.sub(r"^---\n.*?\n---\n", "", texte, flags=re.S)       # en-tête YAML
    texte = re.sub(r"```.*?```", "", texte, flags=re.S)
    lignes = []
    for l in texte.splitlines():
        l = l.strip()
        if not l or l.startswith(("|", "#", ">", "---")) or l.startswith("- [ ]"):
            continue
        l = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", l)
        l = re.sub(r"[*_`]", "", l).lstrip("-•0123456789. ")
        if l and l[-1] not in ".!?:;":
            l += "."
        lignes.append(l)
    return " ".join(lignes)


def kandel_moles(texte):
    phrases = [p for p in re.split(r"[.!?:;]+", texte) if re.search(r"\w", p)]
    mots = re.findall(r"[A-Za-zÀ-ÿœæ'’-]+", texte)
    if len(phrases) < 3 or len(mots) < 50:
        return None
    return 207 - 1.015 * (len(mots) / len(phrases)) - 73.6 * (sum(map(syllabes, mots)) / len(mots))


def verifier_lisibilite(warn, rapport):
    cibles = sorted(glob.glob(os.path.join(ROOT, "livrables", "FR", "*.md")))
    cibles += sorted(glob.glob(os.path.join(ROOT, "documentation", "*-FR.md")))
    for f in cibles:
        s = kandel_moles(prose(open(f, encoding="utf-8").read()))
        if s is None:
            continue
        rapport.append((rel(f), s))
        if s < SEUIL_LISIBILITE:
            warn.append(f"[lisibilité] {rel(f)} : score {s:.0f} (< {SEUIL_LISIBILITE}), phrases à raccourcir.")


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    err, warn, rapport = [], [], []
    n_liens = verifier_liens(err)
    n_proj = verifier_tracabilite(err, warn)
    verifier_lisibilite(warn, rapport)

    for w in warn:
        print("AVERTISSEMENT", w)
    for e in err:
        print("ERREUR", e)
    moyenne = sum(s for _, s in rapport) / len(rapport) if rapport else 0
    resume = (f"{n_liens} liens internes, {n_proj} projet(s) tracé(s), "
              f"lisibilité moyenne {moyenne:.0f} sur {len(rapport)} documents. "
              f"{len(err)} erreur(s), {len(warn)} avertissement(s).")
    print("\n" + resume)

    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as s:
            s.write(f"## Qualité TOGAFrance\n\n{resume}\n\n")
            s.write("".join(f"- ❌ {e}\n" for e in err) + "".join(f"- ⚠️ {w}\n" for w in warn))
            s.write("\n### Défi des 10 ans — lisibilité (Kandel-Moles, plus haut = plus facile)\n\n")
            s.write("| Document | Score |\n| --- | --- |\n")
            s.write("".join(f"| {d} | {v:.0f} |\n" for d, v in sorted(rapport, key=lambda x: x[1])))
    sys.exit(1 if err or (a.strict and warn) else 0)


if __name__ == "__main__":
    main()
