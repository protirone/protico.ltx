<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 1. Projekt(management) **[→ ZP:Sheet:2]**


* **Projekt** vs. **Linientätigkeit**
* Vorhaben vs. Routine
* dezidiertes Ende vs. wiederholbar
* einzigartiges Ziel vs. gleichartige Zielsetzung
* unbekannter Herstellungsprozess vs bekannter Herstellungsprozess



hat  **[→ ZP:Sheet:3]**

*  **Projekteignerin**: Zielentscheiderin, das Gesicht nach außen
*  **Projektsponsorin**: Geldgeberin, Zielentscheiderin
*  **Stakeholder**: nachgelagerte Beeinflusserinnen
*  **Project Steering Committee**: formalisierter Einfluss
*  **Projektmanagerin**: ausführende Leiterin, das Gesicht nach innen

definiert durch  **[→ ZP:Sheet:4]**

* Deutsche Gesellschaft für Projektmanagement
  * fokussiert aufs 'Wie' und 'Definitionen'
  * kommt vom 'Wasserfall'-Modell her
  * deutsch ausgerichtet
  * [https://www.gpm-ipma.de/](https://www.gpm-ipma.de/)

* Project Management Institute
  * fokussiert auf Prozesse und Begriffe
  * kommt vom 'Wasserfall'-Modell her
  * international ausgerichtet
  * [https://www.pmi.org/](https://www.pmi.org/)

**Wasserfallmodell:** **[→ ZP:Sheet:5]** nachgelagerten Bearbeitern Dokus 'über den Zaun werfen'

* Projektmanagerin → 
* → Funktionales Design → 
* → → Technisches Design → 
* → → → Programmierung → 
* → → → → Testen → 
* → → → → → Deployment  

**Nachteile:**

* lange abgeschlossene Zyklen 
* spät erkennbarer Änderungsbedarf
* formalistisch langwieriges Wiederansetzen
* aufwendiges Restaffing
* große 'Reibungsverluste' beim Verstehen
* oft von Wirklichkeit / Markt überholt

### 2. Scrum-Projekt **[→ ZP:Sheet:6]**

**2.1) Idee** **[→ ZP:Sheet:6]**

* Der Productowner 
  * teilt den inhaltlichen Scope in einzelne Arbeitspakete 
  * definiert dazu jeweils das Erledigungskriterium 'Definition of Done' - messbar an ablaufbarer Software
  * priorisiert die einzelnen Aufgaben 
  * pflegt die Liste als *Productbacklog*
  * bestimmt NICHT, wer wann was tut 
* Das Projekt wird in kleinen iterativen Feedbackschleifen namens Sprints umgesetzt
* Die Entwickler
  * nehmen zu sich zu jedem Sprint aus dem Productbacklog von oben so viel Tasks, wie sie sich umzusetzen (Definition of Done) trauen: **Sprintblacklog**
  * organisieren ihre Arbeitsweise und Aufteilung selbst
  * entscheiden letztlich die Art der technischen Umsetzung
* Die Scrummasterin
  * überwacht die Einhaltung der Scrumregeln
  * bestimmt NICHT, wer wann was tut 
  * pflegt Tasksboards Kanban
  * sorgt für Informationsfluss
  

Anmerkung: Scrum

* will das ’Wasserfall’-Problemlösen
* entstanden aus dem Unwohlsein der Web-Sites-Entwickler mit dem traditionellen Projektmanagement
* ist letztlich ein Time- \& Material-Beauftragungsmodell
* getragen von Organisation [https://www.scrum.org/](https://www.scrum.org/)

**2.2) Spirit** **[→ ZP:Sheet:6]**


tdb.

**2.3) Prozess** **[→ ZP:Sheet:7]**

* **Sprintplanning** am Sprintbeginn:
  * *Productowner* hat Produktbacklog repriorisiert / erweitert / reduziert
  * *Productowner* legt für jeden Eintrag eine Definition of Done fest.
  * *Productowner* erläutert seine funktionalen Wünsche (Art der Umsetzung bei Team)
  * *Planning Poker*: für alle (nächsten) Einträge
    * jeder Entwickler bestimmt für sich die Komplexität (1,2,3,5,8,13 | 20, 40)
    * jeder zeigt seine Zahl: Ausreißer nach oben / unter sagen warum
    * Team einigt sich auf eine Komplexitätszahl für den Eintrag
  * *Team* einigt sich auf eine Komplexitätszahl, die sie im Sprint erreichen können.
  * *Team* nimmt von oben Tasks in seinen Sprintbacklog
* **Daily**: 
  * Team steht im Kreis
  * dient der gegenseitigen Information
  * jede sagt sehr kurz:
    * was hat sie gestern getan / erreicht
    * welche Hindernisse es gab (Srummaster: Impedimentlog)
    * was sie heute macht 
* **Sprintreview**: Vorführung dessen was erreicht ist (Lauffähige Software)
* **Sprintretrospektive**: Zwanglose Besprechung, was gut war, was das Team anders machen will, was es zusätzlich braucht.


Anmerkung:

* Warum 'Stilles Zeigen' vor der Diskussion: Damit jeder unbeeinflusst seine Meinung zeigt
* Warum keine inhaltliche Bewertungskriterien, nur Zahlen: Damit das Team seine Intuition ausbildet. Formlisierung führt zu streit, Inutition pendelt sich ein.


