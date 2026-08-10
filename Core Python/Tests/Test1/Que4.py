# Que4....Calculate the cost of painting the following building walls. You need to except and cost of the both exterior and interior walls.

area = int(input("Enter area of one wall: "))
exterior_wall = int(input("Enter cost of exterior wall: "))
interior_wall= int(input("Enter cost of interior wall: "))
interior_cost=interior_wall*area
exterior_cost=exterior_wall*area
total_cost = exterior_cost + interior_cost

print("Total painting cost =", total_cost)