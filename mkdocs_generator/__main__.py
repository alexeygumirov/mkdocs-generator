"""
This script generates an mkdocs.yml file for documentation based on the provided configuration settings and directory structure.

Usage:
    python generate_mkdocs.py [--config CONFIG] [--print-config] [--backup] [--scan-dir SCAN_DIR] [--version]

Arguments:
    --config CONFIG, -c CONFIG
        Path to a YAML file with configuration settings. If not provided, default settings will be used.

    --print-config, -p
        Print the default configuration settings.

    --backup, -b
        Backup the existing docs directory if it exists. If not provided, the existing directory will be deleted and a new one will be created.

    --scan-dir SCAN_DIR, -s SCAN_DIR
        Path to the directory to be scanned for documentation files. Default is the current directory.

    --section-name SECTION_NAME, -n SECTION_NAME
        Name of the section under 'Content' in mkdocs.yml. Default is "Documentation".

    --version
        Print the version of the script.

Example:
    python generate_mkdocs.py --config config.yml --backup --scan-dir /path/to/docs

"""

import os
import argparse
import shutil
import mkdocs_generator.app as app
from mkdocs_generator.generate_config import ConfigMKDOCS


__version__ = "0.1.0"
parser = argparse.ArgumentParser(
    description="Generate mkdocs.yml file for documentation"
)
parser.add_argument(
    "--config",
    "-c",
    type=str,
    default="none",
    help="Path to YAML file with configuration settings",
)
parser.add_argument(
    "--print-config", "-p", action="store_true", help="Print default configuration"
)
parser.add_argument(
    "--backup",
    "-b",
    action="store_true",
    help="Backup existing docs directory if it exists",
)
parser.add_argument(
    "--scan-dir",
    "-s",
    type=str,
    default="./",
    help="Path to a directory to scan for files",
)
parser.add_argument(
    "--section-name",
    "-n",
    type=str,
    default="Documentation",
    help="Name of the documentation section in mkdocs.yml",
)
parser.add_argument("--version", action="version", version=("%(prog)s " + __version__))


def main():
    config = ConfigMKDOCS()

    args = parser.parse_args()
    if args.print_config:
        config = ConfigMKDOCS()
        config.print_generator_config()
        return

    # Load YAML file with settings
    if args.config != "none":
        config.load_generator_config(args.config)

    # Scan directory for documentation files
    if args.scan_dir != "./":
        if not os.path.exists(args.scan_dir):
            print("Error: Directory does not exist: " + args.scan_dir)
            return
        config.scan_dir = args.scan_dir
    # Create .mkdocs directory if it does not exist
    app.make_mkdocs_dir(config.mkdocs_dir)

    # Set content section name
    if args.section_name != "Documentation":
        config.content_section_name = args.section_name

    # Backup .mkdocs/docs directory if it exists otherwise delete it and create a new one
    if args.backup:
        app.backup_mkdocs_dir(os.path.join(config.mkdocs_dir, "docs"))
    else:
        if os.path.exists(os.path.join(config.mkdocs_dir, "docs")):
            shutil.rmtree(os.path.join(config.mkdocs_dir, "docs"))
        os.makedirs(os.path.join(config.mkdocs_dir, "docs"), exist_ok=True)

    # Create index.md and about.md files in .mkdocs/docs directory
    with open(os.path.join(config.mkdocs_dir, "docs", "index.md"), "w") as index_file:
        index_file.write(config.index_file_content)
    with open(os.path.join(config.mkdocs_dir, "docs", "about.md"), "w") as about_file:
        about_file.write(config.about_file_content)

    # Copy documentation files to .mkdocs/docs directory
    app.copy_documentation_files(
        config.scan_dir,
        os.path.join(config.mkdocs_dir, "docs"),
        config.doc_file_name,
        config.example_data_sub_dirs,
    )

    # Create content list for mkdocs.yml
    new_content = [{config.content_section_name: app.create_content_list()}]
    config.update_content_list(new_content)

    # Write mkdocs.yml file
    config.save_mkdocs_config(os.path.join(config.mkdocs_dir, "mkdocs.yml"))


if __name__ == "__main__":
    main()
