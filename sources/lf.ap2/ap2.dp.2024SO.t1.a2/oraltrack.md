<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->
<!-- LTeX:Language=de-DE -->



### 1a 

s. diagrams.pdf


### 1b

zu ergänzen sind die Werte

| Bezeichnung | Beschreibung | API | Auth-Server
|---|---|---|---|
| t_running | Prozess läuft | 3ms | 5ms |
| t_waiting | Prozess wartet | **5ms** | **0ms** |
| t_token | Gesamtzeit für Token-Generierung | **8ms** | **5ms** |

### 1ca

* 60.000 Besucher auf 10 Eingänge = 6000 Besucher / Eingang
* Die Kontrollzeit beträgt 1 Std (18.00 - 19.00) => 3600s kann jedes Kontrollgerät arbeiten.
* Jedes Kontrollgerät braucht 3s pro Person. => 3300s / 3s = 1200 Personen kann ein Gerät in der Zeit kontrollieren.
* Um 6000 Besucher pro Eingang u kontrollieren braucht man 6000/1200 = 5 Geräte.
* => Um 60000 Besucher über 10 Eingänge zu kontrollieren, braucht man 50 Geräte.
* Mit einem Fallback/Reserve von 5% für Geräte, müssen **insgesamt** 50+(50*5/100) = 52.5 = **53 Kontrollgeräte** eingesetzt werden.

### 1cb

**Mehrere AuthServer** über einen Loadbalancer zu einer Kotrolleinheit verbinden.


