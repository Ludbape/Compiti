def vocali_maiuscolo(st: str) -> str:
    st_risultante = ""
    vocali = "aeiouèéùòà"
    for i in st:
        if i in vocali:
            st_risultante += i.upper()
        else:
            st_risultante += i

    return st_risultante
