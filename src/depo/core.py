from src.depo.utils import exist_path
from typing import List
import pathlib
from pathlib import Path


class AbstractDepoUnit:
    def __init__(self, name, path: Path, depo=None, parent=None):
        self._name = name
        self._path = path
        self._alias = None
        self._depo = depo
        self._space = None
        self._parent = parent
        self._id = None

    @property
    def depo(self):
        return self._depo

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path

    @property
    def id(self):
        return self._id

    @property
    def alias(self):
        return self._alias


class Step(AbstractDepoUnit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._status = None
        self.prefix = None
        self.init_step()

    def init_step(self):
        step = self.path
        if not step.exists():
            step.mkdir()

    def __repr__(self):
        return f'Step: {self.name}, on DepoItem(name={self._parent.name})'


class DepoItem(AbstractDepoUnit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._alias = None
        self._steps_path = self._path / 'steps'
        self.init_standart_structures()

    def init_standart_structures(self):
        self.path.mkdir(exist_ok=True)
        std_steps = ('steps', 'render', 'source')
        for step in std_steps:
            path = self.path / step
            if not path.exists():
                path.mkdir()

    def __repr__(self):
        return f'DepoItem("Item: "{self.name}" on Structure: "{self._path.resolve().as_posix()}")'  #

    @property
    def steps(self):
        return [Step(path=step, name=step.name, depo=self.depo, parent=self) for step in self._steps_path.iterdir() if
                step.is_dir()]

    def create_step(self, name, prefix=''):
        if prefix:
            name = f'{prefix}_{name}'
        return Step(name=name, path=self._steps_path / name, depo=self.depo)

    def change_depo(self):
        # move all item with content to another depo
        pass  # TODO

    def destroy(self):
        try:
            print('destroying current item')
            self._path.rmdir()
        except OSError as e:
            # TODO
            # remove all content
            print(f'Nie udało sie as {e}')


class Depo:
    def __init__(self, path: str):
        super().__init__()
        self._path = pathlib.Path(path)
        self._depo = self._path / 'depo'
        self._configs = self._depo / '0000'
        self._items: List[DepoItem] = []
        self.validate_depo()
        self.init_depo_items()

    def items(self):
        return self._items

    def find(self, name):
        for item in self._items:
            if item.name == name:
                return item
        return None

    def __repr__(self):
        return f'DepoStructure({self._path.resolve().as_posix()})'

    def init_depo_items(self):
        self._items = [DepoItem(name=item.name, path=Path(item), depo=self) for item in self._depo.iterdir() if
                       not item.as_posix().endswith('/0000')]

    def validate_depo(self):
        exist_path(self._depo)
        exist_path(self._configs)

    def create_item(self, name: str):
        if not self.find(name):
            item = self._depo / name
            rd = DepoItem(name=name, path=item, depo=self)
            self._items.append(rd)
        else:
            print('')

    def remove_item(self, name: str) -> None:
        if item := self.find(name):
            item.destroy()
            self._items.remove(item)

    @classmethod
    def create_depo(cls, path):
        Path(path).mkdir()
        return cls(path)

class DepoCombine:
    def __init__(self, depos: List[Depo]):
        super().__init__()
        self._depos = depos
        self._current_depo = self._depos[0]

    def items(self) -> List[DepoItem]:
        depos_items = []
        for depo in self._depos:
            for item in depo.items():
                depos_items.append(item)
        return depos_items

    def find(self, name) -> DepoItem | None:
        for depo in self._depos:
            if itm := depo.find(name):
                return itm
        return None

    @property
    def current_depo(self) -> Depo:
        return self._current_depo

    def all_depos(self) -> List[Depo]:
        return self._depos

    def set_current_depo(self, index: int) -> None:
        self._current_depo = self._depos[index]

    def add_depo(self, depo: Depo) -> None:
        self._depos.append(depo)


if __name__ == '__main__':
    dp = DepoCombine([Depo('../../tests/depo_project_1'), Depo('../../tests/depo_project_2')])
    dp.set_current_depo(1)
    print(dp.current_depo)
    new = '3333'
    dp.current_depo.create_item(new)
    tt = dp.find(new)
    tt.create_step('cokolwiek')
    tt.create_step('fx_water')
    tt.create_step('fx_dust')
    tt.create_step('bom bom')
    for s in tt.steps:
        print(s)
