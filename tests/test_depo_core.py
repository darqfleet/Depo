from src.depo.core import DepoItem

class TestDepo:
    def test_current_default(self, depo, depo_structure):
        assert depo.current_depo == depo_structure[0]

    def test_length(self, depo):
        assert len(depo.all_depos()) == 3

    def test_length_items(self, depo):
        assert len(depo.items()) == 9

    def test_items(self, depo):
        item = depo.find('0030')
        assert isinstance(item, DepoItem)