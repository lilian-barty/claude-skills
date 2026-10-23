# English part of /ecrire-sans-tics-ia: audit and rewrite of English text

Partie anglaise du skill. Elle est écrite en anglais parce qu'elle s'applique à des textes anglais, au plus près des mots à chercher.

Its 21 categories and its 43-row replacement table are adapted from [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) by Conor Bronsdon (commit `db1b74219a`, March 2026), MIT License, Copyright (c) 2026 Conor Bronsdon. The rules where this skill is stricter than the original are marked **Override**.

## When to use this part

- An English text must be written or proofread so it does not read as AI-generated.
- Asked to "remove AI-isms", "clean up AI writing", "make this sound less like AI", "audit writing for AI tells".
- After drafting English content with AI and before publishing.
- When auditing documentation, blog posts, marketing copy, slides, handouts or internal communications in English.
- Any HTML or structured file (English or French): use the grep-first method below.

## What it detects

**21 pattern categories:** formatting issues (em dashes, bold overuse, emoji headers, bullet-heavy sections), sentence structure problems (hedging, hollow intensifiers, rule of three), word/phrase replacements (43 entries like leverage to use, utilize to use, robust to reliable), template phrases, transition phrases, structural issues, significance inflation, copula avoidance, synonym cycling, vague attributions, filler phrases, generic conclusions, chatbot artifacts, notability name-dropping, superficial -ing analyses, promotional language, formulaic challenges, false ranges, inline-header lists, title case headings, and cutoff disclaimers.

## Rules from the French part that apply in English too

They override the original source wherever the two conflict.

- **No em dash at all** (`—`), and no double hyphen (`--`) standing in for one. The source allows one per 1,000 words; this skill allows none. Use a comma, a colon, parentheses or two sentences.
- **One form of quotes and apostrophes throughout**: straight (`"` and `'`) with the keyboard profile of the French part, otherwise whatever the text already uses. Inside an HTML attribute, write `&quot;`. When auditing someone else's text, curly quotes, prose em dashes, an Oxford comma or flawless typography are a house-style fix, never evidence that a machine wrote it: Word, Google Docs, macOS and iOS curl quotes by default. Report them as a style item after the AI-ism list, not in it.
- **No opposition for show** (structure 14 of the French part): "It's not X, it's Y", "X, not Y", "Not X: Y", "We don't X, we Y", "X instead of Y" when Y only exists to be rejected. The source tolerates one per piece; this skill tolerates none. A negation that carries information stays.
- **No echo break, no parallel pair, no elliptic reversal, no chopped nuance** (structures 9 to 12 of the French part). They are just as visible in English: "Speed matters. Accuracy matters more." becomes one linked sentence.
- **No label-colon opener** (structure 15 of the French part): a noun phrase plus a colon standing in for a verb reads like a slide ("The result: ...", "Bottom line: ...", "The catch: ...", "My role: ...", "Spoiler: ...", "The kicker: ...", and the question form "The secret? ..."). Put the verb back ("My role was to...", "The group left with..."). A colon after a full clause that introduces a list stays.
- **No comma tag** (structure 17 of the French part): a short chunk hung after a comma to sound crisp, instead of being built into the sentence. Two forms:
  - noun plus bare past participle: "plus its five questions, answered", "the same case, framed", "every step, explained", "your data, cleaned";
  - a trailing precision chunk with counting cadence: "We rework one prompt on one case, in three passes", "One room, one tool, one hour".
  Fix: write the full clause with a verb ("and the answers to its five questions", "we frame the same case", "We rework one prompt on a single case and go over it three times"). Test: if the chunk after the comma has no conjugated verb and could be a slide caption, rewrite it. A normal appositive that names something ("Marie, our trainer, ...") stays.
- **Perplexity and burstiness** still drive the rewrite: a text with zero banned words can still read as AI if every sentence has the same length and every word is the most predictable one.
- **Do not over-correct**: fragments everywhere and gratuitous opinions are the signature of low-end humanizers.
- **Preserve meaning and facts**: no number, name, claim or nuance changes during a proofread.

## Second-generation tells (check after the 21 categories)
Copy that has already been cleaned can still read as generated. Check for: wisdom-shaped sentences nobody would disagree with ("Speed is a feature."), replace them with the fact they gesture at or cut them; self-narration ("Here's why this matters.", "The takeaway is simple."), delete it; tidy closers, a balanced quotable last line that could end any page, end on a number, a name, the offer or the call to action instead; perfect balance, every section the same length, let the strongest section run long and the weakest shrink. Scan the last line of every section and compare section lengths.

## The 21 categories in detail

