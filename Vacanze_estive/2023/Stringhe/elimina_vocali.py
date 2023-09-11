def elimina_vocali(stringa: str) -> str:
    vocali = "aeiouAEIOUèéÈÉÒòùÙàÀ"
    str_risultante = ""
    for lettera in stringa:
        if lettera not in vocali:
            str_risultante += lettera
    return str_risultante
