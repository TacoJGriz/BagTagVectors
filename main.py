"""
Bag Tag to Vector program
Created by Jackson Grizzle
Created for Legit3D
"""

import svgwrite
import tkinter as tk
from tkinter import filedialog, messagebox
import time
import os


# Class used to store the information for each line of text
class Line:
    def __init__(self, text, x=0, y=14, size=14, spacing=16):
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.spacing = spacing


# Starts the process when the button is pressed
def on_button_click():
    if not entry.get() == '':
        # change button text
        button.config(text="Working...")

        custom_font_path = "BeauMed.ttf"

        # Get the data from the input box and make the SVG
        input_text = entry.get()
        text_to_svg(input_text, file_path, font_family="Beaufort Pro", font_path=custom_font_path)

    else:
        messagebox.showwarning("Error", "Please enter data into the appropriate box")


# File Dialog for Output
def on_choose_file():
    # File Picker Dialog
    global file_path
    past_path = file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG files", "*.svg")],
                                             initialfile=file_path, initialdir=file_path)

    # Deals with invalid input
    if not file_path:
        file_path = past_path

    # Updates the label
    file_output_label.config(text="Output location: " + file_path)
    return


# Function to change the spacing of every line in an array
def change_spacing(lines, spacing=16):
    for line in lines:
        line.spacing = spacing

    return


# Creates and writes to the SVG
def text_to_svg(text, output_file="output.svg", font_family="Beaufort Pro", font_path='BeauMed.ttf'):
    # Create an SVG drawing
    dwg = svgwrite.Drawing(output_file, size=(116.22, 10000))

    # add styles for the custom font and text
    dwg.add(dwg.style(f"@font-face {{font-family: '{font_family}'; src: url({font_path});}}"))
    dwg.add(dwg.style("svg text{text-anchor: middle;dominant-baseline: middle;}"))

    # write each tag to the svg
    tag_arr = text.split('\n\n')
    next_y = 15
    for tag in tag_arr:
        (dwg, next_y) = draw_tag(dwg, tag, next_y)

    # Save the SVG file
    dwg.save()
    button.config(text='Done!')
    messagebox.showinfo("Finished", f"Finished! SVG file saved at:\n{file_path}")


# Draws each individual tag
def draw_tag(dwg, text, next_y):
    # formats the text into each line in an array
    lines_text = text.split('\n')
    for line in lines_text:
        line.strip()

    # Turns each line string into a Line Object
    lines = []
    current_y = next_y
    for line in lines_text:
        current_line = Line(line, 0, current_y, 14, 16)
        lines.append(current_line)
        current_y += current_line.size + current_line.spacing

    for i in range(len(lines)):
        if i > 0:
            lines[i].size = 12

    # Rules for each number of lines
    if len(lines) == 1:
        pass
    elif len(lines) == 2:
        # y = (0.5x - 0.5) * len(line.text) > 116.22
        change_spacing(lines, 24)
        lines[0].size = 17
        lines[1].size = 15

        # Decrease text size until it fits
        while ((0.5 * lines[0].size - 0.5) * len(lines[0].text) > 116.22 or (0.5 * lines[1].size - 0.5) *
               len(lines[1].text) > 116.22 and lines[1].size > 11):
            lines[0].size -= 1
            lines[1].size -= 1

        if lines[1].size == 11:
            lines[1].size += 1

    elif len(lines) == 3:
        change_spacing(lines, 20)
        if lines[0].text.isalpha():
            lines[0].size = 16

    elif len(lines) == 4:
        if lines[0].text.isalpha():
            lines[0].size = 16

    elif len(lines) == 5:
        change_spacing(lines, 13)
        for i in range(1, len(lines)):
            lines[i].size = 11

    elif len(lines) == 6:
        change_spacing(lines, 13)
        for i in range(1, len(lines)):
            lines[i].size = 11

    # Decreases line size until each line fits
    for line in lines:
        while (0.5 * line.size - 0.5) * len(line.text) > 117:
            line.size -= 0.1

    for i in range(len(lines)):
        if (i > 1 and (lines[i].size < 11 or (lines[i].size <= 12 and not lines[i].text.find('@') == -1))
                and len(lines) > 3):
            lines[i - 1].spacing -= 2 if lines[i].text.find('@') == -1 else 1

    # Draw each line
    current_y = lines[0].size + next_y
    for line in lines:
        line.y = current_y
        current_y += line.spacing
        dwg.add(dwg.text(line.text, x=["50%"], y=[line.y], font_size=line.size,
                         font_family='Beaufort Pro', style='text'))

    return dwg, current_y + 10


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Bag Tag Text to Vector")
    try:
        root.iconbitmap("3d.ico")
    except:
        print('oh well')

    # decide default save location
    home = os.path.expanduser('~')
    file_path = os.path.join(home, 'Downloads', f"vector_{int(time.time())}.svg")

    # Create widgets
    whitespace_1 = tk.Label(root, text=" ")
    whitespace_2 = tk.Label(root, text=" ")
    label = tk.Label(root, text="Enter data here: ")
    entry = tk.Entry(root, width=50)
    button = tk.Button(root, text="Create Vector", command=on_button_click)
    button_file = tk.Button(root, text="Choose File Location", command=on_choose_file)
    file_output_label = tk.Label(root, text="Output location: " + file_path)

    # Place widgets in the window using grid layout
    whitespace_1.grid(row=0, column=0, pady=5)
    whitespace_2.grid(row=4, column=0, pady=5)
    label.grid(row=1, column=0, padx=10, pady=10)
    entry.grid(row=1, column=1, padx=10, pady=10)
    button.grid(row=3, column=0, columnspan=2, pady=10)
    button_file.grid(row=2, column=0, padx=10, pady=10)
    file_output_label.grid(row=2, column=1, padx=10, pady=10)

    # Start the GUI event loop
    root.mainloop()
