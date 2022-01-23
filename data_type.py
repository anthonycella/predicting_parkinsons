from enum import Enum


class DataType(Enum):
    VARIABLE_1 = "Variable 1"
    VARIABLE_2 = "Varaible 2"
    VARIABLE_3 = "Variable 3"
    VARIABLE_4 = "Variable 4"
    VARIABLE_5 = "Variable 5"
    VARIABLE_6 = "Variable 6"
    VARIABLE_7 = "Variable 7"
    VARIABLE_8 = "Variable 8"
    VARIABLE_9 = "Variable 9"


def get_all_data_types():
    all_data_types = [DataType.VARIABLE_1, DataType.VARIABLE_2, DataType.VARIABLE_3,
                      DataType.VARIABLE_4, DataType.VARIABLE_5,
                      DataType.VARIABLE_6, DataType.VARIABLE_7,
                      DataType.VARIABLE_8, DataType.VARIABLE_9]

    return all_data_types


def get_data_types(columns_wanted):
    full_data_type_list = get_all_data_types()
    data_types = []
    start_column = 4

    for column in columns_wanted:
        data_type_index = column - start_column
        data_type = full_data_type_list[data_type_index]
        data_types.append(data_type)

    return data_types


def get_data_by_data_type(patient, data_type):
    match data_type:
        case DataType.VARIABLE_1:
            return patient.get_variable_one()
        case DataType.VARIABLE_2:
            return patient.get_variable_two()
        case DataType.VARIABLE_3:
            return patient.get_variable_three()
        case DataType.VARIABLE_4:
            return patient.get_variable_four()
        case DataType.VARIABLE_5:
            return patient.get_variable_five()
        case DataType.VARIABLE_6:
            return patient.get_variable_six()
        case DataType.VARIABLE_7:
            return patient.get_variable_seven()
        case DataType.VARIABLE_8:
            return patient.get_variable_eight()
        case DataType.VARIABLE_9:
            return patient.get_variable_nine()


def get_data_points_by_data_type(patients, data_type):
    data_points = []

    for patient in patients:
        data_point = get_data_by_data_type(patient, data_type)
        data_points.append(data_point)

    return data_points


def sort_patients_by_data_type(patients, data_type):
    patients_to_sort = patients

    for first_index in range(0, len(patients)):
        first_patient = patients[first_index]
        first_patient_data = get_data_by_data_type(first_patient, data_type)

        minimum = first_patient_data
        minimum_index = first_index

        for second_index in range(first_index, len(patients)):
            second_patient = patients[second_index]
            second_patient_data = get_data_by_data_type(second_patient, data_type)

            if second_patient_data < minimum:
                minimum = second_patient_data
                minimum_index = second_index

        if minimum_index != first_index:
            patients_to_sort = swap_patients(patients_to_sort, first_index, minimum_index)

    sorted_patients = patients_to_sort
    return sorted_patients


def swap_patients(patients, first_index, second_index):
    temporary_patient = patients[first_index]
    patients[first_index] = patients[second_index]
    patients[second_index] = temporary_patient

    return patients
