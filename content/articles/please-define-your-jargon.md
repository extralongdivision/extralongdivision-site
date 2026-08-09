---
date: '2026-07-14T13:52:01-07:00'
draft: false
title: 'Please Define Your Jargon'
#
# EDIT THESE TODO 
#
author: 'Extra Long Division'
tags: ['opinion', 'techincal-writing']
# description: 'An argument to define every term used.'
# URL is based off the filename
canonicalURL: 'https://extralongdivision.codeberg.org/articles/please-define-your-jargon/'
# author: ["Me", "You"] # multiple authors

#
# Optional
#
showToc: false
TocOpen: false
hidemeta: false
comments: false
disableHLJS: false # to disable highlightjs
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: false
ShowRssButtonInSectionTermList: true
UseHugoToc: false
# cover:
#    image: "<image path/url>" # image path/url
#    alt: "<alt text>" # alt text
#    caption: "<text>" # display caption under cover
#    relative: false # when using page bundles set this to true
#    hidden: true # only hide on current single page
# editPost:
#    URL: "https://github.com/<path_to_repo>/content"
#    Text: "Suggest Changes" # edit text
#    appendFilePath: true # to append file path to Edit link
---

## Split.

If you're a dancer, you probably thought of someone, hips to the ground, with their legs parallel to each other. If you're a runner, you might have thought of your pace at each mile in a marathon. If you're a bowler, you might have thought of the dreaded 7-10 split.

Same word. Different meanings.

Language is like that. Its imprecision can leave things ambiguous. Artists can use this to great effect in novels, poems, plays, etc.

## Technical Writing Cannot be Ambiuous

This is rarely intentional, but ambiguity manifests when we assume jargon we use everyday is obvious. Engineers are notorious for this. I.e, [this post about making a chrome extension](https://dev.to/projekta2/i-built-a-chrome-extension-used-daily-for-pr-review-5-decisions-id-make-differently-4o64) uses the term "MV3"[^1] four times but never defines it.

*The meaning of MV3 is obvious in a post about chrome extensions.*

*You* may know exactly what MV3 means, but an article titled *"5 mistakes I made building an AI chrome extension"* will attract beginners with little domain space knowledge. If everyone assumes the reader knows what MV3 means, how will a novice ever learn the definition?

*Just Google it*.

Let me remind you that search engines personalize your results. Searching "MV3" on a seasoned developer's machine may return docs on migrating a service worker. Someone else may get the [2004 St. Louis Cardinals.](https://www.msn.com/en-us/sports/baseball/father-mcgivney-baseball-s-mv3-carved-the-path/ar-AA1JWQH4)

*Context makes MV3's meaning clear.*

The author controls the article's context, but they do not control the readers' context. When I wrote "split" as the first word of this post, I had no idea how you would perceive it. I do not know if you are a dancer or a bowler or a runner. I have no idea what experiences you have when you read my writing.

I can, however, reduce any ambiguity by defining all the jargon I use. There's a way to do this without being cumbersome.

## Footnotes

Write your post as you normally would, then, for any acronym, add a footnote. Your writing tools likely have built in support.

Seasoned web developers didn't need to read the footnote to know what MV3 meant. Everyone else has already scrolled down, read the definition, and continued reading. Footnotes are friction-less to knowledge area experts and immensely helpful to everyone else.

Do us all a favor [—]({{< relref-emdash-url >}}) please define your jargon.

{{< eld-byline >}}

[^1]: Google Manifest Version 3