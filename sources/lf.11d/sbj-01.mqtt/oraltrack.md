<!--
% This file is part of the Open Source project 'proTironeComputatri'
% (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->


### 1. MQTT **[→ ZP:Sheet:2]**

* stand bis Version 3.1 für *Message Queueing Telemetry Transport*, ab 3.1.1 eigenständiger Begriff
* ist ein leichtgewichtiges Publish/Subscribe-Messaging-Protokoll. 
* basiert auf dem Prinzip des Veröffentlichens von Nachrichten und Abonnierens von Themen, auch bekannt als „Pub/Sub“
* nutzt Topics in Form von gereihten 'Begriffen', die je durch einen Slash getrennt sind
* erlaubt den Subskribern mit Wildcards mehre Sensorenachrichten zu abbonieren
* Publisher bestimmt das Format (gern JSON, aber auch binär oder XML etc.)
* Technisch kann jeder Client Publisher und Subscriber werden.

* [https://de.wikipedia.org/wiki/MQTT](https://de.wikipedia.org/wiki/MQTT)

### 2. MQTT Architektur

### 3. MQTT Protokoll

### 4. MQTT Anwendung 

#### 4.1) 
Über Mosquitto

#### 4.2)
Zur Installation 

**A) Inbetriebnahme des Servers unter Ubuntu 24.04 (LTS)**:

* **A1:** System auf letzte Paketversionen upgraden:
  * `sudo apt-get update`
  * `sudo apt-get upgrade`
* **A2:** Mosquitto-Server installieren:
  * `sudo apt-get install -y mosquitto` # `-y` = *assume yes*
* **A3:** Verifikation:
  * checken, ob Prozess läuft: `ps aux | grep mosquitto`
  * Gegencheck 1: `mosquitto -v` # Version überprüfen. Ergibt in etwa:
  
```
1772566291: mosquitto version 2.0.18 starting
1772566291: Using default config.
1772566291: Starting in local only mode. Connections will only be possible from clients running on this machine.
1772566291: Create a configuration file which defines a listener to allow remote access.
1772566291: For more details see https://mosquitto.org/documentation/authentication-methods/
1772566291: Opening ipv4 listen socket on port 1883.
1772566291: Error: Address already in use
1772566291: Opening ipv6 listen socket on port 1883.
1772566291: Error: Address already in use

```

  * Gegencheck 2: `sudo systemctl status mosquitto` # Prozess überprüfen. Ergibt etwa:

```
> mosquitto.service - Mosquitto MQTT Broker
     Loaded: loaded (/usr/lib/systemd/system/mosquitto.service; enabled; preset: enabled)
     Active: active (running) since Tue 2026-03-03 20:30:25 CET; 1min 43s ago
       Docs: man:mosquitto.conf(5)
             man:mosquitto(8)
    Process: 172341 ExecStartPre=/bin/mkdir -m 740 -p /var/log/mosquitto (code=exited, status=0/SUCCESS)
    Process: 172343 ExecStartPre=/bin/chown mosquitto:mosquitto /var/log/mosquitto (code=exited, status=0/SUCCESS)
    Process: 172345 ExecStartPre=/bin/mkdir -m 740 -p /run/mosquitto (code=exited, status=0/SUCCESS)
    Process: 172347 ExecStartPre=/bin/chown mosquitto:mosquitto /run/mosquitto (code=exited, status=0/SUCCESS)
   Main PID: 172350 (mosquitto)
      Tasks: 1 (limit: 9219)
     Memory: 1.0M (peak: 1.5M)
        CPU: 96ms
     CGroup: /system.slice/mosquitto.service
             |-172350 /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf

```

*  **A4:** Portbelegung überprüfen:
  * `sudo lsof -i -P -n | grep LISTEN` # ggf. grep nach 1883 oder mosquitto
  * `sudo netstat -tuln` # ggf. grep nach 1883
* **A5:** Serverfazit:
  * Hauptkonfiguration: `/etc/mosquitto/mosquitto.conf`
  * Teilkonfigurationen: `/etc/mosquitto/conf.d/`

**B) Inbetriebnahme der Clients unter Ubuntu 24.04 (LTS)**:

* **B.1** Clients installieren
  * `sudo apt install -y mosquitto-clients`
* **B.2** Verifikation
  * `which mosquitto_pub` # ergibt Pfad zu Tool
  * `which mosquitto_sub` # ergibt Pfad zu Tool
  * `mosquitto_pub --version` # Lauffähigkeit überprüfen
  * `mosquitto_sub --version` # Lauffähigkeit überprüfen

**C) Democase unter Ubuntu 24.04 (LTS)**:

* **C1**: Werte eines Typs subskribieren (in eigenem Terminal)
  * `mosquitto_sub -t "home/sensor/temperature"`
