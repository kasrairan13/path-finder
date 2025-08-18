# Path Finder

**Path finder** is a small Python tool in one file. It helps you import code from folders outside your current folder.

## What does it do?
Sometimes in a project, you want to use code from other folders that are not inside your current folder. This tool:

- Checks if you have a `.gitignore` file.
- Reads the `.gitignore` file and finds folders you want to ignore.
- Adds all folders except the ignored ones to Python’s `sys.path`.
- So you can import code from outside folders easily.

## How to use?
Just import it at the start of your script:

```python
import path_finder
```
That’s it! It will fix your import paths automatically.

## How to get it?
You can clone the project from GitHub:

```bash
git clone https://github.com/kasrairan13/path-finder.git
```

## Why use it?
- It is easy to use, only one file.
- It reads .gitignore and ignores folders you don’t want.
- It helps you import code from other folders without problems.

## License
This project is free and open source under the MIT License.
