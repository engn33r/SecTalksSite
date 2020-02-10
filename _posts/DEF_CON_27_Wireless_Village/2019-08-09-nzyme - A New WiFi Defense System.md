---
type: youtube
yt-video-id: HUX5vA6VGLs
homedisplay: iframe
title: nzyme - A New WiFi Defense System
tags: [DEFCON, DEF CON, DEFCON27, DEF CON 27, wireless]
category: DEF_CON_27
layout: post-classic-sidebar-left
speaker: Lennart Koopmann
conf: DEF CON 27
track: Wireless Village
yr: 2019
vidurl: https://www.youtube.com/watch?v=HUX5vA6VGLs
---
In this talk, I am explaining and releasing v1.0.0 of nzyme after 2 years of work. Nzyme is a new and Open Source WiFi IDS that addresses challenges of wireless security by employing deception techniques, fingerprinting and classic signature-based detection methods. In addition to the IDS part of nzyme, it also parses, enriches and forwards every intercepted management frame to a log management system to allow for long-term WiFi DFIR and even threat hunting. Classic signature-based detection supports alerting on unexpected channels, BSSIDs, SSIDs and crypto options as well as deauthentication frame flooding. Using these techniques can be a good start, but they are so easy to bypass by an attacker that more effort is needed. To take the blue team game to a new level, nzyme allows you to spin up fake networks and alert when an attacker attempts to interact with them. A fingerprinting approach detects common attack platforms like WiFi Pineapples, or ESP8266-based deauthers. The talk includes a real quick introduction to WiFi security with a focus on how signature-based detection is not enough, a live-demo of the web interface and some live detection action. I am explaining the fingerprinting approach in depth, and at the end of the talk, there is a demo of DFIR and threat hunting tasks with the collected data in Graylog.