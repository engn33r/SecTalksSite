---
type: youtube
yt-video-id: FoM3u8G99pc
homedisplay: iframe
title: Can Kubernetes Keep a Secret?
tags: [owasp, appsec, kubernetes]
category: AppSec_Cali_2019
layout: post-classic-sidebar-left
speaker: Omer Levi Hevroni
conf: AppSec Cali 2019
yr: 2019
vidurl: https://www.youtube.com/watch?v=FoM3u8G99pc
---
Description: We’ve all experienced it: you’re working on a task, adding some code, and then you need to store some sensitive configuration value. It could be an API key, client secret or an encryption key ― something that’s highly sensitive and must be kept secret. And this is where things get messy. Usually, secret storage is highly coupled with how the code is deployed, and different platforms have different solutions.

Kubernetes has a promise to simplify this process by using the native secret object, which, as the name implies, can be used to store secrets or sensitive configurations. Unfortunately, Kubernetes secrets are fundamentally broken, and a developer who tries to use them will definitely have some issues.

But no need to worry ― there are solid alternatives for storing secrets securely on Kubernetes platform. One solution is to use Kamus, an open-source, git-ops solution, that created by Soluto, for managing secrets on Kubernetes. Kamus can encrypt a secret so it can be decrypted only by your app on runtime - and not by anyone else.

The first part of this session will cover the challenges faced when using Kubernetes secrets (from a usability and security point of view). The second part will discuss some of the existing solutions (Sealed Secrets, Helm Secrets and others), their pros, and cons, and then feature Kamus: how it works, what problems it solves, how it differs from other solutions, and what threats it can help mitigate (and what threats it can’t).

The talk will cover all that is required to know so you can run Kamus on your own cluster and use it for secret management.  Join me for this session to learn how you can build a Kubernetes cluster than can keep a secret ― for real.

Speakers
Omer Levi Hevroni
DevSecOps Engineer, Soluto
I’ve been coding since 4th grade when my dad taught me BASIC and haven’t looked back since. AppSec/DevSecOps enthusiast, and always curious about integrating more hacking tools into the CI/CD pipeline.

-

Managed by the official OWASP Media Project https://www.owasp.org/index.php/OWASP_Media_Project
