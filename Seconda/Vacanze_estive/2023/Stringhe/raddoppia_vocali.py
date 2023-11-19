def raddoppia_vocali(stringa: str) -> str:
    vocali = "aeiouAEIOUèéÈÉÒòùÙàÀ"
    str_risultante = ""
    for lettera in stringa:
        if lettera in vocali:
            str_risultante += 2 * lettera
        else:
            str_risultante += lettera
    return str_risultante
