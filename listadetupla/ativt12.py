datas = (
    (2, 1, 2023),
    (15, 6, 2020),
    (3, 12, 2019),
    (20, 5, 2021),
)


datas_ordenadas = sorted(datas, key=lambda data: (data[2], data[1], data[0]))


for data in datas_ordenadas:
    print(f"{data[0]}/{data[1]}/{data[2]}")