* **C2**: Einfache Werte dazu publizieren (in eigenem Terminal))
  * `mosquitto_pub -t "home/sensor/temperature" -m "30.5" -q 1 -r`
  * `mosquitto_pub -t "home/sensor/temperature" -m "45.2" -q 1 -r`
    * `-t` = Message-Topic
    * `-m` = Message. (Kann z.B. JSON File sein)
    * `-q` = Qos-Level: 
      * 0: The broker/client will deliver the message once, with no confirmation.
      * 1: The broker/client will deliver the message at least once, with confirmation required.
      * 2: The broker/client will deliver the message exactly once by using a four step handshake.
    * `-r`: retain: message will be retained as a "last known good" value on the broker
    * 
* **C3**: Komplex Werte dazu publizieren (in eigenem Terminal))
  * `mosquitto_pub -t "home/sensor/temperature" -m "{'time':'20260304', 'temp':30.5, 'weight':5}" -q 1 -r`
  
Anmerkung: 
* Was *-t* meint, ist durch die Werte / die Sensoren bestimmt
* Ein Topic ist immer eine Begriffsreihe, deren Element durch je einen '/' voneinander getrennt sind.
* Ein Publisher liefert immer eine ausgefüllte Begriffsreihe.
* Ein Subscriber kann Wildcards benutzen
  * `+` wildcard for a single level of hierarchy
  * `#` wildcard for all remaining levels of hierarchy
  
Dahinter steht die Idee, dass alle Sensoren eines Systems durch einen Baum klassifiziert und gruppiert sind.

#### 4.3)
Abstraktes Beispiel:

* **(A)** IST-Analyse
  * Sensor 1 in Raum 1 liefert Temperatur und Luftdruck (Hauptsensor)
  * Sensor 2 in Raum 1 liefert Lautstärke (Nebensensor)
  * Sensor 1 in Raum 2 liefert Temperatur und Luftdruck (Hauptsensor)
  * Sensor 2 in Raum 2 liefert Luftfeuchtigkeit (Nebensensor)
* **(B)** Message-Topic-Design
  * `R1/S1/Temp_Press`
  * `R1/S2/Volume`
  * `R2/S1/Temp_Press`
  * `R2/S2/Humidity`
* **(C)** Alle Werte aus R2 subskribieren: `mosquitto_sub -t "R2/#"`
* **(D)** Alle Temperaturwerte subskribieren: `mosquitto_sub -t "+/+/Temp_Press"`
* **(D)** Alle Hauptsensoren subskribieren: `mosquitto_sub -t "+/S1/#"`
* **(E)** Ein Wertepublikationsskript schreiben:

```
#!/bin/bash

mosquitto_pub -t "R1/S1/Temp_Press" -m "{'T': 31.5, 'P':1.2}" -q 1 -r
mosquitto_pub -t "R1/S1/Temp_Press" -m "{'T': 41.5, 'P':1.3}"-q 1 -r
mosquitto_pub -t "R1/S2/Volume" -m "60" -q 1 -r
mosquitto_pub -t "R1/S2/Volume" -m "63" -q 1 -r
mosquitto_pub -t "R2/S1/Temp_Press" -m "{'T': 32.5, 'P':2.2}" -q 1 -r
mosquitto_pub -t "R2/S1/Temp_Press" -m "{'T': 42.5, 'P':2.3}" -q 1 -r
mosquitto_pub -t "R1/S2/Humidity" -m "82"  -q 1 -r
mosquitto_pub -t "R1/S2/Humidity" -m "72" -q 1 -r

```


Hinweis:

* [https://mosquitto.org/man/mqtt-7.html](https://mosquitto.org/man/mqtt-7.html)
* [https://mosquitto.org/man/mosquitto_pub-1.html]https://mosquitto.org/man/mosquitto_pub-1.html()
* [https://mosquitto.org/man/mosquitto_sub-1.html](https://mosquitto.org/man/mosquitto_sub-1.html)
* [https://www.centron.de/tutorial/mosquitto-mqtt-broker-auf-ubuntu-20-04-installieren-sichern/](https://www.centron.de/tutorial/mosquitto-mqtt-broker-auf-ubuntu-20-04-installieren-sichern/)
* [https://docs.vultr.com/how-to-install-mosquitto-mqtt-broker-on-ubuntu-24-04](https://docs.vultr.com/how-to-install-mosquitto-mqtt-broker-on-ubuntu-24-04)
* [https://docs.litmus.io/litmusedge/how-to-guides/integration-guides/install-mosquitto-mqtt-broker-ubuntu](https://docs.litmus.io/litmusedge/how-to-guides/integration-guides/install-mosquitto-mqtt-broker-ubuntu)