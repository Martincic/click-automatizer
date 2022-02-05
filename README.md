# click-automatizer
Used for repetitive actions which consist of mouse operations

## Disclaimer
Works only on Windows machines since it uses `win32api` and was tested only on Python 3.10. 
**Use responsibly and at your own risk**, if you get banned form websites for automating clicks or if something wrong is clicked I am not responsible.

## Installation
```
pip install -r requirements.txt
```

## Run
```
python click-automatizer
```

## Warning
Be careful with setting timeout to 0 between clicks, this is reason why safety killswitch was introduced. If your mouse goes rouge, you can always press `ESC` key to safely exit the program.

## Inputs

`How many mouse positions do you have before repetition:` - input is integer (a whole number). Here you select the amount of positions which you need to be clicked before repetition. Eg. if you want to automatize downloading photos from messenger, you would input `2` because you need first click for "Download" button, and second click for "next photo". Those two clicks will repeat.

After this step, the program will output the position of your mouse. Do not left click or right click the mouse, because you will lose focus from the terminal. You just want to hover the mouse over position where you need it, and once your position is printed out press `ENTER`. Repeat until you select all positions you need.

`Timeout in seconds between clicks (0 to ignore):` - input is float (decimal number), the program will wait before clicking this amount of time.

`How many times do you want to repeat the combination? (0 for indefinite):` - input is integer (a whole number).

From here, the program will start clicking until it finishes or until terminated with `ESC`.
