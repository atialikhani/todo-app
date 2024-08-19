def get_average(filenames):
    with open(filenames, "r") as f:
        data =f.readlines()[1:]

    values = [float(i) for i in data]
    data = sum(values)/len(values)
    return data


average1 = get_average("file.txt")
average2 = get_average("numbers.txt")
print(average1, average2)