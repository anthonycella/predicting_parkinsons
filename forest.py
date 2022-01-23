from random_forest.tree import *


def get_forest_prediction(forest, patient):
    true_count = 0
    false_count = 0

    for tree in forest:
        prediction = traverse_and_get_prediction(tree, patient)
        if prediction is True:
            true_count += 1
        else:
            false_count += 1

    if true_count >= false_count:
        return True
    else:
        return False


def construct_forest_by_all_data_types(patients, tree_depth):
    forest = []
    data_types = get_all_data_types()

    for data_type in data_types:
        new_tree = construct_decision_tree_from_patients(patients, data_type, tree_depth)
        forest.append(new_tree)

    load_forest(forest, patients)

    return forest


def construct_forest_by_data_types(patients, tree_depth, data_types):
    forest = []

    for data_type in data_types:
        new_tree = construct_decision_tree_from_patients(patients, data_type, tree_depth)
        forest.append(new_tree)

    load_forest(forest, patients)

    return forest


def load_forest(forest, patients):
    # this function is meant to set the predictions on each of the leaf nodes
    for tree in forest:
        add_patients_to_tree(tree, patients)
        traverse_and_set_predictions(tree)
