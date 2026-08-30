# Lynx

A text browser for the World Wide Web. First released 1992.
Still maintained. Still used. Version 2.9.3 is in this directory.

About 109,000 lines of C. Larger than Mosaic — thirty years of
maintenance will do that — but the core is the same idea:
fetch a document, parse it, show it to the user.

Without images. Without JavaScript. Without CSS.
Just the text. Just the links.

---

## Why Lynx Matters

Lynx shows you what a web page actually contains.

Load any modern page in Lynx and you see the ratio: how much is
navigation, how much is advertisement, how much is the actual content
you came for. Pages that look clean in Chrome often reveal, in Lynx,
that they are mostly chrome — decoration, menus, sidebars, tracking
pixels, cookie banners. The signal-to-noise ratio becomes visible.

Lynx also matters for accessibility. Screen readers — the software
that reads web pages aloud for blind and low-vision users — traverse
the document the same way Lynx does: in order, as text, following
the structure the HTML defines. A page that works in Lynx works for
screen readers. A page that breaks in Lynx often breaks for people
who depend on screen readers.

The web was designed to be device-independent. Any browser, any
rendering capability. Lynx is the proof that this design survives.

---

## What to Read

**`src/LYMain.c`** (4,578 lines) — the entry point. Command-line
parsing, configuration loading, the startup sequence. Smaller and
clearer than `gui.c` in Mosaic because there is no GUI to build.

**`src/LYMainLoop.c`** (8,216 lines) — the event loop. Keyboard
input, navigation, following links, the mechanics of how you move
through a document with arrow keys. This is the browser's soul:
a loop that reads a keypress and decides what to do.

**`src/HTML.c`** (8,097 lines) — the HTML handler. Compare this
with Mosaic's `libhtmlw/HTML.c`. Line 2938 is the `case HTML_IMG:`
handler — the moment Lynx encounters an image. It doesn't fetch it.
It doesn't display it. It reads the `ALT` attribute, checks whether
the image is part of a link, and moves on. The image is a placeholder
in the text flow. This is the road not taken, right there in the code.

**`src/GridText.c`** (15,075 lines) — the document model. How a
parsed HTML document becomes a grid of characters on a terminal.
The layout engine for a world without pixels.

**`WWW/Library/Implementation/HTTP.c`** — the HTTP client.
Compare with Mosaic's `libwww2/HTTP.c`. Same protocol, same RFC,
different browser. The protocol is public; anyone can implement it;
here is the second implementation.

---

## The Contrast With Mosaic

Both browsers implement RFC 2616 and RFC 1866. Both parse HTML.
Both follow links. Both handle forms.

Mosaic asks: how do we show this to the user?
Lynx asks: what does this document say?

These are not the same question. The web Mosaic built is the web
of images and layout and visual design — the web that became the
platform for advertising, for social media, for video. The web Lynx
preserves is the web of documents and links and text — the web
Berners-Lee designed.

Both webs are real. One became dominant. The other is still running,
still useful, still installed on the machine you are using right now
if you are on Linux.

---

## Running Lynx

```bash
lynx https://example.com
```

Arrow keys navigate. Enter follows a link. Q quits.
G goes to a URL. / searches. H opens help.

Try it on a page you use every day. Notice what's there.
Notice what isn't.
