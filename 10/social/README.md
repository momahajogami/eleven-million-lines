# Social — Infrastructure Papers and Reading Notes

The social networks did not publish their source. They published their papers.

This directory holds reading notes on the infrastructure papers from the social web era: Facebook, Twitter, and the engineering problems they solved (or failed to solve) at scale.

---

## Facebook

**Haystack (2010)** — "Finding a needle in Haystack: Facebook's photo storage." The object store Facebook built when MySQL + NFS could no longer handle photo reads. By 2009, Facebook was storing 260 billion photos. Haystack eliminated the metadata bottleneck by keeping all object metadata in memory.

**TAO (2013)** — "TAO: Facebook's Distributed Data Store for the Social Graph." The graph database that replaced MySQL for social graph queries. The social graph is read-heavy; TAO is optimized for reads. Edges (friendships, likes, tags) are the primary data structure.

**Unicorn (2013)** — "Unicorn: A System for Searching the Social Graph." How Facebook searches the graph — not by document, but by entity and relationship.

The papers are public. Search for them by title on USENIX or ACM Digital Library.

---

## Twitter

Twitter's scaling story is public and dramatic. The architecture changed completely between 2007 and 2012.

**Early stack (2006-2008):** Ruby on Rails, MySQL, a simple fanout model. Every tweet written to every follower's timeline on write. Works fine at small scale.

**The fail whale era (2008-2009):** The fanout model collapses under load. Tweets from high-follower accounts triggered millions of writes. The "fail whale" (an illustration of Twitter's error page) becomes a cultural meme. The engineering blog posts from this period are candid and worth reading.

**The rewrite:** Move to Scala/JVM for the timeline service. Introduce FlockDB (a graph database for the follow graph), Snowflake (distributed unique ID generation), Finagle (an RPC framework, later open-sourced). Each of these is a response to a specific failure mode.

**Snowflake** (2010) — distributed ID generation without a central coordinator. IDs are 64-bit integers: 41 bits of timestamp, 10 bits of machine ID, 12 bits of sequence number. Simple, elegant, still used.

Twitter engineering blog posts (2007-2012) are the primary text. Search the Wayback Machine for blog.twitter.com.

---

## The Papers as Literature

The infrastructure papers of the social web era are a genre. They share conventions: the problem statement, the prior art, the design decisions, the evaluation. They are written for engineers by engineers and published at USENIX, OSDI, SOSP.

Reading them alongside the business history creates a double vision: the engineering problem (how do we store a billion photos?) and the social problem (what does it mean that a billion photos exist?) in parallel.

That double vision is what this unit is for.
