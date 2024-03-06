from Conic_Section_Class import Conic_Section
def get_shape(CS:Conic_Section):
    Delta = CS.B ** 2 - 4 * CS.A * CS.C
    if Delta < 0 and CS.A != CS.C and CS.B != 0:
        return f"This is an elipse!"
    if Delta < 0 and CS.A == CS.C and CS.B == 0:
        return f"This is a circle!"
    if Delta == 0:
        return f"This is a parabola!"
    if Delta > 0 and CS.A + CS.C != 0:
        return f"This is a hyperbola!"
    if Delta > 0 and CS.A + CS.C == 0:
        return f"This is a rectangular hyperbola!"
