from tinyec.ec import SubGroup, Curve

field = SubGroup(p=37, g=(2, 9), n=42, h=14)
curve = Curve(a=2, b=9, field=field, name='p3709')
print('curve:', curve)

for k in range(0, 42):
    p = k * curve.g
    print(f"{k} * G = ({p.x}, {p.y})")
