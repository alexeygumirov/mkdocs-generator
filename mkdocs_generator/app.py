"""
Functions to create mkdocs documentation from README.md files
"""
import os
import shutil
import frontmatter


def find_readme_files(directory: str = "./", file_name: str = "README.md") -> list:
    """
    Find all files with name README.md in directory and subdirectories

    :param directory: directory to search (default: current directory)

    :param file_name: name of file to search (default: README.md)
    """
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        files[:] = [f for f in files if not f.startswith(".")]
        for file in files:
            if file.endswith(file_name):
                list_of_files.append(os.path.join(root, file))
    return list_of_files


def make_mkdocs_dir(dir: str = "mkdocs") -> None:
    """
    Create directory mkdocs if it does not exist

    :param dir: directory name (default: mkdocs)
    """
    if not os.path.isdir(dir):
        os.system(f"mkdocs new {dir}")


def backup_mkdocs_dir(dir: str = "mkdocs/docs") -> None:
    """
    Backup directory mkdocs/docs if it exists

    :param dir: directory name (default: mkdocs/docs)
    """
    if os.path.isdir(dir) and os.listdir(dir):
        if os.path.isdir(dir.rstrip("/") + ".bak"):
            shutil.rmtree(dir.rstrip("/") + ".bak")
        shutil.move(dir, dir.strip("/") + ".bak")
        os.mkdir(dir)


def copy_documentation_files(
    source_dir: str = "./",
    destination_dir: str = "mkdocs/docs",
    file_name: str = "README.md",
    data_dirs: list = ["image", "images", "example", "examples"],
) -> None:
    """
    Copy documentation files to mkdocs/docs

    :param source_dir: source directory (default: current directory)

    :param destination_dir: destination directory (default: mkdocs/docs)

    :param file_name: name of file to search (default: README.md)

    :param data_dirs: list of sub-directories to copy (default: ["image", "images", "example", "examples"])
    """
    for file in find_readme_files(source_dir, file_name):
        file_dir = os.path.dirname(file.lstrip("./"))
        os.makedirs(os.path.join(destination_dir, file_dir), exist_ok=True)
        shutil.copy(file, os.path.join(destination_dir, file.lstrip("./")))
        for item in data_dirs:
            temp_path = os.path.join(file_dir, item)
            if os.path.isdir(temp_path) and os.listdir(temp_path):
                shutil.copytree(temp_path, os.path.join(destination_dir, temp_path))


def create_content_list(dir: str = "mkdocs/docs", file_name: str = "README.md") -> list:
    """
    Create list of dictionaries with title and path to README.md files for content section of mkdocs.yml

    :param dir: directory name (default: mkdocs/docs)

    :param file_name: name of file to search (default: README.md)
    """
    content_list = []
    readme_files = find_readme_files(dir, file_name)
    for file in readme_files:
        with open(file, "r") as f:
            metadata = frontmatter.load(f)
        if metadata.get("title"):
            content_list.append(
                {metadata.get("title"): file.replace(dir, "").lstrip("/")}
            )
    sorted_content_list = sorted(content_list, key=lambda k: list(k.keys())[0])
    return sorted_content_list
