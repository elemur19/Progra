print("\n=== Fibonacci ==== ")

while True:

    n = int(input("\nIngrese el numero que quiere imprimir: "))

    if n <= 0:
        print("Invalido. ")
    else:
        a = 0
        b = 1

    print("\nFibonacci de", n, "es:")
    for i in range(n):
            print( a, end=" ")
            siguiente = a + b 
            a = b
            b = siguiente
    print()
