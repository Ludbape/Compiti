def elevamento(base: int, esp: int) -> int:
    if esp == 0:
        return 1
    else:
        return base * elevamento(base, esp - 1)
