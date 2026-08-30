# Mastodon

Open source federated social network. Ruby on Rails backend,
React frontend. First released 2016 by Eugen Rochko.

This directory contains a sparse checkout of the core:
models, services, workers, and the database schema.
The full codebase is at github.com/mastodon/mastodon.

---

## Why Mastodon Is Here

Mastodon does what Twitter does. You post. People follow you.
You see a feed of posts from people you follow. You can reply,
boost (retweet), favourite (like).

The difference: you can read every line of it.

This is the counterexample. Facebook's feed algorithm is a trade
secret. Twitter's fanout logic was described in engineering blog
posts but never released. Mastodon's is in `app/services/`. Read it.

Mastodon is also federated — there is no single Mastodon server.
Anyone can run an instance. Instances talk to each other using
ActivityPub, an open W3C protocol. The same logic that makes
HTTP readable (it's a published standard) makes the social
network readable: the protocol is public, anyone can implement it,
here is one implementation.

---

## The Data Structure

**`app/models/status.rb`** — a post. Read the schema comment at
the top of the file. The database table is called `statuses`. Key fields:

- `text` — the content
- `account_id` — who wrote it
- `visibility` — public, unlisted, private, direct
- `in_reply_to_id` — the post this replies to, if any
- `reblog_of_id` — the post this boosts, if any
- `uri` — the unique identifier across the entire federation

A social network is this table, plus the `follows` table that
connects accounts to each other. Everything else is built on top.

**`app/models/account.rb`** (600 lines) — a user. Local accounts
(people on this server) and remote accounts (people on other servers)
are the same model. The `uri` field is what distinguishes them:
a local account has a URI on this server; a remote account has a URI
on theirs. The social graph spans servers.

---

## The Feed Algorithm

**`app/services/fan_out_on_write_service.rb`** (182 lines) —
this is the algorithm that decides whose feed a post appears in.

When you post, `FanOutOnWriteService` runs. It pushes your post
into the home feed of every one of your followers. This is called
*fanout on write*: at write time, not read time, the work is done.

The method is readable:

```ruby
fan_out_to_local_recipients!
fan_out_to_public_recipients! if broadcastable?
fan_out_to_public_streams!    if broadcastable?
```

Three calls. Local followers get it. Public streams (the federated
timeline, the local timeline) get it if it's public. That's the
feed algorithm. No engagement weighting. No watch-time optimization.
No ranking by predicted click-through rate. Chronological order,
delivered to followers.

Compare this with what Twitter's algorithm does — which you cannot
read, because it is not public. The contrast is the lesson.

(Twitter open-sourced a portion of its recommendation algorithm in
2023 under public pressure. The release was partial, contested, and
did not include the full ranking logic. The Mastodon algorithm has
always been fully readable because it was never a secret.)

**`app/services/post_status_service.rb`** (299 lines) — what happens
when you hit post. Validation, mention parsing, hashtag extraction,
media attachment, notification triggering. One post, end to end,
in one file.

---

## The Workers

**`app/workers/`** — background jobs. The social network does most
of its work asynchronously. When you follow someone on another server,
a worker sends an ActivityPub `Follow` activity to their server.
When someone boosts your post, a worker delivers the notification.

This is the federation: HTTP requests between servers, carrying
JSON payloads that describe social actions. You can read the
ActivityPub spec (a W3C standard, public) and then read the workers
and watch one implement the other. Same relationship as HTTP.c and RFC 2616.

---

## What's Not Here

The frontend (React/TypeScript) is not in this checkout.
The full API layer is not here.
To browse everything: searchfox.org doesn't index it, but
github.com/mastodon/mastodon has a web code browser.

The database schema — `db/schema.rb` — is in this checkout.
It is the most readable single document in the codebase:
every table, every column, every relationship, in plain text.
Read it before reading any model file.

---

## The Argument

Mastodon exists because the people who built it believed the
social network should be readable — by users, by regulators,
by researchers, by anyone. The protocol is public. The code
is public. The data model is public. If you don't like how
it works, you can read why it works that way, and you can run
your own instance that works differently.

This is not how Facebook works. It is not how Twitter works.
It is how the web was supposed to work.
