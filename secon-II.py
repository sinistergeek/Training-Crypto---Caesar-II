plain='76 1E 1E 13 20 19 1E 11 5B 20 28 1E 24 20 22 1E 1B 25 14 13 20 1E 1D 14 20 1C 1E 21 14 20 12 17 10 1B 1B 14 1D 16 14 20 18 1D 20 28 1E 24 21 20 19 1E 24 21 1D 14 28 5D 20 03 17 18 22 20 1E 1D 14 20 26 10 22 20 15 10 18 21 1B 28 20 14 10 22 28 20 23 1E 20 12 21 10 12 1A 5D 20 06 10 22 1D 56 23 20 18 23 6E 20 60 61 67 20 1A 14 28 22 20 18 22 20 10 20 20 24 18 23 14 20 22 1C 10 1B 1B 20 1A 14 28 22 1F 10 12 14 5B 20 22 1E 20 18 23 20 22 17 1E 24 1B 13 1D 56 23 20 17 10 25 14 20 23 10 1A 14 1D 20 28 1E 24 20 23 1E 1E 20 1B 1E 1D 16 20 23 1E 20 13 14 12 21 28 1F 23 20 23 17 18 22 20 1C 14 22 22 10 16 14 5D 20 06 14 1B 1B 20 13 1E 1D 14 5B 20 28 1E 24 21 20 22 1E 1B 24 23 18 1E 1D 20 18 22 20 1B 15 1D 15 12 18 1D 1B 22 1E 13 10 5D'
temp=list(filter(None,plain.split(" ")))
messgae = []
nums = range(1, 128)
translated = ''
for t in temp:
    messgae.append(int('0x'+t,16))
print(messgae)
for key in nums:
    translated = ''
    for symbol in messgae:
        translated = translated + chr((symbol+key)%128)
    print(translated.lower())
