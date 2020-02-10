---
type: youtube
yt-video-id: uhbKB_5u6jE
homedisplay: iframe
title: MITM mixed mode butterfly key privacy attack
tags: [DEFCON, DEF CON, DEFCON27, DEF CON 27, crypto, privacy]
category: DEF_CON_27
layout: post-classic-sidebar-left
speaker: Ben Brecht
conf: DEF CON 27
track: Crypto and Privacy Village
yr: 2019
vidurl: https://www.youtube.com/watch?v=uhbKB_5u6jE
---
Butterfly key expansion (BKE) is a somewhat novel concept to create almost indefinitely new matching public and private keys independently of each other based on a seed (or caterpillar) key pair and a shared expansion function. Although this concept was invented for credential provisioning to Vehicle-to-Everything (V2X) communication devices (DOI:10.1109/VNC.2013.6737583) these characteristics makes it interesting for all low bandwidth, low computational power, low secure storage devices. The BKE protocol allows for efficient generation of massive amounts of certificates with no single PKI component knowing which certificate belongs to which device - as required in V2X communication. The approach has since been utilized and implemented and is about to be standardized in IEEE 1609.2.1. One optimization of the butterfly key expansion protocol is called "unified butterfly key expansion" (UBK) (https://eprint.iacr.org/2018/089.pdf), which is about to be included in IEEE 1609.2.1 as well. While learning about this protocol and being involved in the deployment of PKI systems implementing it, I discovered an issue with a scenario where some CAs would implement the "traditional" BKE mechanism and other CAs the UBK approach - which is happening, e.g., in the US, where BKE  is already in production and UBK will be soon: the RA in this case could pretend to implement UBK, where in fact it works with a BKE CA. This way the RA could break one of the central privacy characteristics of the butterfly key expansion protocol: no single PKI component is able to know which public keys/certificates belong to the same device.

BIO
Ben started his career in the automotive industry in 2010. Since 2013, he has been a Program Manager responsible for the global rollout of connected car technology. He was assigned to work in the U.S. to work on Vehicle-to-Everything (V2X) security in 2015. He is currently the Vice Chair of the 5GAA WG7 "security & privacy" and involved in security topics for V2X communication.