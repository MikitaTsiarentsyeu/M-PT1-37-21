
data={("Путиловский","Роман"):["6486447"], ("Путиловская","Анна"):["6139582"],
      ("Путиловский","Иван"):["1227574"], ("Путиловская","Людмила"):["6952726"]}

# ексептион


def get_data():
    return (data)



def add (data,name,phone):
    global data

    if data.get[name]:
        data[name]=data[name].append(phone)
    else:
        data[name]=(phone)
    print(data)


def delete (data,name,phone):
    global data

    if data.get[name]:
        if len.data[name] >=2:
            for i in range(len(data[name])):
                if data[name][i]==phone:
                    del data[name][i]






        y=data.popitem[name]
        print("Удалил",y)
    else:
        print("Такой пары нет")

def find (data, name, phone):
    global data

    if data.get[name]:
        print(name+":"+data.get[name])
    else ("Такого словаря нет")









