# Lab about decision trees made by Kevin Bollengier
import arff
import fileinput
import Dataset


def main():
    data_set = parse_arff()
    print(get_data(data_set))
    pass


def parse_arff()->dict:
    """
    Function that gains data through file input and uses the arff library to parse this into a dictionary.
    :return: Returns a dictionary containing the dataset from the arff file.
    """
    lines = []
    for line in fileinput.input():
        lines.append(line)
    data = arff.loads("\n".join(lines))
    dataset: Dataset = data
    return dataset


def get_attributes(dataset: dict)->list:
    """
    Function that get the attributes from a parsed arff dataset and which returns the attributes with their vallues
    :param dataset: The dataset which is parsed as dict
    :return: The attribute values returned as key value list
    """
    attribute_values = dataset["attributes"]
    return attribute_values


def get_data(dataset: dict)->list:
    """
    Function that gets the data from a parsed arff dataset and returns the data
    :param dataset: The dataset which is parsed as dict.
    :return: The data values returned as multidimensional list
    """
    data_values = dataset["data"]
    return data_values


def make_dec_tree(data: list, attributes: list, data_attributes: list):
    pass


def calc_entropy():
    pass


def calc_inf_gain():
    pass


if __name__ == '__main__':
    main()
