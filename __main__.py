import bin.calibrator as calibrator
import bin.clicker as clicker

print("\nProgram will output your mouse coordinates every %d \n" % (calibrator.TIME_TO_PRINT)+
"seconds. Once you are satisfied with position, press ENTER key to set printed \n" +
"position. When you set all positions, the program will start iterating.")

amount = int(input("How many mouse positions do you have before repetition: "))

mouse_positions = calibrator.calibrateMousePositions(amount)

timeout = input("Timeout in seconds between clicks (0 to ignore): ")
repeat = input("How many times do you want to repeat the combination? (0 for indefinite): ")

clicker.clickPositions(mouse_positions, repeat, timeout)

print("You're all clicked up!")