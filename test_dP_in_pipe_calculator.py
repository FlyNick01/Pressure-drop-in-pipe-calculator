from project import q_to_v, Re, fric_coef, h_f
import math

def test_q_to_v():
    assert q_to_v(1,1) == 4/math.pi
    assert q_to_v(math.pi,1) == 4

def test_Re():
    assert Re(1,1,1,1) == 1
    assert Re(2,2,1,1) == 1

def test_fric_coef():
    assert fric_coef(64, 0.01, 2) == 1

def test_h_f():
    assert h_f(1,1,1,1,1) == 1/2
    assert h_f(2,1,1,1,1) == 1

