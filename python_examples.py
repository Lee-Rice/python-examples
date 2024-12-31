"""Various Python examples used for mentoring."""

# Import the data from the sources module.
from sources import example_data as ex


def dictionary_example(item_list: list):
    """Returns a map of the number of times an item occurs in a list."""
    print("Hashmap example: ")
    item_counts: dict = {}
    for item in item_list:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    for key, value in item_counts.items():
        print(f"\t Key: {key}, Value: {value}")


def assignment_expression_operator() -> int:
    """Attempts to print the values returned by different statements."""
    print("Assignment expression operator example:")
    try:
        print(num=5)
    except TypeError:
        print(
            '\tTypeError: The statement "print(num = 5)" returns nothing, so an error occurs.\n'
        )
    print(f'\tThe value returned by "(num := 5)" is: {(num := 5)}')
    print(
        '\tThe statement "(num := 5)" assigns a value to a variable and returns the value.\n'
    )


def dictionary_iteration(first_dictionary: dict, second_dictionry: dict):
    """Prints the keys of two Python dictionaries."""
    print("Zip function example")

    for key_1, key_2 in zip(first_dictionary, second_dictionry):
        print(f"\tKey 1: {key_1},  Key 2: {key_2}")
    print(f"\tFirst dictionary length: {len(first_dictionary)}")
    print(f"\tSecond dictionary length: {len(second_dictionry)} ")
    print(
        "\tNotice that the number of keys printed corresponds to the shortest dictionary."
    )


dictionary_example(ex.name_list)
print("\n")
assignment_expression_operator()
print("\n")

dictionary_iteration(ex.animals, ex.plants)
