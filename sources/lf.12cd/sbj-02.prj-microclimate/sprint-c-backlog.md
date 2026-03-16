<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


**Sprint C**

---

* [x] MQTT-Broker aktivieren
  * {8} MQTT-Broker installieren (eclipse-mosquitto) 
  * * [X] DoD1: mosquitto ist installiert, Server läuft, 
    * [X] DoD2: Anlieferung ist per `mosquitto_pub` verifiziert,
    * [X] DoD3: Auslieferung ist per `mosquitto_sub` verifiziert,
  * {1} hinreichend großen Testdatensatz pro Sensortyp erstellen.
    * [X] DoD1: Für alle Sensorentypen sind 10 Testwerte + Messzeitpunkt definiert.
    * [X] DoD2: Wenn mit Messreihen gearbeitet wird, sind 10 Testdatensätze definiert.
  * {40} Testdatensatz-Publishing simulieren per Skript  mit/für `mosquitto_pub`
    * [X] DoD: Der Testdatensatz ist per `mosquitto_pub` zum MQTT-Broker übertragen
  * {13} Testdatensatz-Subscribing simulieren per Skript mit/für `mosquitto_sub`
    * [X] DoD: Der Testdatensatz ist per `mosquitto_sub` vom MQTT-Broker abgeholt
  * {5} Daten(file)format im Aggregator festlegen
    * [X] DoD: In einer Spezifikation ist festgelegt, wie die Daten im Aggregator abgelegt werden

* [X] Datenevaluation aktivieren
  * {8} Annahmeformat der Testdaten im/für Evaluator festlegen
    * [X] DoD: In einer Spezifikation ist festgelegt, wie die Daten im Evaluator ankommen und wo sie wie übergangshalber abgelegt werden
  * {8} Testdaten im/für Evaluator im Annahmeformat bereitstellen
    * [X] DoD: Testdaten sind wie spezifiziert zur Evaluation abgelegt
 





