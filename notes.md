input() returns the value typed by the user, which can then be stored in a variable.
A variable is a named container that stores data, such as name, bill, tip_percentage, or total.
In hello.py, .strip() removes extra spaces and .title() formats the name with capital letters.
One bug I hit was that user input is text by default, so I had to convert bill and tip percentage to float before doing calculations.
