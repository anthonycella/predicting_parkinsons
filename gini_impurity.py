from random_forest.probability import *
from random_forest.tree import get_nodes_from_split_point


def get_total_gini_impurity(left_list, right_list):
    left_gini_impurity = get_gini_impurity(left_list)
    right_gini_impurity = get_gini_impurity(right_list)

    total_gini_impurity = left_gini_impurity + right_gini_impurity
    return total_gini_impurity


def get_gini_impurity_dictionary_by_split_points(patients, split_points, data_type):
    # print("Inside gini impurity dictionary: " + str(len(patients)))
    gini_impurity_dictionary = {}
    for split_point in split_points:
        value = split_point

        left_patients, right_patients = get_nodes_from_split_point(patients, split_point, data_type)

        left_gini_impurity_value = get_gini_impurity(left_patients)
        right_gini_impurity_value = get_gini_impurity(right_patients)

        left_gini_impurity_weight = len(left_patients) / len(patients)
        right_gini_impurity_weight = len(right_patients) / len(patients)

        left_gini_impurity = left_gini_impurity_value * left_gini_impurity_weight
        right_gini_impurity = right_gini_impurity_value * right_gini_impurity_weight

        gini_impurity = left_gini_impurity + right_gini_impurity
        key = gini_impurity

        gini_impurity_dictionary[key] = value

    return gini_impurity_dictionary


def get_gini_impurity(patient_list):

    probability_class_zero = get_probability_class_zero(patient_list)
    probability_class_one = get_probability_class_one(patient_list)

    probability_class_zero_squared = probability_class_zero ** 2
    probability_class_one_squared = probability_class_one ** 2

    gini_impurity = 1 - (probability_class_one_squared + probability_class_zero_squared)
    return gini_impurity
