---
marp: true
theme: default
size: 16:9
paginate: true
title: From Records to Royalties
description: A four-hour tracklist hackathon at GEMA
lang: en
style: |
  @font-face { font-family: TheSans; src: local("TheSansOfficeLF"); font-weight: 400; }
  @font-face { font-family: TheSans; src: local("TheSansOfficeLF-Bold"); font-weight: 700; }
  section { --ink: #3F3F3F; --petrol: #007E7F; --yellow: #FFCB05; font-family: TheSans, Arial, sans-serif; background: #FAFAF7; color: var(--ink); padding: 60px 76px; display: flex; flex-direction: column; justify-content: flex-start; place-content: start start; font-size: 28px; line-height: 1.25; }
  section::after { font-size: 15px; color: #777; bottom: 28px; right: 42px; }
  h1, h2, h3, p { margin: 0; padding: 0; }
  h1,h2,h3 { color: inherit; font-weight: 700; }
  h1 { font-size: 92px; line-height: 1.04; letter-spacing: -2.8px; }
  h2 { font-size: 60px; line-height: 1.07; letter-spacing: -1.3px; }
  h3 { font-size: 28px; line-height: 1.2; }
  p { font-size: 26px; }
  small { font-size: 20px; }
  .label { font-size: 17px; letter-spacing: 1.4px; text-transform: uppercase; color: #666; }
  .accent { color: var(--petrol); }
  .rule { height: 1px; background: #D7D7D0; }
  .brand-logo { position: absolute; top: 50px; right: 76px; width: 43px; height: auto; }
  section.cover { border-left: 16px solid var(--yellow); padding-left: 76px; }
  section.cover h1 { margin-top: 100px; }
  section.cover .question { color: var(--petrol); }
  section.cover .intro { margin-top: 44px; font-size: 28px; max-width: 800px; }
  section.cover .event { position:absolute; left:76px; bottom:58px; font-size:20px; }
  .flow-diagram { width: 1128px; height: 370px; margin-top: 30px; }
  .flow-diagram text { font-family: TheSans, Arial, sans-serif; }
  .flow-questions { display:flex; border-top:1px solid #D7D7D0; padding-top:22px; gap:52px; font-size:24px; }
  .flow-questions strong { color:var(--petrol); margin-right:12px; font-size:17px; }
  .release-layout { display:grid; grid-template-columns:1fr 80px 1fr; align-items:center; margin-top:52px; }
  .release-data { border-top:3px solid var(--petrol); padding-top:23px; }
  .release-data .album { font-size:48px; margin:20px 0 3px; font-weight:700; }
  .release-data .artist { font-size:27px; }
  .release-data .identifier { margin-top:30px; font-family: monospace; font-size:22px; }
  .release-data .caption { margin-top:10px; font-size:18px; color:#666; }
  .release-gap { text-align:center; font-size:34px; color:var(--petrol); }
  .tracklist { padding-left:35px; }
  .tracklist .label { margin-bottom:18px; }
  .tracklist .missing-title { font-size:33px; font-weight:700; margin-bottom:23px; }
  .track-row { display:flex; align-items:center; gap:25px; height:44px; color:#888; font-size:18px; }
  .track-row i { display:block; height:1px; background:#C7C7BE; width:100%; }
  .takeaway { position:absolute; bottom:79px; left:76px; font-size:27px; }
  .takeaway mark { background:var(--yellow); color:var(--ink); padding:3px 9px; }
  section.challenge { background:var(--petrol); color:#FFF; }
  section.challenge::after { color:#C4DEDE; }
  section.challenge h2 { font-size:70px; }
  .automation { display:grid; grid-template-columns:260px 70px 400px 70px 328px; align-items:center; margin-top:65px; }
  .automation .edge { font-size:27px; }
  .automation small { display:block; margin-top:13px; color:#C5E3E3; font-size:20px; }
  .automation .arrow { text-align:center; font-size:36px; color:#B1D7D7; }
  .automation .method { border:1px solid #8BC0C0; padding:34px 25px; font-size:35px; font-weight:700; text-align:center; color:var(--yellow); }
  .requirements { margin-top:55px; padding-top:25px; border-top:1px solid #74AEAE; display:flex; gap:36px; font-size:23px; }
  .requirements span { flex:1; }
  .bonus { margin-top:28px; font-size:22px; line-height:1.4; color:#E1F0F0; }
  .bonus strong { color:var(--yellow); }
  .kit { display:grid; grid-template-columns:430px 1fr; gap:70px; margin-top:52px; }
  .quantity { font-size:156px; letter-spacing:-6px; line-height:.95; font-weight:700; color:var(--petrol); }
  .kit .data-label { font-size:26px; margin-top:20px; }
  .kit .start { margin-top:38px; font-size:27px; line-height:1.35; }
  .kit .start strong { border-bottom:6px solid var(--yellow); }
  .resource { padding:0 0 26px; margin-bottom:23px; border-bottom:1px solid #D7D7D0; }
  .resource p { font-size:23px; color:#666; margin-top:8px; }
  .resource:last-child { border:0; }
  .schedule { display:grid; grid-template-columns:300px 1fr; gap:90px; margin-top:44px; }
  .schedule .focus { border-top:6px solid var(--yellow); padding-top:25px; }
  .schedule .focus strong { display:block; font-size:105px; line-height:1; color:var(--petrol); letter-spacing:-3px; }
  .schedule .focus p { font-size:29px; margin-top:13px; }
  .schedule .focus small { display:block; margin-top:30px; color:#666; line-height:1.4; }
  .agenda-row { display:grid; grid-template-columns:90px 1fr 90px; align-items:center; height:58px; border-bottom:1px solid #D7D7D0; font-size:25px; }
  .agenda-row .time { color:#666; font-size:21px; }
  .agenda-row .duration { font-size:19px; text-align:right; color:#666; }
  .agenda-row.build { background:#E5F1EF; margin-left:-17px; margin-right:-17px; padding:0 17px; color:var(--petrol); font-weight:700; }
  .agenda-row.pitch { font-weight:700; }
  .schedule-note { margin-top:24px; font-size:18px; color:#666; }
  .pitch-layout { display:grid; grid-template-columns:380px 1fr; gap:90px; margin-top:48px; }
  .pitch-time { font-size:145px; font-weight:700; line-height:1; letter-spacing:-5px; color:var(--petrol); }
  .pitch-time span { font-size:38px; letter-spacing:0; margin-left:10px; }
  .pitch-sub { font-size:25px; margin-top:8px; }
  .pitch-questions { display:grid; grid-template-columns:1fr 1fr; gap:36px; }
  .pitch-questions h3 { font-size:27px; }
  .pitch-questions p { font-size:22px; color:#666; margin-top:10px; line-height:1.35; }
  .closing { position:absolute; left:76px; right:76px; bottom:68px; padding-top:23px; border-top:6px solid var(--yellow); font-size:28px; font-weight:700; }
---
<!-- _class: cover -->
<div class="label">GEMA · Tracklist hackathon</div>
<img class="brand-logo" src="data:image/png;base64,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M2fOtFXij1CB8efly5cbGmoZhlCBGRjkAiMwg0xhBGaQKYzADDKFEZhBpkhFYLW1taK0tFQ8//zzomfPnmL//fcXW265pVhnnXXEuuuuK3bYYQfRrVs3cffdd4uff/5ZzObkCdcWTPy/X79+Ypdddmnyewcff/yxuPDCC1XeWfHyyy8XEz178L/++uvaa3W8+OKLxfTp0+2UyYBL6KGHHtLmr+Orr76qra+ouPbaa8Xqq68u/sWJdRkhJ4EtWbJEvPnmm+LII48Um2yyiVhppZUUEdWJJ54orr/+etG/f3/18g4//HCx9tpriw022ED8/ve/F+ecc4547LHHxA8//CDeeecdJcLtt99eW2E//vijuPrqq8Vuu+0m2rVr13gfP6688spK4HvuuafYfffdxdZbby3WWGONwLSbbbaZQPxuIOw///nPKo8OHTpo0zlcZZVVxNNPP22nTIYxY8aoOtDl77B9+/bqmtNPP118yJYJCQVWX18vtthiC5XnAQccIOoSnhsZhkQCIwmt0Lnnnqsq1nl4voYLLrhAtWg6VFZWirPPPlu1bE4aN/0E5mDhwoWiT58+SkC69JBWcOTIkXaKX0HaIUOGqJZyr732UmJ3p9MJzAHPW15eLtZbb70mabw86aSTxKIctnZCoO761PHmm29WLV2uePzxxxvzXH/99cV/2UQmA8QWGJd/++23Yp999mny4FTMPffco76MIJCelsGbHoYJDODc44vzpnV47LHHqnsEYfHixeKzzz4Te++9d2O6IIE5uPLKK5vcy8uOHTuKCveWTzHAcx144IHafB2utdZaYpZ7M7yEmD9/vmrdnXxpFa+77jr7r+kitsCmTp0qOnfu3OTB4V84wDNGVjzk7373uyZ5RBEY+Otf/9oknZt0zVFRU1MjttpqK5UuisBeeeWVZvfz8rLLLrOvjodBgwapFx308ey333721bnh888/b9aC77jjjom72yDEEhhf57777tukYHCjjTYS33zzjX1VdIwdO1bZVU4+UQV2ySWXNLm/m3EEBugqVltttUgCw+jnHgxYMAe894bYn1Ni7ktPt3rooYcquxF71M9W7Nq1q50iOXjdV1xxRbN78DMfUNqILLB58+aJ4447rkmhHB522GGJjETExCDByaclBDZu3Djxm9/8JpbAbr31VnHUUUc1u7fDe++9104RDYMH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" alt="GEMA">
<h1>Music creates value.<br><span class="question">Who gets paid?</span></h1>
<p class="intro">Find the songs on a record.<br>Help connect music use to its creators.</p>
<p class="event">4 hours &nbsp; / &nbsp; Around 4 teams &nbsp; / &nbsp; 4–5 people per team</p>

<!--
Open with the music, then the people behind it. GEMA represents composers, lyricists and music publishers and administers rights on their behalf. Keep this high-level: today is about recovering release tracklists, one small but useful part of a much larger process.
Source: GEMA, “What is GEMA?” https://www.gema.de/en/w/help/gema/organisation/questions-and-answers/what-is-gema
-->

---

<h2>Music use becomes<br><span class="accent">royalties for creators.</span></h2>
<svg class="flow-diagram" viewBox="0 0 1128 370" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Usage metadata flows from music use to GEMA. Licence revenue enters separately. Royalties flow to composers, lyricists and publishers.">
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="none" stroke="#007E7F" stroke-width="1.3"/></marker></defs>
<g fill="#3F3F3F" font-size="25"><text x="0" y="47">Streaming</text><text x="0" y="96">Radio &amp; TV</text><text x="0" y="145">Video on demand</text><text x="0" y="194">Live / setlists</text><text x="0" y="243" font-weight="700">Physical releases</text></g>
<g fill="none" stroke="#7FA9A4" stroke-width="2"><path d="M253 39H290Q320 39 320 69V145H410"/><path d="M253 88H300Q320 88 320 108V145"/><path d="M253 137H320"/><path d="M253 186H300Q320 186 320 166V145"/><path d="M253 235H290Q320 235 320 205V145"/></g>
<path d="M335 145H420" stroke="#007E7F" stroke-width="2" marker-end="url(#arrow)"/>
<text x="335" y="108" fill="#007E7F" font-size="18">Usage data</text>
<circle cx="544" cy="145" r="103" fill="#007E7F"/>
<text x="544" y="158" fill="#FFF" font-size="43" font-weight="700" text-anchor="middle">GEMA</text>
<path d="M668 145H814" stroke="#007E7F" stroke-width="2" marker-end="url(#arrow)"/>
<text x="690" y="108" fill="#007E7F" font-size="18">Royalties</text>
<g fill="#3F3F3F" font-size="28"><text x="850" y="100">Composers</text><text x="850" y="150">Lyricists</text><text x="850" y="200">Publishers</text></g>
<path d="M544 309V266" stroke="#007E7F" stroke-width="2" marker-end="url(#arrow)"/>
<text x="544" y="339" fill="#3F3F3F" font-size="22" text-anchor="middle">Licence revenue</text>
</svg>
<div class="flow-questions"><span><strong>01</strong> Which music?</span><span><strong>02</strong> Who gets paid?</span><span><strong>03</strong> How much?</span></div>

<!--
This is a deliberately simplified business view, not a complete payout architecture. GEMA licenses music use and distributes royalties to the creators and publishers it represents. Usage information helps identify the works used and support allocation. Revenue is a distinct input; the arrow does not mean metadata itself creates money. The five usage categories are examples, not a complete inventory. This slide is about usage and release metadata, not raw-audio recognition. Physical-release tracklists support identifying the music on a product; recovering them does not itself identify every rights holder or calculate a payment.
Sources: GEMA, “What is GEMA?” https://www.gema.de/en/w/help/gema/organisation/questions-and-answers/what-is-gema ; GEMA, “What are royalties?” https://www.gema.de/en/w/help/creators/royaltiespay-out/royalties/what-are-royalties
-->

---

<h2>Known release.<br><span class="accent">Missing tracklist.</span></h2>
<div class="release-layout"><div class="release-data"><div class="label">A record from your dataset</div><p class="album">Aspiral</p><p class="artist">EPICA</p><p class="identifier">4065629733131</p><p class="caption">Supplied barcode · edition still to verify</p></div><div class="release-gap">→</div><div class="tracklist"><div class="label">The information we need</div><p class="missing-title">Which songs are on it?</p><div class="track-row">01<i></i></div><div class="track-row">02<i></i></div><div class="track-row">03<i></i></div><div class="track-row">…<i></i></div></div></div>
<p class="takeaway">Same album title. Different editions. <mark>The details matter.</mark></p>

<!--
We have release information, but some tracklists are missing. An album title, artist or barcode may identify a product, but we still need the songs on the correct edition. Bonus tracks, regional editions and reissues can matter. Without that information, one of the links needed for subsequent allocation is missing. Tracklist recovery is the workshop scope; rights-holder identification and payment calculation are not. The supplied Aspiral / EPICA / 4065629733131 example is an actual row from the workshop CSV, not a verified release match. Empty track lines illustrate missing data; they do not assert the number of songs.
-->

---

<!-- _class: challenge -->
<h2>Find the tracklist.<br>Make it repeatable.</h2>
<div class="automation"><div class="edge">Release information<small>Title · artist · barcode</small></div><div class="arrow">→</div><div class="method">Your automated<br>prototype</div><div class="arrow">→</div><div class="edge">Tracks + sources<small>Song titles + artists.<br>Evidence for the match.</small></div></div>
<div class="requirements"><span>Match the right edition.</span><span>Check against sources.</span><span>Show uncertainty.</span></div>
<p class="bonus"><strong>Optional bonus:</strong> Track length + credits<br>Lyricists · composers · producers · more metadata, with sources.</p>

<!--
The method is yours to choose: catalog APIs, automated web search, AI, scripts, no-code tools, or combinations. Start with five varied records, then test one fresh input. Target the correct edition and ordered tracks with song titles, performing artists and source links. Once the discovery workflow works, optionally enrich tracks with duration (mm:ss or seconds), lyricists, composers, producers and other useful metadata. Match the recording/version, keep roles separate, cite sources and mark missing or conflicting values rather than guessing. The bonus is optional; prioritize a working prototype. Manual checks are useful for evaluation; manually gathering all tracklists is not the solution. Build a runnable automated prototype using code or no-code tools. Manually entering release information or pressing Run is fine; finding the tracklist should be automated. You may copy the first five inputs from CSV; automating CSV import is optional. If you get stuck, show the work, diagnose the failure and explain what remains. Clearly distinguish what you tested from what you propose.
-->

---

<h2>Everything you need<br><span class="accent">to get started.</span></h2>
<div class="kit"><div><div class="quantity">1,000</div><p class="data-label">records in CSV</p><p class="start"><strong>Start with five.</strong><br>Then test one fresh input.</p></div><div><div class="resource"><h3>GitHub starter</h3><p>Data, challenge and optional Python examples.</p></div><div class="resource"><h3>Gemini on Vertex AI</h3><p>Optional AI access for your experiments.</p></div><div class="resource"><h3>Your choice of tools</h3><p>APIs, search, code or no-code.<br>Build something that runs.</p></div></div></div>

<!--
Open the workshop repository and the CSV dataset. Walk through the data notes and optional setup. The organizer supplies the project, location, model and access details separately; no credentials belong on a slide. The optional Python example calls Gemini without web search. AI-generated tracklists still need to be checked against real sources. No-code tools are welcome: make the workflow run automatically. Begin with five varied examples, then test a fresh record to check repeatability. You can save this fresh-input check before the pitch; do not tune the approach to that example. Five self-selected examples do not estimate accuracy over all 1,000 records. Explain honestly if the implementation stalls. Workshop repository: https://github.com/cloudIT4IPM/ai4-lmu-hackathon
-->

---

<h2>Four hours.<br><span class="accent">Time to make something.</span></h2>
<div class="schedule"><div class="focus"><strong>130</strong><p>minutes to build<br>and test</p><small>Get one record working.<br>Then improve the method.</small></div><div><div class="agenda-row"><span class="time">00:00</span><span>Intro + teams</span><span class="duration">20 min</span></div><div class="agenda-row"><span class="time">00:20</span><span>Sketch the approach</span><span class="duration">20 min</span></div><div class="agenda-row build"><span class="time">00:40</span><span>Build + test</span><span class="duration">130 min</span></div><div class="agenda-row"><span class="time">02:50</span><span>Prepare your pitch</span><span class="duration">20 min</span></div><div class="agenda-row pitch"><span class="time">03:10</span><span>Pitch to everyone</span><span class="duration">40 min</span></div><div class="agenda-row"><span class="time">03:50</span><span>Discuss</span><span class="duration">10 min</span></div><p class="schedule-note">10 minutes per team. Everyone presents to the full group.</p></div></div>

<!--
All times are elapsed from the start, not clock times. Intro and team formation: 00:00–00:20. Aim for approximately four teams of four to five people. Sketch concept, sources and success checks: 00:20–00:40. Build and test an automated prototype: 00:40–02:50. Prepare the pitch: 02:50–03:10. Four teams pitch to all participants at ten minutes each: 03:10–03:50. Joint discussion: 03:50–04:00. Take short breaks within the working session when needed.
-->

---

<h2>Show what works.<br><span class="accent">Make the case for more.</span></h2>
<div class="pitch-layout"><div><div class="pitch-time">10<span>min</span></div><p class="pitch-sub">Your team. In front of everyone.</p></div><div class="pitch-questions"><div><h3>Demonstrate it.</h3><p>Show results and<br>what you checked.</p></div><div><h3>Explain your choices.</h3><p>Why this approach?<br>What are its strengths?</p></div><div><h3>Name the limits.</h3><p>Failures, uncertainty<br>and human review.</p></div><div><h3>Estimate the cost.</h3><p>What would it take<br>to process 1,000 records?</p></div></div></div>
<p class="closing">Share what worked. Learn from each other.</p>

<!--
Imagine a panel deciding which idea to support next. Make us want to invest, and give us reasons to believe. Choose your format: live demo, slides, workflow sketch, or a combination. Each team has ten uninterrupted minutes in front of everyone; questions follow in the joint discussion. A good estimate can be rough, but should state its assumptions and consider search/API fees, runtime, setup effort and human review across 1,000 records. Discuss each approach: value, repeatable automation, evidence, sound judgment and clear communication. A runnable automated prototype is the goal; if it stalls, show evidence of the implementation and explain the remaining blocker honestly. Thank everyone, then move into teams.
-->
