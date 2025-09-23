from src.depo.utils import exist_path
from typing import List
import pathlib
from pathlib import Path


class DepoItem:
    def __init__(self, name, path: Path, structure=None):
        self._name = name
        self._path = path
        self._alias = None
        self._structure = structure
        self._steps_path = self._path / 'steps'
        self.id = None

    def __repr__(self):
        return f'DepoItem("Item: "{self.name}" on Structure: "{self._path.resolve().as_posix()}")'  #

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

    def destroy(self):
        try:
            print('destroing current item')
            self._path.rmdir()
        except OSError as e:
            print(f'Nie udało sie as {e}')


class AbstractDepo:
    def __init__(self):
        self._items = []


class DepoStructure:
    def __init__(self, structure: str):
        super().__init__()
        self.structure = pathlib.Path(structure)
        self.depo = self.structure / 'depo'
        self.configs = self.depo / '0000'
        self._items: List[DepoItem] = []
        self.validate_structure()
        self.init_structure()

    def items(self):
        return self._items

    def item(self, name):
        for item in self._items:
            if item.name == name:
                return item
        return None

    def __repr__(self):
        return f'DepoStructure({self.structure.resolve().as_posix()})'

    def init_structure(self):
        self._items = [DepoItem(name=item.name, path=Path(item), structure=self) for item in self.depo.iterdir() if
                       not item.as_posix().endswith('/0000')]

    def validate_structure(self):
        exist_path(self.depo)
        exist_path(self.configs)

    def create_item(self, name: str):
        if not self.item(name):
            item = self.depo / name
            rd = DepoItem(name=name, path=item, structure=self)
            self._items.append(rd)

        else:
            print('')

    def remove_item(self, name: str) -> None:
        if item := self.item(name):
            item.destroy()
        self._items.remove(item)


class Depo:
    def __init__(self, structures: List[DepoStructure]):
        super().__init__()
        self._structures = structures
        self._current_depo = self._structures[0]
        # self.init_structures()

    def items(self):
        structures_items = []
        for structure in self._structures:
            for curr_item in structure.items():
                structures_items.append(curr_item)
        return structures_items

    @property
    def current_structure(self):
        return self._current_depo


    def structures(self):
        return self._structures

    def set_current_depo(self, index: int) -> None:
        self._current_depo = self._structures[index]

    def add_structure(self, structure: DepoStructure) -> None:
        self._structures.append(structure)
        # self.append_structures(structure.items())

    # def append_structures(self, depo_items: List[DepoItem]) -> None:
    #     self._items.extend(depo_items)
    #
    # def init_structures(self) -> None:
    #     for index, _ in enumerate(range(len(self._structures))):
    #         self.append_structures(self._structures[index].items())


if __name__ == '__main__':
    dp = Depo([DepoStructure('../../tests/depo_project_1'), DepoStructure('../../tests/depo_project_2')])
    a = dp.items()
    b = dp.current_structure.items()
    dp.current_structure.create_item('9999')
    dp.current_structure.remove_item('0010' )
    dp.current_structure.remove_item('0030')
    print(a)
    print(b)
    dp.current_structure.remove_item('9999')
    print(a)
    print(b)
    dp.current_structure.create_item('0030')
    dp.current_structure.create_item('0033')
    dp.set_current_depo(1)
    dp.current_structure.create_item('0033')
    dp.current_structure.remove_item('0033')
    print(dp.items())
    print(dp.structures()[1].items())
