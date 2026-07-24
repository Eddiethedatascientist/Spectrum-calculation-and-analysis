import os
import guilib as ui
import data_processing as data
states = {
    "textbox": None,
    "canvas": None,
    "subplot": None,
    "click 1": None,
    "click 2": None,
    "energy": None,
    "intensity": None,
    "update intensity": None,
    "figure": None
}
def load_handler ():
    """
    Function used for the load button for initial data processing
    """
    path = data.open_folder()
    try: 
        energy_list, intensity_list, line = data.read_data(path)
    except OSError:
        ui.open_msg_window("Error", "Please choose a valid measurement folder", error=True)
    except ValueError:
        ui.open_msg_window("Error", "The measurement files have invalid data", error=True)
    except Exception:
        ui.open_msg_window("Error", "An unexpected error occurs. Please try again!", error=True)
    else: 
        if states["energy"] is None:
            states["energy"] = energy_list
        if states["intensity"] is None:
            states["intensity"] = intensity_list
        content = f"Processed {line} data lines and {line * 2} floats"
        ui.write_to_textbox(states["textbox"], content, clear=False)
        states["subplot"].clear()
        states["subplot"].plot(energy_list, intensity_list, 'b')
        states["subplot"].set_title("Spectrum Analysis")
        states["subplot"].set_xlabel("Binding energy (eV)")
        states["subplot"].set_ylabel("Intensity (arbitrary units)")
        states["canvas"].draw()

def update_handler(event):
    """
    Function takes in the data in the click of users
    """
    x = event.xdata
    y = event.ydata
    if states["click 1"] is None:
        states["click 1"] = (x, y)
        content_1 = f"Point 1 coodinates: ({x:.3f}, {y:.3f})"
        ui.write_to_textbox(states["textbox"], content_1, clear=False)
    else:
        x1, y1 = states["click 1"]
        x2, y2 = x, y
        states["click 2"] = (x, y)
        content_2 = f"Point 2 coordinates: ({x:.3f}, {y:.3f})"
        ui.write_to_textbox(states["textbox"], content_2, clear=False)

def update_handler_button ():
    """
    Function to update the figure through the update button
    """
    if states["click 1"] is None or states["click 2"] is None:
        write = "Select two different points on the graph excepts the peaks before pressing the update button!"
        ui.open_msg_window("Error", write, error=True)
    if states["click 1"] is not None and states["click 2"] is not None:
        x1, y1 = states["click 1"]
        x2, y2 = states["click 2"]
        if x1 == x2 and y1 == y2:
            ui.open_msg_window("Error", "The points are the same. Please try again", error=True)
            states["click 1"] = None
            states["click 2"] = None
        elif x1 == x2:
            ui.open_msg_window("Error", "Cannot remove background with a vertical line. Please try again!", error=True)
            states["click 1"] = None
            states["click 2"] = None
        else: 
            slope, y_intercept = data.determine_line(x1, y1, x2, y2)
            states["update intensity"] = data.remove_background(slope, y_intercept, states["energy"], states["intensity"])
            states["subplot"].clear()
            states["subplot"].plot(states["energy"], states["update intensity"], 'r')
            states["subplot"].set_title("Spectrum Analysis")
            states["subplot"].set_xlabel("Binding energy (eV)")
            states["subplot"].set_ylabel("Intensity (arbitrary units)")
            states["canvas"].draw()
            states["click 1"] = None
            states["click 2"] = None

def save_figure (fig):
    """
    Save the spectrum figure to a specific location
    """
    path = ui.open_save_dialog("Save", initial=".")
    print(path)
    print(os.path.exists(path))
    if not path.endswith(".png"):
        path += ".png"
    name = os.path.basename(path)
    directory = os.path.dirname(path)
    content1 = (
            "-------------------- \n"
            "The file is saved successfully \n"
            f"File name: {name} \n"
            f"File location: {directory} \n"
            "--------------------"
            )
    content2 = "The file already exist. Please change the file name!"
    if path is not None:
        if os.path.exists(path) is True:
            ui.open_msg_window("Error", content2, error=True)
        else: 
            fig.savefig(path)
            ui.write_to_textbox(states["textbox"], content1, clear=False)
        
def save_handler ():
    """
    Allow the user to save the drawn figure in a specific location
    """
    save_figure(states["figure"])
    
def spectrum_area():
    """ 
    Calculate the spectrum through the analysis button
    """
    if states["click 1"] is None or states["click 2"] is None:
        er = "Select two points on the graph except for the peak area before pressing Calculate!"
        ui.open_msg_window("Error", er, error=True)
    if states["click 1"] is not None and states["click 2"] is not None:
        x1, y1 = states["click 1"]
        x2, y2 = states["click 2"]
        if x1 < x2: 
            min_i, max_i = data.determine_index(x1, x2, states["energy"])
        else:
            min_i, max_i = data.determine_index(x2, x1, states["energy"])
        sliced_energy = states["energy"][min_i:max_i + 1]
        sliced_intensity = states["update intensity"][min_i: max_i + 1]
        area = data.calculate_peak_area(sliced_intensity, sliced_energy)
        content = f"The area under spectrum is {area:.3f}"
        ui.write_to_textbox(states["textbox"], content, clear=False)

def get_instruction ():
    """
    Show instruction to the user
    """
    message = ( "Welcome to spectrum calculation program. In this window, you will be given explicit instructons on how to use the program properly. \n\n"
            "+ Button Instruction gives the specific instructions on how to use the program. \n\n"
            "+ Button Load is used to load the data to draw the graph. Select the correct data folder and let it does the rest! \n\n"
            "+ Button Update is used to update the figure without background signals. Select two points on the figure except for the peaks and select Update after you saw the coordinates in the textbox. \n\n"
            "+ Button Calculate is used to calculate the area below peaks. Select two new points on the graph except for peak area and when you saw the coordinates on the textbox, press the button. \n\n"
            "+ Button Save is used to save the figure. Press the button and select the destination you want. By default, the destination is your current code file. Type save name and press Enter. \n\n"
            "+ Button Quit is used to close the program!" )
    ui.open_msg_window("Instruction", message, error=False)          
              
def main():
    """
    Create the graphical interface of the program and assign the graphical elements
    to their handler function 
    """
    window = ui.create_window("Spectrum analysis")
    left_frame = ui.create_frame(window, ui.LEFT)
    right_frame = ui.create_frame(window, ui.RIGHT)
    top_frame = ui.create_frame(right_frame, ui.TOP)
    bottom_frame = ui.create_frame(right_frame, ui.BOTTOM)
    states["textbox"] = ui.create_textbox (bottom_frame, width=75, height=20)
    ui.create_button(left_frame, "Instructions", get_instruction)
    ui.create_button(left_frame, "Load", load_handler)
    states["canvas"], states["figure"], states["subplot"] = ui.create_figure(top_frame, update_handler, width=600, height=500)
    ui.create_button(left_frame, "Update", update_handler_button)
    ui.create_button(left_frame, "Calculate", spectrum_area)
    ui.create_button(left_frame, "Save figure", save_handler)
    ui.create_button(left_frame, "Quit", ui.quit)
    ui.start()

if __name__ == "__main__":
    main()
