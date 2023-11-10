# `mkdocs-generate` program

This script creates a `mkdocs` static site from a directory of documentation files.
The generated static site is used with [MkDocs](https://www.mkdocs.org/) to build and serve the documentation.
It scans through all subdirectories of the given directory and searched for the documentation files (`markdown`), images and examples.

Then it creates new `mkdocs` project directory (if it is not already present) and copies all files to the relevant subdirectories into the `docs` directory of the `mkdocs` project.

```sh
./mkdocs
├── docs
│   ├── about.md
│   ├── index.md
│   ├── ipam/...
│   ├── vpc/...
│   └── ...
└── mkdocs.yml
```

The script also generates a `mkdocs.yml` file based on the provided configuration settings and directory structure.

## Requirements for the documentation files metadata

The script uses the title from the metadata of the documentation files to generate the navigation structure of the `mkdocs` site.
The metadata is stored in the YAML format in the beginning of the documentation file.

```markdown
---
title: "Title of the documentation file"
---

# Title of the documentation file

Content...
```

## Installation

1. Create Python virtual environment and activate it:
2. Clone the script repository
3 Install the script using `pip`:

```sh
pip install mkdocs-generate/.
```

## Parameters

```
mkdocs-generate [--config CONFIG] [--print-config] [--backup] [--scan-dir SCAN_DIR] [--version]
```

- `--config CONFIG, -c CONFIG`: Path to a YAML file with configuration settings. If not provided, default settings will be used.
- `--print-config, -p`: Print the default configuration settings.
- `--backup, -b`: Backup the existing docs directory if it exists. If not provided, the existing directory will be deleted and a new one will be created.
- `--scan-dir SCAN_DIR, -s SCAN_DIR`: Path to the directory to be scanned for documentation files. Default is the current directory.
- `--version`: Print the version of the script.

### Example

```
mkdocs-generate -c generate_config.yml -b -s ./tf-modules
```

## Version

0.1.0

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
