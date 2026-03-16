<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

---

### Produktbacklog

**Sprint A:**

* [X] **MVP-Teil-A**
  * {2} exemplarische Datenerhebung mit einem Sensor 
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist mit Sensor gemessen
  * {5} Übertragung der Daten an den 'Data-Aggregator'
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Aggregator'-Datenbereich abgelegt
* [X] **MVP-Teil-B**
  * {5} Konzeption des Datenhaltungssystems
    * [X] DoD: Technisches Datenhaltungssystem läuft mit einem Test-Datensatz
  * {3} exemplarische Integration der erhaltenen Daten von **MVP-Teil-A**
    * [X] DoD: Technisches Datenhaltungssystem läuft mit dem Mess-Datensatz
* [X] **MVP-Teil-C**
  * {8} exemplarische Datenlieferung an Daten-Evaluator
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Evaluator'-Datenbereich abgelegt
  * {1} Berechnung eines initialen Markanten (Durchschnitt)
    * [X] DoD: Temperaturdurchschnitt ist automatisiert berechnet.
* [X] **MVP-Teil-D**
  * {13} exemplarischer Abruf eines Ergebnisses in einem Client
    * [X] DoD: Aussage über Messung und Temperaturdurchschnitt kann in einem Client abgerufen werden.
* [X] **MVP (Durchstichsvariante)**
  * {0} 1 Messung automatisiert über die ganze Kette schicken
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist mit Sensor gemessen
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Aggregator'-Datenbereich abgelegt
    * [X] DoD: Technisches Datenhaltungssystem läuft mit dem Mess-Datensatz
    * [X] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Evaluator'-Datenbereich abgelegt
    * [X] DoD: Temperaturdurchschnitt ist automatisiert berechnet.
    * [X] DoD: Aussage über Messung und Temperaturdurchschnitt kann in einem Client abgerufen werden.

---

**Sprint B (Zwischensprint)**

* [X] **Systemarchitektur erstellen**
    * [X] Übertragung (Protokoll, Port, Software) von Sensor zur Data-Aggregatur konzipiert/dokumentiert 
    * [X] Übertragung im Data-Aggregatur zu MQTT-Broker (Protokoll, Port, Software) konzipiert/dokumentiert
    * [X] Übertragung vom MQTT-Broker zu persistentes Datenhaltungssystem (Protokoll, Port, Software) konzipiert/dokumentiert
    * [X] Datensatzstuktur im Datenhaltungssystem konzipiert/dokumentiert
    * [X] Übertragung vom Datenhaltungssystem zum Datenevaluator (Protokoll, Port, Software) konzipiert/dokumentiert
    * [X] Datenevaluator (Software, Rechner) konzipiert/dokumentiert
    * [X] Übertragung vom Datenevaluator zu Datenpräsentatoren (Protokoll, Port, Software) konzipiert/dokumentiert
    * [X] Gesamtleitbild ist erstellt.

---

**Sprint C**

* [X] MQTT-Broker aktivieren
  * {8} MQTT-Broker installieren (eclipse-mosquitto) 
  * * [X] DoD1: mosquitto ist installiert, Server läuft, 
    * [X] DoD2: Anlieferung ist per `mosquitto_pub` verifiziert,
    * [X] DoD3: Auslieferung ist per `mosquitto_sub` verifiziert,
  * {1} hinreichend großen Testdatensatz pro Sensortyp erstellen.
    * [X] DoD1: Für alle Sensorentypen sind 10 Testwerte + Messzeitpunkt definiert.
    * [X] DoD2: Wenn mit Messreihen gearbeitet wird, sind 10 Testdatensätze definiert.
  * {5} Testdatensatz-Publishing simulieren per Skript  mit/für `mosquitto_pub`
    * [X] DoD: Der Testdatensatz ist per `mosquitto_pub` zum MQTT-Broker übertragen
  * {5} Testdatensatz-Subscribing simulieren per Skript mit/für `mosquitto_sub`
    * [X] DoD: Der Testdatensatz ist per `mosquitto_sub` vom MQTT-Broker abgeholt
  * {5} Daten(file)format im Aggregator festlegen
    * [X] DoD: In einer Spezifikation ist festgelegt, wie die Daten im Aggregator abgelegt werden
  * {13} Testdatensatz im Aggregator bei Eintreffen im Daten(file)format ablegen
    * [X] DoD1: MQTT-Subscription-Client ist in Python programmiert
    * [X] DoD2: MQTT-Subscription-Client legt die Daten gemäß Spezifikation als Datei(en) ab

