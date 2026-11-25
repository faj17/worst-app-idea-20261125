# BUILD_LOG — worst-app-idea-20261125

Competition: u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23
("The Worst App Idea Ever Pitched", $2, free entry)
Kit: ~/workspace/makefun/worst-app-idea-20261125/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23-kit/
Gate: /output/entry.txt must be UTF-8, 1–240 chars, not only whitespace.
Transcripts: standard bundle flow (NOT strict transcripts — "strict" appears
0 times in GET /api/competitions/<slug>/requirements).
Deadline: 2026-11-26T16:50:00Z = 23:50 WIB 26 Nov 2026 (kit competition.yaml;
the requirements endpoint's deadlines/how_to_submit fields name a different
slug and an earlier close — treated as a stale template, kit + competition
endpoint agree on 26 Nov 16:50 UTC).

## Candidates drafted (char counts verified with Python len())

1. (192) "DustWatch is a $9.99-a-month app that live-streams the dust settling on your bookshelves in 4K and alerts you the instant a single new particle lands, so serious collectors never miss a speck."
2. (195) "PuddleWatch alerts you the instant a puddle near you evaporates, with a live countdown, a neighbourhood evaporation leaderboard, and premium cloud sync so you never miss a puddle drying up again."
3. (180) "SighTrack is a mindfulness app that records every sigh you make, graphs your disappointment over time, and shares your weekly sigh streak with friends so nobody ever exhales alone."
4. (185) "QueuePal is a premium app that holds your place in lines you are not standing in, with live queue-cam, push alerts when your imaginary spot moves, and a pro tier that queues for queues."
5. (180) "Napkin is a subscription app that photographs every napkin you use, rates its absorbency with AI, and builds a shareable gallery of your finest spills so friends never miss a wipe."

## Pick

Candidate 1, tightened to 218 chars: the "$9.99" price became "$10" so the
text holds exactly one period (one sentence, no decimal-point ambiguity),
and a weekly dust report was added to use the 240 chars better:

"DustWatch is a $10-a-month app that live-streams the dust settling on your bookshelves in 4K, alerts you the instant a single new particle lands, and sends a weekly dust report so serious collectors never miss a speck."

Why it wins the set: a named product with a price (sounds like a real
pitch), a vivid picture (4K livestream of dust), a problem literally nobody
has (missing a speck of dust land), deadpan confidence ("serious
collectors"), and one clean sentence with no second idea. PuddleWatch is
close but "evaporation leaderboard" is a second joke crowding the first;
SighTrack and QueuePal are one-note; Napkin's gallery is a weaker image
than a 4K dust livestream. None of the candidates copies any fixed text or
example from the rules (none quoted in the brief).

## Rubric self-score (0/1 per criterion, judge order)

1. Names a specific app + what it uselessly does, one sentence: 1
2. Uselessness funny via absurd logic / deadpan confidence / mismatch
   (nobody needs dust alerts; "serious collectors"): 1
3. Sounds like a real pitch — product name, price, what it does, who it
   is for: 1
4. Uses 240 chars well — 218 chars, one clean sentence, no padding: 1
5. Vivid, specific picture, not a generic app joke: 1

Total: 5/5. No criterion scored 0.

## Verification

`python3 main.py` run 2026-11-25: /output/entry.txt content equals the line
above, 218 chars, single line, one period, within the 1–240 gate.
Build VERIFIED.
