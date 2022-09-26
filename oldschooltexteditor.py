from os import system


def main():
    p1 = Typing()
    p1.clrscr()
    p1.title()
    while True:
        x = input("->> ")
        if x.strip() == "//quit":
            quit()
        p1.clrscr()
        p1.write(x + " ")
        p1.title()
        p1.show()


class basicop:
    def clrscr(self):
        try:
            system("cls")
        except:
            try:
                system("clear")
            except:
                print("\n" * 100)

    def file_input(self, filename):
        with open(filename) as f:
            f = f.read()
        return f


class Typing(basicop):
    def __init__(self) -> None:
        typed = ""
        file_path = None
        self.typed = typed
        self.file_path = file_path
        self.state = []

    def undo(self):
        for j, i in enumerate(self.state):
            if i == self.typed:
                self.typed = self.state[j - 1]

    def redo(self):
        for j, i in enumerate(self.state):
            if i == self.typed:
                if self.state[-1] == self.typed:
                    pass
                else:
                    self.typed = self.state[j + 1]
                break

    def show(self):
        print(self.typed)

    def write(self, char):
        def special_typed():
            try:
                x = char.split(" ")
                match x[0][2:]:
                    case "dc":
                        try:
                            num = int(char[5:].strip())
                            if self.typed[-1] == " ":
                                self.typed = self.typed[:-1]
                                print("space is cleared")
                            self.typed = self.typed[:-num]
                        except:
                            print("you can only use numbers")
                    case "del":
                        print("All writing deleted")
                        self.typed = ""
                        self.state.append(self.typed)
                    case "undo":
                        self.undo()
                        print("executed undo")
                    case "redo":
                        self.redo()
                        print("executed redo")
                    case "br":
                        self.typed += "\n"
                        self.state.append(self.typed)
                    case "save":
                        name = char[7:].strip()
                        if name == "" and self.file_path is not None:
                            name = self.file_path
                        self.save_file(name)
                        self.file_path = name
                        print("saved")

                    case "open":
                        name = char[7:].strip()
                        self.typed = self.file_input(name)
                        self.file_path = name
                        print(f"opened {name}")
                    case "help":
                        print(
                            """
                        Here you can see List of special methods of this notepad
                        Here "<..>" represents required parameter

                        "//undo" -undoing any act
                        "//redo" -redoing any act
                        "//save<space>" -saving in opened file
                        "//save <filename with extension>" -saving into filname , can use "c:/..../../test.txt" as filename
                        "//open <filename with extension>" -opening a filname 
                        "//del" -clearing all writing
                        "//dc <num of characters>" deletes the num of characters , can be used as backspace 
                        "//br" -for a new line
                        """
                        )

            except:
                print("invalid command")

        if char[:2] == "//":
            special_typed()
        elif char == " ":
            self.typed += "\n"
        else:
            self.typed += char
            self.state.append(self.typed)
            if len(self.state) > 7:
                self.state = self.state[-7:]

    def title(self):
        titl = """
                        OldSchool NOTEPAD BY PRASH"""
        info = """                      use '//help' for info about functions """
        print(titl, "\n" + "-" * len(titl), "\n" + info + "\n" + "-" * len(info))
        print("opened", self.file_path)
        print("---")

    def save_file(self, file_name):
        with open(file_name, "w") as f:
            f.write(self.typed)


if __name__ == "__main__":
    main()
