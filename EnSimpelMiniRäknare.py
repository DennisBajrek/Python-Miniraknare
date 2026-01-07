"""
Detta program är en simpel miniräknare som kan lösa
grundläggande beräkningar baserat på användarens inmatning.
Programet kan lösa addition, subtraktion, multiplikation och
division.
"""

def utfor_berakning(tal1, operator, tal2):
    # Gör beräkning beroende på vald operator.
    if operator == '+':
        return tal1 + tal2
    elif operator == '-':
        return tal1 - tal2
    elif operator == '*':
        return tal1 * tal2
    elif operator == '/':
        if tal2 == 0:
            return None
        return tal1 / tal2
    elif operator == '//':
        if tal2 == 0:
            return None
        return tal1 // tal2
    elif operator == '%':
        if tal2 == 0:
            return None
        return tal1 % tal2
    else:
        return None


while True:
    inmatning = input("Vad vill du räkna ut: ")

    delar = inmatning.split()
    tal1_str, operator, tal2_str = delar

    # Konverterar inmatningen till flyttal
    tal1 = float(tal1_str)
    tal2 = float(tal2_str)

    resultat = utfor_berakning(tal1, operator, tal2)

    if resultat is None:
        if operator in ['/', '//', '%'] and tal2 == 0:
            print("Error: Division med 0")
        else:
            print("Felaktig operator")
    else:
        print(f"{tal1} {operator} {tal2} = {resultat}")

    print()