---
type: youtube
yt-video-id: 28SM5ILpHEE
homedisplay: iframe
title: Easy PAKE Oven
tags: [DEFCON, DEF CON, DEFCON27, DEF CON 27, crypto, privacy]
category: DEF_CON_27
layout: post-classic-sidebar-left
speaker: Steve Thomas
conf: DEF CON 27
track: Crypto and Privacy Village
yr: 2019
vidurl: https://www.youtube.com/watch?v=28SM5ILpHEE
---
Everything you need to know about PAKEs and then some: what, why, which, blind salt, quantum resistance, APIs, HSMs, password KDFs, secret salts, and recovering a lost secret salt.

PAKEs need to be easy to use and hard to misuse, otherwise adoption rates will be low. Take SRP, almost every implementation has functions like "calculateA", "calculateU", etc. To use these libraries you need to know exactly how SRP works. Some programmers might choose to send the server verifier first because it saves a trip. If the library doesn't prevent it, then this breaks SRP and let's anyone make password guesses offline. With a good API a programmer only needs to know they want to use a PAKE and the rest is relaying messages to and from the library until it's done.

BIO
I do stuff... sometimes.