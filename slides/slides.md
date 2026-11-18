---
marp: true
theme: default
size: 16:9
paginate: true
title: From Records to Royalties
description: A four-hour tracklist hackathon at GEMA
lang: en
style: |
  @font-face { font-family: TheSansLocal; src: local("TheSansOfficeLF"); font-weight: 400; }
  @font-face { font-family: TheSansLocal; src: local("TheSansOfficeLF-Bold"); font-weight: 700; }
  :root { --ink: #3F3F3F; --yellow: #FFCB05; --petrol: #007E7F; --violet: #614E8B; --orange: #F15A22; }
  section { font-family: TheSansLocal, "TheSansOfficeLF", Arial, sans-serif; background: #FAFAF7; color: var(--ink); padding: 54px 66px 52px; justify-content: flex-start; place-content: start start; font-size: 26px; line-height: 1.2; }
  section::after { font-size: 15px; color: #777; bottom: 22px; right: 38px; }
  section::before { content: "TRACKLIST HACKATHON"; position: absolute; left: 66px; bottom: 23px; font-size: 12px; letter-spacing: 2px; color: #777; }
  h1, h2, h3, p { margin: 0; }
  h1 { font-size: 64px; line-height: 1.02; letter-spacing: -1.6px; color: inherit; font-weight: 700; }
  h2 { font-size: 52px; line-height: 1.06; letter-spacing: -1px; color: inherit; font-weight: 700; }
  .eyebrow { font-size: 17px; letter-spacing: 2.2px; text-transform: uppercase; margin-bottom: 18px; font-weight: 700; }
  .subtitle { font-size: 26px; line-height: 1.35; }
  .yellow { color: var(--yellow); }
  .muted { color: #767676; }
  .kicker { color: var(--petrol); }
  section.dark { background: var(--ink); color: #FFF; }
  section.dark::before, section.dark::after { color: #C6C6C0; }
  .hero-copy { position: relative; z-index: 2; width: 660px; margin-top: 55px; }
  .hero-copy h1 { font-size: 78px; line-height: 1.02; }
  .hero-copy .subtitle { margin-top: 34px; max-width: 480px; }
  .record { position: absolute; width: 555px; height: 555px; right: -91px; top: 95px; transform: rotate(-13deg); }
  section.hero .eyebrow { color: var(--yellow); }
  .brand-logo { position: absolute; width: 48px; height: auto; top: 36px; right: 42px; }
  .flow { margin-top: 32px; width: 1148px; height: 418px; }
  svg text { font-family: TheSansLocal, "TheSansOfficeLF", Arial, sans-serif; }
  section.problem h2 { max-width: 880px; }
  .problem-record { position: absolute; width: 400px; height: 400px; left: -100px; top: 260px; transform: rotate(-13deg); }
  .metadata { position: absolute; left: 370px; top: 262px; width: 345px; border-left: 5px solid var(--petrol); padding: 6px 0 8px 24px; }
  .metadata .tiny { font-size: 16px; letter-spacing: 2px; margin-bottom: 18px; }
  .metadata p { font-size: 28px; margin-bottom: 14px; }
  .barcode { margin-top: 22px; width: 220px; height: 52px; background: repeating-linear-gradient(90deg,#3F3F3F 0 2px,transparent 2px 5px,#3F3F3F 5px 6px,transparent 6px 10px,#3F3F3F 10px 14px,transparent 14px 18px); }
  .missing { position: absolute; left: 806px; top: 253px; width: 340px; min-height: 257px; background: #FFF; padding: 30px; box-shadow: 12px 12px 0 #E8E8E0; }
  .missing h3 { font-size: 21px; letter-spacing: 1px; }
  .trackline { margin-top: 20px; height: 20px; border-bottom: 2px dashed #B5B5AD; font-size: 16px; color: #8B8B85; }
  .gap-label { position: absolute; left: 370px; top: 573px; font-size: 27px; font-weight: 700; color: var(--violet); }
  section.challenge h2 { max-width: 1060px; }
  .approach-flow { display: grid; grid-template-columns: 250px 72px 430px 72px 310px; align-items: center; margin-top: 64px; }
  .endpoint { font-size: 28px; line-height: 1.3; }
  .endpoint small { display: block; font-size: 18px; color: #C6C6C0; margin-top: 14px; }
  .arrow { color: var(--yellow); font-size: 50px; text-align: center; }
  .your-approach { background: var(--yellow); color: var(--ink); padding: 40px 14px; text-align: center; font-size: 37px; font-weight: 700; line-height: 1.1; }
  .principles { display: flex; gap: 48px; margin-top: 55px; font-size: 22px; }
  .principles span { border-top: 3px solid #888; padding-top: 14px; flex: 1; }
  .kit-layout { display: grid; grid-template-columns: 420px 1fr; gap: 66px; margin-top: 45px; }
  .big-number { font-size: 144px; font-weight: 700; letter-spacing: -7px; line-height: 1; color: var(--petrol); }
  .data-desc { font-size: 29px; margin-top: 12px; }
  .tool-row { border-top: 2px solid #D6D6CF; padding: 23px 0; }
  .tool-row h3 { font-size: 31px; }
  .tool-row p { font-size: 22px; color: #70706B; margin-top: 8px; }
  .tool-row:first-child { border-color: var(--petrol); }
  .kit-choice { position: absolute; left: 66px; right: 66px; bottom: 87px; display: flex; gap: 24px; align-items: center; }
  .kit-choice strong { background: var(--yellow); padding: 13px 21px; font-size: 23px; }
  .kit-choice span { font-size: 24px; }
  .timeline { position: relative; margin-top: 45px; height: 280px; }
  .timeline-bar { position: absolute; left: 0; top: 98px; display: grid; grid-template-columns: 20fr 20fr 130fr 20fr 40fr 10fr; width: 1148px; height: 68px; gap: 3px; }
  .timeline-bar div { background: #666; }
  .timeline-bar div:nth-child(2) { background: var(--violet); }
  .timeline-bar div:nth-child(3) { background: var(--yellow); }
  .timeline-bar div:nth-child(4) { background: #999; }
  .timeline-bar div:nth-child(5) { background: var(--petrol); }
  .timeline-bar div:nth-child(6) { background: var(--orange); }
  .phase { position: absolute; font-size: 21px; line-height: 1.2; }
  .phase small { display: block; font-size: 17px; color: #C6C6C0; margin-top: 8px; }
  .p1 { left:0; top: 9px; } .p2 { left:100px; top: 185px; } .p3 { left:240px; top: 9px; } .p4 { left:804px; top:185px; } .p5 { left:913px; top:9px; } .p6 { right:0; top:185px; text-align:right; }
  .phase.big { font-size: 33px; color: var(--yellow); }
  .time-mark { position: absolute; top: 174px; font-size: 13px; color: #CCC; }
  .t1 { left: 0; } .t3 { left: 193px; } .t5 { left: 908px; }
  .pitch-callout { margin-top: 8px; display: flex; align-items: baseline; gap: 22px; }
  .pitch-callout strong { font-size: 59px; color: var(--yellow); }
  .pitch-callout p { font-size: 26px; }
  .pitch-callout small { font-size: 18px; color: #C6C6C0; display: block; margin-top: 10px; }
  section.final { background: var(--yellow); }
  section.final h2 { font-size: 65px; max-width: 960px; }
  section.final .eyebrow { margin-bottom: 24px; }
  .pitch-meta { position: absolute; right: 66px; top: 60px; text-align: right; font-size: 19px; }
  .pitch-meta strong { display: block; font-size: 53px; line-height: 1; }
  .questions { display: grid; grid-template-columns: 1fr 1fr; gap: 27px 62px; margin-top: 52px; }
  .question { font-size: 28px; padding-top: 17px; border-top: 2px solid #A78500; }
  .question span { font-size: 17px; display: block; margin-top: 8px; }
  .winning { margin-top: 35px; font-size: 27px; font-weight: 700; }
---
<!-- _class: dark hero -->
<div class="eyebrow">From records to royalties</div>
<div class="hero-copy"><h1>Music creates value.<br><span class="yellow">Who gets paid?</span></h1><p class="subtitle">A four-hour tracklist hackathon.</p></div>
<div class="record"><svg viewBox="0 0 530 530" xmlns="http://www.w3.org/2000/svg" aria-label="Vinyl record with yellow centre label"><circle cx="265" cy="265" r="258" fill="#242424"/><g fill="none" stroke="#484848" stroke-width="1.5"><circle cx="265" cy="265" r="240"/><circle cx="265" cy="265" r="227"/><circle cx="265" cy="265" r="214"/><circle cx="265" cy="265" r="201"/><circle cx="265" cy="265" r="188"/><circle cx="265" cy="265" r="175"/><circle cx="265" cy="265" r="162"/><circle cx="265" cy="265" r="149"/><circle cx="265" cy="265" r="136"/></g><circle cx="265" cy="265" r="115" fill="#FFCB05"/><text x="265" y="236" text-anchor="middle" font-size="17" font-weight="700" letter-spacing="3" fill="#3F3F3F">SIDE A</text><text x="265" y="278" text-anchor="middle" font-size="26" font-weight="700" fill="#3F3F3F">THE RECORD</text><text x="265" y="316" text-anchor="middle" font-size="16" fill="#3F3F3F">What’s on it?</text><circle cx="265" cy="265" r="6" fill="#242424"/></svg></div>
<img class="brand-logo" src="data:image/png;base64,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M2fOtFXij1CB8efly5cbGmoZhlCBGRjkAiMwg0xhBGaQKYzADDKFEZhBpkhFYLW1taK0tFQ8//zzomfPnmL//fcXW265pVhnnXXEuuuuK3bYYQfRrVs3cffdd4uff/5ZzObkCdcWTPy/X79+Ypdddmnyewcff/yxuPDCC1XeWfHyyy8XEz178L/++uvaa3W8+OKLxfTp0+2UyYBL6KGHHtLmr+Orr76qra+ouPbaa8Xqq68u/sWJdRkhJ4EtWbJEvPnmm+LII48Um2yyiVhppZUUEdWJJ54orr/+etG/f3/18g4//HCx9tpriw022ED8/ve/F+ecc4547LHHxA8//CDeeecdJcLtt99eW2E//vijuPrqq8Vuu+0m2rVr13gfP6688spK4HvuuafYfffdxdZbby3WWGONwLSbbbaZQPxuIOw///nPKo8OHTpo0zlcZZVVxNNPP22nTIYxY8aoOtDl77B9+/bqmtNPP118yJYJCQVWX18vtthiC5XnAQccIOoSnhsZhkQCIwmt0Lnnnqsq1nl4voYLLrhAtWg6VFZWirPPPlu1bE4aN/0E5mDhwoWiT58+SkC69JBWcOTIkXaKX0HaIUOGqJZyr732UmJ3p9MJzAHPW15eLtZbb70mabw86aSTxKIctnZCoO761PHmm29WLV2uePzxxxvzXH/99cV/2UQmA8QWGJd/++23Yp999mny4FTMPffco76MIJCelsGbHoYJDODc44vzpnV47LHHqnsEYfHixeKzzz4Te++9d2O6IIE5uPLKK5vcy8uOHTuKCveWTzHAcx144IHafB2utdZaYpZ7M7yEmD9/vmrdnXxpFa+77jr7r+kitsCmTp0qOnfu3OTB4V84wDNGVjzk7373uyZ5RBEY+Otf/9oknZt0zVFRU1MjttpqK5UuisBeeeWVZvfz8rLLLrOvjodBgwapFx308ey333721bnh888/b9aC77jjjom72yDEEhhf57777tukYHCjjTYS33zzjX1VdIwdO1bZVU4+UQV2ySWXNLm/m3EEBugqVltttUgCw+jnHgxYMAe894bYn1Ni7ktPt3rooYcquxF71M9W7Nq1q50iOXjdV1xxRbN78DMfUNqILLB58+aJ4447rkmhHB522GGJjETExCDByaclBDZu3Djxm9/8JpbAbr31VnHUUUc1u7fDe++9104RDYMH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" alt="GEMA">

<!--
Open with the music, then the people behind it. GEMA represents composers, lyricists and music publishers and administers rights on their behalf. Keep this high-level: today is about recovering release tracklists, one small but useful part of a much larger process.
Source: GEMA, “What is GEMA?” https://www.gema.de/en/w/help/gema/organisation/questions-and-answers/what-is-gema
-->

---

<div class="eyebrow kicker">The bigger picture</div>
<h2>Turning music use into royalties.</h2>
<svg class="flow" viewBox="0 0 1148 418" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Usage metadata from streaming, radio and television, video on demand, live setlists and physical releases enters GEMA processing. Licence revenue enters separately. Royalties flow to composers, lyricists and publishers.">
<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#007E7F"/></marker><marker id="b" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#F15A22"/></marker></defs>
<text x="0" y="25" fill="#007E7F" font-size="17" font-weight="700" letter-spacing="2">MUSIC USE</text>
<g fill="#3F3F3F" font-size="25"><text x="0" y="77">Streaming</text><text x="0" y="123">Radio &amp; TV</text><text x="0" y="169">Video on demand</text><text x="0" y="215">Live / setlists</text><text x="0" y="261">Physical releases</text></g>
<path d="M256,155 H354" fill="none" stroke="#007E7F" stroke-width="4" marker-end="url(#a)"/><text x="258" y="116" fill="#007E7F" font-size="18">Usage</text><text x="258" y="139" fill="#007E7F" font-size="18">metadata</text>
<rect x="378" y="15" width="374" height="287" rx="3" fill="#007E7F"/><text x="408" y="70" font-size="37" font-weight="700" fill="white">GEMA</text><path d="M408,94 H722" stroke="#71BABB" stroke-width="1"/>
<g font-size="27" fill="white"><text x="408" y="142">Which music?</text><text x="408" y="194">Who gets paid?</text><text x="408" y="246">How much?</text></g>
<path d="M769,155 H866" fill="none" stroke="#007E7F" stroke-width="4" marker-end="url(#a)"/><text x="774" y="131" fill="#007E7F" font-size="18">Royalties</text>
<g font-size="27" fill="#3F3F3F"><text x="893" y="118">Composers</text><text x="893" y="164">Lyricists</text><text x="893" y="210">Publishers</text></g>
<rect x="378" y="351" width="374" height="48" fill="#FBE5D8"/><text x="565" y="383" text-anchor="middle" font-size="23" fill="#923500">Licence revenue</text><path d="M565,345 V314" stroke="#F15A22" stroke-width="4" fill="none" marker-end="url(#b)"/>
</svg>

<!--
This is a deliberately simplified business view, not a complete payout architecture. GEMA licenses music use and distributes royalties to the creators and publishers it represents. Usage information helps identify the works used and support allocation. Revenue is a distinct input; the arrow does not mean metadata itself creates money. The five usage categories are examples, not a complete inventory. This slide is about usage and release metadata, not raw-audio recognition. Physical-release tracklists support identifying the music on a product; recovering them does not itself identify every rights holder or calculate a payment.
Sources: GEMA, “What is GEMA?” https://www.gema.de/en/w/help/gema/organisation/questions-and-answers/what-is-gema ; GEMA, “What are royalties?” https://www.gema.de/en/w/help/creators/royaltiespay-out/royalties/what-are-royalties
-->

---

<!-- _class: problem -->
<div class="eyebrow kicker">One missing piece</div>
<h2>We know the record.<br>What’s on it?</h2>
<div class="problem-record"><svg viewBox="0 0 530 530" xmlns="http://www.w3.org/2000/svg" aria-label="Vinyl record with yellow centre label"><circle cx="265" cy="265" r="258" fill="#242424"/><g fill="none" stroke="#484848" stroke-width="1.5"><circle cx="265" cy="265" r="240"/><circle cx="265" cy="265" r="227"/><circle cx="265" cy="265" r="214"/><circle cx="265" cy="265" r="201"/><circle cx="265" cy="265" r="188"/><circle cx="265" cy="265" r="175"/><circle cx="265" cy="265" r="162"/><circle cx="265" cy="265" r="149"/><circle cx="265" cy="265" r="136"/></g><circle cx="265" cy="265" r="115" fill="#FFCB05"/><text x="265" y="236" text-anchor="middle" font-size="17" font-weight="700" letter-spacing="3" fill="#3F3F3F">SIDE A</text><text x="265" y="278" text-anchor="middle" font-size="26" font-weight="700" fill="#3F3F3F">THE RECORD</text><text x="265" y="316" text-anchor="middle" font-size="16" fill="#3F3F3F">What’s on it?</text><circle cx="265" cy="265" r="6" fill="#242424"/></svg></div>
<div class="metadata"><div class="tiny">RELEASE INFORMATION</div><p>Title ✓</p><p>Artist ✓</p><p>Barcode ✓</p><div class="barcode" aria-hidden="true"></div></div>
<div class="missing"><h3>TRACKLIST ?</h3><div class="trackline">01</div><div class="trackline">02</div><div class="trackline">03</div><div class="trackline">04</div></div>
<p class="gap-label">Missing tracks → a gap in the allocation chain.</p>

<!--
We have release information, but some tracklists are missing. The record illustration and checkmarks are schematic, not a claim that every dataset field is populated. An album title, artist or barcode may identify a product, but we still need the songs on the correct edition. Bonus tracks, regional editions and reissues can matter. Without that information, one of the links needed for subsequent allocation is missing. Tracklist recovery is the workshop scope; rights-holder identification and payment calculation are not.
-->

---

<!-- _class: dark challenge -->
<div class="eyebrow yellow">Your challenge</div>
<h2>Build a way to find out.<br>Automatically.</h2>
<div class="approach-flow"><div class="endpoint">Release information<small>Title · artist · barcode</small></div><div class="arrow">→</div><div class="your-approach">YOUR<br>APPROACH</div><div class="arrow">→</div><div class="endpoint">Tracklist + sources<small>The correct edition.<br>In the right order.</small></div></div>
<div class="principles"><span>Make it repeatable.</span><span>Show your working.</span><span>Explain the limits.</span></div>

<!--
The method is yours to choose: catalog APIs, automated web search, AI, scripts, no-code tools, or combinations. Start with five varied records, then test one fresh input. Target the correct edition and ordered tracks, including durations where available and source links. Manual checks are useful for evaluation; manually gathering all tracklists is not the solution. Build a runnable automated prototype using code or no-code tools. Manually entering release information or pressing Run is fine; finding the tracklist should be automated. You may copy the first five inputs from CSV; automating CSV import is optional. If you get stuck, show the work, diagnose the failure and explain what remains. Clearly distinguish what you tested from what you propose.
-->

---

<div class="eyebrow kicker">Your starting kit</div>
<h2>Enough to get moving.</h2>
<div class="kit-layout"><div><div class="big-number">1,000</div><div class="data-desc">records in CSV</div><p class="subtitle muted" style="margin-top: 24px">Start with 5.<br>Then try a fresh input.</p></div><div><div class="tool-row"><h3>GitHub starter</h3><p>Dataset · brief · optional code examples</p></div><div class="tool-row"><h3>Gemini on Vertex AI</h3><p>Optional AI access for your experiments</p></div><div class="tool-row"><h3>Your choice of tools</h3><p>APIs · search · code · no-code</p></div></div></div>
<div class="kit-choice"><strong>Code or no-code</strong><span>Build a runnable automated prototype.</span></div>

<!--
Open the workshop repository and the CSV dataset. Walk through the data notes and optional setup. The organizer supplies the project, location, model and access details separately; no credentials belong on a slide. The optional Python example calls Gemini without web search. AI-generated tracklists still need to be checked against real sources. No-code tools are welcome: make the workflow run automatically. Begin with five varied examples, then test a fresh record to check repeatability. You can save this fresh-input check before the pitch; do not tune the approach to that example. Five self-selected examples do not estimate accuracy over all 1,000 records. Explain honestly if the implementation stalls. GitHub is the repository host selected for workshop delivery; no QR code or remote URL is included until the organizer supplies the real one.
-->

---

<!-- _class: dark -->
<div class="eyebrow yellow">The plan</div>
<h2>Four hours. Make them count.</h2>
<div class="timeline"><div class="timeline-bar"><div></div><div></div><div></div><div></div><div></div><div></div></div><div class="phase p1">Intro<small>20 min</small></div><div class="phase p2">Sketch<small>20 min</small></div><div class="phase p3 big">Build + test<small>130 min</small></div><div class="phase p4">Prepare<small>20 min</small></div><div class="phase p5">Pitches<small>40 min</small></div><div class="phase p6">Discuss<small>10 min</small></div><div class="time-mark t1">00:00</div><div class="time-mark t3">00:40</div><div class="time-mark t5">03:10</div></div>
<div class="pitch-callout"><strong>03:10</strong><p>Pitches start. Everyone together.<small>10 minutes per team · with 3 teams, more time for discussion</small></p></div>

<!--
All times are elapsed from the start, not clock times. Intro and team formation: 00:00–00:20. Sketch concept, sources and success checks: 00:20–00:40. Build and test an automated prototype: 00:40–02:50. Prepare the pitch: 02:50–03:10. Four teams pitch to all participants at ten minutes each: 03:10–03:50. Joint discussion and selection: 03:50–04:00. With three teams, use the remaining ten minutes for discussion. Take short breaks within the working session when needed. The phase-band widths represent durations.
-->

---

<!-- _class: final -->
<div class="eyebrow">Your pitch</div>
<h2>Convince us<br>to take it further.</h2>
<div class="pitch-meta"><strong>10 min</strong>per team</div>
<div class="questions"><div class="question">Does it work?<span>Show examples. Tell us what you checked.</span></div><div class="question">Why this approach?<span>Make the value and your choices clear.</span></div><div class="question">What are the trade-offs?<span>Name limits, failure cases and human review.</span></div><div class="question">What happens at scale?<span>Estimate cost. Explain your next step.</span></div></div>
<p class="winning">The strongest practical idea wins.</p>

<!--
Imagine a panel deciding which idea to support next. Make us want to invest, and give us reasons to believe. Choose your format: live demo, slides, workflow sketch, or a combination. Each team has ten uninterrupted minutes in front of everyone; questions follow in the joint discussion. A good estimate can be rough, but should state its assumptions and consider search/API fees, runtime, setup effort and human review across 1,000 records. We select the most convincing overall project: value, repeatable automation, evidence, sound judgment and clear communication. A runnable automated prototype is the goal; if it stalls, show evidence of the implementation and explain the remaining blocker honestly. There is no material prize. Thank everyone, then move into teams.
-->
