item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"   # 7.5% sales tax

print('=' *40)
print("STORE RECEIPT")
print('=' *40)

print(f"{item1_name} ${item1_price:} x {item1_qty:} = ${float(item1_price) * int(item1_qty):.2f}")
print(f"{item2_name} ${item2_price:} x {item2_qty:} = ${float(item2_price) * int(item2_qty):.2f}")
print(f"{item3_name} ${item3_price:} x {item3_qty:} = ${float(item3_price) * int(item3_qty):.2f}")
print('-' *40)
print(f"Subtotal: ${float(item1_price) * int(item1_qty) + float(item2_price) * int(item2_qty) + float(item3_price) * int(item3_qty):.2f}")
print(f"Tax: ${((float(item1_price) * int(item1_qty) + float(item2_price) * int(item2_qty) + float(item3_price) * int(item3_qty)) * float(tax_rate)):.2f}")
print ('=' *40)# to seperate the total from the rest of the receipt.
print(f"Total: ${((float(item1_price) * int(item1_qty) + float(item2_price) * int(item2_qty) + float(item3_price) * int(item3_qty)) * (1 + float(tax_rate))):.2f}")
print('=' *40)


                                                            
                                                