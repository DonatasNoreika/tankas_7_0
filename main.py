from tankas import Tankas

tankas = Tankas()

while True:
    tankas.musio_laukas()
    tankas.info()
    pasirinkimas = int(input("""
1 - pirmyn
2 - atgal
3 - kairen
4 - desinen
5 - sauti
0 - iseiti
"""))
    match pasirinkimas:
        case 1:
            tankas.pirmyn()
        case 2:
            tankas.atgal()
        case 3:
            tankas.kairen()
        case 4:
            tankas.desinen()
        case 5:
            tankas.sauti()
        case 0:
            break
