import os
import numpy as np
import guilib as ui
def read_data(path):
    """ 
    Read data from measurement text file in a folder. The function will return 
    two list: the energy list for the binding energy of electrons and the second 
    list is the total intensity in all measurement file. At the end of the function, 
    there is a count variable to output the total number of line read 
    """
    value_initialize = []
    energy = []
    count_line = 0
    for i in range(500):
        value_initialize.append(float(0))
    for file in os.listdir(path):
        value = []
        file_path = os.path.join(path, file)
        with open(file_path, "r", encoding="UTF-8") as target:
            for i, line in enumerate(target):
                try:
                    num1, num2 = line.strip().split(" ")
                    num1 = float(num1)
                    num2 = float(num2)
                except ValueError:
                    print(f"There is an error in line {i} of file {file}")
                else:
                    if num1 not in energy:
                        energy.append(num1)
                    else:
                        pass
                    value.append(num2)
                    count_line += 1
            for i, item in enumerate(value):
                value_initialize[i] += item
    return energy, value_initialize, count_line

def open_folder():
    """ 
    Let the user to open the specific folder which contains the datasets and return
    the path to the folder which will be the parameter of the read_data function
    """
    folder_path = ui.open_folder_dialog("Load", initial=".")
    return folder_path

  

def remove_background(s, y_inter, data_list1, data_list2):
    """ 
    Calculate the background value and remove it from the total 
    intensity of the entire dataset. The function returns the dataset after
    cleaning the background signal. Data_list 1 is energy list, data_list2 is
    the pre-updated intensity list.
    """
    background = []
    cleaned_list = []
    for i in range(len(data_list1)):
        background.append(float(0))
    for i, item in enumerate(data_list1):
        background[i] += item * s + y_inter
    for i, item in enumerate(background):
        new_data = data_list2[i] - background[i]
        cleaned_list.append(new_data)
    return cleaned_list

def determine_index(min_bound, max_bound, slice_list):
    """
    Determine the minimum and maximum index and then use them
    to slice in a list. Return the minimum and maximum index.
    """
    for i, item in enumerate(slice_list):
        if item >= min_bound:
            min_index = i
            break
    for i, item in enumerate(slice_list):
        if item > max_bound:
            max_index = i
            break
    return min_index, max_index

def calculate_peak_area (y_data_list, x_data_list):
    """
    Calculate the peak area by using numpy function
    with two datasets.
    """
    area = np.trapezoid(y_data_list, x_data_list)
    return area

def determine_line(x1, y1, x2, y2):
    """
    Determine the line slope and y-intercept based on the two points coordinates
    """
    if x1 == x2 and y1 == y2:
        return "These points are the same! Try again"
    elif x1 == x2:
        return "This is a vertical line! Try again"
    else:
        s = (y2 - y1) / (x2 - x1)
        y_inter = (x2 * y1 - x1 * y2) / (x2 - x1)
        return s, y_inter

