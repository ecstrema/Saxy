# Contributing

These are the steps to use the automatic build system (recommended):

1) Clone or download this repo.

2) Install [fontforge for windows](https://fontforge.github.io/en-US/), then search your install for a `fontforge-console.bat`, and double-click it. From there you have a python environment that includes fontforge via the command:

    `ffpython`

3) Now you can run:

    `ffpython scripts/build.py`

    This will generate all the files in the redist directory.
