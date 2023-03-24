def nascondi(s: str, to_hide: str) -> str:
    return (
        s.replace(to_hide, len(to_hide) * "*")
        if to_hide in s
        else "La stringa da nascondere non è presente nella frase"
    )


def main() -> None:
    f = input("Insersci una frase: ")
    p = input("Inserisci ciò che vuoi nascondere: ")
    print(nascondi(f, p))


if __name__ == "__main__":
    main()
