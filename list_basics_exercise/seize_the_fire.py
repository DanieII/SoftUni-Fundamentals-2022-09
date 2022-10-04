fires = input().split("#")
water = int(input())
tracking_put_out_cells = []
total_fire_put_out = 0
for current_cell in fires:
    cell = current_cell.split(" = ")
    type_of_fire = cell[0]
    value_of_cell = int(cell[1])
    if water - value_of_cell < 0:
        continue
    elif type_of_fire == "High" and 81 <= value_of_cell <= 125:
        water -= value_of_cell
        tracking_put_out_cells.append(value_of_cell)
    elif type_of_fire == "Medium" and 51 <= value_of_cell <= 80:
        water -= value_of_cell
        tracking_put_out_cells.append(value_of_cell)
    elif type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        water -= value_of_cell
        tracking_put_out_cells.append(value_of_cell)
effort = sum(tracking_put_out_cells) * 0.25
print("Cells:")
for cells_put_out in tracking_put_out_cells:
    print(f"- {cells_put_out}")
    total_fire_put_out += cells_put_out
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_put_out}")
