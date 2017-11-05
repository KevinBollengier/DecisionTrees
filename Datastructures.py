from typing import List, Tuple


class DataSet:
    def __init__(self, rows: List[List[str]]):
        self.rows = rows


class DecisionTree:
    def __init__(self, root_node: 'DecisionNode'):
        self.root_node = root_node
    pass


class DecisionNode:
    def __init__(self, attribute: 'Attribute', dataset: DataSet, children: List['DecisionNode']):
        self.name = attribute.name
        self.dataset = dataset
        self.children = children


class Attribute:
    def __init__(self, name: str, values: List[str]):
        self.name = name
        self.values = values
