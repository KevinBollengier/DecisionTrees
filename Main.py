# Lab about decision trees made by Kevin Bollengier
from typing import List, Tuple

import arff
import fileinput
import Dataset
import math


def main():
    data_set = parse_arff()
    data = get_data(data_set)
    attributes = get_attributes(data_set)
    id3(data, attributes, -1)


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


def get_data(dataset_lastcolumn: dict)->list:
    """
    Function that gets the data from a parsed arff dataset and returns the data
    :rtype: list
    :param dataset_lastcolumn: The dataset which is parsed as dict.
    :return: The data values returned as multidimensional list
    """
    data_values = dataset_lastcolumn["data"]
    return data_values


def calc_entropy(dataset: list)->float:
    """
    Function that calculates the entropy of a given attribute
    :param dataset: Index of listitem and tuple which gives a list of values of that specific attribute
    :return: The entropy as float.
    """
    amount_value = {}
    for value in dataset:
        amount_value[value] = amount_value.get(value, 0) + 1
    result = 0
    for key, value in amount_value.items():
        result -= value/len(dataset) * math.log(value / len(dataset), 2)
    return result


def calc_inf_gain(dataset: list, attribute: list, entropy: float, index: int)->float:
    """
    Function which calculates the information gain given the data and attributes
    :param index: Column
    :param dataset: The dataset
    :param attribute: List containing the attribute values
    :param entropy: Entropy calculated on the dataset
    :return: The information gain as float value.
    """
    infogain = entropy
    for value in attribute[1]:
        data_sub_set = [row[-1] for row in dataset if row[index] == value]
        infogain -= (len(data_sub_set) / len(dataset) * calc_entropy(data_sub_set))
    return infogain


def get_highest_ig(dataset: list, entropy: float, attributes: list)->Tuple[str, List[str]]:
    """
    Function that returns the name of the best attribute to split on
    :param dataset: The dataset
    :param entropy: The entropy of the dataset
    :param attributes: List of tuples containing the attributes
    :return: Tuple of the best attribute
    """
    info_gain_per_attr = {}
    for attr in range(len(dataset[0]) - 1):
        info_gain_per_attr[attr] = calc_inf_gain(dataset, attributes[attr], entropy, attr)
    return attributes[max(info_gain_per_attr.keys())]


def split_attr(dataset: List[str], best_attribute: Tuple[str, List[str]], index: int)->List[List[str]]:
    splitted_sets = []
    for value in best_attribute[1]:
        filter_rows = []
        for row in dataset:
            if row[index] == value:
                filter_rows.append(row)
        splitted_sets.append(filter_rows)
    return splitted_sets


def id3(dataset, attributes, tree_depth):
    tree_depth += 1
    entropy = calc_entropy([row[i] for row in dataset for i in range(len(row)) if i == len(attributes)-1])
    best_attribute = get_highest_ig(dataset, entropy, attributes)
    subsets = split_attr(dataset, best_attribute, attributes.index(best_attribute))
    # TODO: print the tree


if __name__ == '__main__':
    main()
