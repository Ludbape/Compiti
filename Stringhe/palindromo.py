def palindromo(s: str):
    return True if s == s[::-1] else False


def main():
    st = input("Inserisci uan stringa:")
    if palindromo(st):
        print("La parola inserita è palidroma")
    else:
        print("La parola inserita non è palidroma")


if __name__ == "__main__":
    main()
