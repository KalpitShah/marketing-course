"""Generate all framework diagrams into marketing-program/images/.

Usage:  python3 scripts/make_diagrams.py
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from diagram_lib import (  # noqa: E402
    ACCENT, ACCENT_SOFT, GREEN, GREEN_SOFT, WARM, WARM_SOFT, ROSE, ROSE_SOFT, PANEL, LINE, PAPER, MUTED, INK,
    Canvas, cycle, edge_arrow, flow, funnel, matrix, rings, stack, table, timeline, tree,
)

OUT = os.path.join(os.path.dirname(__file__), "..", "marketing-program", "images")
os.makedirs(OUT, exist_ok=True)

D: dict[str, str] = {}

# ---------------- Week 1: how marketing works ----------------
D["w01-marketing-system.svg"] = flow(
    "How software marketing actually works",
    ["Audience", "Attention", "Trust", "Conversion", "Retention", "Advocacy"],
    subs=["a specific group with a shared problem", "they notice you in a channel", "they believe you can solve it",
          "they sign up or buy", "they keep getting value", "they tell others"],
    caption="Every tactic you will ever run maps to one of these six jobs. Diagnose which one is broken before picking a tactic.",
)
D["w01-marketing-vs-sales-vs-growth.svg"] = table(
    "Marketing, sales and growth: who does what",
    ["Function", "Core question", "Typical owner in a startup", "Main output"],
    [
        ["Marketing", "Who should want us, and why?", "Founder, then first marketer", "Positioning, messaging, demand, pipeline"],
        ["Sales", "How do we close this specific buyer?", "Founder, then first AE", "Closed deals, objections learned"],
        ["Growth", "Which loops compound users and revenue?", "Founder or PM plus engineer", "Experiments, activation, loops"],
        ["Product marketing", "How do we launch and explain what we built?", "Founder or PMM", "Launches, enablement, competitive intel"],
    ],
    col_widths=[170, 280, 250, 270],
)
D["w01-in-market-95-5.svg"] = matrix(
    "Most of your market is not buying this quarter",
    "Time horizon", "Share of buyers",
    [["About 5% in-market now", "Capture with search, reviews, sales, comparisons"],
     ["About 95% out-of-market", "Build memory with content, brand, community"],
     ["Short-term: conversion", "Performance channels, activation, offers"],
     ["Long-term: mental availability", "Be the name they recall when the problem arrives"]],
    caption="Based on the Ehrenberg-Bass and LinkedIn B2B Institute 95-5 finding. You need both halves, staffed differently.",
)

# ---------------- Week 2: customer research ----------------
D["w02-jtbd-forces.svg"] = Canvas(900, 420, "The four forces of a switch (Jobs to be Done)").render()
c = Canvas(900, 440, "The four forces of a switch (Jobs to be Done)")
c.box(330, 180, 240, 90, "Buyer decides to switch", fill=ACCENT_SOFT, stroke=ACCENT, size=15)
c.box(40, 90, 240, 70, "Push of the current situation", "pain with the status quo", fill=GREEN_SOFT, stroke=GREEN)
c.box(620, 90, 240, 70, "Pull of the new solution", "attraction of your product", fill=GREEN_SOFT, stroke=GREEN)
c.box(40, 300, 240, 70, "Anxiety about the new", "will it work for us? is it risky?", fill=ROSE_SOFT, stroke=ROSE)
c.box(620, 300, 240, 70, "Habit of the present", "inertia, switching cost, comfort", fill=ROSE_SOFT, stroke=ROSE)
c.arrow(280, 125, 330, 200, color=GREEN, width=3)
c.arrow(620, 125, 570, 200, color=GREEN, width=3)
c.arrow(330, 250, 280, 335, color=ROSE, width=3)
c.arrow(570, 250, 620, 335, color=ROSE, width=3)
c.caption("Progress happens when push plus pull outweighs anxiety plus habit. Your messaging has to work on all four, not just pull.")
D["w02-jtbd-forces.svg"] = c.render()
D["w02-interview-flow.svg"] = flow(
    "A customer discovery interview in 30 minutes",
    ["Context (5 min)", "Last time story (10 min)", "Alternatives (5 min)", "Buying process (5 min)", "Wrap (5 min)"],
    subs=["role, team, tools, how success is measured", "walk through the most recent time the problem showed up",
          "what they tried, what they pay for, what failed", "who decides, who blocks, what budget", "who else should I talk to?"],
    caption="Ask about the past, not the future. Specific stories beat opinions.",
)
D["w02-research-methods.svg"] = matrix(
    "Choosing a research method",
    "Breadth (how many people)", "Depth (how much you learn per person)",
    [["1:1 interviews", "10 to 20 conversations, the best early tool"],
     ["Support and sales call reviews", "listen to recordings at scale"],
     ["Usability sessions", "watch 5 people use the product"],
     ["Surveys and review mining", "quantify what interviews found"]],
)

# ---------------- Week 3: segmentation and ICP ----------------
D["w03-icp-scorecard.svg"] = table(
    "Ideal customer profile scorecard (example criteria)",
    ["Dimension", "Great fit", "OK fit", "Poor fit"],
    [
        ["Problem intensity", "Costs them money or time weekly", "Occasional annoyance", "Nice to have"],
        ["Existing workaround", "Spreadsheets, scripts, or a paid tool", "Nothing yet", "Already solved well"],
        ["Access to buyer", "You can reach 100 of them this month", "Reachable through partners", "Cannot find them"],
        ["Willingness to pay", "Budget line exists", "Would need to create budget", "Expects free"],
        ["Expansion potential", "Grows with usage or seats", "Flat", "One-off"],
    ],
    col_widths=[200, 260, 250, 260],
)
D["w03-beachhead-bowling.svg"] = Canvas(10, 10).render()
c = Canvas(900, 460, "Beachhead first, then adjacent segments (bowling pin strategy)")
c.box(370, 300, 160, 70, "Beachhead segment", "win decisively here", fill=ACCENT_SOFT, stroke=ACCENT)
c.box(200, 180, 160, 70, "Adjacent segment A", "same buyer, new use case", fill=GREEN_SOFT, stroke=GREEN)
c.box(540, 180, 160, 70, "Adjacent segment B", "same use case, new buyer", fill=GREEN_SOFT, stroke=GREEN)
c.box(60, 70, 150, 64, "Segment C", fill=WARM_SOFT, stroke=WARM)
c.box(300, 70, 150, 64, "Segment D", fill=WARM_SOFT, stroke=WARM)
c.box(450, 70, 150, 64, "Segment E", fill=WARM_SOFT, stroke=WARM)
c.box(690, 70, 150, 64, "Segment F", fill=WARM_SOFT, stroke=WARM)
c.arrow(400, 300, 300, 252)
c.arrow(500, 300, 600, 252)
c.arrow(250, 180, 150, 136)
c.arrow(300, 180, 360, 136)
c.arrow(600, 180, 540, 136)
c.arrow(650, 180, 750, 136)
c.caption("Each win gives you references, content and word of mouth that make the next segment cheaper to enter.")
D["w03-beachhead-bowling.svg"] = c.render()
D["w03-tam-sam-som.svg"] = rings(
    "Market sizing that founders can defend",
    ["SOM: who you can realistically win in 2 to 3 years", "SAM: who your product and channels can serve", "TAM: everyone with the problem"],
    caption="Build SOM bottom-up: number of accounts you can reach times realistic win rate times price. Investors and you both trust that more.",
)

# ---------------- Week 4: positioning ----------------
D["w04-positioning-canvas.svg"] = flow(
    "Positioning canvas (April Dunford's components, in order)",
    ["Competitive alternatives", "Unique attributes", "Value for customers", "Best-fit customers", "Market category"],
    subs=["what they would do without you", "what you have that they do not", "what those attributes enable",
          "who cares the most about that value", "the frame that makes it obvious"],
    caption="Work left to right. The category comes last because it is a choice, not a fact.",
)
D["w04-category-choices.svg"] = table(
    "Three ways to frame your category",
    ["Style", "What you say", "When it works", "Risk"],
    [
        ["Head-to-head", "We are a better X", "Existing budget line, clear buyer, you win on the criteria that matter", "You fight the leader on their turf"],
        ["Big fish, small pond", "X built for [segment]", "A segment is underserved by the generic leaders", "Segment might be too small"],
        ["Create a new game", "A new way to do Y", "Existing category cannot describe you; you have resources to educate", "Expensive, slow, often fails"],
    ],
    col_widths=[170, 210, 330, 260],
)
D["w04-alternatives-map.svg"] = matrix(
    "Map the alternatives before you position",
    "Cost and effort to the buyer", "How well it solves the job",
    [["Do nothing / spreadsheet", "cheap, weak: your most common competitor"],
     ["Hire people or agency", "expensive, works, does not scale"],
     ["Generic tool", "cheap, partial fit"],
     ["Direct competitors", "you have to beat these on something specific"]],
)

# ---------------- Week 5: messaging ----------------
D["w05-messaging-hierarchy.svg"] = stack(
    "Messaging hierarchy",
    ["Proof points (numbers, logos, quotes, demos)", "Supporting messages (3 to 4 reasons to believe)", "Value proposition (the outcome for the best-fit customer)", "One-line position (what you are, for whom)"],
    subs=["evidence for every claim above", "each maps to a unique attribute", "written in the customer's words", "anchored in the category you chose"],
    caption="Top of the pyramid is what people remember. The base is what makes them believe it.",
)
D["w05-features-benefits-outcomes.svg"] = flow(
    "Feature to benefit to outcome",
    ["Feature", "Benefit", "Outcome", "Proof"],
    subs=["what it is: 'real-time sync'", "what it does: 'no stale data'", "why they care: 'ship reports the same day'", "'Acme cut reporting from 3 days to 3 hours'"],
    caption="Founders write features. Buyers buy outcomes. Every message should be able to walk this chain in both directions.",
)
D["w05-objection-map.svg"] = table(
    "Objection map: what stops a buyer, and what answers it",
    ["Objection", "What they are really asking", "Message or proof that answers it"],
    [
        ["Does it work for a team like ours?", "Fit", "Case study from the same segment; ICP language on the site"],
        ["Is it hard to set up?", "Effort and risk", "Time-to-value number; migration guide; free trial"],
        ["Why not the incumbent?", "Differentiation", "Comparison page on the criteria you win"],
        ["Will you be around?", "Trust", "Customers, funding, uptime, security page"],
        ["Is it worth the price?", "Value", "ROI math in their terms; pricing anchored to a value metric"],
    ],
    col_widths=[290, 220, 430],
)

# ---------------- Week 6: copy and landing pages ----------------
D["w06-landing-page-anatomy.svg"] = stack(
    "Anatomy of a high-converting software landing page",
    ["Final call to action and FAQ", "Pricing or plan summary", "Social proof: logos, quotes, numbers", "How it works: 3 steps or a short demo", "Problem and outcome: why this matters", "Hero: headline, subhead, proof, one CTA, product visual"],
    bottom_up=False,
    caption="Order matters less than clarity. A visitor should know what it is, who it is for, and why it is better within 5 seconds.",
)
D["w06-headline-formulas.svg"] = table(
    "Headline formulas that work for software",
    ["Formula", "Pattern", "Example shape"],
    [
        ["Outcome for whom", "[Outcome] for [ICP]", "Error tracking for mobile teams"],
        ["Kill the pain", "Stop [pain] with [category]", "Stop losing deals to slow quotes"],
        ["Contrast", "[Old way] is over. [New way] in [time]", "Deploy in minutes, not weeks"],
        ["Specific claim", "[Number] [result] for [ICP]", "Cut cloud spend 30% in 30 days"],
        ["Category plus twist", "The [category] that [unique attribute]", "The CRM that fills itself in"],
    ],
    col_widths=[220, 340, 380],
)
D["w06-cro-loop.svg"] = cycle(
    "Conversion optimization loop",
    ["Find the leak in the funnel", "Form a hypothesis from research", "Change copy, layout or offer", "Measure against a baseline", "Keep, revert, or dig deeper"],
    caption="Most landing page wins come from clarity and proof, not colors and button shapes.",
)

# ---------------- Week 7: brand ----------------
D["w07-brand-layers.svg"] = rings(
    "What a software brand is made of",
    ["Promise: the one thing customers can count on", "Personality and voice: how it sounds", "Distinctive assets: name, logo, color, mascot, sound", "Experience: every touchpoint from ad to invoice"],
    caption="Brand is the memory people have of you. Distinctive assets make that memory retrievable.",
)
D["w07-distinctive-vs-differentiated.svg"] = matrix(
    "Distinctive versus differentiated",
    "Differentiated (meaningfully different from rivals)", "Distinctive (easily recognized and recalled)",
    [["Recognizable but generic", "known, but for nothing in particular"],
     ["The goal", "instantly recognizable and clearly better for someone"],
     ["Invisible", "no one remembers you and nothing stands out"],
     ["Better but unknown", "great product, no memory; the common founder trap"]],
)
D["w07-voice-chart.svg"] = table(
    "Voice chart: fill this in for your company",
    ["Trait", "We are", "We are not", "Example line"],
    [
        ["Confident", "direct, specific", "boastful, vague", "'Ships in one deploy. No migration.'"],
        ["Technical", "precise, honest about limits", "jargon for its own sake", "'Works with Postgres 12 and up.'"],
        ["Warm", "human, plain", "cutesy, over-familiar", "'Something broke. Here is the fix.'"],
    ],
    col_widths=[150, 240, 240, 310],
)

# ---------------- Week 8: narrative ----------------
D["w08-strategic-narrative.svg"] = flow(
    "Strategic narrative structure",
    ["Name the change in the world", "Show winners and losers", "Tease the promised land", "Introduce the obstacles", "Present your product as the bridge", "Prove it"],
    subs=["an undeniable shift", "what happens to those who adapt or do not", "the new state everyone wants", "why it is hard to get there", "features framed as obstacles removed", "customers who made it"],
    caption="Andy Raskin's structure, used by Zuora, Drift and hundreds of SaaS decks. It works because it starts with the buyer's world, not your product.",
)
D["w08-story-arc.svg"] = Canvas(10, 10).render()
c = Canvas(900, 420, "Customer story arc (use for case studies, demos and founder stories)")
pts = [(80, 320), (250, 280), (420, 300), (560, 140), (720, 160), (840, 110)]
labels = ["Ordinary world", "Trigger event", "Failed attempts", "Turning point", "New normal", "Proof"]
for i in range(len(pts) - 1):
    c.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], color=ACCENT, width=3)
for i, (x, y) in enumerate(pts):
    c.circle(x, y, 9, fill=ACCENT_SOFT, stroke=ACCENT, sw=2)
    c.text(x, y + (28 if i % 2 == 0 else -28), labels[i], size=13, weight="600")
c.caption("Tension comes from the failed attempts. Without them the story is a feature list.")
D["w08-story-arc.svg"] = c.render()
D["w08-demo-structure.svg"] = timeline(
    "A product demo that sells (15 minutes)",
    ["Confirm the pain", "Show the end state", "Walk the path", "Handle objections", "Agree next step"],
    subs=["2 min, their words", "3 min, the 'wow' first", "6 min, only the relevant path", "3 min, from the objection map", "1 min, specific and dated"],
)

# ---------------- Week 9: channel strategy ----------------
D["w09-channel-landscape.svg"] = tree(
    "The channel landscape",
    "Ways a software company can reach buyers",
    ["Owned", "Earned", "Paid", "Product-led", "Sales-led"],
    grandchildren=[["Website and SEO", "Email and newsletter", "Blog, docs, YouTube"],
                   ["PR and press", "Reviews and word of mouth", "Community and social"],
                   ["Search ads", "Social ads", "Sponsorships and newsletters"],
                   ["Free tier and trials", "Referrals and invites", "Integrations and marketplaces"],
                   ["Outbound", "Partners and resellers", "Events and webinars"]],
    height=520,
)
D["w09-product-channel-fit.svg"] = matrix(
    "Product-channel fit",
    "Average contract value", "Time to value",
    [["Slow value, low price", "hard: needs content, community and patience"],
     ["Slow value, high price", "sales-led, events, outbound, partners"],
     ["Fast value, low price", "self-serve, SEO, virality, marketplaces"],
     ["Fast value, high price", "PLG plus sales assist, paid search, reviews"]],
    caption="Brian Balfour's core point: products are built for channels, not the other way around. Your price and time-to-value decide which channels can work.",
)
D["w09-bullseye.svg"] = rings(
    "Bullseye channel selection",
    ["Focus: 1 or 2 channels you go all in on", "Test: 3 to 5 cheap experiments this quarter", "Brainstorm: every plausible channel"],
    caption="From Traction by Gabriel Weinberg and Justin Mares. Most startups find one channel that works; find it before spreading out.",
)

# ---------------- Week 10: content ----------------
D["w10-content-flywheel.svg"] = cycle(
    "The content flywheel",
    ["Talk to customers and sales", "Write what they search and ask", "Distribute in the channels they use", "Capture email and signups", "Learn what converted"],
    caption="Content compounds only if you close the loop from what customers ask to what you publish next.",
)
D["w10-library-vs-publication.svg"] = matrix(
    "Library or publication?",
    "Reader intent", "Content shelf life",
    [["Evergreen library", "guides, docs, comparisons, glossaries: built for search"],
     ["Reference and tools", "calculators, templates, benchmarks"],
     ["Publication", "opinion, research, newsletter: built for subscribers and sharing"],
     ["Newsjacking and launches", "timely, short-lived, distribution first"]],
    caption="Pick one primary model. Libraries serve search intent; publications build audience. Mixing them without intent makes both weak.",
)
D["w10-content-pipeline.svg"] = flow(
    "Content production pipeline",
    ["Idea backlog", "Brief", "Draft", "Expert review", "Publish", "Distribute", "Refresh"],
    subs=["from calls, search, community", "audience, angle, keyword, CTA", "founder or writer", "engineer or customer checks it",
          "site plus docs plus repo", "email, social, communities, partners", "update top pages quarterly"],
    height=240,
)

# ---------------- Week 11: SEO ----------------
D["w11-search-intent.svg"] = table(
    "Search intent decides the page you need",
    ["Intent", "Query looks like", "Page that wins", "Business value"],
    [
        ["Informational", "how to rotate API keys", "Guide or doc", "Low now, builds trust"],
        ["Commercial investigation", "best error monitoring tools", "Comparison, listicle, alternatives page", "High"],
        ["Transactional", "[product] pricing, [product] free trial", "Pricing page, signup", "Very high"],
        ["Navigational", "[competitor] login", "Not yours to win", "None"],
    ],
    col_widths=[200, 270, 280, 190],
)
D["w11-topic-cluster.svg"] = tree(
    "Topic cluster architecture",
    "Pillar page: the complete guide to [core topic]",
    ["Subtopic guide", "Comparison page", "Integration or use case page", "Glossary term"],
    grandchildren=[["how-to articles", "templates"], ["X vs Y", "alternatives to X"], ["[product] for [use case]", "[product] plus [tool]"], ["what is [term]"]],
    height=430,
    caption="Internal links flow up to the pillar and across siblings. Search engines read this as topical authority.",
)
D["w11-seo-priorities.svg"] = stack(
    "SEO priorities for a small software company",
    ["Links and mentions: partners, PR, communities", "Content that matches intent, refreshed", "On-page basics: titles, headings, internal links, speed", "Technical foundation: crawlable, indexable, fast, no duplicate pages"],
    caption="Fix the base first. Content on an uncrawlable site is wasted. Links matter, but they cannot save weak pages.",
)

# ---------------- Week 12: paid ----------------
D["w12-cac-math.svg"] = Canvas(10, 10).render()
c = Canvas(960, 470, "Paid acquisition math you must know by heart")
rows = [
    ("Spend", "$10,000"), ("Clicks (CPC $5)", "2,000"), ("Signups (CVR 8%)", "160"), ("Paying customers (16% of signups)", "26"),
    ("CAC", "$385"), ("Monthly revenue per customer", "$60"), ("Gross margin 80%, 20 month lifetime", "LTV $960"), ("LTV:CAC", "2.5 (target 3+)"),
]
y = 70
for i, (k, v) in enumerate(rows):
    fill = ACCENT_SOFT if i < 4 else (WARM_SOFT if i < 7 else GREEN_SOFT)
    stroke = ACCENT if i < 4 else (WARM if i < 7 else GREEN)
    c.box(60, y, 520, 36, k, fill=fill, stroke=stroke, size=13, radius=6)
    c.box(600, y, 300, 36, v, fill=PAPER, stroke=stroke, size=13, radius=6)
    y += 42
c.caption("Change one input at a time and see what happens to LTV:CAC. Conversion rate and retention usually move it more than CPC.")
D["w12-cac-math.svg"] = c.render()
D["w12-channel-fit-paid.svg"] = table(
    "Which paid channel for which job",
    ["Channel", "Best for", "Signal", "Watch out"],
    [
        ["Google Search", "Capturing existing demand", "Keyword intent", "Expensive generic terms; competitors bidding on your name"],
        ["LinkedIn", "Reaching a defined B2B title", "Job title and company", "High CPC; needs strong offer"],
        ["Meta and TikTok", "Creating demand for broad products", "Interests and creative", "Weak for niche B2B; creative fatigue"],
        ["Newsletter and podcast sponsorships", "Trusted reach into a niche", "Audience fit", "Hard to attribute; ask for promo codes"],
        ["Retargeting", "Nudging warm visitors", "Site behavior", "Frequency caps; do not over-invest"],
    ],
    col_widths=[220, 250, 200, 270],
)
D["w12-paid-test-plan.svg"] = timeline(
    "A four-week paid channel test",
    ["Set up tracking", "Launch 2 to 3 ad sets", "Kill losers, scale winners", "Decide"],
    subs=["UTMs, conversion events, budget cap", "distinct audiences and hooks", "judge on signups and quality, not clicks", "scale, iterate, or stop with a written verdict"],
)

# ---------------- Week 13: email ----------------
D["w13-lifecycle-map.svg"] = flow(
    "Lifecycle email map",
    ["Welcome", "Onboarding", "Activation nudge", "Engagement", "Expansion", "Win-back"],
    subs=["set expectations, one action", "3 to 5 emails to first value", "triggered when a key step is missed",
          "newsletter, product updates", "usage-based upgrade prompts", "lapsed users, honest and short"],
    caption="Behavior-triggered emails beat scheduled blasts. Each email should have one job and one call to action.",
)
D["w13-deliverability-stack.svg"] = stack(
    "Deliverability stack",
    ["Content: plain, relevant, easy to unsubscribe", "List hygiene: double opt-in, remove bounces, sunset inactive", "Reputation: warm up domains, consistent volume", "Authentication: SPF, DKIM, DMARC on a sending subdomain"],
    caption="Gmail and Yahoo require authentication and low spam rates for bulk senders. Get the base right before you write a single campaign.",
)
D["w13-newsletter-model.svg"] = matrix(
    "What kind of newsletter should you send?",
    "Effort per issue", "Value to the reader",
    [["Curated links plus commentary", "cheap, useful, builds habit"],
     ["Original insight or data", "expensive, most shareable, builds authority"],
     ["Product update digest", "cheap, low value unless they are active users"],
     ["Long-form essays", "expensive, great for founder brand, slow to compound"]],
)

# ---------------- Week 14: social and founder-led ----------------
D["w14-founder-content-loop.svg"] = cycle(
    "Founder-led distribution loop",
    ["Do the work and notice something", "Post a specific, opinionated take", "Replies and DMs reveal what resonates", "Turn winners into long-form content", "Long-form drives signups and follows"],
    caption="The asset is your point of view, built in public. Consistency beats virality.",
)
D["w14-post-formats.svg"] = table(
    "Social post formats that reliably perform for software founders",
    ["Format", "Structure", "Why it works"],
    [
        ["Lesson from a mistake", "What we did, what broke, what we changed", "Vulnerability plus a usable lesson"],
        ["Before and after", "Screenshot or number, then the change", "Concrete, visual, credible"],
        ["Contrarian take", "Common belief, why it is wrong, what to do instead", "Triggers replies and shares"],
        ["Build in public", "Metric this week, what we tried, what is next", "Serial narrative keeps people following"],
        ["Teardown", "Analyze a known product or page", "Borrowed relevance, shows expertise"],
    ],
    col_widths=[220, 400, 320],
)
D["w14-platform-fit.svg"] = matrix(
    "Which platform for which audience",
    "Audience is consumer", "Content is short-form video",
    [["LinkedIn, X", "B2B text and screenshots; founders and operators"],
     ["Instagram, TikTok", "consumer, visual, trend-driven"],
     ["YouTube long-form, Reddit, Hacker News, Discord", "developers, technical buyers, deep dives"],
     ["YouTube Shorts, TikTok", "consumer apps, demos and hooks"]],
)

# ---------------- Week 15: community, devrel, partnerships ----------------
D["w15-community-rings.svg"] = rings(
    "Community concentric model",
    ["Core: contributors, champions, advisors", "Active: post, answer, attend, give feedback", "Members: joined, mostly read", "Audience: follow you but have not joined"],
    caption="Move people inward on purpose: name the next step for each ring and make it easy.",
)
D["w15-devrel-loop.svg"] = cycle(
    "Developer relations loop",
    ["Ship docs and samples devs actually need", "Show up where devs are: GitHub, Discord, meetups", "Collect friction and feature gaps", "Feed product and content", "Celebrate community builders"],
)
D["w15-partnership-types.svg"] = table(
    "Partnership types for a software platform",
    ["Type", "What you exchange", "Example", "Founder effort"],
    [
        ["Integration", "Product value both ways", "Listing in each other's marketplaces", "Engineering plus co-marketing"],
        ["Co-marketing", "Audience access", "Joint webinar, guest post, shared report", "Low to medium"],
        ["Referral or affiliate", "Leads for a fee", "Consultants recommend you", "Program design and tracking"],
        ["Reseller or channel", "Distribution for margin", "Agencies or MSPs sell you", "High: enablement and support"],
        ["Ecosystem or platform", "Building on a bigger platform", "App store, cloud marketplace", "Medium, ongoing"],
    ],
    col_widths=[190, 220, 300, 230],
)

# ---------------- Week 16: growth loops and PLG ----------------
D["w16-funnel-vs-loop.svg"] = Canvas(10, 10).render()
c = Canvas(1000, 460, "Funnel versus loop")
# funnel on left
stages = ["Visitors", "Signups", "Activated", "Paying"]
top_w, bot_w, x0, y = 300, 120, 60, 80
h = 70
for i, s in enumerate(stages):
    w1 = top_w - (top_w - bot_w) * i / 4
    w2 = top_w - (top_w - bot_w) * (i + 1) / 4
    cx = x0 + top_w / 2
    c.polygon([(cx - w1 / 2, y), (cx + w1 / 2, y), (cx + w2 / 2, y + h - 6), (cx - w2 / 2, y + h - 6)], fill=PANEL, stroke=LINE)
    c.text(cx, y + (h - 6) / 2, s, size=13, weight="600")
    y += h
c.text(x0 + top_w / 2, 385, "Linear: every user costs new input", size=13, color=MUTED)
# loop on right
import math as _m
cx, cy, r = 720, 230, 120
names = ["New user", "Uses product", "Creates output or invite", "Reaches others"]
pts = []
for i in range(4):
    a = -_m.pi / 2 + i * 2 * _m.pi / 4
    pts.append((cx + r * _m.cos(a), cy + r * _m.sin(a)))
for i, (px, py) in enumerate(pts):
    c.box(px - 80, py - 28, 160, 56, names[i], fill=ACCENT_SOFT, stroke=ACCENT, size=13)
for i in range(4):
    x1, y1 = pts[i]
    x2, y2 = pts[(i + 1) % 4]
    edge_arrow(c, x1, y1, 160, 56, x2, y2, 160, 56, curve=-18, color=ACCENT, width=2.5)
c.text(cx, 385, "Compounding: output of one cycle is input to the next", size=13, color=MUTED)
c.caption("Reforge's framing. Funnels describe a journey; loops describe an engine. Design for loops, measure with funnels.")
D["w16-funnel-vs-loop.svg"] = c.render()
D["w16-loop-types.svg"] = table(
    "Common growth loops for software",
    ["Loop", "How it compounds", "Real examples", "Requirement"],
    [
        ["Viral (invites)", "Users invite collaborators who become users", "Slack, Figma, Notion", "Multiplayer value"],
        ["User-generated content", "Users create public pages that rank in search", "Canva templates, Zapier integration pages, GitHub", "Public artifacts"],
        ["Paid loop", "Revenue from cohort funds the next cohort's ads", "Most DTC and mobile apps", "Fast payback"],
        ["Content loop", "Content brings readers who become customers who inspire content", "HubSpot, Ahrefs", "Editorial engine"],
        ["Embed or badge", "Product output carries a link", "Calendly, Typeform, 'Sent from' footers", "Shareable output"],
    ],
    col_widths=[190, 300, 270, 180],
)
D["w16-plg-motion.svg"] = flow(
    "Product-led growth motion",
    ["Discover", "Try without talking to anyone", "Reach first value fast", "Habit forms", "Hit a limit", "Upgrade or expand"],
    subs=["search, word of mouth, marketplace", "free tier or trial, no demo gate", "activation event within minutes",
          "returns weekly on their own", "seats, usage, features", "self-serve or sales-assist"],
    caption="PLG is not a pricing page. It is a product that markets and sells itself up to the point where a human adds value.",
)

# ---------------- Week 17: retention and activation ----------------
D["w17-retention-curves.svg"] = Canvas(10, 10).render()
c = Canvas(900, 440, "Retention curves: the shape tells you if you have product-market fit")
ox, oy = 90, 360
c.arrow(ox, oy, 840, oy, color=INK)
c.arrow(ox, oy, ox, 60, color=INK)
c.text(470, 400, "Weeks since signup", size=13, color=MUTED)
c.add(f'<g transform="translate(45,210) rotate(-90)">')
c.text(0, 0, "% of cohort still active", size=13, color=MUTED)
c.add("</g>")
def curve(fn, color, label, lx, ly):
    pts = []
    for w in range(0, 25):
        x = ox + w * 30
        yv = fn(w)
        pts.append(f"{x},{oy - yv * 2.8}")
    c.add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="3"/>')
    c.text(lx, ly, label, size=13, weight="600", color=color, anchor="start")
curve(lambda w: 100 * (0.55 + 0.45 * _m.exp(-w / 3)), GREEN, "Flattens: real retention, PMF signal", 560, 185)
curve(lambda w: 100 * (0.25 + 0.75 * _m.exp(-w / 4)), WARM, "Flattens low: works for a niche", 560, 270)
curve(lambda w: 100 * _m.exp(-w / 5), ROSE, "Never flattens: leaky bucket, do not scale", 500, 335)
D["w17-retention-curves.svg"] = c.render()
D["w17-activation-path.svg"] = flow(
    "Find and shorten the activation path",
    ["Signup", "Setup moment", "Aha moment", "Habit moment"],
    subs=["account created", "the required config: connect data, invite, install", "first real value: the report, the deploy, the message", "value repeats on a natural cadence"],
    caption="Define each moment as an event in your analytics. Then measure the time and drop-off between them, and attack the biggest gap.",
)
D["w17-churn-reasons.svg"] = table(
    "Churn reasons and the lever that fixes each",
    ["Reason", "Signal", "Lever"],
    [
        ["Never activated", "No key event in first 7 days", "Onboarding, setup help, defaults"],
        ["Wrong customer", "Churn concentrated in a segment", "ICP and messaging: stop acquiring them"],
        ["Value faded", "Usage decays before cancel", "Engagement loops, new use cases, reminders"],
        ["Champion left", "Owner change on the account", "Multi-user adoption, exec relationships"],
        ["Price or budget", "Cancel at renewal, downgrade requests", "Packaging, value metric, annual plans"],
    ],
    col_widths=[220, 340, 380],
)

# ---------------- Week 18: analytics ----------------
D["w18-metrics-tree.svg"] = tree(
    "Metrics tree for a subscription software product",
    "Net revenue growth",
    ["New customers", "Activation rate", "Retention (logo and revenue)", "Expansion", "Price and packaging"],
    grandchildren=[["Traffic by channel", "Visitor to signup", "Signup to paid"],
                   ["Setup completion", "Time to first value"],
                   ["Week 4 and month 6 retention", "Churn reasons"],
                   ["Seat growth", "Usage growth", "Upgrade rate"],
                   ["ARPA", "Discounting"]],
    height=460,
    caption="Every metric on the tree should have an owner and a definition. Pick one input metric per quarter to move.",
)
D["w18-attribution-models.svg"] = table(
    "Attribution models and what they hide",
    ["Model", "Credits", "Good for", "Blind spot"],
    [
        ["First touch", "The channel that started it", "Understanding awareness", "Ignores what closed the deal"],
        ["Last touch", "The channel just before conversion", "Optimizing bottom of funnel", "Over-credits search and retargeting"],
        ["Multi-touch", "Split across touches", "Long B2B journeys", "Still misses dark social and word of mouth"],
        ["Self-reported", "What the user says", "Cheap, catches podcasts and communities", "Memory is imperfect"],
        ["Incrementality tests", "Lift versus a holdout", "The truth about paid", "Needs volume and discipline"],
    ],
    col_widths=[170, 260, 260, 270],
)
D["w18-instrumentation.svg"] = flow(
    "Minimum analytics instrumentation",
    ["UTM on every link", "Web analytics", "Product events", "Identity join", "Revenue data", "Dashboard"],
    subs=["source, medium, campaign", "page views and referrers", "signup, setup, aha, habit, upgrade", "anonymous visitor to user to account",
          "plans, MRR, churn from billing", "one page, weekly review"],
    height=240,
)

# ---------------- Week 19: experimentation ----------------
D["w19-experiment-loop.svg"] = cycle(
    "Growth experimentation process",
    ["Pick the metric to move", "Generate ideas from data and research", "Prioritize with ICE", "Run a clean test", "Analyze and document", "Share learnings and repeat"],
)
D["w19-ice-scoring.svg"] = table(
    "ICE prioritization (score 1 to 10)",
    ["Idea", "Impact", "Confidence", "Ease", "ICE"],
    [
        ["Add social proof to signup page", "6", "8", "9", "7.7"],
        ["Rewrite onboarding emails", "7", "6", "7", "6.7"],
        ["Launch referral program", "9", "4", "3", "5.3"],
        ["New pricing page layout", "5", "5", "6", "5.3"],
    ],
    col_widths=[400, 130, 140, 130, 140],
    caption="ICE is a conversation tool, not a formula. Its job is to surface disagreement about impact and confidence.",
)
D["w19-ab-test-checklist.svg"] = stack(
    "Before you trust an A/B test",
    ["Decide and document, including the null result", "Run the full pre-set duration, ignore early peeks", "Sample size computed in advance for the minimum effect you care about", "One clear hypothesis and one primary metric", "Random assignment that actually works, verified with an A/A test"],
    bottom_up=False,
)

# ---------------- Week 20: pricing ----------------
D["w20-value-metric.svg"] = table(
    "Choosing a value metric",
    ["Value metric", "Examples", "Pros", "Cons"],
    [
        ["Per seat", "Slack, Figma, Linear", "Simple, predictable, grows with adoption", "Discourages adding users; seat sharing"],
        ["Usage", "Twilio, AWS, Stripe", "Aligns with value, low entry barrier", "Unpredictable bills, revenue lags"],
        ["Tiered features", "Most SaaS Good-Better-Best", "Easy to explain, upsell path", "Fence design is hard"],
        ["Outcome-based", "Some fintech and ad tools", "Perfect alignment", "Attribution disputes, hard to forecast"],
    ],
    col_widths=[170, 230, 290, 270],
)
D["w20-pricing-research.svg"] = Canvas(10, 10).render()
c = Canvas(900, 520, "Van Westendorp price sensitivity (simplified)")
ox, oy = 90, 380
c.arrow(ox, oy, 840, oy, color=INK)
c.arrow(ox, oy, ox, 60, color=INK)
c.text(470, 420, "Price", size=13, color=MUTED)
c.add(f'<g transform="translate(45,220) rotate(-90)">')
c.text(0, 0, "% of respondents", size=13, color=MUTED)
c.add("</g>")
def cv(fn, color, label, lx, ly):
    pts = [f"{ox + i * 7.5},{oy - fn(i / 100) * 300}" for i in range(0, 101)]
    c.add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="3"/>')
    c.line(lx, ly, lx + 26, ly, color=color, width=4)
    c.text(lx + 34, ly, label, size=12, weight="600", color=color, anchor="start")
sig = lambda x, k, m: 1 / (1 + _m.exp(-k * (x - m)))
cv(lambda x: 1 - sig(x, 12, 0.35), GREEN, "Too cheap (quality doubt)", 90, 470)
cv(lambda x: 1 - sig(x, 12, 0.55), ACCENT, "Bargain", 330, 470)
cv(lambda x: sig(x, 12, 0.5), WARM, "Getting expensive", 470, 470)
cv(lambda x: sig(x, 12, 0.7), ROSE, "Too expensive", 690, 470)
c.line(ox + 0.45 * 750, oy, ox + 0.45 * 750, 90, color=LINE, dashed=True)
c.line(ox + 0.62 * 750, oy, ox + 0.62 * 750, 90, color=LINE, dashed=True)
c.text(ox + 0.535 * 750, 300, "Acceptable range", size=12, color=MUTED)
D["w20-pricing-research.svg"] = c.render()
D["w20-packaging-tiers.svg"] = Canvas(10, 10).render()
c = Canvas(960, 480, "Good-Better-Best packaging for a software platform")
tiers = [("Free or Starter", "individuals and evaluation", ["core feature", "usage cap", "community support"], PANEL, LINE),
         ("Team (anchor)", "the plan most should buy", ["everything in Starter", "collaboration", "integrations", "email support"], ACCENT_SOFT, ACCENT),
         ("Enterprise", "buyers with procurement", ["SSO and audit logs", "SLA and support", "custom contracts"], WARM_SOFT, WARM)]
for i, (name, who, feats, fill, stroke) in enumerate(tiers):
    x = 60 + i * 300
    c.box(x, 70, 260, 340, "", fill=fill, stroke=stroke)
    c.text(x + 130, 100, name, size=17, weight="700")
    c.text(x + 130, 128, who, size=12, color=MUTED)
    yy = 175
    for f in feats:
        c.text(x + 30, yy, "• " + f, size=13, anchor="start")
        yy += 30
c.caption("Fence features by who needs them (SSO for enterprises), not by what is hardest to build. Make the middle tier the obvious choice.")
D["w20-packaging-tiers.svg"] = c.render()

# ---------------- Week 21: GTM ----------------
D["w21-gtm-motions.svg"] = table(
    "Go-to-market motions",
    ["Motion", "Typical ACV", "Buyer", "Primary channels", "Team you need"],
    [
        ["Self-serve", "Under $5k", "Individual or small team", "SEO, content, product loops, marketplaces", "Product, growth, support"],
        ["PLG plus sales assist", "$5k to $50k", "Team lead with a budget", "PLG loops plus inbound plus targeted outbound", "Growth plus a few sales reps"],
        ["Sales-led (mid-market)", "$25k to $250k", "Director or VP", "Outbound, events, partners, content", "AEs, SDRs, SEs, marketing"],
        ["Enterprise", "$250k plus", "C-level and procurement", "Executive relationships, partners, ABM", "Field sales, solutions, customer success"],
    ],
    col_widths=[180, 130, 190, 260, 180],
)
D["w21-launch-timeline.svg"] = timeline(
    "Launch timeline",
    ["T minus 6 weeks: positioning and assets", "T minus 3: beta customers and quotes", "T minus 1: press, partners, community warmed up", "Launch day: everywhere at once", "T plus 2 weeks: follow-up wave"],
    subs=["messaging, page, demo video", "3 quotable customers", "embargoed briefings, partner posts", "HN, PH, email, social, partners", "lessons, integrations, second story"],
    height=320,
)
D["w21-sales-marketing-handoff.svg"] = flow(
    "Marketing to sales handoff",
    ["Lead", "MQL", "SQL", "Opportunity", "Closed won", "Expansion"],
    subs=["any known contact", "fits ICP and showed intent", "sales accepted after a conversation", "qualified, budget and timeline",
          "signed", "back to marketing and CS"],
    caption="Agree on definitions in writing. Most sales and marketing conflict is two teams using the same word for different things.",
)

# ---------------- Week 22: plan and cadence ----------------
D["w22-planning-cascade.svg"] = stack(
    "Planning cascade",
    ["Weekly: metrics review, experiment decisions, content shipped", "Monthly: channel performance, budget reallocation", "Quarterly: 3 to 5 bets, OKRs, positioning check", "Annual: revenue target, ICP, primary channels, brand direction"],
    caption="Plans live at the top. Learning happens at the bottom. Review upward on a fixed cadence and do not reopen the annual plan weekly.",
)
D["w22-marketing-budget.svg"] = Canvas(10, 10).render()
c = Canvas(900, 420, "Example budget split for an early-stage software company")
segs = [("Content and SEO", 30, ACCENT), ("Paid acquisition tests", 20, WARM), ("Tools and data", 15, GREEN), ("Events and community", 15, "#7c3aed"), ("Brand and design", 10, "#0891b2"), ("Reserve for what works", 10, ROSE)]
x = 60
for name, pct, color in segs:
    w = pct * 7.8
    c.add(f'<rect x="{x}" y="150" width="{w}" height="70" fill="{color}" opacity="0.85" stroke="{PAPER}" stroke-width="2"/>')
    c.text(x + w / 2, 185, f"{pct}%", size=14, weight="700", color=PAPER)
    c.text(x + w / 2, 250 if segs.index((name, pct, color)) % 2 == 0 else 285, name, size=12, color=INK, max_chars=16)
    x += w
c.caption("Illustrative, not a rule. The right split follows your channel tests: money moves toward what shows payback.")
D["w22-marketing-budget.svg"] = c.render()
D["w22-weekly-dashboard.svg"] = table(
    "One-page weekly marketing dashboard",
    ["Row", "Metric", "This week", "Trend", "Owner"],
    [
        ["Reach", "Visitors by channel", "", "", ""],
        ["Capture", "Signups and signup rate", "", "", ""],
        ["Activate", "% reaching first value in 7 days", "", "", ""],
        ["Revenue", "New MRR, expansion, churn", "", "", ""],
        ["Pipeline", "MQL to SQL to opportunity", "", "", ""],
        ["Learning", "Experiments concluded, content shipped", "", "", ""],
    ],
    col_widths=[150, 350, 150, 150, 140],
)

# ---------------- Week 23: stack, automation, team ----------------
D["w23-marketing-stack.svg"] = tree(
    "A lean marketing stack",
    "Data warehouse or a spreadsheet as the source of truth",
    ["Website and CMS", "Analytics", "Email and lifecycle", "CRM", "Content and social"],
    grandchildren=[["Framework site plus docs", "Landing page tool"], ["Web analytics", "Product analytics", "UTM discipline"], ["ESP with triggers", "Transactional email"], ["Pipeline and accounts", "Enrichment"], ["Scheduler", "Design tool", "AI drafting"]],
    height=440,
)
D["w23-ai-in-marketing.svg"] = matrix(
    "Where AI helps and where it hurts in marketing",
    "Task is judgment-heavy", "Task is high-volume",
    [["Automate", "tagging, summaries, first drafts, variants, data cleanup"],
     ["Assist, then review", "landing page drafts, ad variants, research synthesis"],
     ["Use sparingly", "one-off scripts, transcript search"],
     ["Keep human", "positioning, brand voice, customer conversations, pricing"]],
)
D["w23-first-hire.svg"] = table(
    "Who to hire first",
    ["Situation", "Hire", "Do not hire", "Why"],
    [
        ["No positioning or messaging yet", "Nobody; do it yourself", "A demand-gen manager", "They will scale a message that does not exist"],
        ["Self-serve, content-driven", "Content lead or growth marketer who writes", "Brand agency", "Output matters more than polish"],
        ["Sales-led, mid-market", "Product marketer or demand-gen lead", "Junior social media manager", "Sales needs enablement and pipeline"],
        ["Proven channel needs scaling", "Specialist in that channel", "Generalist", "You know what works; go deep"],
    ],
    col_widths=[230, 270, 200, 240],
)

# ---------------- Week 24: capstone ----------------
D["w24-marketing-system.svg"] = cycle(
    "The repeatable marketing system",
    ["Research: talk to 5 customers a month", "Position: revisit quarterly", "Message: update site and sales assets", "Distribute: 1 to 2 focus channels plus loops", "Measure: one dashboard, weekly", "Learn: experiments and retros"],
    r=200, width=820, height=600,
    caption="The system is the deliverable. Tactics change every year; this loop does not.",
)
D["w24-90-day-plan.svg"] = timeline(
    "Your first 90 days after this program",
    ["Days 1 to 30: fix foundations", "Days 31 to 60: run channel tests", "Days 61 to 90: double down and systematize"],
    subs=["positioning, site, analytics, lifecycle emails", "2 to 3 paid or organic tests with written verdicts", "scale the winner, document the playbook, set the cadence"],
    height=300,
)
D["w24-maturity-model.svg"] = table(
    "Marketing maturity model: where are you?",
    ["Level", "Positioning", "Channels", "Measurement", "Cadence"],
    [
        ["1 Ad hoc", "Founder's head", "Whatever came up", "Vanity metrics", "None"],
        ["2 Defined", "Written, on the site", "One channel tested", "Signups and revenue tracked", "Monthly check"],
        ["3 Repeatable", "Validated with customers", "One channel scaling plus loops", "Metrics tree and dashboard", "Weekly review"],
        ["4 Compounding", "Owns a category frame", "Multiple channels plus brand", "Attribution plus incrementality", "Quarterly planning, weekly ops"],
    ],
    col_widths=[150, 220, 220, 200, 150],
)

for name, svg in D.items():
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)
print(f"wrote {len(D)} diagrams to {os.path.abspath(OUT)}")
