
<!--
% This file is part of the Open Source project 'proTirone'
% (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
% It is distributed under the terms of the creative commons license
% CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
-->


## Pakete von innen nach außen:

### P1 echo (tcp/ipv4)

* L7: 
> "Well done"
* L4 (tcp): `0xFFFB 0x0007 4*x 4*x 0x0 3*x 4*x
* L3 (ip): 4*x 4*x 1*x 0x06 2*x 0x23451234 0x43215423>
* L2 (ef): 8*x 0x847321 0x123748 4*x 0x0800 4*? 12*x


### P2 http (tcp/ipv4)

* L7: 
> "GET /index.html HTTP/1.1\n
> Host: http://tierschutz.hessen.de/\n
> \n
> "
* L4 (tcp): `0xFFFA 0x0050 4*x 4*x 0x0 3*x 4*x`
* L3 (ip): 4*x 4*x 1*x 0x06 2*x 0x23451234 0x43215423
* L2 (ef): 8*x 0x847321 0x123748 4*x 0x0800 4*? 12*a

### P3 http (udp/ipv4)
* L7: 
> "GET /index.html HTTP/3.0\n
> Host: http://vegan.de/\n
> \n
> "
* L4 (udp): `0xFFFC 0x0050 0x0030 2*x`
* L3 (ip): 4*x 4*x 1*x 0x11 2*x 0x23451234 0x43215423
* L2 (ef): 8*x 0x847321 0x123748 4*x 0x0800 4*? 12*a


### P4 telnet (tcp/ipv6)
* L7:
> "echo ‘well done’"
* L4 (tcp): `0xFFFD 0x0011 4*x 4*x 0x0 0x? 3*x 4*x`
* L3 (ipv6): 4*x 0x10 0x06 1*x 0x2001234767891618 0x2001816198767432
* L2 (ef): 8*x 0x847321 0x123748 4*x 0x86DD 4*? 12*