### 1. Formatting
- **Em dashes (—)**: replace with commas, periods, parentheses, or rewrite as two sentences. Target: zero (**Override**: zero is a hard rule, not a target). This applies to headings and section titles too, not just body prose.
- **Bold overuse**: strip bold from most phrases. One bolded phrase per major section at most, or none. If something is important enough to bold, restructure the sentence to lead with it instead.
- **Emoji in headers**: remove entirely. No `## 🚀 What This Means`. Exception: social posts may use one or two emoji sparingly, at the end of a line, never mid-sentence. (The French part's exception for functional emoji in scannable documents also applies.)
- **Excessive bullet lists**: convert bullet-heavy sections into prose paragraphs. Bullets only for genuinely list-like content (feature comparisons, step-by-step instructions, API parameters).

### 2. Sentence structure
- **"It's not X, it's Y" / "This isn't about X, it's about Y"**: rewrite as a direct positive statement. The source allows one per piece if it serves the argument; **Override**: none.
- **Hollow intensifiers**: cut `genuine`, `real` (as in "a real improvement"), `truly`, `quite frankly`, `to be honest`, `let's be clear`, `it's worth noting that`. Just state the fact.
- **Hedging**: cut `perhaps`, `could potentially`, `it's important to note that`, `to be clear`. Make the point directly.
- **Missing bridge sentences**: each paragraph should connect to the last. If paragraphs could be rearranged without the reader noticing, add connective tissue.
- **Compulsive rule of three**: vary groupings. Use two items, four items, or a full sentence instead of triads. Max one "adjective, adjective, and adjective" pattern per piece.

### 3. Words and phrases to replace (43 entries)

| Replace | With |
|---|---|
| delve / delve into | explore, dig into, look at |
| landscape (metaphor) | field, space, industry, world |
| tapestry | (describe the actual complexity) |
| realm | area, field, domain |
| paradigm | model, approach, framework |
| embark | start, begin |
| beacon | (rewrite entirely) |
| testament to | shows, proves, demonstrates |
| robust | strong, reliable, solid |
| comprehensive | thorough, complete, full |
| cutting-edge | latest, newest, advanced |
| leverage (verb) | use |
| harness | use, take advantage of |
| pivotal | important, key, critical |
| underscores | highlights, shows |
| meticulous / meticulously | careful, detailed, precise |
| navigate / navigating | work through, handle, deal with |
| foster | encourage, support, build |
| elevate | improve, raise, strengthen |
| seamless / seamlessly | smooth, easy, without friction |
| unleash | release, enable, unlock |
| streamline | simplify, speed up |
| empower | enable, let, allow |
| game-changer | describe what specifically changed and why it matters |
| utilize | use |
| commence | start, begin |
| ascertain | find out, determine, learn |
| endeavor | effort, attempt, try |
| in order to | to |
| due to the fact that | because |
| serves as | is |
| features (verb) | has, includes |
| boasts | has |
| presents (inflated) | is, shows, gives |
| watershed moment | turning point, shift (or describe what changed) |
| marking a pivotal moment | (state what happened) |
| the future looks bright | (cut: say something specific or nothing) |
| only time will tell | (cut: say something specific or nothing) |
| nestled | is located, sits, is in |
| vibrant | (describe what makes it active, or cut) |
| thriving | growing, active (or cite a number) |
| despite challenges... continues to thrive | (name the challenge and the response, or cut) |
| showcasing | showing, demonstrating (or cut the clause) |

Like the French list, this table is illustrative: kill the pattern, not only the word. Replacing "pivotal" with "crucial" keeps the problem. The best choice depends on context; some flagged words are fine where they carry their literal meaning.

### 4. Template phrases
These slot-fill constructions signal that a sentence was generated, not written. If a phrase has a blank where a noun or adjective could go and still sound the same, it is too generic.
- "a [adjective] step towards [adjective] AI infrastructure": describe the specific capability, benchmark, or outcome.
- "a [adjective] step forward for [noun]": same rule, say what actually changed.

### 5. Transition phrases to remove or rewrite
- "Moreover" / "Furthermore" / "Additionally": restructure so the connection is obvious, or use "and", "also", "on top of that".
- "In today's [X]" / "In an era where": cut or state specific context.
- "It's worth noting that" / "Notably": just state the fact.
- "In conclusion" / "To summarize": your conclusion should be obvious.
- "When it comes to": just talk about the thing directly.
- "At the end of the day": cut.
- "That said" / "That being said": cut or use "but", "yet" or "however". Don't overuse any one of them.

### 6. Structural issues
- **Uniform paragraph length**: vary deliberately. Include some 1 to 2 sentence paragraphs and some longer ones. If every paragraph is roughly the same size, fix it.
- **Formulaic openings**: if the piece opens with broad context before getting to the point ("In the rapidly evolving world of..."), rewrite to lead with the news or the insight. Context can come second.
- **Suspiciously clean grammar**: don't sand away all personality. Deliberate fragments, sentences starting with "And" or "But", comma splices for effect: if the natural voice uses them, keep them (within the over-correction guardrail).

### 7. Significance inflation
- Phrases like "marking a pivotal moment in the evolution of..." or "a watershed moment for the industry" inflate routine events into history-making ones. State what happened and let the reader judge significance.
- If the sentence still works after you delete the inflation clause, delete it.

### 8. Copula avoidance
- AI text avoids "is" and "has" by substituting fancier verbs: "serves as", "features", "boasts", "presents", "represents". These sound like a press release.
- Default to "is" or "has" unless a more specific verb adds meaning.

### 9. Synonym cycling
- AI rotates synonyms to avoid repeating a word: "developers... engineers... practitioners... builders" in the same paragraph. Human writers repeat the clearest word.
- If the same noun or verb appears three times in a paragraph and it is the right word, keep all three. Forced variation reads as thesaurus abuse.

### 10. Vague attributions
- "Experts believe", "Studies show", "Research suggests", "Industry leaders agree", without naming the expert, study, or leader. Either cite a specific source or drop the attribution and state the claim directly.

### 11. Filler phrases
Strip mechanical padding that adds words without meaning:
- "In order to": "To"
- "Due to the fact that": "Because"
- "It is important to note that": (just state it)
- "At the end of the day": (cut)
- "In terms of": (rewrite)
- "The reality is that": (cut or just state the claim)

### 12. Generic conclusions
- "The future looks bright", "Only time will tell", "One thing is certain", "As we move forward": filler disguised as conclusions. Cut them. If the piece needs a closing thought, make it specific to the argument.

### 13. Chatbot artifacts
- "I hope this helps!", "Certainly!", "Absolutely!", "Great question!", "Feel free to reach out", "Let me know if you need anything else": conversational tics from chat interfaces, not writing. Remove entirely.
- Also watch for "In this article, we will explore..." or "Let's dive in!": AI meta-narration. Cut or rewrite with a direct opening.

### 14. Notability name-dropping
- AI text piles on prestigious citations to manufacture credibility: "cited in The New York Times, BBC, Financial Times, and The Hindu". If a source matters, use it with context: "In a 2024 NYT interview, she argued...". One specific reference beats four name-drops.

### 15. Superficial -ing analyses
- Strings of present participles used as pseudo-analysis: "symbolizing the region's commitment to progress, reflecting decades of investment, and showcasing a new era of collaboration". These say nothing. Replace with specific facts or cut entirely.

### 16. Promotional language
- AI defaults to tourism-brochure prose: "nestled within the breathtaking foothills", "a vibrant hub of innovation", "a thriving ecosystem". Replace with plain description: "is a town in the Gonder region", "has 12 startups". If you wouldn't say it in conversation, cut it.

### 17. Formulaic challenges
- "Despite challenges, [subject] continues to thrive" or "While facing headwinds, the organization remains resilient". A non-statement. Name the actual challenge and the actual response, or cut the sentence.

### 18. False ranges
- AI creates false breadth by pairing unrelated extremes: "from the Big Bang to dark matter", "from ancient civilizations to modern startups". These sound sweeping but say nothing. List the actual topics or pick the one that matters.

### 19. Inline-header lists
- Bullet lists where each item starts with a bold header that repeats itself: "**Performance:** Performance improved by...". Strip the bold header and write the point directly. If the list items need headers, they should probably be paragraphs.

### 20. Title case headings
- AI over-capitalizes headings: "Strategic Negotiations And Key Partnerships" instead of "Strategic negotiations and key partnerships". Use sentence case for subheadings. Title case only for the piece's main title, if at all.

### 21. Cutoff disclaimers
- "While specific details are limited based on available information", "As of my last update", "I don't have access to real-time data". Model limitations leaking into prose. Either find the information or remove the hedge. Never publish a sentence that admits the writer didn't look something up.

## Example

**Prompt:**
```
Audit this for AI writing patterns:

"In today's rapidly evolving AI landscape, developers are embarking on a pivotal journey to leverage cutting-edge tools that streamline their workflows. Moreover, these robust solutions serve as a testament to the industry's commitment to fostering seamless experiences."
```

**Output:** four sections.
1. **Issues found**: every AI-ism quoted (landscape, embarking, pivotal, leverage, cutting-edge, streamline, robust, serves as, testament to, fostering, seamless, Moreover, In today's rapidly evolving...)
2. **Rewritten version**: "Developers are starting to use newer AI tools to simplify their work. These tools are reliable, and they're making development less painful."
3. **What changed**: summary of edits
4. **Second-pass audit**: re-reads the rewrite to catch any surviving tells

## Output format

When asked for an audit and rewrite, return four sections:

1. **Issues found**: a list of every AI-ism identified, with the offending text quoted and its category. Ground every finding: quote the exact text and name its category. A word that appears only as a suggested replacement in the right column of the table is never a finding. A single soft word used once in its literal sense ("robust" for a structure that bears weight) is a judgment call: mention it after the list, not in it. Say whether the audit ran a grep or a script, or was done by reading only.
2. **Rewritten version**: the full rewritten content. Preserve the original structure, intent and all specific technical details. Only change what the guidelines require.
3. **What changed**: a brief summary of the major edits. Not every word, just the meaningful changes.
4. **Second-pass audit**: re-read the rewrite. Identify any remaining tells that survived the first pass (recycled transitions, lingering inflation, copula avoidance, filler phrases, anything from the 21 categories). Fix them, return the corrected text inline, and note what changed in this pass. If the rewrite is clean, say so.

When asked for an audit only (the user wants to validate before anything is changed), stop after section 1 and give each issue its proposed fix, in a before / after table: passage, category, proposed correction. Apply nothing until the user agrees.

## Methodology for HTML and structured files

When auditing prose embedded in HTML, markdown, or any structured file format, **always start with a grep before doing the literary analysis**. A continuous read of a 500+ line file will miss patterns buried in late sections.

**Step 1: grep exhaustively first.**
```bash
grep -n " — " file.html          # All em dashes
grep -n "\bvraiment\b\|seamless\|robust\|leverage\|streamline" file.html
```

**Step 2: triage each occurrence.**
- **Functional** (keep): label separators (`Phase 1 — Détail`), title tags, quoted speech. **Override**: in visible text, even a label separator is better as a colon or a middle dot in a metadata line.
- **Rhetorical** (fix): `X — twist/kicker`, `X — mais Y`, `X — et vous le savez`, definition dashes (`outbound — aller chercher`).

**Step 3: fix in one pass**, starting from the bottom of the file to preserve line numbers.

**Why this matters:** literary analysis on HTML misses patterns for two reasons: (1) tags and CSS between prose dilute attention across 500+ lines; (2) em dashes in labels look identical to em dashes in body text when reading sequentially. The grep finds every instance; the triage separates structural from rhetorical. Skip the grep and you'll catch 60% of the problems.

**Large files** (embedded base64 images, long scripts): never read them whole. Extract the visible strings with a script (parse the data arrays, the template strings, the SVG `<text>` labels), number them, audit the numbered list, and count entries in and out.

## Two-pass rewrite (mandatory before returning any rewrite)

One cleaning pass always leaves tells behind. After producing a rewrite, audit your own output before showing it:

1. Produce the draft rewrite.
2. Ask, in writing: "What still makes this text obviously AI-generated?" Answer in three bullets maximum, quoting the surviving tells.
3. Revise those exact spots.
4. Return the final version only, followed by a short list of what changed.

Never present the draft as final. The second pass is where sentence rhythm gets fixed, and rhythm is what a reader notices first.

### Optional: voice calibration

When the user provides a sample of their own writing, study it before rewriting: how long their sentences run, which words they reach for, how they open a paragraph, how they punctuate and move from one idea to the next. Replace each AI pattern with one taken from the sample, not with your own habits. Someone who writes "stuff" should not get "elements" back. Without a sample, keep the plain, varied, opinionated default.

The two-pass rewrite and this calibration follow the approach of [humanizer](https://github.com/blader/humanizer) (MIT License).

## Tone calibration

The goal is writing that sounds like a person wrote it. Direct. Specific. The writing should demonstrate confidence, not assert it.

If the original writing is already strong, say so and make only the necessary cuts. Don't over-edit for the sake of it. For a non-native international audience (students, mixed teams), prefer short common words and one idea per sentence: plain English is not the same as flat English.

## Self-check before returning an English text

1. Zero em dash, zero double hyphen used as a dash.
2. One form of quotes and apostrophes throughout (straight ones with the keyboard profile).
3. No entry of the 43-row table left where it carries the AI meaning, and no synonym that keeps the same emphasis.
4. No "It's not X, it's Y" or other opposition for show; no echo break or parallel pair; no comma tag ("the same case, framed", "one prompt on one case, in three passes").
5. No chatbot artifact, cutoff disclaimer, vague attribution or generic conclusion.
6. Sentence lengths vary; paragraphs are not all the same size.
7. Headings in sentence case.
8. Second pass done, as described above.

Points 1 to 5 must be at zero occurrences, otherwise rewrite before returning. Points 6 to 8 are judged, not counted.

## Limitations

- Does not detect AI-generated code, only prose.
- Pattern matching is guideline-based, not absolute: some flagged words are fine in context.
- The replacement table suggests alternatives but the best choice depends on context.
- Cannot verify factual claims or find real citations to replace vague attributions.
- On HTML and structured files: always grep first, never rely on sequential reading alone.

The COMPLETENESS module at the end of `SKILL.md` ("Module EXHAUSTIVITÉ") applies to this part as well.
