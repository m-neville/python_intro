def volume_cylinder(radius, height):
    """Calculates the volume of a cylinder """
    v = 22 / 7 * radius ** 2 * height
    return v


print(volume_cylinder(radius=7, height=10))
print(volume_cylinder(radius=10.65, height=32.33))

v1 = volume_cylinder(height=17, radius=10)


def volume_cone(radius, height, decimals=2):
    v = 1 / 3 * 22 / 7 * radius ** 2 * height
    v = round(v, decimals)
    return v


print(volume_cone(radius=8.5, height=6, decimals=3))
print(volume_cone(radius=7.2, height=5.9))