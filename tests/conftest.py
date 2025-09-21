from src.depo.core import *
import pytest
import pathlib
import os

@pytest.fixture
def depo_structure():

    depos = [DepoStructure(f'depo_project_1'),
             DepoStructure(f'depo_project_2'),
             DepoStructure(f'depo_project_3')]
    return depos

@pytest.fixture
def depo(depo_structure):
    return Depo(depo_structure)