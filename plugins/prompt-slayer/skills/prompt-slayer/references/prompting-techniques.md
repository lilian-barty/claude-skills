# Prompting techniques: why the modules work

Reference for Prompt Slayer. It explains what each module A to H does and which technique to add when a prompt fails one of its tests. It changes neither the answer format nor the golden rule: we build the prompt, we don't do the work.

## 1. Examples rather than rules (few-shot)

A model imitates better than it obeys. Two to five input and output pairs show the expected behaviour more reliably than a paragraph of instructions.

Use it for:
- an output that must keep exactly the same shape (classification, extraction, JSON);
- a level of detail or a tone that is hard to describe;
- an edge case you want handled in a specific way.

How many depends on the task. Two examples are often enough to fix a format; a nuanced judgment needs four or five. Every example costs tokens on every call, which adds up in an automation that runs a thousand times a day.

Example, sorting an agency's incoming emails:

```
Put each email in exactly one category: quote, complaint, application, other.
Reply with a JSON object.

Email: "Hi, could you send me a price for redoing our company website?"
Answer: {"category": "quote", "urgency": "normal"}

Email: "Invoice #2041 has been wrong for 3 weeks and nobody answers."
Answer: {"category": "complaint", "urgency": "high"}

Email: "Please find my resume attached for the project manager role."
Answer: {"category": "application", "urgency": "low"}

Email: {{ email }}
Answer:
```

Common mistakes:
- examples far from the real task: the model copies their shape and misses the intent;
- examples that are all alike: include at least one edge case (here, the irritated complaint);
- so many examples that the model loses sight of the original instruction.

In Prompt Slayer, this is the "few-shot" variant. For Claude, put the examples in an `<examples>` tag.

## 2. Reasoning before concluding

Asking for the reasoning steps before the answer helps on tasks where one wrong intermediate step spoils everything after it: calculations, reconciliations, diagnoses, decisions you want to be able to audit.

Two ways to do it:
- the short instruction ("think step by step before answering");
- imposed steps, which are more reliable because they say what to check.

Example, matching an invoice against a purchase order:

```
Say whether this invoice can be paid.

Check in this order:
1. Is the supplier the same on both documents?
2. Does every invoiced line appear on the purchase order?
3. Are quantities and unit prices identical?
4. Does the invoice total equal the sum of its lines?
Then conclude with "pay" or "hold", with the reason in one sentence.

Purchase order: {{ order }}
Invoice: {{ invoice }}
```

Adapt to the target:
- so-called reasoning models already think internally. Imposing the steps (module D) still helps; demanding that they display all their reasoning helps far less and makes the output longer;
- in an automation, reasoning must never pollute the output. Ask for it in a dedicated JSON field (`"checks"`) or not at all.

## 3. Improving in versions

A good prompt is rarely right the first time. Start simple, measure on the same inputs, tighten.

Example, meeting minutes:

```
Version 1: "Write the minutes of this meeting."
What comes out: anywhere from 5 to 40 lines, with the decisions buried in the narrative.

Version 2: "List the decisions made, then the actions with their owner."
What comes out: a stable structure, but deadlines get invented for actions that had none.

Version 3: the same instruction, plus "if no deadline was given, write 'not set'".
What comes out: stable, faithful, and no more invented dates.
```

Rules that save time:
- one change per version, otherwise you can't tell which one worked;
- the same inputs for every version, edge cases included (that is what the three-case test plan is for);
- when the stakes justify it, two variants compared on the same inputs;
- in production, monitoring over time: a change in the underlying model sometimes breaks a prompt that used to work.

In a tool that does the work itself (Claude Code, an agent), you can end the prompt with a review loop: 2 or 3 reviewers, each assigned one angle (structure, substance, fit with the request), critique the deliverable against the original request; the agent fixes it and resubmits, 5 rounds at most. Every round costs time and tokens, and the gain has not been measured here: keep it for deliverables that are worth it.

## 4. Add complexity only when a test calls for it

Four levels, to climb only when the level below fails:

1. The instruction alone: "Write the minutes of this meeting."
2. Constraints: "10 lines at most, decisions first."
3. A method: "Find the decisions, then the actions and their owners, then write."
4. Examples: one or two model minutes.

