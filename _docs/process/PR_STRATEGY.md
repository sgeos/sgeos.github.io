# PR Strategy

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Process for handling incoming pull requests on this single-author repository. This blog is not organized around external contributions, so incoming PRs are the exception rather than the norm. When one arrives, follow the process below rather than merging directly, even when the change appears trivial.

## Overview

Every incoming PR is treated as an untrusted proposal from an untrusted source. The four-step process applies uniformly whether the PR is from an official bot, a returning contributor, or a first-time author.

1. Assess whether the PR is legitimate and non-malicious.
2. If the PR identifies a real problem, resolve it independently from first principles rather than merging the PR's patch.
3. Close the PR with a comment referencing the resolving commit.
4. Investigate the author to inform future PR handling from the same account.

The rationale is that the value in an incoming PR is the problem identification, not the patch. The maintainer's own understanding of the codebase produces a better fix than a drive-by patch even when the drive-by patch is technically correct, and produces a materially better fix when the drive-by patch has subtle defects.

## Step 1: Legitimacy and Maliciousness Assessment

Evaluate whether the PR is a good-faith contribution, a low-effort bot submission, or a supply-chain attack precursor. Look at the PR content and the author profile together.

### PR Content Signals

- Does the PR identify a real problem? Verify the problem exists in the current tree.
- Does the PR's patch match the identified problem? A mismatch is a signal of scripted or superficial contribution.
- Does the patch introduce any URL, dependency, or endpoint that is not from a canonical upstream source? External-URL substitution is a supply-chain vector even when the substitute appears plausible.
- Does the patch modify configuration or build files in ways unrelated to the stated intent?
- Does the patch touch security-sensitive surfaces such as authentication, cryptography, network transport, or code execution paths?

### Author Profile Signals

The signals below are individually weak. In combination they build a picture. Bot-farming accounts typically exhibit several of these.

- Account age versus PR volume. New accounts with hundreds of PRs are more likely automated than active volunteers.
- Ratio of forks to original repositories. All-forks profiles suggest reputation inflation rather than substantive work.
- Follower and following counts. Legitimate contributors accumulate a small social graph over time.
- Bio and profile fields. Placeholder bios and empty fields correlate with automation.
- Contact anonymity. Anonymized email services and absent contact channels reduce accountability.
- Fork bursts. Multiple forks created within seconds or minutes of each other indicate scripted forking rather than genuine interest.
- Cross-project topic diversity. A single account submitting PRs across unrelated ecosystems suggests scraping rather than engagement.

### Verdict Categories

- **Good-faith contribution.** Proceed to first-principles resolution. Consider whether the author's identified problem is complete or partial.
- **Bot-farming, non-malicious.** Proceed to first-principles resolution but treat the patch content as untrusted. The author gains no direct trust from this PR being acted upon.
- **Suspected malicious.** Do not act on the patch content. Close the PR with a neutral comment. Document the account for future reference. Consider blocking if the platform supports it.

## Step 2: First-Principles Resolution

If Step 1 confirms a real problem, resolve the problem independently rather than merging the PR.

- Read the current state of the affected files directly.
- Identify the root cause and any adjacent issues the PR did not surface.
- Design the fix using canonical upstream documentation and the maintainer's own understanding of the codebase.
- Verify the fix against the actual failure mode, not against the PR's description.
- Commit the fix with a standard commit message. The commit body may reference the closing PR number with a GitHub `Closes GH-N` trailer, but the body describes the fix from the maintainer's perspective rather than the PR author's.

Independent resolution avoids several failure modes.

- Blind merges of technically-correct-looking patches can miss subtle defects such as configuration incompatibilities across version boundaries.
- Blind merges normalize accepting patches from bot-farming accounts, which increases exposure to eventual supply-chain compromise from the same source.
- Blind merges attribute credit to the PR author without corresponding responsibility. Independent resolution attributes both credit and responsibility to the maintainer.

## Step 3: Close the PR

After the fix is committed and pushed, close the PR with a comment.

- Reference the resolving commit hash so external readers can trace the resolution.
- If the PR's patch was technically incomplete or defective, note the specific defect that the independent fix addressed. This is diagnostic information for the PR author and for future contributors reading the issue tracker.
- Keep the tone neutral. Do not thank the author when the account signals are bot-farming, and do not accuse the author of malice when the signals are ambiguous. Neutrality preserves optionality for future engagement.

If the PR is a Dependabot bot submission and the same change has been applied directly, Dependabot will typically detect the update on push and auto-close its PR. No explicit close command is required in that case.

## Step 4: Author Investigation

After closing, investigate the author to inform future PR handling.

- Retrieve the author's full public GitHub profile via `gh api users/<login>`.
- List the author's public repositories via `gh api users/<login>/repos` and inspect the mix of forks versus originals.
- Query the author's cross-GitHub PR history via `gh api "search/issues?q=author:<login>+is:pr"` for total count and pattern.
- Document notable findings in `MEMORY.md` under a working-conventions entry if the account is likely to submit future PRs. Bot-farming accounts frequently do.

Author investigation informs future PR review but does not retroactively justify or reverse the current PR handling. The current PR is judged on its own merits.

## Commit and PR Message Conventions

The commits produced by this process follow the standard [Git Strategy](./GIT_STRATEGY.md) conventions. Additional PR-specific practices:

- Use `Closes GH-N` in the commit body to link the PR. GitHub will render the linkage on the resolved PR page.
- The commit summary describes the fix, not the PR reference. `fix: replace deprecated MathJax v2 CDN with official v3 jsdelivr endpoint and v3-compatible config` is preferable to `fix: resolve PR #3`.
- Close comments reference the commit hash rather than the PR number, so external readers arriving from the PR page can navigate to the resolving commit.

## Reference Case

The rocket propellant chemistry series publication push on 2026-07-11 surfaced four existing PRs against this repository. The four-step process was applied uniformly.

- **PR #1** identified a one-character typo in a draft file that no longer exists in the repository. Owner closed as no-longer-applicable. No independent action was required because the problem no longer existed.
- **PR #2** was a Dependabot dependency bump for `nokogiri`. Dependabot auto-closed the PR when it detected the dependency was no longer present in the repository. No action was required.
- **PR #3** identified that the MathJax include used a deprecated HTTP CDN URL and an untrusted third-party fork script. Author's account signals were consistent with bot farming. Their patch changed the CDN URL to the correct MathJax v3 endpoint but left the incompatible v2 configuration call intact, which would have silently broken math rendering under v3. Independent fix in commit `c03cb1f` replaced the deprecated CDN with the official jsdelivr v3 endpoint and translated the v2 `MathJax.Hub.Config` call to the v3 `window.MathJax` configuration shape.
- **PR #4** was a Dependabot dependency bump for `concurrent-ruby` to pick up three low-severity CVE fixes. Independent Gemfile.lock bump in commit `7b432d7`. Dependabot detected the update on push and auto-closed its PR.

## Related Sections

- [Git Strategy](./GIT_STRATEGY.md) for commit conventions
- [Publication Review](./PUBLICATION_REVIEW.md) for pre-publication verification
- [URL Verification](./URL_VERIFICATION.md) for the canonical bot-detected-URL catalogue
