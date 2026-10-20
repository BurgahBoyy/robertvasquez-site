"""Rob 10-19: "update robertvasquez.com have it use my personal email spelled out [like the] dot capital [one], and anything
that u think would make it stronger content wise throw it in".
- Contact: the personal Gmail, spelled out the same way the vfe.capital address was (no mailto, so scrapers miss it).
- Shipped: Tourney Now (a client's golf marketplace, now in the client's acceptance testing) and Sail Solutions (the
  studio: solutions.sailwellness.app). Numbers are the ones published on solutions.sailwellness.app.
- Experience: Sail Solutions and Tourney Now. Product count 6 -> 7 (Tourney Now)."""
p = "index.html"; s = open(p, encoding="utf-8").read()
R = [
 ('<span class="mailbtn r d2">rob at vfe dot capital</span>',
  '<span class="mailbtn r d2">robertdanielvasquez at gmail dot com</span>'),
 ('<div class="prod r d4"><div class="ptop"><span class="ptags">Web Design &middot; Freelance</span>',
  '<a class="prod r d1" href="https://solutions.sailwellness.app" target="_blank" rel="noopener"><div class="ptop"><span class="ptags">Software Studio &middot; B2B</span><span class="pill live"><span class="pd"></span>Live</span></div><h4>Sail Solutions &rarr;</h4><p>My software studio: compliance-ready platforms built in days, not quarters. Six platforms in the portfolio, from payments to campaign software.</p></a>\n'
  '        <div class="prod r d2"><div class="ptop"><span class="ptags">Sports &middot; Marketplace</span><span class="pill beta"><span class="pd"></span>Client testing</span></div><h4>Tourney Now</h4><p>A golf tournament marketplace built for a client: registration, payments, live scoring and leaderboards. About 193,000 lines of code in 8 days, now in the client&rsquo;s acceptance testing.</p></div>\n'
  '        <div class="prod r d4"><div class="ptop"><span class="ptags">Web Design &middot; Freelance</span>'),
 ('        <div class="exp-row rx d1"><div class="when">Since 2026</div><div><h5>Vasquez Factoring Exchange</h5>',
  '        <div class="exp-row rx d1"><div class="when">Since 2026</div><div><h5>Sail Solutions</h5><div class="role">Founder &amp; Lead Engineer</div></div></div>\n'
  '        <div class="exp-row rx d1"><div class="when">2026</div><div><h5>Tourney Now</h5><div class="role">Platform Architect (client build)</div></div></div>\n'
  '        <div class="exp-row rx d1"><div class="when">Since 2026</div><div><h5>Vasquez Factoring Exchange</h5>'),
 ('<span>6 products, 5 sites, 6 kits in ~2 years</span>', '<span>7 products, 5 sites, 6 kits in ~2 years</span>'),
 ('<span class="u" data-count="6">0</span> products in 2 years', '<span class="u" data-count="7">0</span> products in 2 years'),
]
for a, b in R:
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("ok")
