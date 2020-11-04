order = input("What do you want to order?")
pricelist = {"apples": 2, "bananas": 5}
quantity = int(input("How many?"))
priceofproduct= pricelist[order]
firstprice = priceofproduct * quantity
secondorder = input("Anything else?")
if secondorder == "no":
    print(firstprice)
else:
    order_2 = input("What do you want to order?")
    quantity2 = int(input("How many?"))
    priceofproduct2 = pricelist[order_2]
    secondprice = priceofproduct2 * quantity2
    totalprice = firstprice + secondprice
    print(totalprice)

