# cretate a function that prints the double of a number.
def stampa_doppio(n):
    """print the double of a number

    Args:
        n (int): any number you want to double
    """
    print(n * 2)
if __name__ == "__main__":
    n = int(input("Inserisci un numero: "))
    stampa_doppio(n)