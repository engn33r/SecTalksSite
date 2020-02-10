---
type: youtube
yt-video-id: jM4wKCGvbp0
homedisplay: iframe
title: First Try DNS Cache Poisoning with IPv4 and IPv6
tags: [DEFCON, DEF CON, DEFCON27, DEF CON 27, network]
category: DEF_CON_27
layout: post-classic-sidebar-left
speaker: Travis Palmer
conf: DEF CON 27
track: Packet Hacking Village
yr: 2019
vidurl: https://www.youtube.com/watch?v=jM4wKCGvbp0
---
DNS fragmentation attacks are a more recent series of cache poisoning attacks on resolvers. Even if DNSSEC is fully implemented, an attacker can still poison various unsigned records in the response. These types of attacks are difficult but have been considered feasible over IPv4, but impossible over IPv6. Unfortunately, changes to the Linux kernel have made the entropy limiting this attack inferable off-path, poisoning on the first iteration is now possible. This talk will cover how this attack is carried out, and mitigations that can be put in place by operators of DNS servers to limit its effectiveness.

Travis (Travco) Palmer is a Security Research Engineer at Cisco. Travis is a certified OSCP and OSCE who has been getting paid to either fix or break something for over seven years. He is a fan (and sometimes-contributer) of a number of simulator/sandbox video games, and keeper of too many unfinished hardware projects.

Brian Somers is a Site Reliability Engineer for Cisco Umbrella (formerly OpenDNS). He specializes in large scale development on Unix-like platforms, software design & architecture, low level C development, and FreeBSD development.