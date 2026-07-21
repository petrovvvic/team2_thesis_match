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

Eine Plattform wo Professoren der HWR aktiv Betreuungsangebote einstellen (Themenfelder, Anforderungen und Verfügbarkeit), und Studis gezielt nach passendem Betreuer suchen und anfragen können.

**Registrierung & Login:** Studierende und Professoren registrieren sich mit ihrer HWR-E-Mail. Die Plattform erkennt automatisch die Rolle und zeigt nur relevante Inhalte an.

**Professor/in-Feed:** durchsuchbare Übersicht aller Professoren die aktiv Betreuungsplätze anbieten. Suche nach Name oder Forschungsbereich, filterbar nach Facheinheit und Verfügbarkeit.

**Profil-Detailseite:** jeder Professor/in hat eine Profilseite mit Themenfeldern, Anforderungen und aktuellem Verfügbarkeitsstatus.

**Anfrage-Flow:** Studis stellen eine strukturierte Anfrage direkt über die Plattform — mit Prüfer-Rolle (Erst-/Zweitprüfer:in), Arbeitstitel, Kurzbeschreibung und gewünschtem Zeitraum.

**Meine Anfragen:** Studierende sehen alle gesendeten Anfragen mit aktuellem Status und können sie bearbeiten oder zurückziehen

**Betreuer-Dashboard:** Professoren sehen alle eingegangenen Anfragen übersichtlich und können annehmen oder ablehnen und ihren Status verwalten  

**Chat:** Studierende und Professor:innen kommunizieren pro Anfrage direkt über einen Nachrichtenverlauf inklusive PDF-Anhängen — strukturiert statt per E-Mail.

**Profil:** alle Nutzer verwalten ihr Profil; Professoren pflegen zusätzlich Facheinheit, Forschungsbereiche, Anforderungen und ihre Verfügbarkeit

**Top-Betreuer Rangliste:** API-gestützte Rangliste der meistgefragten Professoren nach Anfragevolumen



## Target User(s)

- Studis die aktiv einen Betreuer für ihre Abschlussarbeit (BA) suchen, besonders solche ohne persönliche Kontakte zu Professoren.
- Professorinen und Professoren der HWR die ihr Betreuungsangebot transparent kommunizieren und eingehende Anfragen strukturiert verwalten möchten.

## Value Proposition Canvas

Der Canvas fasst zusammen, welche Aufgaben, Frustrationen und Ziele (Customer Profile) die App mit welchen Funktionen adressiert (Value Map). Die Pains und Jobs stammen aus den Umfragen (siehe [Product Discovery](product-discovery/02-users-problems.md)).

### Studierende (primäres Segment)

| Customer Profile | Value Map (App) |
| --- | --- |
| **Customer Jobs:** passende Betreuung finden, Thema fachlich klären, Anfrage stellen, Überblick behalten | **Products & Services:** Professor-Feed, Profil-Detailseite, strukturierte Anfrage, „Meine Anfragen", Chat |
| **Pains:** kennt keine passenden Professor:innen, keine Info zu Themen/Kapazität, lange Wartezeit, mehrfache Absagen, Zeitverlust durch fachlich unpassende Themen | **Pain Relievers:** Feed zeigt Professor:innen, Themenfelder und Verfügbarkeit vorab; Filter nach Facheinheit; strukturierte Anfrage verhindert Missverständnisse; Statusübersicht |
| **Gains:** schnell eine passende Betreuung, Transparenz über Verfügbarkeit, weniger Absagen | **Gain Creators:** gezielte, passende Anfragen; schnellere Rückmeldung; kein E-Mail-Chaos |

### Professor:innen (sekundäres Segment)

| Customer Profile | Value Map (App) |
| --- | --- |
| **Customer Jobs:** fachlich passende, gut vorbereitete Anfragen erhalten, Anfragen verwalten, Aufwand senken | **Products & Services:** Profil mit Forschungsbereichen und Verfügbarkeit, Anfrageformular mit Pflichtfeldern, Betreuer-Dashboard |
| **Pains:** unstrukturierte und fachlich unpassende Anfragen, Verwaltungsaufwand, kein Überblick | **Pain Relievers:** strukturierte Pflicht-Anfragen, Dashboard mit Annehmen/Ablehnen und Statusverwaltung |
| **Gains:** weniger Fehl-Anfragen, Studierende schneller einschätzen | **Gain Creators:** vollständige, vergleichbare Anfragen; klare Übersicht |

## Happy Path

