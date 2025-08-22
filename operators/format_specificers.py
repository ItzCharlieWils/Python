#format specificers ={value :flags} format a value based on whatflags are inserted
#                             flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate 3 spaces, fill with zeroes
# :< = left justify
# :> = right justify
# :^ = center justify
# :0 = fill with zeroes
# :+ = always show sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator


price1 = 3.1415
price2 = -987.65
price3 = 12.34

print(f"price 1 is {price1:.3f}")
print(f"price 2 is {price2:.3f}")
print(f"price 3 is {price3:.1f}")

print(f"price 1 is ${price1:+}")
print(f"price 2 is ${price2:+}")
print(f"price 3 is ${price3:+}")

print(f"Price 1 is ${price1:,.2f}")
print(f"Price 2 is ${price2:,.2f}")
print(f"Price 3 is ${price3:,.2f}")
