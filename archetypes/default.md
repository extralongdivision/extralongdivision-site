---
date: '{{ (time.AsTime (.Date)).UTC }}'
draft: true
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
---
