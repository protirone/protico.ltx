<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09/16:SSH:01**</span>

Sie erhalten einen

* einen Ubuntu 25.04 Serverrechner mit
  * einem User `gsldkm` mit Passwort `.gsldkPw4all` und 
  * einem User `root` mit Passwort `lgsldkPw4all`
* und für das Schul-Wlan einen WLAN-User `fius` mit Passwort `fachinformatikeruser`.

**Organisieren Sie Server und Client so, dass Sie sich per ssh vom Client auf den Server einloggen können.**

1. Ermitteln Sie bitte für alle Teilschritte zuerst, "wie man das macht", 
2. setzen Sie dann den gewonnenen Plan um und
3. dokumentieren und erläutern Sie Ihre Schritte in einer Markdown-Datei:
   
* [ ] Checken und aktivieren Sie ggfls. einen ssh-Server auf dem Serverrechner.
* [ ] Binden Sie den ssh-Server ins Schul-Wlan ein.
* [ ] Checken und aktivieren Sie ggfls. einen ssh-Client auf Ihrem Arbeitsrechner (W11, MACOS oder WSL).
* [ ] Erzeugen Sie mit den richtigen Rechten einen `.ssh`-Ordner in Ihrem Homeverzeichnis.
* [ ] Erzeugen Sie ein (neues) eigenes ssh-Schlüsselpaar.
* [ ] Organisieren Sie für den User auf Ihrem Client-Rechner einen Ssh-Zugriff auf den ssh-Server
* [ ] Loggen Sie sich von ihrem Client-Rechner per ssh auf den ssh-Server ein.
* [ ] Erkunden Sie mit `find`, `grep` und `ls -la` die Umgebung auf dem ssh-Server.
* [ ] Legen Sie per remote-Befehl im Homeverzeichnis des ssh-users auf dem ssh-Server einen Ordner mit dem Namen Ihrer Klasse an. (`mkdir -p wieauchimmer`)
* [ ] Erzeugen Sie per remote-Befehl eine Datei, die Ihrem Vornamen entspricht (nur 7bit-Ascii)
* [ ] Bitte ermitteln Sie, welches Schlüsselpaar genutzt wird, wenn Sie sich selbst noch gar keinen ssh-Schüssel erzeugt haben.
* [ ] Bitte ermitteln Sie die Schwäche des Verfahrens bis hier hin!
  
---

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09/16:SSH:02**</span>

**Automatisieren Sie jetzt ihren Zugang so, dass Sie das Passwort des Users auf dem Server nicht mehr eingeben müssen.**

* [ ] Erzeugen Sie sich mit `ssh-keygen` ein eigenes Schlüsselpaar.
* [ ] Transferieren Sie Ihren neue generierten öffentlichen Schlüssel an die richtige Stelle auf dem ssh-Server-Rechner.
* [ ] Loggen Sie sich wieder aus und wieder ein. Beschreiben Sie den Unterschied.
  
---

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09/16:SSH:03**</span>


Bringen Sie folgende Beschreibung eines Tunnels von Heise mit Ihrem Rechner als Client und dem Tuxedo-Server zum Laufen.

* `ssh gsldkm@SERVERIP -L 9000:SERVERIP:80`

> *"Zunächst wird eine ganz normale SSH-Verbindung mit dem Nutzer "gsldkm" zum SSH-Server aufgebaut. Die Option "L" leitet dann den Tunnel ein: Zunächst folgt der lokale Port "9000", dann die Adresse des Webservers "SERVER:80". Es folgt die Passwortabfrage. Anschließend können Sie im Browser auf dem lokalen Rechner "127.0.0.1:9000" eingeben und bekommen zu sehen, was auch unter "SERVER:80" zu sehen ist.* (vgl. [https://www.heise.de/tipps-tricks/SSH-Tunnel-nutzen-so-geht-s-4320041.html](https://www.heise.de/tipps-tricks/SSH-Tunnel-nutzen-so-geht-s-4320041.html))

---

<span style="color: green;">_ÜBUNG_</span> <span style="color:magenta;">**LF09/16:SSH:04**</span>

Steigern Sie jetzt die Komplexität

1. Erzeugen Sie von Ihrem Rechner zum Tuxedo-Server einen Tunnel.
2. Holen Sie von dort aber nicht die Tuxedo-eigene-Html-Seite, sondern die vom Lehrerrechner.

Achtung: Recht tricky. Szenario: Sie sitzen hinter einer Firewall, die nur ssh durchlässt, tunneln Ihre Arbeitsaufträge auf einen Ihnen zugänglichen Server vor der Firewall, lassen sich den Inhalt von dort holen und ausliefern.

Viel Spaß beim Grübeln, Recherchieren und Lösen. 

---