### Studi sucht einen Betreuer

1. **Registrierung:** Studi gibt Name, HWR-E-Mail, Passwort ein und wählt Rolle "Studierende/r"
2. **Professor-Feed:** Studi sieht alle verfügbaren Betreuer, filtert nach Facheinheit und Verfügbarkeit
3. **Profil-Detailseite:** Studi klickt auf einen Professorprofil, liest Themenfelder und Anforderungen
4. **Anfrage-Flow:** Studi füllt strukturierte Anfrage aus (Prüfer-Rolle, Arbeitstitel, Kurzbeschreibung, Zeitraum) und sendet ab
5. **Meine Anfragen:** Studi verfolgt den Status seiner Anfrage
   
**End State:** Anfrage liegt beim Professor vor ✓



### Professor nimmt Anfrage an

1. **Registrierung:** Professor/in gibt Name, HWR-E-Mail, Passwort ein und wählt Rolle "Professor/in"
2. **Profil:** Professor trägt Facheinheit, Forschungsbereiche, Anforderungen und Verfügbarkeit ein
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
- Chat mit dem Prof
- Betreuer-Dashboard 
- Profil 
- Top-Betreuer Rangliste via JSON-API





# Target Scope & UI Screens


---
## Screen 1a — Registrieren

Neue Nutzer/in registrieren sich mit Name, HWR-E-Mail, Passwort und Rollenauswahl.

![Screen 1a](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-19%20094937.png)


## Screen 1b — Login

Bestehende Nutzer/in loggen sich mit E-Mail und Passwort ein.

![Screen 1b](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-19%20095014.png)


## Screen 2 — Professor-Feed

Durchsuchbare Übersicht aller Professorinnen und Professoren der HWR die aktiv 
Betreuungsplätze anbieten. Filterbar nach Fachbereich. 
Jede Karte zeigt Name, Fachbereich und freie Plätze.

![Screen 2](https://github.com/petrovvvic/team2_thesis_match/blob/3ddfeabb3cf5b0f6ca5cc236aa22253ffcf291e4/docs/assets/images/Screenshot%202026-07-20%20133058.png)


----

## Screen 3 — Profil-Detailseite

Jeder Professor/in hat eine eigene Seite mit Themenfeldern, Anforderungen und Verfügbarkeitsstatus. Direkte Möglichkeit eine Anfrage zu stellen.

![Screen 3 - Profil-Detailseite](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/9ea398e4b7b7fdba98ae8ce9374aaba406ff6ee5/docs/assets/images/Screenshot%202026-07-20%20133136.png)

## Screen 4 — Anfrage-Flow

Studierende füllen ein strukturiertes Formular aus mit Thema, Typ, Zeitraum und Kurzbeschreibung. Nach Absenden erscheint eine Bestätigung.

![Screen 4 - Anfrage-Flow](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-17%20201446.png)

---

## Screen 5 — Studis-Dashboard

Studierende sehen alle ihre gesendeten Anfragen mit aktuellem Status (ausstehend oder angenommen).

![Screen 5](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/9ea398e4b7b7fdba98ae8ce9374aaba406ff6ee5/docs/assets/images/Screenshot%202026-07-20%20133205.png)

## Screen 6 — Betreuer-Dashboard

Professorinnen und Professoren sehen alle eingegangenen Anfragen mit Statistik. Jede Anfrage kann direkt angenommen oder abgelehnt werden.

![Screen 6 - Betreuer](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/823f51aa4059faf5ec534373e171773c3158b076/docs/assets/images/Screenshot%202026-07-20%20133226.png)

---

## Screen 7 — Profil

Alle Nutzer sehen ihr Profil. Professorinnen und Professoren können zusätzlich Themenfelder, Anforderungen und Kapazitäten verwalten und jederzeit aktualisieren.

![Screen 7](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/main/docs/assets/images/Screenshot%202026-05-19%20095348.png)

---

##  Screen 8 - Chatt

Studierende und Professorinnen/Professoren können zu jeder Betreuungsanfrage direkt Nachrichten austauschen und PDF-Anhänge versenden.

![Screen 7](https://raw.githubusercontent.com/petrovvvic/team2_thesis_match/0d17136ac1c7d4b6a66b5150e3e211330d2338c6/docs/assets/images/Screenshot%202026-07-20%20133252.png)


## API — Top-Betreuer Rangliste

Rankt die meistgefragten Professorinnen und Professoren nach Anfragevolumen. Abrufbar direkt über die URL











