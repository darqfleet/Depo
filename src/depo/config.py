import yaml
from pathlib import Path

class Config:
    EXTESIONS = ('.yaml', '.toml')
    def __init__(self, configs_dir: Path):
        self._config_dir = configs_dir
        self._all_configs = {}
        self.configure()

    def configure(self):
        self.explore_configs()

    def set_configs_dir(self, path):
        self._config_dir = path
        self.configure()

    def explore_configs(self):
        for c in self._config_dir.iterdir():
            if c.suffix in Config.EXTESIONS:
                config_name = c.name.split('.')[0]
                self._all_configs[config_name] = c

    def get_one(self, name):
        return self._all_configs.get(name)

    @staticmethod
    def config_data(config_file_path):
        with open(config_file_path, 'r') as file:
            if str(config_file_path).endswith('yaml'):
                data = yaml.safe_load(file)
                return data
        return file.readlines()

    @property
    def all_configs(self):
        return self._all_configs
