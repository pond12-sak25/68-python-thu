survey_resaluts = [
    ["python", "c++", "javascript"],
    ["#c", "python", "javascript"],
    ["python", "java",],
    ["javascript", "python", "c++"],
    ["python", "java", "c++", "javascript"],
]

choices_sets = [set(day) for day in survey_resaluts]
common_languages = set.intersection(*choices_sets)
print("1.languages chosen by all participants:", common_languages)

single_paticipant_choices = set.union(*choices_sets)
print("2.languages chosen by at least one participant:", single_paticipant_choices)

first_one_choices = choices_sets[0]
last_one_choices = choices_sets[-1]
first_one_choices_not_in_last = list(first_one_choices - last_one_choices)
print("3.languages chosen by the first participant but not by the last:", first_one_choices_not_in_last)