* [X] Datenauslieferung aktivieren
  * { } HTTP-Anfrage vom Evaluator an Aggregator designen (Parameter)
    * [X] DoD: Es ist spezifiziert, was Evaluatoren-Clients als Datenparameter vorgeben können. 
  * { } Aggregator-HTTP-Server installieren (Apache2) 
    * [X] DoD1: `Apache2` ist installiert und konfiguriert
    * [X] DoD2: `Apache2` kann auf Datenbereich zugreifen
    * [X] DoD3: `Apache2` liefert Beispieldaten über Browser aus
  * { } Datenzugriffsmodul programmieren
    * [X] DoD1: Auslieferungsmodul ist programmiert + empfängt Datanausschnittsparameter
    * [X] DoD2: Auslieferungsmodul stellt Datenausschnitt gemäß Parameter zusammen
    * [X] DoD3: `Apache2` liefert erfragten Datenausschnitt über Browser aus.
  * {X} HTTP-Client mit Request und Ablage im Fileformat in Python programmieren
    * [X] DoD1: HTTP-Client ist in Python programmiert
    * [X] DoD2: HTTP-Client holt die Datenausschnitte ab
    * [X] DoD3: gemäß Spezifikation als Datei(en) ab

---

* [X] Sensorik erweitern
  * { } Sensorik auf Temperatur und Luftfeuchtigkeit erweitern.
    * [X] DoD: Sensoren für Temperatur, Luftdruck und Luftfeuchtigkeit liefern Daten
  * { } Sensoren testweise aktivieren
    * [X] DoD: Datensätze für Temperatur, Luftdruck und Luftfeuchtigkeit sind über MQTT-Broker und MQTT-Subscription-Client abgeholt und abgelegt
  * { } Daten(file)format für Aggregator mitbestimmen
    *  [X] DoD: Daten(file)format ist final spezifiziert

---
* [X] Datenevaluation aktivieren
  * {8} Annahmeformat der Testdaten im/für Evaluator festlegen
    * [X] DoD: In einer Spezifikation ist festgelegt, wie die Daten im Evaluator ankommen und wo sie wie übergangshalber abgelegt werden
  * {8} Testdaten im/für Evaluator im Annahmeformat bereitstellen
    * [X] DoD: Testdaten sind wie spezifiziert zur Evaluation abgelegt
  * {8} Datenevaluationsmodule in Python designen und programmieren
    * [X] DoD: Framework für ein Evaluationsmodul ist programmiert
    * [X] DoD: Basic-Evaluation 'Datensatzanzahl' ist programmiert
  * {3} Grundlegende Auswertungen (Durchschnitt, Median) implementieren
    * [X] DoD: Median-Evaluation-Modul ist programmiert
    * [X] DoD: Durchschnitt-Evaluation-Modul ist programmiert


**HEAP**

* { } System für einen Produktionslauf von 3*24 vorbereiten und den ausführen
  * [ ] DoD: Das System ist ohne Eingreifen 3*24 gelaufen
  * [ ] DoD: Alle Daten sind über 3*24 gespeichert
* { } Datenauswertung mit relevanten Analysen für den Bestand eines Produktionslauf von 3*24 vorbereiten und ausführen
  * [ ] DoD: Alle 3*24-Daten sind als Ganzes ausgewertet
  * [ ] DoD: Es gibt relevante Aussagen über das Mikroklima an den Schulräumen.
* { } System für eine stündliche, dann tägliche und schließlich wöchentliche Datensicherung im Round-Robin-Verfahren vorbereiten und Datensicherung aktivieren
  * [ ] DoD: Datensicherung ist konzipiert und mit Skripten ausführbar gemacht
  * [ ] DoD: Datensicherung läuft während des 3*24 Produktionslaufes
* { } Loggingsystem implementieren, um den Zustand während Produktionslaufes zu überwachen
  * [ ] DoD: Loggingsystem ist konzipiert und mit Skripten ausführbar gemacht
  * [ ] DoD: Loggingsystem läuft während des 3*24 Produktionslaufes
  
* { } Prozess der Datenerhebung designen und dokumentieren in BPMN
* { } Datenanalyse auf Bestand gemäß `lf.11c/sbj-04.dta-evaluation` erweitern
* { } Analyse der Prozessgüte auf Bestand gemäß `sbj-02.prc-analysis` erweitern