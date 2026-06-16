---
title: Value Proposition
nav_order: 1
---

{: .no_toc }
# Value Proposition

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## The Problem

An der HWR gibt es keinen zentralen Weg für Studierende, einen passenden Betreuer für ihre Abschlussarbeit zu finden. Welche Professor/in welche Themen betreut, wie seine Anforderungen aussehen und ob überhaupt noch Betreuungsplätze frei sind, all das ist nicht öffentlich zugänglich. Studierende sind gezwungen, Professoren einzeln per E-Mail zu kontaktieren, ohne zu wissen ob das Thema passt oder ob Kapazität vorhanden ist. Das führt zu langen Wartezeiten, mehrfachen Absagen und im schlimmsten Fall zu einer Betreuung die thematisch nicht optimal ist.

Professorinnen und Professoren stehen vor dem umgekehrten Problem: Betreuungsanfragen kommen ungefiltert per E-Mail, ohne einheitliche Struktur und ohne Vorabinformationen zum geplanten Thema. Es gibt keinen Weg, das eigene Betreuungsangebot sichtbar zu machen oder eingehende Anfragen übersichtlich zu verwalten.


## Our Solution

Eine Plattform wo Professoren der HWR aktiv Betreuungsangebote einstellen (Themenfelder, verfügbare Plätze, Anforderungen), und Studis gezielt nach passendem Betreuer suchen und anfragen können.

**Registrierung & Login:** Studierende und Professoren registrieren sich mit ihrer HWR-E-Mail. Die Plattform erkennt automatisch die Rolle und zeigt nur relevante Inhalte an.

**Professor/in-Feed:** durchsuchbare Übersicht aller Professoren die aktiv Betreuungsplätze anbieten, filterbar nach Fachbereich und Themenfeld.--> Kein Überblick wer Betreuungen anbietet.

**Profil-Detailseite:** jeder Professor/in hat eine Profilseite mit Themenfeldern, Anforderungen, aktuell verfügbaren Plätzen und Bewertungen anderer Studierender. 

**Anfrage-Flow:** Studis stellen eine strukturierte Anfrage mit Thema, Typ, Zeitraum und Kurzbeschreibung direkt über die Plattform

**Meine Anfragen:** Studierende sehen alle gesendeten Anfragen 
  mit aktuellem Status

**Betreuer-Dashboard:** Professoren sehen alle eingegangenen Anfragen übersichtlich und können annehmen oder ablehnen und ihren Status verwalten  

**Profil:** alle Nutzer verwalten ihr Profil; Professoren pflegen zusätzlich Themenfelder, Anforderungen und Kapazitäten

**Top-Betreuer Rangliste:** API-gestützte Rangliste der meistgefragten Professoren nach Anfragevolumen und Bewertung



## Target User(s)

- Studis die aktiv einen Betreuer für ihre Abschlussarbeit (BA/MA) suchen, besonders solche ohne persönliche Kontakte zu Professoren.
- Professorinen und Professoren der HWR die ihr Betreuungsangebot transparent kommunizieren und eingehende Anfragen strukturiert verwalten möchten.

## Happy Path

### Studi sucht einen Betreuer

1. **Registrierung:** Studi gibt Name, HWR-E-Mail, Passwort ein und wählt Rolle "Studierende/r"
2. **Professor-Feed:** Studi sieht alle verfügbaren Betreuer, filtert nach Fachbereich
3. **Profil-Detailseite:** Studi klickt auf einen Professorprofil, liest Themenfelder, Anforderungen und Bewertungen
4. **Anfrage-Flow:** Studi füllt strukturierte Anfrage aus (Thema, Zeitplan, Kurzbeschreibung) und sendet ab
5. **Meine Anfragen:** Studi verfolgt den Status seiner Anfrage
   
**End State:** Anfrage liegt beim Professor vor ✓



### Professor nimmt Anfrage an

1. **Registrierung:** Professor/in gibt Name, HWR-E-Mail, Passwort ein und wählt Rolle "Professor/in"
2. **Profil:** Professor trägt Themenfelder, Anforderungen und Kapazitäten ein
3. **Betreuer-Dashboard:** Professor sieht eingegangene Anfragen
4. **Anfrage annehmen:** Professor akzeptiert eine Anfrage




## Target Scope

ThesisMatch konzentriert sich auf den Kernprozess: Professorinnen und Professoren veröffentlichen ihre Betreuungsangebote, Studierende können diese gezielt finden und anfragen strukturiert und ohne E-Mail-Chaos.

Geplante Kernfunktionen:

- Registrierung & Login mit Rollenauswahl
- Professor-Feed mit Suche und Filter
- Profil-Detailseite
- Anfrage-Flow 
- Meine Anfragen 
- Betreuer-Dashboard 
- Profil 
- Top-Betreuer Rangliste via JSON-API




## Screen 1a — Registrieren

Neue Nutzer/in registrieren sich mit Name, HWR-E-Mail, Passwort und Rollenauswahl.

![Screen 1a](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-19%20094937.png)


## Screen 1b — Login

Bestehende Nutzer/in loggen sich mit E-Mail und Passwort ein.

![Screen 1b](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-19%20095014.png)


## Screen 2 — Professor-Feed

Durchsuchbare Übersicht aller Professorinnen und Professoren der HWR die aktiv 
Betreuungsplätze anbieten. Filterbar nach Fachbereich. 
Jede Karte zeigt Name, Fachbereich, freie Plätze und Bewertung.

![Screen 2](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-17%20201412.png)

## Screen 3 — Profil-Detailseite

Jeder Professor/in hat eine eigene Seite mit Themenfeldern, 
Anforderungen, verfügbaren Plätzen und Bewertungen. 
Direkte Möglichkeit eine Anfrage zu stellen.

![Screen 3 - Profil-Detailseite](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-17%20201428.png)


## Screen 4 — Anfrage-Flow

Studierende füllen ein strukturiertes Formular aus mit Thema, 
Typ, Zeitraum und Kurzbeschreibung. Nach Absenden erscheint 
eine Bestätigung.

![Screen 3 - Anfrage-Flow](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-17%20201446.png)



## Screen 5 — Meine Anfragen

Studierende sehen alle ihre gesendeten Anfragen mit aktuellem Status (ausstehend oder angenommen).

![Screen 4](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-19%20095225.png)

## Screen 6 — Betreuer-Dashboard

Professorinnen und Professoren sehen alle eingegangenen Anfragen mit Statistik. Jede Anfrage kann direkt angenommen oder abgelehnt werden.

![Screen 6 - Betreuer-Dashboard](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-19%20095259.png)



## Screen 7 — Profil

Alle Nutzer sehen ihr Profil. Professorinnen und Professoren können zusätzlich Themenfelder, Anforderungen und Kapazitäten verwalten und jederzeit aktualisieren.

![Screen 7](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-19%20095348.png)



## Screen 8 — Top-Betreuer Rangliste

API-gestützte Rangliste der meistgefragten Professorinnen und Professoren nach Anfragevolumen und Bewertung. 

![Screen 6 - Rangliste](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-17%20201545.png)

