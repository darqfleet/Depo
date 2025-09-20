import os
from utils import exist_path
from typing import List
import pathlib

class DepoItem:
    def __init__(self, name, path, parent=None):
        self._name = name
        self._path = path
        self._alias = None
        self._parent = parent
        self.id = None

    def __repr__(self):
        return f'DepoItem("{self.name} {self._path}")'

    @property
    def name(self):
        return self._name

    @property
    def alias(self):
        return f'alias_for {self._name}'

    def get(self):
        return self._name


class DepoStructure:
    def __init__(self, structure: str, db=None):
        self.db = db
        self.structure = pathlib.Path(structure)
        self.depo = self.structure / 'depo'
        self.configs = self.depo / '0000'
        self.validate_structure()

    def __repr__(self):
        return f'DepoStructure({self.structure.resolve().as_posix()})'

    def validate_structure(self):
        exist_path(self.depo)
        exist_path(self.configs)

    def items(self) -> List[DepoItem]:
        return [DepoItem(name=item.name, path=item, parent=self) for item in self.depo.iterdir() if not item.as_posix().endswith('/0000')]


class Depo:
    def __init__(self, structures: List[DepoStructure]):
        self._structures = structures
        self._current_depo = self._structures[0]
        self._items: List[DepoItem] = []
        self.merge_structures()

    def items(self):
        return self._items

    def set_current_depo(self):
        # TODO
        pass

    def add_depo(self):
        # TODO
        pass

    @property
    def current_depo(self):
        return self._current_depo

    def append_structures(self, depo_items: List[DepoItem]) -> None:
        self._items.extend(depo_items)

    def merge_structures(self) -> None:
        for index, _ in enumerate(range(len(self._structures))):
            self.append_structures(self._structures[index].items())


if __name__ == '__main__':
    depos = [DepoStructure('../../tests/depo_project_1'),]
    #          DepoStructure('../depo_project_2'),
    #          DepoStructure('/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/tests/depo_project_3')]
    project = Depo(depos)
    itm = project.items()
    for i in itm:
        print(i)

    # a = pathlib.Path('/mnt/alien2')
    # b = pathlib.Path('/mnt/alien')
    # d = pathlib.Path('/mnt/alien3')
    # c =[a, b]
    # print(d in c)
