# Simple cash register
itemCost=input('please enter the cost of the item: ')
cashPaid=input('enter the cash given:')
Change=int(cashPaid)-int(itemCost)
print('Your item costs $'+ str(itemCost) +'and you gave me $'+str(cashPaid) +\
      'dollars. Your change is $'+str(Change) )
