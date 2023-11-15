import yaml


class ConfigMKDOCS:
    DEFAULT_CONFIG = {
        "mkdocsDir": "mkdocs",
        "mkdocsYAMLTemplate": {
            "site_name": "mkdocs site",
            "site_dir": "public",
            "theme": "readthedocs",
            "nav": [{"Home": "index.md"}, {"About": "about.md"}, {"Content": []}],
        },
        "contentSectionName": "Documentation",
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
        self.content_section_name = "Documentation"
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

        self.mkdocs_dir = config.get("mkdocsDir", self.DEFAULT_CONFIG["mkdocsDir"])
        self.mkdocs_yaml_template = config.get(
            "mkdocsYAMLTemplate", self.DEFAULT_CONFIG["mkdocsYAMLTemplate"]
        )
        self.content_section_name = config.get(
            "contentSectionName", self.DEFAULT_CONFIG["contentSectionName"]
        )
        self.index_file_content = config.get(
            "indexFileContent", self.DEFAULT_CONFIG["indexFileContent"]
        )
        self.about_file_content = config.get(
            "aboutFileContent", self.DEFAULT_CONFIG["aboutFileContent"]
        )
        self.doc_file_name = config.get(
            "docFileName", self.DEFAULT_CONFIG["docFileName"]
        )
        self.example_data_sub_dirs = config.get(
            "exampleDataSubDirs", self.DEFAULT_CONFIG["exampleDataSubDirs"]
        )
        self.scan_dir = config.get("scanDir", self.DEFAULT_CONFIG["scanDir"])

    def print_generator_config(self):
        """
        Print mkdocs generator settings to console in the YAML format
        """

        print(yaml.dump(self.DEFAULT_CONFIG, sort_keys=False))

    def save_mkdocs_config(self, mkdocs_yaml_file):
        try:
            with open(mkdocs_yaml_file, "w") as f:
                yaml.dump(self.mkdocs_yaml_template, f, sort_keys=False)
        except FileNotFoundError:
            raise FileNotFoundError("Could not save mkdocs config file")

    def update_content_list(self, new_content):
        old_content = self.mkdocs_yaml_template["nav"].copy()
        for item in old_content:
            if item.keys() == {"Content"}:
                item["Content"] = new_content
                break
        self.mkdocs_yaml_template["nav"] = old_content.copy()
