# Git workflow

## What to commit

Commit source code, configuration, dependency declarations, documentation,
notebooks, tests, and GitHub Actions workflows. The raw training data may only
be committed when you have permission to distribute it.

Do not normally commit local environments, MLflow databases, model binaries,
generated processed arrays, reports, logs, or inference outputs. These are
reproducible run artifacts; inspect `.gitignore` before staging files.

## Stage and review

Run these commands from the repository root:

```powershell
git status --short
git add README.md GIT_WORKFLOW.md config.yaml requirements.txt .gitignore .github docs notebooks pipelines src tests
git diff --cached --check
git diff --cached --stat
git status
```

Review the staged file list and diff before committing. Do not use `git add .`
when generated artifacts or datasets are present.

## Commit and push

After confirming that only intended files are staged:

```powershell
git commit -m "Describe the project change"
git push
```

Verify the commit and synchronization state with:

```powershell
git log -1 --oneline
git status --short --branch
```

## Undoing a staging mistake

To unstage a file without deleting its local changes:

```powershell
git restore --staged path/to/file
```

Avoid `git restore path/to/file` unless you intend to discard its working-copy
changes.
