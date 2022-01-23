from data.extract_data import get_patients
from helper_methods.results import get_tree_accuracy, get_forest_accuracy
from random_forest.forest import *


def main():
    file_path_name = ""
    wants_to_include_standard_of_truth = True

    patients = get_patients(file_path_name, wants_to_include_standard_of_truth)

    forest = construct_forest_by_all_data_types(patients, 3)

    forest_accuracy = get_forest_accuracy(forest, patients)
    print(forest_accuracy)


main()
