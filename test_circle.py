import pytest
from geo_figures import Circle
from geo_figures import Square


class TestCircle:
    @pytest.mark.parametrize("r, target_perimeter", [(2, 12.57), (-2, 12.57), (1.33, 8.36), (0, 0)])
    def test_circle_calculate_perimeter_valid(self, r, target_perimeter):
        cir = Circle(r)
        assert cir.perimeter == target_perimeter

    @pytest.mark.parametrize("r, target_area", [(2, 12.57), (-2, 12.57), (1.33, 5.56), (0, 0)])
    def test_circle_calculate_area_valid(self, r, target_area):
        cir = Circle(r)
        assert cir.area == target_area

    @pytest.mark.parametrize("r, a, sum_of_area", [(2, 4, 28.57), (-2, 1, 13.57), (1.77, 10, 109.84), (0, 2, 4)])
    def test_add_area_circle_and_square(self, a, r, sum_of_area):
        cir = Circle(r)
        sq = Square(a)
        assert cir.add_area(sq) == sum_of_area

    def test_add_area_circle_and_not_valid(self):
        r = 2
        cir = Circle(r)
        assert cir.add_area(1) == 'ошибка, введите фигуру'

    def test_circle_check_angles(self):
        r = 2
        cir = Circle(r)
        assert cir.angles == 0
