import pytest
from geo_figures import Triangle


class TestTriangle:

    @pytest.fixture()
    def triangle_1_2_3(self):
        tri = Triangle(1, 2, 3)
        return tri

    def test_calculate_perimeter_and_area(self, triangle_1_2_3):
        assert triangle_1_2_3.perimeter == 6
        assert triangle_1_2_3.area == 18.97

    def test_triangle_check_angles(self, triangle_1_2_3):
        assert triangle_1_2_3.angles == 3

    def test_triangle_check_name(self, triangle_1_2_3):
        assert triangle_1_2_3.name == 'triangle'

    def test_triangle_add_area_same_triangle(self, triangle_1_2_3):
        assert triangle_1_2_3.add_area(triangle_1_2_3) == 37.94

    def test_triangle_add_area_not_valid_figure(self, triangle_1_2_3):
        assert triangle_1_2_3.add_area('1, 2, 3') == 'ошибка, введите фигуру'
