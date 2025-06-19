---
description: >-
  Here is a collection of official and unofficial syntax highlighters for
  BoxLang
icon: highlighter-line
---

# Syntax Highlighters

## SyntaxHighlighter

BoxLang brush module for [SyntaxHighlighter](https://github.com/syntaxhighlighter/syntaxhighlighter).  Please check out the instructions on how to build your own SyntaxHighligther and add custom brushes.

{% @github-files/github-code-block url="https://github.com/ortus-boxlang/brush-boxlang" %}

### Installation

```bash
npm install brush-boxlang
```

### Example

```javascript
SyntaxHighlighter.brushes.BoxLang = require('brush-boxlang').default;
SyntaxHighlighter.all();
```
