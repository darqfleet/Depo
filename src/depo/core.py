import pathlib
import os

from src.depo.exceptions import DepoWarning
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
        self.depo = f'{structure}/depo'
        self.configs = f'{self.depo}/0000'
        self.validate_structure()

    def validate_structure(self):
        exist_path(self.depo)
        exist_path(self.configs)

    def items(self):
        items = self.delete_0000(os.listdir(self.depo))
        return [DepoItem(name, parent=self) for name in items]

    def delete_0000(self, items: list) -> list:
        items.remove('0000')
        return items


class DepoCombain:
    def __init__(self, depos: List[DepoStructure]):
        self.depos = depos
        self.items = self.merge_structures()

    def merge_structures(self):
        DepoWarning('item not unique')
        items = []
        for index, v in enumerate(range(len(self.depos))):
            items.extend(self.depos[index].items())
        return items


if __name__ == '__main__':
    depos = [DepoStructure('/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/tests/depo_project_test'),
             DepoStructure('/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/tests/depo_project_test_second'),
             DepoStructure('/home/ydanilovsky@nolabel.local/PycharmProjects/Depo/tests/depo_project_test_third')]
    project = DepoCombain(depos)
    items = project.items
    print(items)
    # print(items.name)
