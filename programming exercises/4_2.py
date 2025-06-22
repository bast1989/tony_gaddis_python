START  = 10
END = 31
STEP = 5
KAL = 4.2

for i in range(START, END, STEP):
    print(f'Количество минут на беговой дорожке: {i}',
          f'количество сожжённых калорий: {i * KAL} ')