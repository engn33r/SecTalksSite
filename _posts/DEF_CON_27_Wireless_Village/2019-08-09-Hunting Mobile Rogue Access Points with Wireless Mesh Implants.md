---
type: youtube
yt-video-id: oTcitUA9mhg
homedisplay: iframe
title: Hunting Mobile Rogue Access Points with Wireless Mesh Implants
tags: [DEFCON, DEF CON, DEFCON27, DEF CON 27, wireless]
category: DEF_CON_27
layout: post-classic-sidebar-left
speaker: m1n1
conf: DEF CON 27
track: Wireless Village
yr: 2019
vidurl: https://www.youtube.com/watch?v=oTcitUA9mhg
---
We performed a case study with the most basic attack profile: the bad BSSID is known and the blue team is searching for the physical device, which is on the move. The theater was the DEFCON 26 wireless CTF. Since we did pretty well in DEFCON 25's, locating the stationary rogue access point, we hoped to evolve our tactics. We attempted to create a cheap and easy to deploy solution that can be used in the field to track down and locate rogue mobile operators using C2 infrastructure. Utilizing system-on-chip espressif hardware, the espressif SDK, and several open source projects, an extensible wireless mesh command and control software was written to create a framework from which wireless implants could be placed in the field within proximity of one another, and communicated with over a simple Python script running on a raspberry pi as a root node. Once the operator walks through the mesh, the intention is to receive an alert and physically hone in on the rogue AP. https://github.com/joeminicucci/fox_trap