from src.depo.utils import exist_path
from typing import List
import pathlib

class AbstractDepo:
    pass

class DepoItem:
    def __init__(self, name, path, structure=None):
        self._name = name
        self._path = path
        self._alias = None
        self._structure = structure
        self._steps_path = self._path / 'steps'
        self.id = None

    def __repr__(self):
        return f'DepoItem("Item: "{self.name}" on Structure: "{self._path.resolve().as_posix()}")'


    @property
    def name(self):
        return self._name


    @property
    def alias(self):
        return f'alias_for {self._name}'

    @property
    def steps(self):
        return [step for step in self._path.iterdir()]

    def structure(self):
        return self._structure


    def get(self):
        return self._name


class DepoStructure:
    def __init__(self, structure: str, db=None):
        self.db = db
        self.structure = pathlib.Path(structure)
        self.depo = self.structure / 'depo'
        self.configs = self.depo / '0000'
        self._items:List[DepoItem] = []
        self.validate_structure()
        self.init_structure()


    def __repr__(self):
        return f'DepoStructure({self.structure.resolve().as_posix()})'

    def init_structure(self):
        self._items = self.items()


    def validate_structure(self):
        exist_path(self.depo)
        exist_path(self.configs)


    def items(self) -> List[DepoItem]:
        return [DepoItem(name=item.name, path=item, structure=self) for item in self.depo.iterdir() if not item.as_posix().endswith('/0000')]


    def item(self):
        pass

    def create_item(self):
        pass

    def remove_item(self):
        pass

class Depo:
    def __init__(self, structures: List[DepoStructure]):
        self._structures = structures
        self._current_depo = self._structures[0]
        self._items: List[DepoItem] = []
        self.init_structures()


    def structures(self):
        return self._structures


    def items(self):
        return self._items


    def item(self, name: str):
        for i in self._items:
            if i.name == name:
                return i
        return None


    def set_current_depo(self, index:int) -> None:
        self._current_depo = self._structures[index]


    def add_depo(self, structure: DepoStructure) -> None:
        self._structures.append(structure)
        self.append_structures(structure.items())


    @property
    def current_depo(self) -> DepoStructure:
        return self._current_depo


    def append_structures(self, depo_items: List[DepoItem]) -> None:
        self._items.extend(depo_items)


    def init_structures(self) -> None:
        for index, _ in enumerate(range(len(self._structures))):
            self.append_structures(self._structures[index].items())


if __name__ == '__main__':
    dp = Depo([DepoStructure('../../tests/depo_project_1')])
    print(dp.item('0030'))