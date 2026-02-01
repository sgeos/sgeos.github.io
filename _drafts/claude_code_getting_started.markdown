---
layout: post
mathjax: true
comments: true
title: "Getting Started with Claude Code"
date: 2026-01-31 12:10:25 +0000
categories: [ai, ai-tools, development, developer-productivity, tutorial]
---
The landscape of software development is shifting rapidly
with the emergence of agentic AI systems.
These systems do not merely assist with code completion.
They can plan, execute, and iterate
on multi-step workflows across an entire codebase.

[Claude Code][claude_home] is Anthropic’s entry into this space.
It is a command line tool that allows developers
to delegate substantial portions
of a development workflow to Claude directly from the terminal.
Rather than operating as a conversational assistant or autocomplete engine,
Claude Code can navigate repositories, run builds and tests, modify files,
and converge on working implementations with limited supervision.

This post has three concrete goals.

- First, it introduces Claude Code from the perspective
of a working developer, focusing on installation, core controls,
and the role of the `CLAUDE.md` configuration file in shaping agent behavior.

- Second, it demonstrates a real, nontrivial artifact
generated using Claude Code.
Specifically, a [Constant Product Market Maker (CPMM)][post_cpmm] fee
and price impact calculator implemented in Rust,
compiled to WebAssembly, and [embedded in this Jekyll page][post_wasm].

- Third, it examines where the generated result succeeded, where it failed,
and why those outcomes were driven by specification quality
rather than model limitations.
The intent is not to market agentic tooling,
but to show what it currently does well, where it requires careful guidance,
and how to collaborate with it productively.

> The following CPMM calculator was generated with a single prompt.
> See below for details.
>
> Note that the calculator is cut off due to this blog's CSS wrapper.
> The text above and below the calculator widget
> was pulled from the generated `example.html` file.
> The inline styles are part of the `generated example.html` output
> and are shown to illustrate the artifact Claude Code produced.

