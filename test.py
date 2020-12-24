
from ex1 import tri
def test_tri():
    assert tri([1,2,5,3])== [1,2,3,5] , "test erroné pour une liste qui contient des nombres positive"
    assert tri([-1,-2,-3,-4])== [-4, -3, -2, -1], "test erroné pour qui contients des  mombres négatives"
    assert tri([-1,2,-2,5]) == [-2, -1, 2, 5], "test erroné pour les mombres réels"
