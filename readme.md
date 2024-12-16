# Bag Tag to Vector Program
**Created by Jackson Grizzle for Legit 3D**
## Purpose
The intended use of this program is to turn the data from the Chrome extension to an `.SVG` file

## Directions
### Python Project vs Standalone

Via GitHub:
 - Clone the project 
 - Run `main.py`

Via GitFront
 - Navigate to `\output\main.exe`
 - Download `main.exe` and run it

`main.exe` can be renamed and moved to different directories

### Use
 - Right click, select all, and copy in the bottom section of the Chrome extension
 - Paste the data into the box labeled *'Enter Data Here'*
 - The default output is in the default Downloads folder
 - To change the output file location or name click *'Choose File Location'* and pick a new file destination
 - Press *'Create Vector'*
 - If all goes well, there will be a popup confirming the process is finished. You can close the window 

### Notes
 - The SVG output will NOT work in Lightburn until converted to paths 
 - The SVG file will ONLY WORK in the same directory as `BeauMed.ttf` until converted to paths

## Converting to Paths
We can use a program called Inkscape to convert each text object to a path. We do this so Lightburn and other programs
will be able to read the SVG file
### Installing Inkscape
 - [Visit Inkscape's website and install Inkscape](https://inkscape.org/release/inkscape-1.3.2/windows/64-bit/exe/dl/)
 - Download `BeauMed.ttf`
 - Go to `Windows settings > Personalization > Fonts > Browse and Install fonts` and choose `BeauMed.ttf`
 - Make sure this font shows up as "Beaufort Pro"
 - Everything should be ready to use

### Using Inkscape
 - Open Inkscape and open the SVG file
 - Verify that the font *is* Beaufort Pro and not the default Sans Serif
 - If everything looks good, select everything with `Ctrl + A`
 - Press `Shift + Ctrl + C` or navigate to `Paths > Object to Paths` to convert the text to a path
 - Save with `Ctrl + S` or navigate to `File > Save` 

The SVG file should now be good to use in Lightburn or any other external software

### If the font appears to be incorrect in inkscape...
 - Download the program from GitHub or GitFront again to ensure you are using the latest version
 - Make sure you have `BeauMed.ttf` installed to Windows or in Inkscape's custom font folder