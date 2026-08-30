# WebKit

WebKit is the rendering engine that powers Safari. Google forked it in 2013 to create Blink, which powers Chrome. The lineage: KDE's KHTML → Apple's WebKit → Google's Blink.

The fork is architecturally interesting: two companies took the same codebase and made different bets. Apple optimized for battery life and tight OS integration. Google optimized for JavaScript performance and cross-platform reach.

## Source

```
git clone https://github.com/WebKit/WebKit
```

Large but structured. The important directories:

- `Source/WebCore/` — the rendering engine: HTML parser, CSS engine, layout engine, DOM
- `Source/JavaScriptCore/` — the JavaScript engine (called Nitro or SquirrelFish at various points)
- `Source/WebKit/` — the embedding API that lets browsers use WebCore

## What to read for orientation

`Source/WebCore/html/parser/HTMLDocumentParser.cpp` — how HTML becomes a DOM tree. Follow the token stream from bytes to nodes.

`Source/WebCore/layout/` — the layout engine. How the DOM tree becomes a visual arrangement.

## The Blink fork

When Google forked WebKit to create Blink, they removed 7 build targets and 8.8 million lines of code in the first week. The divergence is now significant: WebKit and Blink are cousins, not twins.

Blink source lives in the Chromium repository (`chromium/src/third_party/blink/`). The Chromium repo is enormous (~30GB). Use Code Search: https://source.chromium.org/
