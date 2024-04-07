numbers = []
while True:
    num = input("Enter a number (or 'done' vaghti ke adad hara vared kardid):")
    
    if num.lower() == 'done':
        break
    
    try:
        num = float(num)
        numbers.append(num)
    except ValueError:
        print("bayad adad vared konid.")
        
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"miangin adad ha => : {average}")
else:
    print("ghabl as vared kardan 'done' adad vared konid.")

