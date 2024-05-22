import string


class FileReader(object):
    def __init__(self, file):
        self.file = file

    def read_file(self):
        file = open(self.file, 'r')
        print(file.read())
        file.close()
        return self.file

    # count rows, strings, punctuation marks
    def counter(self, *args):
        strings = 0
        marks = 0
        file = self.file
        with open(file) as file_object:
            print("------------------------------------")
            print("counter for file:", file)
            lines = file_object.readlines()
            print("lines count:", len(lines))

            for line in lines:
                clear_line = ' '.join(word.strip(string.punctuation) for word in line.split())
                strings += len(clear_line.split())
                marks += sum(tuple(line.count(c) for c in string.punctuation))
            print("strings count:", strings)
            print("marks count:", marks)

        file_object.close()
        return lines, strings, marks

    def file_cleaner(self):
        open(self.file, 'w').close()
        print("------------------------------------")
        print("Cleaning done!")

    def file_append(self, arg):
        with open(self.file, "a") as file_object:
            file_object.write(arg)
        file_object.close()
        print("------------------------------------")
        print("Append complete!")

    # private func
    def __get_dict(self):
        f = 3

    # public func
    def create_stat_file(self):
        with open(self.file, 'w') as file_object:
            file_object.write("test.txt\nq w e\n321")
        file_object.close()
        return print("Done!")


sample_file = "ttt.txt"

# FileReader(sample_file).create_stat_file()
a = FileReader(sample_file).read_file()
print("file name:", a)
FileReader(a).counter()
FileReader(a).file_cleaner()
FileReader(a).file_append("asdsad dsa\ndsad!")
