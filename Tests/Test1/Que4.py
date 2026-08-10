# Que4....Calculate the cost of painting the following building walls. You need to except and cost of the both exterior and interior walls.

area = float(input("Enter area of one wall: "))
ec = float(input("Enter cost of exterior wall: "))
ic = float(input("Enter cost of interior wall: "))
exterior_area = area * 2
interior_area = area * 2
exterior_cost = exterior_area * ec
interior_cost = interior_area * ic
total_cost = exterior_cost + interior_cost
print("Exterior painting cost =", exterior_cost)
print("Interior painting cost =", interior_cost)
print("Total painting cost =", total_cost)