# mkdocs-includex

This MkDocs plugin includes files in your markdown documents.

## Setup

Install the plugin using pip:

`pip3 install git+https://github.com/fxl0206/mkdocs-includex.git


Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - includex:
    src_path: docs/sources
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## Config

* `src_path` - The path to your source files

## Usage

Assuming you have a file at "docs/sources/hello.c" and that the `src_path` property is set to "docs/sources" add the following to your .md file to include it:

```md
{{ include('hello.c') }}
```
