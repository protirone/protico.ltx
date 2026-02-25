<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->

---

### 4.) Produktbacklog

* **MVP-Teil-A**
  * {2} exemplarische Datenerhebung mit einem Sensor 
    * [ ] DoD: Temperatur (Luftfeuchtigkeit) ist mit Sensor gemessen
  * {5} Übertragung der Daten an den 'Data-Aggregator'
    * [ ] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Aggregator'-Datenbereich abgelegt
* **MVP-Teil-B**
  * {5} Konzeption des Datenhaltungssystems
    * [ ] DoD: Technisches Datenhaltungssystem läuft mit einem Test-Datensatz
  * {3} exemplarische Integration der erhaltenen Daten von **MVP-Teil-A**
    * [ ] DoD: Technisches Datenhaltungssystem läuft mit dem Mess-Datensatz
* **MVP-Teil-C**
  * {8} exemplarische Datenlieferung an Daten-Evaluator
    * [ ] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Evaluator'-Datenbereich abgelegt
  * {1} Berechnung eines initialen Markanten (Durchschnitt)
    * [ ] DoD: Temperaturdurchschnitt ist automaisiert berechnet.
* **MVP-Teil-D**
  * {13} exemplarischer Abruf eines Ergebnisses in einem Client
    * [ ] DoD: Aussage über Messung und Temperaturdurchschnitt kann in einem Client abgerufen werden.
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
* **MVP-Teil-A**
  * {2} exemplarische Datenerhebung mit einem Sensor 
    * [ ] DoD: Temperatur (Luftfeuchtigkeit) ist mit Sensor gemessen
  * {5} Übertragung der Daten an den 'Data-Aggregator'
    * [ ] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Aggregator'-Datenbereich abgelegt
* **MVP-Teil-B**
  * {5} Konzeption des Datenhaltungssystems
    * [ ] DoD: Technisches Datenhaltungssystem läuft mit einem Test-Datensatz
  * {3} exemplarische Integration der erhaltenen Daten von **MVP-Teil-A**
    * [ ] DoD: Technisches Datenhaltungssystem läuft mit dem Mess-Datensatz
* **MVP-Teil-C**
  * {8} exemplarische Datenlieferung an Daten-Evaluator
    * [ ] DoD: Temperatur (Luftfeuchtigkeit) ist im 'Data-Evaluator'-Datenbereich abgelegt
  * {1} Berechnung eines initialen Markanten (Durchschnitt)
    * [ ] DoD: Temperaturdurchschnitt ist automaisiert berechnet.

#### 5.B)
Sprint B

#### 5.C)
Sprint C

#### 5.D)
Sprint D

#### 5.E)
Sprint E

### 6) Projektabschluss




