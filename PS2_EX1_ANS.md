# D100 – Problem Set 2, Exercise 1: Questions and Answers

## Q1. When you added `.gitignore` to ignore `.csv` files, was the file indeed ignored?

No, the existing World Bank GDP CSV file was not ignored retroactively.

Although we added `*.csv` to `.gitignore`, running:

```bash
git ls-files "*.csv"
```

returned:

```text
data/API_NY.GDP.MKTP.KD_DS2_en_csv_v2_64.csv
```

This confirms that the CSV file remains tracked by Git.

The reason is that `.gitignore` applies to untracked files, but does not automatically remove previously committed files from Git's index.

To stop tracking an existing file while preserving the local copy, we could use:

```bash
git rm --cached <filename>
```

followed by a commit. Newly created, untracked CSV files matching `*.csv` would be ignored automatically.

For this exercise, we have documented the existing behaviour without removing the GDP dataset, as it is used by our analysis.

## Q2. Why do we have to add `additional_dependencies` to mypy in `.pre-commit-config.yaml`?

Pre-commit runs mypy in an isolated Python environment, which does not automatically contain the packages installed in the project's Conda environment.

The `additional_dependencies` setting installs the specified packages and type stubs into mypy's hook environment.

In our configuration:

```yaml
additional_dependencies: [types-seaborn, polars, pandas-stubs, matplotlib]
```

For example, `pandas-stubs` provides type information for pandas, while `polars` and `matplotlib` make those packages available in the hook environment.

This helps mypy analyse third-party library usage more effectively and makes the type-checking setup more consistent across contributors' machines.

## Verification

We independently ran:

```bash
pre-commit run --all-files
```

All configured checks passed, including the standard hooks, flake8 and mypy.

We also inspected the repository's tracked CSV files using `git ls-files "*.csv"` to verify the behaviour of `.gitignore`.