<div id="claude-output">
    <style>
        #claude-output {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            max-width: 800px;
            margin: 2rem auto;
            padding: 1rem;
            border: 2px solid blue;
            border-radius: 8px;
            background: #ccf;
        }
        #claude-output h1 {
            text-align: center;
            font-weight: bold;
            font-size: 2em;
            color: #333;
        }
        #claude-output h2 {
            font-weight: bold;
            font-size: 1.5em;
            color: #333;
        }
        .cpmm-calculator {
            background: white;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .cpmm-section {
            border: 1px solid #ddd;
            border-radius: 6px;
            margin-bottom: 1rem;
            overflow: hidden;
        }
        .cpmm-section-header {
            background: #4a90d9;
            color: white;
            padding: 0.75rem 1rem;
            font-weight: 600;
            text-align: center;
        }
        .cpmm-row {
            display: flex;
            gap: 1rem;
            padding: 0.75rem 1rem;
            border-bottom: 1px solid #eee;
        }
        .cpmm-row:last-child {
            border-bottom: none;
        }
        .cpmm-field {
            flex: 1;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .cpmm-field label {
            min-width: 140px;
            font-weight: 500;
            color: #555;
        }
        .cpmm-field input[type="text"] {
            flex: 1;
            padding: 0.5rem;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-family: monospace;
            font-size: 0.95rem;
        }
        .cpmm-field input[type="text"]:focus {
            outline: none;
            border-color: #4a90d9;
            box-shadow: 0 0 0 2px rgba(74, 144, 217, 0.2);
        }
        .cpmm-slider-row {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            padding: 0.75rem 1rem;
            border-bottom: 1px solid #eee;
        }
        .cpmm-slider-row label {
            font-size: 0.85rem;
            color: #777;
        }
        .cpmm-slider {
            width: 100%;
            height: 8px;
            cursor: pointer;
        }
        #delta-empty {
            visibility: hidden;
        }
    </style>
    <h1>CPMM Fee and Price Impact Calculator</h1>
    <p>
        This calculator demonstrates Constant Product Market Maker (CPMM) mathematics.
        Adjust the initial liquidity and price, then modify the final price to see
        the wallet deltas and fee collection for a hypothetical trade.
    </p>

    <!-- The WASM UI will be injected before this script element -->
    <script type="module" id="cpmm_calculator">
        import init, { inject_ui } from "/assets/wasm/post_claude_code_getting_started/post_claude_code_getting_started.js";
        async function run() {
            await init();
            inject_ui("cpmm_calculator");
        }
        run();
    </script>

    <h2>Formulas Used</h2>
    <ul>
        <li><strong>Invariant:</strong> k = x &middot; y = L&sup2;</li>
        <li><strong>Price:</strong> P = y / x</li>
        <li><strong>Base Reserves:</strong> x = L / &radic;P</li>
        <li><strong>Quote Reserves:</strong> y = L &middot; &radic;P</li>
        <li><strong>Wallet Delta:</strong> Opposite of pool reserve changes</li>
        <li><strong>Fee:</strong> Collected on the input side of the trade</li>
    </ul>

    <h2>Interpretation</h2>
    <ul>
        <li>Positive base delta: trader receives base tokens</li>
        <li>Negative quote delta: trader pays quote tokens</li>
        <li>Fee is collected on whichever token the trader is paying</li>
    </ul>
</div>

## Software Versions

```sh
# Date (UTC)
$ date -u "+%Y-%m-%d %H:%M:%S +0000"
2026-01-31 12:10:25 +0000

# OS and Version
$ uname -vm
Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6000 arm64

$ sw_vers
ProductName:		macOS
ProductVersion:		14.6.1
BuildVersion:		23G93

# Hardware Information
$ system_profiler SPHardwareDataType | sed -n '8,10p'
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 32 GB

# Shell and Version
$ echo "${SHELL}"
/bin/bash

$ "${SHELL}" --version  | head -n 1
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin23)

# Claude Code Installation Versions
$ claude --version
2.1.17 (Claude Code)
```

## Installation and Setup

First, [login to Claude][claude_login] and select a plan.
There is a free plan, but it is limited to about 40 messages per day,
and agentic features are not available.
It is only suitable for casual experimentation or initial onboarding
into the Claude ecosystem.
A Pro plan is sufficient for a general agentic workflow
without premium features,
while a Max plan is recommended for power user agentic workflows.
See [this article][claude_limits] for more information on Claude limits.

On Mac, run the following commands to install and set up Claude Code.
Note that you will need to set up billing to complete the process.
If you prefer a video, [this tutorial][claude_tutorial_video] covers
installation, setup, and prototyping of a basic browser-based application.

```sh
curl -fsSL https://claude.ai/install.sh
claude
```

If all went well, you should see something like the following.

```
Welcome to Claude Code v2.1.17
…………………………………………………………………………………………………………………………………………………………

     *                                       █████▓▓░
                                 *         ███▓░     ░░
            ░░░░░░                        ███▓░
    ░░░   ░░░░░░░░░░                      ███▓░
   ░░░░░░░░░░░░░░░░░░░    *                ██▓░░      ▓
                                             ░▓▓███▓▓░
 *                                 ░░░░
                                 ░░░░░░░░
                               ░░░░░░░░░░░░░░░░
       █████████                                        *
      ██▄█████▄██                        *
       █████████      *
…………………█ █   █ █………………………………………………………………………………………………………………

 Logged in as user@email.com
 Login successful. Press Enter to continue…
```

Answer the remaining setup questions, and exit then Claude.
You can press **Ctrl+C** twice or use the `/exit` command to exit Claude.
Alternatively, you can press **Ctrl+Z** to suspend Claude,
and run `fg` to resume the session.

## Basic Usage Controls & Keybindings

Claude Code provides an interactive terminal interface designed
for rapid navigation and control of agentic tasks. 

### Core Navigation

| Shortcut | Action |
| :--- | :--- |
| **`Shift + Tab`** | **Cycle Permission Modes**: Instantly toggle between **Plan Mode** (read-only), **Auto-Accept** (no prompts), and **Standard Mode**. |
| **`Esc`** | **Cancel**: Abort the current model generation or tool execution. |
| **`Esc` + `Esc`** | **Rewind**: Open the checkpoint menu to revert files and context to a previous state. |
| **`Ctrl + O`** | **Toggle Verbosity**: Show or hide the "Inner Monologue" and detailed tool logs. |
| **`Ctrl + G`** | **External Editor**: Open your current draft prompt in your system's default editor (e.g., VS Code, Vim). |

### Terminal & Input

| Shortcut | Action |
| :--- | :--- |
| **`Ctrl + R`** | **History Search**: Interactively search through previous prompts and shell commands. |
| **`Ctrl + L`** | **Clear**: Clear the terminal screen while preserving the conversation context. |
| **`Ctrl + V`** | **Paste Image**: Attach an image or file path from your clipboard for multimodal analysis. |
| **`Up / Down`** | **History Navigation**: Cycle through your recent command and prompt history. |
| **`Shift + Enter`** | **Multiline Input**: Insert a newline without submitting the prompt. Run `/terminal-setup` if this is not native in your environment. |

### Model & Thinking

| Shortcut | Action |
| :--- | :--- |
| **`Opt + T`** (Mac) / **`Alt + T`** | **Toggle Extended Thinking**: Enable or disable the model's high-reasoning mode for the next turn. |
| **`Opt + P`** (Mac) / **`Alt + P`** | **Model Picker**: Quick-switch between Claude Sonnet 4.5 and Opus 4.5. |
| **`Ctrl + B`** | **Background Task**: Move a long-running process, like a build or test suite, to a background agent. |

> **Pro Tip**:
> Use the `/keybindings` command in any active session to view
> a dynamic list of shortcuts or to map your own custom bindings
> in `~/.claude/keybindings.json`.

## The Four Components of Agentic AI

Agentic AI consists of four components:

1. **The Model:**
The underlying AI system, like Claude Sonnet 4.5,
that processes information and generates responses.
The model's reasoning ability, knowledge, and instruction-following
set the baseline for what the agent can accomplish.

2. **The Context:**
The information the model has access to during a task.
Context holds project-specific knowledge,
and files like `CLAUDE.md` load context into every session.

  - Conversation history.
  - Files it can read, like `CLAUDE.md`.
  - Previous tool outputs.
  - System prompts and instructions.

3. **The Prompt:**
The instructions that guide the model's behavior.
For agentic systems, prompts often include instructions on
*how* to break down complex tasks and when to use which tools.

  - User requests, like "implement feature X".
  - System-level directives, like how to use tools and coding standards.
  - Task decomposition and planning strategies.

4. **The Tools:**
The capabilities that extend the model beyond text generation.

  - File system operations, like read, write, and edit.
  - Shell commands, like running tests, and git operations.
  - Search tools.
  - API calls.

### Claude 4.5 Model Family

As of early 2026, Claude Code is powered by the Claude 4.5 model family,
specifically utilizing Claude Sonnet 4.5 as its default balanced engine
and Claude Opus 4.5 for high-complexity reasoning tasks.
Sonnet is primarily used for speed, coding precision, and agentic loops.
Opus is employed for complex architecture and multi-system debugging.

## CLAUDE.md Configuration File

`CLAUDE.md` is a special configuration file that
Claude automatically reads at the start of each session,
providing project-specific context without needing to repeat yourself.
It is case-sensitive and must be exactly `CLAUDE.md`,
specifically uppercase `CLAUDE` with a lowercase `.md` extension.

This file should include the following.
- **Project context:** A single line summarizing the project.
- **Common commands:** Build, test, lint, and deployment commands.
- **Code style:** Formatting preferences, module preferences (ES modules vs CommonJS, etc.)
- **Directory structure:** Key directories with summary descriptions.
- **Workflows:** How your team implements features or fixes bugs.
- **Domain terminology:** Domain-specific jargon and acronyms.
- **Gotchas:** Project-specific warnings or unusual behaviors.

The fastest way to generate a `CLAUDE.md` file
is to run `/init` in your project directory.
This will generate a file that can be customized for your project.

### Hierarchical CLAUDE.md Files

Claude reads `CLAUDE.md` files hierarchically.

- First from your home directory: `${HOME}/.claude/CLAUDE.md`
- Second, from your project root.
- Finally from individual directories.

This allows you to organize knowledge at different levels of specificity.
Here is an example master `CLAUDE.md` intended for mission-critical code.
Note that the contents are not appropriate for all development styles!
You will need to draft contents that are appropriate for the kinds of
projects you work on.

**Example `${HOME}/.claude/CLAUDE.md` full listing**
````
## Writing Style
- Prose should be polite, professional, and academic.
- Avoid contractions. Spell out acronyms on first use.
- Avoid parentheticals, em-dashes, en-dashes, colons, and semicolons in prose.
- Wrap draft prose in quadruple backticks to preserve nested code blocks.

## Epistemic and Engineering Rigor
- Distinguish facts, inferences, and hypotheses explicitly.
- State epistemic state clearly with explicit uncertainty markers.
- Challenge unsupported premises. Flag assumptions about correctness, security, concurrency, integrity, and error handling.
- State unaddressed concerns about correctness, security, edge cases, and failure modes explicitly.
- Never imply completeness where verification is incomplete.
- Prioritize correctness over conversational harmony. Expect technical disagreement.
- Provide verifiable, auditable outputs. Assume independent verification.
- Prioritize precision over elegance or narrative coherence.
- Avoid personas, affective mirroring, or unwarranted authority.
- Never infer unstated intent, emotions, or identity.

## Code Implementation
- Ecosystem conventions take precedence when conflicts arise with universal directives.
- Adhere to ecosystem conventions and standard tooling for the target language and stack.
- Leverage type systems for correctness. Use strongest available type constraints.
- Use simple, verifiable control flow. Avoid recursion, complex branching, and saltation where feasible.
- Ensure loop termination is verifiable through static analysis, testing, or formal proof as appropriate.
- Prefer predictable resource usage. Avoid dynamic allocation where determinism or resource bounds are required.
- Keep functions focused on single responsibilities. Decompose when cognitive load or context limits readability.
- Verify invariants, preconditions, and postconditions at runtime using language-appropriate mechanisms.
- Minimize state visibility. Declare variables at smallest scope to enable local reasoning.
- Validate contracts at function boundaries. Handle all error conditions and validate all parameters.
- Limit abstraction complexity appropriate to context. Avoid gratuitous metaprogramming and obfuscation.
- Maximize automated error detection. Use standard linting and static analysis for the ecosystem. Strive for zero warnings.
- Document failure modes, edge cases, rationale, assumptions, constraints, invariants, and technical debt.
- Explain decisions, not implementations. Document security boundaries, trust models, and threat surfaces.
- Enable verification by humans and tools. Prefer constructs amenable to review and static analysis.

## Verification and Security
- Test edge cases, boundaries, and failure modes. Include negative tests for error paths.
- Write tests before or alongside implementation. Document test rationale and coverage gaps.
- Prefer determinism where feasible. Document and flag non-determinism explicitly, especially in concurrent contexts.
- Treat all external inputs as untrusted. Validate and sanitize at system boundaries.
- Design for secure failure modes. Default deny for authorization decisions.
- Minimize attack surface. Use cryptographic primitives correctly. Never implement custom cryptographic primitives or algorithms.
- Document trust boundaries and security assumptions.
````

### Keep CLAUDE.md Focused

Keep your `CLAUDE.md` concise.
Context is precious,
and every line competes for attention with your actual coding tasks.
Add to it organically when you find yourself repeating instructions,
rather than trying to document everything upfront.

## Other Useful .md Files

### Plan.md File

`Plan.md` is automatically generated by Claude
to help it stay on track and maintain context across sessions.
It is a working todo list that persists across chats.

### AGENTS.md

Some teams maintain an `AGENTS.md` file synced with `CLAUDE.md` for
compatibility with other AI IDEs like Cursor and Zed.

### Task-Specific Markdown Checklists

For large tasks requiring multiple steps,
you can have Claude use a markdown file
as a checklist and a working scratchpad.
For example, when fixing numerous lint errors,
you could tell Claude to write all errors to a markdown checklist,
and then address each one systematically.

### External Documentation References

Rather than cramming everything into `CLAUDE.md`,
you can reference other markdown files with specific instructions like:

> For complex usage or if you encounter a `FooError`,
> see `path/to/relevantdoc.md` for advanced troubleshooting steps.

### Sample Project

I added the above `${HOME}/.claude/CLAUDE.md` to my system
and ran the following command to generate a new project
and start Claude Code.

```sh
PROJECT_NAME="post_claude_code_getting_started"
cargo new --lib "${PROJECT_NAME}"
cd "${PROJECT_NAME}"
claude
```

In theory, I should have added a project-based `CLAUDE.md` file.
I got ahead of myself and provided a prompt that produced a working result.
The output was useful and technically sound, but it did not capture my intent.
This is actually a wonderfully illustrative example
of how specification quality directly shapes agentic outcomes.
This is the prompt I used.

````markdown
Please review the following blog posts of mine.
https://sgeos.github.io/rust/wasm/jekyll/2026/01/26/webasm_on_jekyll.html
https://sgeos.github.io/crypto/defi/rust/2026/01/29/constant_amm_mathematics.html

The goal is to generate a CPMM fee and price impact calculator with a UI something like the following.
The math can be found in the CPMM article.
The delta section reflects wallet deltas for someone making a transaction,
and assumes the fees are sent to a treasury.

```
+-------------------------------------------------------------+
|                     Initial Price Section                   |
+-------------------------------------------------------------+
| Liquidity: [Textbox]   Price: [Textbox]                     |
+-------------------------------------------------------------+
| Logarithmic Price Slider (Adjust the price)                 |
+-------------------------------------------------------------+
| Base Reserves: [Textbox]   Quote Reserves: [Textbox]        |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
|                     Final Price Section                     |
+-------------------------------------------------------------+
| Fee %: [Textbox]   Price: [Textbox]                         |
+-------------------------------------------------------------+
| Logarithmic Price Slider (Adjust the price further)         |
+-------------------------------------------------------------+
| Base Reserves: [Textbox]   Quote Reserves: [Textbox]        |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
|                         Delta Section                       |
+-------------------------------------------------------------+
| (empty lefthand side)   Price Delta: [Textbox]              |
+-------------------------------------------------------------+
| Base Reserves Delta: [Textbox]   Quote Reserves Delta: [Textbox] |
+-------------------------------------------------------------+
| Base Reserves Fee Collected: [Textbox]   Quote Reserves Fee Collected: [Textbox] |
+-------------------------------------------------------------+
```
````

The resulting widget can be found near the top of this post.
The [companion repository][companion_repo] for this post has full source code,
including some extra files, like `README.md`, that were generated
and added for completeness.

It took Claude Code about five and a half minutes to generate
the source code and `example.html` from the prompt.
This prompt is an excellent example of getting what you ask for
instead of getting what you want.

Here is where the prompt succeeded.

- The UI layout and CSS styling were exactly what I was hoping for.
- Liquidity and price correctly calculate reserves.
- The slider acts as an alternative input method for the price.
- The fee input feeds the fee output in a straightforward way.
- Fees are only collected from the asset the trader pays into the pool.
- Delta section was delivered as requested, even if not as desired.

The project was also generated in accordance with the master
`CLAUDE.md` file.

- Code follows Rust ecosystem conventions.
- Code is factored into comprehensible single-responsibility units.
- Code is commented.
- Error checking is rigorous.
- Includes commented tests.
- `example.html` file that embeds WASM was generated.
- `cargo clippy` was run and it passed.

Where the project did not give me what I wanted, this was mainly
a problem with my specification.

- Reserves cannot be entered to rebalance liquidity or price.
I did not ask for this functionality.
- When a trader pays $\Delta x$ for a nominal $\Delta y$,
only $\Delta y_net = \Delta y \cdot (1 - f)$ should be subtracted
from the pool, and the trader should receive $\Delta x_net$.
I asked for "Base/Quote Reserves Delta",
not $\Delta x_net$ and $\Delta y_net$.

Note that a human would not be able to read my mind either.
This was a specification problem, not a code generation problem.

## Conclusion

This experiment highlights several practical lessons
about working with agentic AI systems.

First, Claude Code is capable of producing structurally sound,
idiomatic projects when given sufficient context.
The generated CPMM calculator followed Rust ecosystem conventions,
passed linting, included tests, and produced
a functional WebAssembly integration without manual intervention.
These are not superficial achievements,
and they meaningfully reduce setup and scaffolding effort.

Second, agentic systems are literal in the way experienced engineers
expect junior collaborators to be literal.
The model implemented exactly what was specified,
including ambiguities and imprecisions. Where the output diverged from intent,
the root cause was incomplete or underspecified requirements rather than
incorrect reasoning or faulty execution.

Third, configuration files such as CLAUDE.md materially shape outcomes.
Providing explicit guidance on epistemic rigor, code quality,
and verification practices resulted in outputs that were auditable and
conservative rather than speculative or overly confident.

Finally, this workflow reinforces a familiar engineering truth.
Delegation does not eliminate the need for clear thinking.
It raises the premium on precise specifications, explicit assumptions,
and well defined success criteria.
Agentic AI changes the mechanics of development,
but it does not change the responsibility model.
The developer remains accountable for correctness, clarity, and intent.

Used thoughtfully, Claude Code is not a replacement for engineering judgment.
It is a force multiplier for it.

## Future Reading

To transition from basic usage to high-assurance engineering with Claude Code,
it is essential to move beyond simple prompts
and master the systemic controls of the environment.
The [authoritative documentation][claude_docs] is the primary resource
for understanding the transition from a conversational interface
to an agentic workflow.

Specifically, developers should prioritize the study
of [Agent Hooks][claude_hooks], which allow for the injection of deterministic
checks—such as security linters or formatters—directly into the agent's
execution loop.
To manage the high context demands of modern projects,
understanding the [300 Line Rule][claude_best_practices]
and the implementation of [Sub-agents][claude_subagents]
is vital for maintaining model performance and preventing "rule drift."

For integration with external data and documentation,
the [Model Context Protocol (MCP)][mcp_main] and its specific
[implementation in Claude Code][claude_mcp] provide the standard
for extending the agent's knowledge base.
Finally, as reasoning requirements scale, users should review
the documentation on [Model Configuration][claude_model_config] and
[Thinking Levels][claude_thinking] to learn
how to manually adjust the model's reasoning budget,
and familiarize themselves with
the [Interactive Mode Guide][claude_keybindings]
to master the `Shift+Tab` and `Esc` control schemes
that prevent "runaway" agentic loops.

## References

- [Claude, Agent Hooks and Lifecycle Events][claude_hooks]
- [Claude, Best Practices: Context Management and the 300 Line Rule][claude_best_practices]
- [Claude, Interactive Mode Guide and Keybindings][claude_keybindings]
- [Claude, Login][claude_login]
- [Claude, Model Configuration][claude_model_config]
- [Claude, Model Context Protocol (MCP) Specification][mcp_main]
- [Claude, Sub-agents and Context Isolation][claude_subagents]
- [Claude, Thinking Levels][claude_thinking]
- [Claude, Using MCP with Claude Code][claude_mcp]
- [Claude Code allows you double tap esc key to edit previous messages][claude_edit]
- [Claude Code Limits Explained (2026 Edition)][claude_limits]
- [Claude Code Official Documentation][claude_docs]
- [Claude Code Tutorial for Beginners, Video][claude_tutorial_video]
- [GitHub Companion Repository][companion_repo]
- [Related Post, Constant Product AMM Mathematics][post_cpmm]
- [Related Post, WASM on a Jekyll Blog with Rust and wasm-bindgen][post_wasm]

[claude_best_practices]: https://code.claude.com/docs/en/best-practices#context-management
[claude_docs]: https://platform.claude.com/docs/en/home
[claude_edit]: https://www.reddit.com/r/ClaudeAI/comments/1ln8d6z/claude_code_allows_you_double_tap_esc_key_to_edit/
[claude_home]: https://code.claude.com
[claude_hooks]: https://code.claude.com/docs/en/hooks-guide
[claude_keybindings]: https://code.claude.com/docs/en/interactive-mode
[claude_limits]: https://www.truefoundry.com/blog/claude-code-limits-explained
[claude_login]: https://claude.ai/login
[claude_mcp]: https://code.claude.com/docs/en/mcp
[claude_model_config]: https://code.claude.com/docs/en/model-config
[claude_subagents]: https://code.claude.com/docs/en/hooks#agent-based-hooks
[claude_thinking]: https://code.claude.com/docs/en/common-workflows#use-extended-thinking-thinking-mode
[claude_tutorial_video]: https://www.youtube.com/watch?v=eMZmDH3T2bY
[companion_repo]: https://github.com/sgeos/post_claude_code_getting_started?tab=readme-ov-file
[mcp_main]: https://modelcontextprotocol.io
[post_cpmm]: {% post_url 2026-01-29-constant_amm_mathematics %}
[post_wasm]: {% post_url 2026-01-26-webasm_on_jekyll %}

