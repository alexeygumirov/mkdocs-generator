import yaml


class ConfigMKDOCS:
    """
    Class to generate configuration for this mkdocs generator and for mkdocs
    """
    DEFAULT_CONFIG = {
        "mkdocsDir": "mkdocs",
        "mkdocsYAMLTemplate": {
            "site_name": "mkdocs site",
            "site_dir": "public",
            "theme": "readthedocs",
            "nav": [{"Home": "index.md"}, {"About": "about.md"}, {"Content": []}],
        },
        "indexFileContent": """# Index

    This is the mkdocs generated documentation site.""",
        "aboutFileContent": """# About

    This is automatically generated documentation.""",
        "docFileName": "README.md",
        "exampleDataSubDirs": ["image", "images", "example", "examples"],
        "scanDir": "./",
    }

    def __init__(self):
        """
        Generate default settings for mkdocs.yml
        """
        self.mkdocs_dir = "mkdocs"
        self.mkdocs_yaml_template = {
            "site_name": "mkdocs site",
            "site_dir": "public",
            "theme": "readthedocs",
            "nav": [
                {"Home": "index.md"},
                {"About": "about.md"},
                {"Content": []},
            ],
        }
        self.index_file_content = """# Index

    This is the mkdocs generated documentation site."""
        self.about_file_content = """# About

    This is automatically generated documentation."""
        self.doc_file_name = "README.md"
        self.example_data_sub_dirs = ["image", "images", "example", "examples"]
        self.scan_dir = "./"

    def load_generator_config(self, yaml_file):
        """
        Load settings from YAML file

        :param yaml_file: YAML file with settings
        """
        try:
            with open(yaml_file, "r") as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            config = self.DEFAULT_CONFIG

        self.mkdocs_dir = config.get("mkdocsDir", ".mkdocs")
        self.mkdocs_yaml_template = config.get("mkdocsYAMLTemplate")
        self.index_file_content = config.get("indexFileContent")
        self.about_file_content = config.get("aboutFileContent")
        self.doc_file_name = config.get("docFileName", "README.md")
        self.example_data_sub_dirs = config.get(
            "exampleDataSubDirs", ["image", "images", "example", "examples"]
        )
        self.scan_dir = config.get("scanDir", "./")

    def print_generator_config(self):
        """
        Print mkdocs generator settings to console in the YAML format
        """
        print(yaml.dump(self.DEFAULT_CONFIG, sort_keys=False))

    def save_mkdocs_config(self, mkdocs_yaml_file):
        """
        Save mkdocs config file

        :param mkdocs_yaml_file: path to mkdocs.yml
        """
        try:
            with open(mkdocs_yaml_file, "w") as f:
                yaml.dump(self.mkdocs_yaml_template, f, sort_keys=False)
        except FileNotFoundError:
            raise FileNotFoundError("Could not save mkdocs config file")

    def update_content_list(self, new_content):
        """
        Update content list in the navigation section of the mkdocs.yml

        :param new_content: new content list
        """
        old_content = self.mkdocs_yaml_template["nav"].copy()
        for item in old_content:
            if item.keys() == {"Content"}:
                item["Content"] = new_content
                break
        self.mkdocs_yaml_template["nav"] = old_content.copy()
