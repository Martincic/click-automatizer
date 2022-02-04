import bin.calibrator as calibrator

print("\nProgram will output your mouse coordinates every %d \n" % (calibrator.TIME_TO_PRINT)+
"seconds. Once you are satisfied with position, press ENTER key to set printed \n" +
"position. When you set all positions, the program will start iterating.")

amount = int(input("How many mouse positions do you have before repetition: "))
mouse_positions = calibrator.calibrateMousePositions(amount)

input("Do you want a timeout between clicks? (0 to ignore): ")


print("You're all clicked up!")