from src.depo.core import *
import pytest
import pathlib
import os

@pytest.fixture
def depo_structure():

    depos = [Depo(f'depo_project_1'),
             Depo(f'depo_project_2'),
             Depo(f'depo_project_3')]
    return depos

@pytest.fixture
def depo(depo_structure):
    return DepoCombaine(depo_structure)