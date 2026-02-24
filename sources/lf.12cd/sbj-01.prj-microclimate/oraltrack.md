<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

### 0.) Context

* Themen seitens des Rahmenlehrplans **[→ ZP:Sheet:2]**
* Topic-Checkliste für 11c / Anfang 2. Halbjahr
* Topic-Checkliste für 11d / Anfang 2. Halbjahr

Wer ist 'voraus'?

### 1.) Zeithorizont **[→ ZP:Sheet:3]**

* Wochenliste im Überblick
* Constraint: 'AP2-Termin'
* Constraint: 'Zensurfestlegung'

→ 5 Wochen à 3 Tage à 4 Doppelstunden

**Gordischer Knoten der Anforderungen**:

### 2.) Scopestatement **[→ ZP:Sheet:4]**

---

<!-- uebung::start -->
<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF12cd:Mikroklima:01**</span>

Bitte bauen Sie ein Mikroklima-Reportsystem:

* Im Lehrerzimmer, in 2 Klassenräumen und im Flur sollen Temperatur, Luftfeuchtigkeit und Luftdruck gemessen werden.
* Die erhobenen Daten sollen auf einem 'Data-Aggregator' gesammelt und strukturiert gehalten werden.
* Für den 'Data-Aggregator' soll eine Datensicherung eingeplant sein.
* Der 'Data-Aggregator' soll Daten auf Anfrage an einen 'Data-Evaluator' liefern können.
* Der 'Data-Aggregator' soll Aussagen über die Datenlage ableiten, z.B. (aber nicht nur): 
  * Was ist Minimum, was Maximum, wo liegt der Median. 
  * Wie hängen Luftfeuchtigkeit und Temperatur zusammen? 
  * Gibt es einen Zusammenhang zwischen Schüleranwesenheit?
  * Ist ein Lüftungskonzept zu erkennen? Sinkt die Temperatur in den Pausen?
  * Gibt es eine schulweite Nachtabsenkung?
  * ...
* Der 'Data-Aggregator' soll Übersichten an optische und textuelle Clients liefern.

Bitte realisieren Sie das Projekt so, dass Vorgehen und Resultate es auf der 175 Jahr-Feier gezeigt werden können.

<!-- uebung::end -->

---

### 3.) Verfahren

* 5 Wochensprints a je 3 Tagen mit je 4 Doppelstunden.
* Sprint-Planning (45min.) am 1. Tag des Sprints
* Daily (15.min) morgens am 2. und 3. Tag
* Sprint-Review (25min.) am Ende 3. Tag
* Sprint-Retro (20min.) am Ende 3. Tag

* Digitale Vernetzer: Aufbau des Systems incl. Sensorik und Datenhaltung
* Daten- u. Prozessanalytiker: automatisierte Auswertung der Daten inkl. Codeimplementierung und Darstellung


### 4.) Produktbacklog

* **MVP-Teil-A**
  * { } exemplarische Datenerhebung mit einem Sensor
  * { } Übertragung der Daten an den 'Data-Aggregator'
* **MVP-Teil-B**
  * { } Konzeption des Datenhaltungssystems
  * { } exemplarische Integration von 
* **MVP-Teil-C**
  * { } exemplarische Datenlieferung an Daten-Evaluator
  * { } Berechnung eines initialen Markanten (Durchschnitt)
* **MVP-Teil-D**
  * { } exemplarischer Abruf eines Ergebnisses in einem Client
* **MVP (Durchstichsvariante)**
  * { } Erhebung einer Messung mit einem Sensor
  * { } ordnungsgemäße Übertragung an den Daten-Aggregator
  * { } ordnungsgemäße Integration in den Daten-Aggregator
  * { } ordnungsgemäße Anfrage und Auslieferung von bzw. an Daten-Evaluator
  * { } ordnungsgemäße Berechnung von Minimum, Maximum im Daten-Evaluator
  * { } ordnungsgemäße Anfrage und Auslieferung des Ergebnisses von bzw. an Data-Visualizer
* { } Sensorik auf Temperatur und Luftfeuchtigkeit erweitern.
* { } Übertragung zum Data-Aggregator auf Temperatur und Luftfeuchtigkeit erweitern.
* { } Data-Aggregator zum MQTT-Broker machen (auf MQTT umstellen) mit (eclipse-mosquitto)
* { } Data-Evaluator auf MQTT-Subscriber umstellen.
* { } Prozess der Datenerhebung designen und dokumentieren in BPMN
* { } Datenevaluation auf Durchschnitt, Median erweitern
* { } Auslieferung an Data-Visualizer auf Durchschnitt, Median erweitern
* { } Berechnungen auf weitere Aussagen erweitern
  * ...
* { } Berechnung der Prozessgüte erweitern  

### 5.) Sprints


#### 5.A)
Sprint A

#### 5.B)
Sprint B

#### 5.C)
Sprint C

#### 5.D)
Sprint D

#### 5.E)
Sprint E

### 6) Projektabschluss




