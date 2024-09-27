from point import Point
from triangle import Triangle
from rectangle import Rectangle
from cercle import Cercle

p1 = Point(2,3)
p2 = Point(2,6)
t1 = Triangle(p1,3,4)
c1 = Cercle(p2,3)
c2 = Cercle(p1, 2)
r1 = Rectangle(p1,5,2)

def test_distance_coordonnee():
    assert p1.distanceCoord(2,3) == 0

def test_distance_point():
    assert  p1.distancePoint(p2) == 3

def test_hypothenuse():
    assert t1.hypothenuse() == 5

def test_isocele():
    assert t1.isocele() == False

def test_perimetre():
    assert t1.perimetre() == 12
    assert t1.surface() == 6

def test_diametre():
    assert c1.diametre() == 6

def test_perimetre():
    assert round(c1.perimetre(),2) == 18.85

def test_cercle_surface():
    assert round(c1.surface(),2) == 28.27

def test_cercle_intersection():
    assert c1.intersection(c2) == True

def test_cercle_point():
    assert c1.point(5,6) == True

def test_rectangle_surface():
    assert r1.surface() == 10

def test_rectangle_perimetre():
    assert r1.perimetre() == 14

def test_rectangle_point():
    assert r1.point(p1) == True

def test_rectangle_points():
    assert r1.points() == [[2, 5], [7, 5], [2, 3], [7, 3]]

