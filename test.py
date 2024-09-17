from tkinter import filedialog, messagebox

d = {1: 'D:/!!__ПечатьПризыв/Выгрузка 074/366_A/Юра 1', 2: 'D:/!!!__АРМИЯ__!!!/!!!!!!!___212/КАЛИНИНГРАД_АЛЬБОМ/jpg/001.jpg', 3: 'D:/!!!__АРМИЯ__!!!/!!!!!!!___212/КАЛИНИНГРАД_АЛЬБОМ/366_A/Юра 2'}
q = d.values()

print(d)
for t, r in enumerate(q,1):
    if "Юра " in r:
        print(r)
        rr=r.split('/')[-2]
        print(rr)
        a = r.replace("366_A", "400")
        d[t] = a
        print(d)
        print(t)

