class WithResource:

    def __init__(self, name, mode="rt"):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


def append_to_file(text, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')

    with WithResource(filename, 'r') as res:
        lines = res.readlines()
        print("Чётные строки файла:")

        for index, line in enumerate(lines, start=1):
            if index % 2 == 0:
                print(f"{index}. {line.strip()}")


with WithResource("example.txt", "w") as res:
    res.write("Первая строка\nВторая строка\nТретья строка\nЧетвертая строка\n")


append_to_file("Пятая строка", "example.txt")