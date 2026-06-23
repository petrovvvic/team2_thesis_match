---
title: Solution Elements
parent: Product Discovery
nav_order: 3
---

{: .no_toc }
# Solution Elements

## Vorgehen

Aus den in der Need-Finding-Phase identifizierten Problemen (siehe [Target Users + Problems](02-users-problems.md)) haben wir konkrete Sub-Probleme abgeleitet. Für jedes Sub-Problem wurde ein Solution Element entwickelt, das sich direkt in einem Screen der App widerspiegelt. So lässt sich jede Funktion auf ein reales Nutzerproblem zurückführen.

Die Spalte *Quelle* unterscheidet zwischen Umfrage (durch die Studi-/Prof-Umfragen belegt) und Annahme (von uns angenommen, nicht direkt belegt).

## Sub-Problem → Solution → Screen

| # | Sub-Problem | Quelle | Solution Element | Screen |
| --- | --- | --- | --- | --- |
| 1 | Studierende kennen keine passenden Professor:innen und wissen nicht, wer welche Themen betreut. | Umfrage | Durchsuchbarer Professor-Feed mit Profilen (Themenfelder, Fachbereich). | Screen 2 (Feed), Screen 3 (Profil-Detail) |
| 2 | Vor der Anfrage gibt es keine Information über freie Betreuungsplätze / Kapazität. | Umfrage | Verfügbarkeits-Anzeige im Profil + Filter nach Fachbereich/Verfügbarkeit. | Screen 2, Screen 3 |
| 3 | Lange Kommunikation, bis sich herausstellt, dass das Thema fachlich nicht passt → Zeitverlust. | Umfrage | Strukturierte Anfrage (Thema, Typ, Zeitraum, Kurzbeschreibung) vorab. | Screen 4 (Anfrage-Flow) |
| 4 | Professor:innen erhalten unstrukturierte und fachlich unpassende Anfragen. | Umfrage | Pflichtfelder im Anfrageformular → vollständige, vergleichbare Anfragen. | Screen 4 |
| 5 | Professor:innen haben hohen Verwaltungsaufwand und keinen Überblick über eingehende Anfragen. | Umfrage | Betreuer-Dashboard mit Status sowie Annehmen/Ablehnen. | Screen 6 (Dashboard) |
| 6 | Studierende verlieren den Überblick über den Status ihrer Anfragen. | Annahme | „Meine Anfragen" mit Statusanzeige. | Screen 5 |
| 7 | Kommunikation läuft unstrukturiert per E-Mail. | Umfrage | Anfragebezogener Chat direkt in der Plattform. | Chat |

## Ideenfindung (Brainstorming)

Im Brainstorming entstanden mehr Ideen, als am Ende umgesetzt wurden. Neben den oben gewählten Lösungen wurden u. a. ein Bewertungssystem für Professor:innen und eine Tinder-artige Swipe-UI für das Matching diskutiert. Beide wurden nach der Evaluation bewusst verworfen.Die Begründung steht unter [Tests](04-tests.md).

## Prototypen / Wireframes

Auf Basis der Solution Elements wurden Wireframes für die zentralen Screens erstellt. Die Screens sind auf der Seite [Value Proposition → Target Scope & UI Screens](../01-value-proposition.md) abgebildet; die Bilddateien liegen in `docs/assets/images/`.

## Raw Material

- Wireframes / UI-Screens: `docs/assets/images/` (eingebunden auf der [Value-Proposition-Seite](../01-value-proposition.md))
- Umfragen als Beleg für die Sub-Probleme: siehe [Target Users + Problems](02-users-problems.md)
- Verworfene Ideen (Bewertungssystem, Swipe-UI): siehe [Tests](04-tests.md)
