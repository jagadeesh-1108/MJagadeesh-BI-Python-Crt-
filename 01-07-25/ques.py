t = int(input("Enter the number of buffets: "))
for i in range(t):
    n = int(input("Enter the size of buffet: "))
    item = []
    for i in range(n):
        value = input("Enter the Dish: ")
        item.append(value)
    dish_types = set(item)
    max_dishes = 0
    result = item[0]
    for dish in dish_types:
        count = 0
        i = 0 
        while i<n:
            if item[i] == dish:
                count += 1
                i+=2
            else:
                i+=1
        if count > max_dishes or (count==max_dishes and dish < result):
            max_dishes = count
            result = dish
print(result)