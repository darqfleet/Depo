import yaml
from pathlib import Path
from src.depo_gui import CONFIG_DIR


class Config:
    def __init__(self, configs_dir: Path):
        self._config_dir = configs_dir
        self._all_configs = []
        self._config: str | None = None
        self.configure()

    def configure(self):
        self.explore_configs()

    def set_configs_dir(self, path):
        self._config_dir = path
        self.configure()

    def explore_configs(self):
        for c in self._config_dir.iterdir():
            self._all_configs.append(c)

    def config_data(self, index: int):
        config_file_path = str(self._all_configs[index])
        with open(config_file_path, 'r') as file:
            if config_file_path.endswith('yaml'):
                data = yaml.safe_load(file)
                return data
        return file.readlines()

    @property
    def config_list(self):
        return self._all_configs

if __name__ == '__main__':
    a = Config(CONFIG_DIR / 'themes')
    print(a.config_data(5))