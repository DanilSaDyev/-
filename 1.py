import math 
def distance_to_horizon(height):
    R = 6350
    distance = math.sqrt(2 * height * R + height**2)
    return distance

print("Расстояние до линии горизонта от точки с высотой 1км:", distance_to_horizon(1), "км")
print("Расстояние до линии горизонта от точки с высотой 2км:", distance_to_horizon(2), "км")
print("Расстояние до линии горизонта от точки с высотой 3км:", distance_to_horizon(3), "км")
print("Расстояние до линии горизонта от точки с высотой 4км:", distance_to_horizon(4), "км")
print("Расстояние до линии горизонта от точки с высотой 5км:", distance_to_horizon(5), "км")
print("Расстояние до линии горизонта от точки с высотой 6км:", distance_to_horizon(6), "км")
print("Расстояние до линии горизонта от точки с высотой 7км:", distance_to_horizon(7), "км")
print("Расстояние до линии горизонта от точки с высотой 8км:", distance_to_horizon(8), "км")
print("Расстояние до линии горизонта от точки с высотой 9км:", distance_to_horizon(9), "км")
print("Расстояние до линии горизонта от точки с высотой 10км:", distance_to_horizon(10), "км")
print("Расстояние до линии горизонта от точки с высотой 11км:", distance_to_horizon(11), "км")
print("Расстояние до линии горизонта от точки с высотой 12км:", distance_to_horizon(12), "км")
print("Расстояние до линии горизонта от точки с высотой 13км:", distance_to_horizon(13), "км")
print("Расстояние до линии горизонта от точки с высотой 14км:", distance_to_horizon(14), "км")
print("Расстояние до линии горизонта от точки с высотой 15км:", distance_to_horizon(15), "км")
