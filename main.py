from tankas import Tankas

tankas = Tankas()

while True:
    tankas.info()
    pasirinkimas = int(input("""
1 - pirmyn
2 - atgal
3 - kairen
4 - desinen
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
        case 0:
            break
