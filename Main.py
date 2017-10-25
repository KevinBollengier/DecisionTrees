import arff
import fileinput
import Dataset


def main():
    read_data()
    pass


def read_data()->dict:
    """
    Function that gains data through file input and uses the arff library to parse this into a dictionary.
    :return: Returns a dictionary containing the dataset from the arff file.
    """
    lines = []
    for line in fileinput.input():
        lines.append(line)
    data = arff.loads("\n".join(lines))
    dataset: Dataset = data
    # for values in data:
    #     print(values)
    return dataset


if __name__ == '__main__':
    main()
