def decode_metar(metar):
    parts = metar.split()

    print(f"Станция: {parts[0]}")

    # Время
    time = parts[1]
    print(f"Время: {time[:2]} числа {time[2:4]}:{time[4:6]} UTC")

    # Ветер
    wind = parts[2]
    if wind == "00000KT":
        print("Ветер: штиль")
    elif "VRB" in wind:
        print(f"Ветер: переменный {wind[3:5]} узлов")
    else:
        print(f"Ветер: {wind[:3]}° {wind[3:5]} узлов")

    # Видимость
    vis = parts[3]
    if vis == "9999":
        print("Видимость: хорошая (10+ км)")
    elif vis == "CAVOK":
        print("Видимость: отличная")
    else:
        print(f"Видимость: {vis} м")


    for part in parts[4:]:
        if part.startswith('RA'):
            print("Погода: дождь")
        elif part.startswith('SN'):
            print("Погода: снег")
        elif part.startswith('TS'):
            print("Погода: гроза")
        elif part.startswith('FG'):
            print("Погода: туман")
        elif part.startswith('FEW'):
            print("Облака: немного")
        elif part.startswith('SCT'):
            print("Облака: рассеянные")
        elif part.startswith('BKN'):
            print("Облака: разорванные")
        elif part.startswith('OVC'):
            print("Облака: сплошные")
        elif '/' in part and part.replace('M', '').replace('/', '').isdigit():
            temp, dew = part.split('/')
            print(f"Температура: {temp.replace('M', '-')}°C")
            print(f"Точка росы: {dew.replace('M', '-')}°C")
        elif part.startswith('Q'):
            print(f"Давление: {part[1:]} гПа")


print("===ДЕКОДЕР===")
metar = "LFPG 041000Z 27016KT 9999 SCT022 BKN030 15/11 Q1006 NOSIG"
decode_metar(metar)