
def get_split_points_by_values(numbered_values):
    split_points = []

    for current_index in range(0, len(numbered_values) - 1):
        next_index = current_index + 1

        current_point = numbered_values[current_index]
        next_point = numbered_values[next_index]

        split_point_unrounded = (current_point + next_point) / 2
        split_point = round(split_point_unrounded, 5)
        split_points.append(split_point)

    return split_points


def get_best_split_point(patients, split_points, data_type):
    from helper_methods.gini_impurity import get_gini_impurity_dictionary_by_split_points
    gini_impurity_dictionary = get_gini_impurity_dictionary_by_split_points(patients, split_points, data_type)
    gini_impurities = gini_impurity_dictionary.keys()

    best_gini_impurity = min(gini_impurities)
    best_split_point = gini_impurity_dictionary[best_gini_impurity]

    return best_split_point
