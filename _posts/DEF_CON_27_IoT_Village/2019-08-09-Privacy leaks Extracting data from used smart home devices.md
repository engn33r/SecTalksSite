---
type: youtube
yt-video-id: Iit4SmzQ2Uo
homedisplay: iframe
title: Privacy leaks Extracting data from used smart home devices
tags: [DEFCON, DEF CON, DEFCON27, DEF CON 27, IoT]
category: DEF_CON_27
layout: post-classic-sidebar-left
speaker: Dennis Giese
conf: DEF CON 27
track: IoT Village
yr: 2019
vidurl: https://www.youtube.com/watch?v=Iit4SmzQ2Uo
---
Remember the good old fun sport, where people bought random hard drives from eBay and did forensics on them? Did you know you can do the same thing with used IoT devices too? Most end-users have no idea what kind of information their devices are storing and how to securely clean their devices (if that even is possible). Lets explore together what the risks are and how we can extract that data.
Many IoT devices collect a lot of data and log files. Of course, most of this data is sent to the Cloud. However, often this data is also stored locally on the device and never deleted in the lifetime of those devices, not even on a factory reset (in contrast to Smart Phones nowadays). This might surprise many people, and especially end users might not be aware of that. Due to the design of IoT devices, there is usually no real way, like for notebooks or PCs, for end users to clean the devices before they sell them on eBay or discard them. The devices may hold sensitive information like Wi-Fi credentials, nearby access points, cloud communication log files, maps, or audio samples.
In this talk I will show some examples of interesting IoT devices from various vendors and how to extract the corresponding information. We will use software methods (rooting) and hardware methods (flash dumping). Using this information, I will show how I am able to find the original owner of the device. Also I discuss various challenges and tricks of the methods, and how to prevent this kind of data leakage for yourself.

Bios:
Dennis is a grad student at Northeastern University and TU Darmstadt. He was a member of one European ISP's CERT for several years. While being interested in physical security and lockpicking, he enjoys applied research and reverse engineering malware and all kinds of smart devices. His latest area of research is reverse engineering of various IoT ecosystems. He has presented at the Chaos Communication Congress, REcon BRX and DC 26