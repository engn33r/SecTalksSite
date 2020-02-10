---
type: youtube
yt-video-id: GBTu1hk4_VQ
homedisplay: iframe
title: Evaded Microsoft ATA
tags: [DEFCON, DEF CON, DEFCON27, DEF CON 27, blue team]
category: DEF_CON_27
layout: post-classic-sidebar-left
speaker: Siyu Zhu
conf: DEF CON 27
track: Blue Team Village
yr: 2019
vidurl: https://www.youtube.com/watch?v=GBTu1hk4_VQ
---
Due to internal environment of Windows domains is always too tolerant, and enterprises are more concerned about border defenses than internal security, the penetration behavior based on Windows Active Directory has become more and more popular and aggressive. The emergence of MicrosoftATA allows BlueTeam to perceive and discover most domain penetration activities, however, there are many bypassing techniques for MicrosoftATA recently, and the detection dimension of MicrosoftATA is not comprehensive enough, especially the persistence part. It's a compelling problem whether the Red Team can ensure their behaviors not to be detected after bypassing the detection of MicrosoftATA. In my recent research, the security event log of domain controller details the activity of entities in the domain. Most AD Attacks leave traces in the logs. These logs can be collected and analyzed in real time, helping you quickly detect attacks before an attacker compromises the domain controller. I will detail how to find exceptional behavior from a large number of domain controller security event logs and use a variety of analysis approaches to determine attacks, while taking into account false alarm rate. It's worth mentioning that we don't collect security event log of all computers, only domain controllers. As a result, these ideas are applicable in a large-scale intranet environment, helping Blue Team build its own Advanced Threat Analytics.