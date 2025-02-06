
a_list = [[[1, 2, 3], 2, [1, 3]],  # First Row
          [1, 2, 3]]  # Second Row
def search(nested_list, value):
    indices = []
    def find_index_of_list_element(nested_list, current_path=[]):
        if isinstance(nested_list, list):
            for index, element in enumerate(nested_list):
                new_path = current_path + [index]
                find_index_of_list_element(element, new_path)
        elif nested_list == value:
            indices.append(current_path)

    find_index_of_list_element(nested_list)
    print(indices)


search(a_list, [1,2,3])

