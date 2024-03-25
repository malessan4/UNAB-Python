# Si el número es múltiplo de 3 -> Fizz
# Si el número es múltiplo de 5 -> Buzz
# Si el número es múltiplo de 5 y además de 3 -> FizzBuzz
# Si no es múltiplo de 3 o de 5 -> número

for numero in range (0, 50):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
        