import pytest
from geo_figures import Square


class TestSquare:
    @pytest.mark.parametrize("a, target_perimeter", [(2, 8), (-2, 8), (1.33, 5.32), (0, 0)])
    def test_square_calculate_perimeter_valid(self, a, target_perimeter):
        sq = Square(a)
        assert sq.perimeter == target_perimeter

    @pytest.mark.parametrize("a, target_area", [(2, 4), (-2, 4), (1.33, 1.77), (0, 0)])
    def test_square_calculate_area_valid(self, a, target_area):
        sq = Square(a)
        assert sq.area == target_area

    @pytest.mark.parametrize("a1, a2, sum_of_area", [(2, 4, 20), (-2, 1, 5), (1.77, 10, 103.13), (0, 2, 4)])
    def test_add_area_square_and_square(self, a1, a2, sum_of_area):
        sq1 = Square(a1)
        sq2 = Square(a2)
        assert sq1.add_area(sq2) == sum_of_area

    def test_add_area_square_and_not_valid(self):
        a = 2
        sq1 = Square(a)
        assert sq1.add_area('square') == 'ошибка, введите фигуру'

    def test_square_check_name(self):
        a = 2
        sq1 = Square(a)
        assert sq1.name == "square"
