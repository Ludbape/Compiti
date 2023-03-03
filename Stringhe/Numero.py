def main() -> None:
    stringa: str = input("Inserisci una stringa: ")
    if stringa.isnumeric():
        print("La stringa contiene solo numeri")
    else:
        print("La stringa contiene anche caratteri non numerici")


if __name__ == "__main__":
    main()
