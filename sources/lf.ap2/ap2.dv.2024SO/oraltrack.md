<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->



### 2aa

Das LoRaWan-Gateway ist veraltet, weil seine

* Mobilfunkschnittstelle nur 3G, heute 5G
* Reichweite nur 1,5 km beträgt, heute aber mit LoRaWan bis zu 10km möglich sind
* Ethernetschnittstelle nur 10Mbps bietet, heute stehen mehr als 1Gbps zur Verfügung
* Netzwerkprotokolle *Telnet* und *HTTP* Daten unverschlüsselt übertragen. Besser wäre *https* und *ssh*

### 2ab

* UDP/IP ist zustandsloses Protokoll: 
  * Nachrichten werden im Sinne von Fire&Forget ohne Ergebnisrückmeldungen gesendet. 
  * Der Umgang mit verlorenen Paketen muss auf App-Ebene (Layer VII) geregelt werden
* TCP/IP ist zustandsbehaftetes Protkoll:
  * 3 Wege-Handshake sorgt dafür, dass beide wissen, dass kommuniziert wird
  * Diue zur Nachricht gehörenden Pakete werden auf Netzwerkebene nummeriert, sodass deren Reihenfolge auf der Netzwerkebene des Empfängers (Layer IV / V) restauriert und fehlende Pakete nachgefordert werden.

### 2ba

* Beim Edge-Computing und beim FOG-Computing werden gesammelte Rohdaten noch vor der Endverarbeitung aggegriert und verdichtet.
* Beim Edge-Computing 
  * steht die Datenaggregationskomponente in der Nähe der Datenerhebung (Edge = Kante = am Rand/an der Kante des Netzes)
  * werden die verdichteten Daten fast über das ganze Netz zum endgültigen Datenverarbeitungszentrum übertragen
* Beim FOG-Computing 
  * steht die Datenaggregationskomponente irgendwo zwischen Datenerhebung und endgültigen Datenverarbeitungszentrum
  * werden die verdichteten Daten über den verblieben Netzteil zum endgültigen Datenverarbeitungszentrum übertragen

### 2bb

Die Vorverdichtung / Aggregation erhobener Daten nahe (näher) an der Datenerhebung reduziert die Übertragungsmenge und damit die Netzübertragungskosten. 


### 2bc

* QoS für Netzverfügbarkeit
* SaaS-Angebote im Rechenzentrum (IaaS/DaaS/...)
* QOS für Datensicherung im Rechenzentrum