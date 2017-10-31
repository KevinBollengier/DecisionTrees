# Lab about decision trees made by Kevin Bollengier
import arff
import fileinput
import Dataset
import math


def main():
    data_set = parse_arff()
    # print(get_attributes(data_set))
    attributes = get_attributes(data_set)
    entropy = calc_entropy(attributes[0][1])
    information_gain = calc_inf_gain(get_data(data_set), entropy, attributes[0])
    print(information_gain)


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
    :return: The attribute values returned as a list of tuples
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


def calc_entropy(attribute: list)->float:
    """
    Function that calculates the entropy of a given attribute
    :param attribute: Index of listitem and tuple which gives a list of values of that specific attribute
    :return: The entropy as float.
    """
    amount_value = {}
    for value in attribute:
        amount_value[value] = amount_value.get(value, 0) + 1
    result = 0
    for key, value in amount_value.items():
        result -= value/len(attribute) * math.log(value/len(attribute), 2)
    return result


def calc_inf_gain(dataset: list, entropy: float, attribute: list)->float:
    """
    Function which calculates the information gain given the data and attributes
    :param dataset: The data received from the get_data function
    :param entropy: The entropy received from calc_entropy
    :param attribute: Index of listitem and tuple which gives the list of values for that specific attribute
    :return: The information gain as float value.
    """
    infogain = entropy
    dict_list = []
    for record in dataset:
        val_freq = {}
        for value in record:
            val_freq[value] = val_freq.get(value, 0) + 1
        dict_list.append(val_freq)
    for dictionary in dict_list:
        for key, value in dictionary.items():
            # TODO: waiting on feedback to see if my quiz was correct
            infogain -= int(value) / len(dict_list) * (int(value)/len(dict_list) * math.log(int(value)/len(dict_list), 2))
    return infogain


def id3():
    pass


if __name__ == '__main__':
    main()
