---
type: youtube
yt-video-id: kDlA3hVB9Os
homedisplay: iframe
title: HACK DMI PWNING HDMI FOR FUN AND PROFIT
tags: [DEFCON, DEF CON, DEFCON27, DEF CON 27, IoT]
category: DEF_CON_27
layout: post-classic-sidebar-left
speaker: Hyejin Jeong
conf: DEF CON 27
track: IoT Village
yr: 2019
vidurl: https://www.youtube.com/watch?v=kDlA3hVB9Os
---
HDMI is used by many display devices as an interface for transmitting high-definition video and audio data. The HDMI usage rate is expected to increase further as many global IT companies such as Samsung, Google, and Apple are joining the HDMI Forum. HDMI is provided for transmitting digital television audiovisual signals from HDMI source device to the HDMI sink device. It delivers not only the audiovisual signal but also controls, status and data information in both directions. Although there is a weakness that HDMI requires a direct line connection, considering the HDMI usage rate of AV devices, the impact of HDMI vulnerability is huge.
So we will explain the CEC and DDC protocols that transmit bidirectional data in detail and explain the reason why they are considered as attack vectors. Simply put, CEC protocol is used to control devices connected to HDMI. The DDC protocol is used by the HDMI source device to obtain information about the status and function of the HDMI sink device. In particular, we will talk about the structure of each protocol's messages and how we sent them. After that, we will introduce the fuzzer we made and release the source code of it. There are CEC fuzzer with USB-CEC adapter, DDC fuzzer with our own test cable, and DDC fuzzer of Ubuntu graphics driver. And I will present about the vulnerabilities which we found in the set-top box as a result of our fuzzer, and the crash we got from Windows. If we find something else, we'll disclose it also."

Bio:
Hyejin Jeong is a mentee of BoB 7th vulnerability assessment track and major in software at Soongsil University. She is interested in system and IoT hacking. Currently, she enjoys studying various attack vectors.

Jeonghoon Shin(@singi21a), a security researcher in Theori, member of SeoulPlusBadAss Team. He is interested on Browser N-Day exploits and vulnerabilities.
He discovered over 10 major browser bugs:
- Google Chrome (CVE-2017-5052, CVE-2016-5129)
- Apple Safari( CVE-2018-4088, CVE-2017-7157, CVE-2017-13856, CVE-2017-2464, CVE-2016-1857, CVE-2016-7632)
- MS ChakraCore (CVE-2018-0858)
- MS IE (CVE-2015-2411)
- Apple OS X Bluetooth (CVE-2016-1735)
- Apple OS X Intel Graph Driver (CVE-2016-7106)
- Apple OS X Intel Graph Driver (CVE-2015-7076)
He has spoken at conferences such as zer0con, PoC, and HITB about ""Fuzzing Javascript Engines"". He is also a reviewer of HITB and KIMCHICON.