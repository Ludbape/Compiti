def separa(st: str) -> str:
    st_risualtante = ""
    for i in st:
        if i == st[-1]:
            st_risualtante += i
            break
        st_risualtante += i + "-"
    return st_risualtante
