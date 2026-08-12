---
date: '{{ .Date }}'
draft: true
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
#
# EDIT THESE
#
author: 'Extra Long Division'
tags: ['']
# description: 'I forgot to fill out the description.'
# URL is based off the filename
canonicalURL: '{{ absURL .Site.Params.articles_path }}{{ .File.ContentBaseName }}/'
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

{{< written-by-a-human >}}

{{< eld-byline >}}

[Why are there footnotes?]({{< relref-jargon-url >}})
