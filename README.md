# Claude Code skills for working with AI

**English** · [Français](README.fr.md)

Skills for [Claude Code](https://claude.com/claude-code) that I wrote for my own work and use every day. The first one designs prompts for other AI tools and for automations. The other three help write in French with AI: the first scores the tells of a generated text, the second removes them, the third does the final proofread.

| Plugin | Language | Skills | What it does |
|---|---|---|---|
| `prompt-slayer` | English | `/prompt-slayer` | Builds a ready-to-paste prompt for ChatGPT, Claude, Perplexity, Midjourney, an n8n node, a Make module or a custom GPT, with a portable version and a three-case test plan. It never does the task itself. |
| `prompt-slayer-fr` | French | `/prompt-slayer` | The same skill, in French. |
| `ecriture-fr` | French (and English for `/ecrire-sans-tics-ia`) | `/diagnostic-tics-ia`, `/ecrire-sans-tics-ia`, `/relecture-finale` | Writing and proofreading in French: scoring and removing AI tells, then grammar, typography and consistency checks across a set of documents. |

## Contents

- [Prompt Slayer](#prompt-slayer)
- [French writing: ecriture-fr](#french-writing-ecriture-fr)
- [Installation](#installation)
- [Usage](#usage)
- [Limitations](#limitations)
- [Repository layout](#repository-layout)
- [Credits](#credits)
- [Author](#author)

## Prompt Slayer

The prompts I see fail almost always break in the same places: a format that is described but never shown, no instruction for missing information, nothing that says what to do off topic. Prompt Slayer builds the prompt around those failure points, then gives you three tests to check it before you rely on it.

For a one-off question in ChatGPT, it is overkill: a clear two-line instruction will do. It earns its place when the prompt has to run on its own, last, or be handed over to someone.

The skill has one rule it never breaks: **it does not do the work.** Ask it for a product description and you get the prompt that will write good product descriptions, ready to paste into the tool of your choice.

For every request, it returns:

1. the goal restated in one sentence;
2. a diagnosis: task type, where the prompt will run, complexity, risk, success criteria;
3. one question if critical information is missing, otherwise the assumptions it made;
4. the **target prompt**, tuned to the tool you named;
5. a **portable prompt** that works on any model;
6. variants when useful (compact, safe, few-shot);
7. a **test plan**: a nominal case, an edge case and an out-of-scope case, each with the exact input and what a good output looks like;
8. one practical tip.

Where the prompt will run changes it more than the choice of model does:

| Context | What the prompt must handle |
|---|---|
| Chat | A person can rephrase, so the prompt may ask questions. |
| Persistent system prompt (custom GPT, agent) | Edge cases on its own, off-topic requests, attempts to extract the prompt. |
| Automation (n8n, Make, API call) | No human in the loop: strict JSON output, no questions, messy inputs, a JSON error object instead of free text. |
| Client deliverable | Someone else maintains it: documented variables, installation settings, the three tests, a maintenance note. |

The skill ships with a reference on prompting techniques (`references/prompting-techniques.md`): examples rather than rules, reasoning steps, versioning, the order of blocks, templates, system prompts, planning for failure, and a symptom, cause, remedy table to fix an agent or a GPT that drifts.

## French writing: ecriture-fr

These three skills are in French because they work on French text. They are listed here for completeness; the [French README](README.fr.md) describes them in full.

- **`/diagnostic-tics-ia`** scores the AI writing tells of a French text out of 25, quotes each passage with the name of its pattern and notes what sounds human. The score counts writing patterns; it does not say who wrote the text and must never be used to accuse anyone.
- **`/ecrire-sans-tics-ia`** writes or reworks a text so it no longer carries the tells of generated writing: empty emphasis, staged oppositions ("it's not X, it's Y"), mechanical lists of three, sentences of equal length, predictable words. It detects the language and also handles English text, with 21 pattern categories and a 43-row replacement table adapted from [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing). It is meant to make writing better, and it was not designed to hide the use of AI or to fool a detector.
- **`/relecture-finale`** proofreads French or English text without touching style or rhythm, and writes a change log. Its consistency mode checks a set of related documents (a study and its appendices, one-pagers and their PDFs, slides and their notes) against a register of facts, with a Python script and a snapshot that flags any change nobody planned. The script comes with a self-test of 11 checks.

## Installation

### Requirements

- [Claude Code](https://claude.com/claude-code)
- For the consistency mode of `/relecture-finale` only: Python 3 with PyYAML (`pip install pyyaml`), and `pdftotext` from Poppler to read PDFs.

### With the Claude Code plugin manager

```
/plugin marketplace add lilian-barty/claude-skills
/plugin install prompt-slayer@lilian-barty-skills
```

Then restart Claude Code. The French version installs with `prompt-slayer-fr@lilian-barty-skills`; there is no need to install both. The French writing skills install with `ecriture-fr@lilian-barty-skills`.

### Manual installation

Copy a skill folder, for example `plugins/prompt-slayer/skills/prompt-slayer`, into `~/.claude/skills/`.

### Check

For the consistency script:

```
python ~/.claude/skills/relecture-finale/scripts/auto_test.py
```

The expected result is "11/11 contrôles passés". After a plugin installation, the script is in `~/.claude/plugins/cache/lilian-barty-skills/ecriture-fr/<version>/skills/relecture-finale/scripts/`.

## Usage

In Claude Code:

```
/prompt-slayer a system prompt for a support chatbot that only answers from our FAQ
/prompt-slayer debug this n8n prompt: it sometimes returns text instead of JSON
```

A request in plain words works too: "write me a prompt for Midjourney", "why does my custom GPT keep going off topic?".

## Limitations

- Prompt Slayer builds and tests prompts on paper: it does not run them against the target model. The test plan is there for you to run.
- Model behaviour changes with each release. The tool-specific advice in the skill reflects current practice and should be checked against a model you don't know.
- `/ecrire-sans-tics-ia` and `/relecture-finale` follow French conventions by default. Their typographic choices (quotes, numbers, spacing) can be switched to a "keyboard profile" described in each skill.
- The skills run in Claude Code. The consistency script needs Python on your machine.

## Repository layout

```
claude-skills/
├── .claude-plugin/
│   └── marketplace.json            the marketplace and its three plugins
├── plugins/
│   ├── prompt-slayer/              English plugin
│   │   ├── .claude-plugin/         plugin manifest
│   │   └── skills/prompt-slayer/
│   │       ├── SKILL.md            instructions Claude follows
│   │       └── references/
│   │           └── prompting-techniques.md
│   ├── prompt-slayer-fr/           French plugin, same layout
│   └── ecriture-fr/                French writing plugin
│       └── skills/
│           ├── diagnostic-tics-ia/SKILL.md
│           ├── ecrire-sans-tics-ia/
│           │   ├── SKILL.md
│           │   └── references/anglais.md     English rules
│           └── relecture-finale/
│               ├── SKILL.md
│               ├── references/coherence-paquet.md
│               └── scripts/        controle.py and its self-test
├── CHANGELOG.md
├── LICENSE
├── README.md                       this page
└── README.fr.md                    French version
```

## Credits

- The English rules of `/ecrire-sans-tics-ia` adapt [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) by Conor Bronsdon (MIT License, Copyright (c) 2026 Conor Bronsdon).
- Its two-pass rewrite follows the approach of [humanizer](https://github.com/blader/humanizer) (MIT License).
- Two of its French rules draw on [le-unslop](https://github.com/painhardcore/le-unslop) and [slopcheck-fr](https://github.com/tns-research/slopcheck-fr) (MIT License).

Everything else is original work.

## Author

Lilian Barty-Christophe, AI adoption and automation consultant in Paris. I help teams adopt AI and I build the tools they adopt: prompts, automations, small applications.

These skills come from that work. I use Prompt Slayer to write the prompts behind automations and custom GPTs, and every text I publish goes through the two writing skills. Two more of my skills live in their own repositories: [skill-refacto](https://github.com/lilian-barty/skill-refacto) (proven refactoring) and [skill-tdah](https://github.com/lilian-barty/skill-tdah).

Website: [lilian-barty.fr](https://www.lilian-barty.fr/)

## License

[MIT](LICENSE)
