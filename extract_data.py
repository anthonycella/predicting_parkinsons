import csv

from data.patient import Patient


def construct_patient_from_row(row, wants_to_include_standard_of_truth):
    patient_id = row[0]

    standard_of_truth = int(row[1])

    age = int(row[2])
    variable_one = float(row[3])
    variable_two = float(row[4])
    variable_three = float(row[5])
    variable_four = float(row[6])
    variable_five = float(row[7])
    variable_six = float(row[8])
    variable_seven = float(row[9])
    variable_eight = float(row[10])
    variable_nine = float(row[11])

    if wants_to_include_standard_of_truth:
        new_patient = Patient(patient_id, age, variable_one, variable_two,
                              variable_three,
                              variable_four, variable_five,
                              variable_six,
                              variable_seven, variable_eight, variable_nine, standard_of_truth)

    else:
        new_patient = Patient(patient_id, age, variable_one, variable_two,
                              variable_three,
                              variable_four, variable_five,
                              variable_six,
                              variable_seven, variable_eight, variable_nine)

    return new_patient


def get_patients(file_path_name, user_wants_to_include_standard_of_truth):
    input_data_file_path_name = file_path_name
    data_file = open(input_data_file_path_name)
    file_reader = csv.reader(data_file)

    wants_to_include_standard_of_truth = user_wants_to_include_standard_of_truth
    patients = []

    has_ignored_first_row = False

    for row in file_reader:
        if not has_ignored_first_row:
            has_ignored_first_row = True
        else:
            new_patient = construct_patient_from_row(row, wants_to_include_standard_of_truth)
            patients.append(new_patient)

    return patients
