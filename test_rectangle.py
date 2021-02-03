import pytest
from geo_figures import Rectangle
from geo_figures import Square


class TestRectangle:
    @pytest.mark.parametrize("a, b, target_perimeter", [(1, 2, 6), (-2, 1.7, 7.4)])
    def test_rectangle_calculate_perimeter_valid(self, a, b, target_perimeter):
        rec = Rectangle(a, b)
        assert rec.perimeter == target_perimeter

    @pytest.mark.parametrize("a, b, target_area", [(1, 2, 2), (-2, 1.7, 3.4)])
    def test_rectangle_calculate_area_valid(self, a, b, target_area):
        rec = Rectangle(a, b)
        assert rec.area == target_area

    @pytest.mark.parametrize("a, b, r, sum_of_area", [(2, 4, 2, 12), (-2, 1, 3, 11)])
    def test_add_area_rectangle_and_square(self, a, b, r, sum_of_area):
        rec = Rectangle(a, b)
        sq = Square(r)
        assert rec.add_area(sq) == sum_of_area
        assert sq.add_area(rec) == sum_of_area

    def test_add_area_rectangle_and_not_valid_class_of_figure(self):
        a = b = r = 2
        rec = Rectangle(a, b)
        sq = Square(r)
        sq.name = 'other_figure'
        assert rec.add_area(
            sq) == 'ошибка, введите фигуру, являющуюся объектом классов Triangle, Rectangle, Square, Circle'

    def test_rectangle_check_angles(self):
        a = b = 2
        rec = Rectangle(a, b)
        assert rec.angles == 4
