# NCSA Mosaic

Marc Andreessen and Eric Bina. University of Illinois, 1993.
The browser that made the web visual.

Source is in `src/`. About 95,000 lines of C across five libraries
and the main application. Small enough to read. Old enough to be clear.

---

## The Libraries

```
libhtmlw/   — HTML parser and renderer
libwww2/    — HTTP, FTP, Gopher, MIME: the network layer
libXmx/     — X Window System abstraction
libnet/     — lower-level networking
src/        — the application: GUI, image handling, main loop
```

The division is clean. `libhtmlw` knows about HTML. `libwww2` knows
about the network. `src/` connects them to a window on your screen.

---

## What to Read First

**`libwww2/HTTP.c`** (1,070 lines) — the entire HTTP client.
One file. Opens a socket, writes a request, reads the response.
This is what happens when you type a URL and press enter.
The web is this file, running on a server somewhere that sends back text.

**`libhtmlw/HTMLparse.c`** — the tag recognizer.
Line 1378 is where `<IMG>` becomes a real thing:

```c
else if (caseless_equal(str, MT_IMAGE))
{
    type = M_IMAGE;
}
```

One comparison. One assignment. The image tag enters the parse tree.
Everything that followed — the visual web, the GIF economy, the JPEG,
the banner ad, the meme — is downstream of this.

**`libhtmlw/HTMLformat.c`**, line 2787 — the image placed inline:

```c
tptr = ParseMarkTag(mptr->start, MT_IMAGE, "SRC");
```

This line reads the `SRC` attribute. Line 2827 calls `SetElement` to
place the image in the document flow, beside the text, not in a
separate window. This is the decision Tim Berners-Lee objected to.
This is the line that changed what the web looks like.

**`src/mo-www.c`** (1,776 lines) — the glue layer. Where a URL
becomes an HTTP request becomes parsed HTML becomes something
the GUI can display. Follow one request through this file and
you have followed a URL from start to screen.

**`src/img.c`** (948 lines) — image decoding and display.
GIF, JPEG, PNG: the formats that made the visual web possible,
all handled here.

---

## A Note on the Code

This is 1993 C. No templates, no objects, no memory management beyond
`malloc` and `free`. The functions are long. The variable names are
short. The comments are sparse.

Read it the way you read an old building: the structure is visible
because there is nothing hiding it. The HTML parser is a switch
statement and a loop. The HTTP client is a socket and a buffer.
The whole browser is closer to 100,000 lines than to a million.

Modern browsers are tens of millions of lines. The distance between
Mosaic and Chrome is the distance between a hand-drawn map and a
satellite image. Both show you the same territory. Only one shows
you how the map is made.

---

## The Context

Mosaic was not the first web browser. Berners-Lee's original browser
ran on NeXT workstations. Mosaic was the first to run on multiple
platforms and display images inline.

The `<IMG>` tag was proposed by Andreessen on the www-talk mailing
list in February 1993. Berners-Lee's response suggested alternatives.
The proposal was implemented before the discussion concluded.
That is how the visual web happened: a decision made faster than
the conversation about it.

The CHANGES file in the root of this repo is worth reading.
It is a record of the browser being invented in real time.
