import arff
import fileinput


def main():
    read_data()
    pass


def read_data():
    lines = []
    for line in fileinput.input():
        lines.append(line)
    data = arff.loads("\n".join(lines))
    print(data)
    pass


if __name__ == '__main__':
    main()
