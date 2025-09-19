import os
from utils import exist_path
from typing import List


class DepoItem:
    def __init__(self, name, parent=None):
        self.__name = name
        self.__alias = None
        self.parent = parent
        self.id = None

    def __repr__(self):
        return f'DepoItem("{self.name}")'

    @property
    def name(self):
        return self.__name

    @property
    def alias(self):
        return f'alias_for {self.__name}'

    def get(self):
        return self.__name


class DepoStructure:
    def __init__(self, structure: str, db=None):
        self.db = db
        self.structure = structure
        self.depo = f'{structure}/depo'
        self.configs = f'{self.depo}/0000'
        self.validate_structure()

    def __repr__(self):
        return f'DepoStructure({self.structure})'

    def validate_structure(self):
        exist_path(self.depo)
        exist_path(self.configs)

    def items(self) -> List[DepoItem]:
        depo_items = self.exclude_pipeline_catalog(os.listdir(self.depo))
        return [DepoItem(name, parent=self) for name in depo_items]

    @staticmethod
    def exclude_pipeline_catalog(depo_items: List[str]) -> List[str]:
        depo_items.remove('0000')
        return depo_items


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
    depos = [DepoStructure('/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/tests/depo_project_1'),
             DepoStructure('/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/tests/depo_project_2'),
             DepoStructure('/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/tests/depo_project_3')]
    project = Depo(depos)
    itm = project.items()
    for i in itm:
        print(i.parent)