Mapping to the modules: level 1 is module B, level 2 modules E and F, level 3 module D, level 4 examples in module C or the few-shot variant. FAST mode stops at level 1 or 2; PRO mode climbs as high as the criteria require.

## 5. The order of blocks

The order that gives the most stable outputs:

```
Standing context -> instruction -> examples -> data -> output format
```

Two consequences:
- long data (a document, a transcript, an export) goes after the instructions and is clearly delimited (tags, blocks, quotes), otherwise the model takes a sentence from the data for an instruction;
- when the input is long, repeat the output format at the very end: it is the last thing the model reads.

## 6. Templates

A reusable prompt is a fixed structure, variables and, when needed, passages that only appear in some cases. You stop rewriting, and related tasks stay consistent with one another.

Example, replying to a customer review, in an n8n node:

```
Write a reply to this review posted on {{ $json.platform }}.
Rating: {{ $json.rating }} out of 5.
Review: """{{ $json.text }}"""

If the rating is 3 or lower, acknowledge the specific problem mentioned and offer a direct contact.
If the rating is 4 or 5, thank the reviewer and pick up one detail from the review.
80 words at most, signed "{{ $json.signature }}".
```

In Prompt Slayer, the `[UPPERCASE]` variables of the client deliverable play this role. In n8n or Make they become expressions (`{{ $json.field }}` in n8n, field mapping in Make): document which ones can arrive empty, and what the prompt should do then.

## 7. The system prompt

The system prompt holds what does not change from one exchange to the next: role, level of expertise, output format, safety rules. User messages carry the variable content.

Example, an internal HR assistant:

```
You answer employees' questions about leave and absences, based on the policy provided between <policy> tags.

Rules:
- Cite the section of the policy you rely on.
- If the policy does not answer, say so and point to the HR team; never invent a rule.
- Never give information about another employee.
- If the question is not about leave or absences, say that you only cover that topic.

Format: the answer in 3 sentences at most, then "Section: ...".
```

For a persistent system prompt (custom GPT, agent), always plan, on top of the rules in the "Adapting to the target tool" section of SKILL.md, what it does when a request falls outside its scope and what it does when information is missing.

## 8. Planning for failure in the prompt

A solid prompt says what to do when things go wrong:
- a fallback instruction ("if the email has no order number, return null");
- a confidence level on uncertain answers;
- several interpretations when the request is ambiguous, in a chat only: in an automation, apply the default;
- an explicit way to report what is missing, rather than inventing it.

This is the core of the SAFE and AUTOMATION modules.

## 9. Diagnosing an agent or a GPT that drifts

When the user brings an existing prompt that misbehaves, look in this order:

| Symptom | Likely cause | Remedy |
|---|---|---|
| Output whose shape varies | Format described, never shown | Examples (section 1) and format repeated at the end (section 5) |
| Shallow answer to a complex problem | No method imposed | Checking steps (section 2) |
| Invented facts or sources | No rule for uncertainty | SAFE module and fallback instructions (section 8) |
| Data taken for instructions | Data not delimited | Tags or blocks, order of blocks (section 5) |
| Drifts out of its role during the exchange | No out-of-scope behaviour | Section 7 |
| Breaks the workflow downstream | Free text instead of JSON, questions asked | AUTOMATION module |
| Used to work, doesn't anymore | Model or inputs have changed | Replay the test plan, change one thing at a time (section 3) |

The deliverable is still a corrected prompt, never the execution of the task.

## 10. Habits that pay off

1. Write precisely: a vague prompt gives inconsistent outputs.
2. Show: an example beats a description.
3. Test on varied, representative inputs, not only on the ideal case.
4. Iterate often, in small touches: changing one word is sometimes enough.
5. In production, measure instead of assuming.
6. Version prompts like code: a date per version, what changed and why.
7. Write down the intent for whoever will maintain the prompt (that is the maintenance note of the client deliverable).

## 11. Frequent mistakes

- Starting with a complex prompt before trying the simple one.
- Examples that do not match the task.
- Too many examples or too much data for the model's context window.
- An instruction that can be read two ways.
- Testing only the nominal case.
