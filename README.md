                                                          # Python_Calculator
This is a simple calculator made by Python Language using Tkinter.
Anybody having a basic knowledge of python functions, python operators can easily make this simple calculator.
In this python program firstly I have imported lambda function which is used for mathematical calculation.
Then I have imported Tkinter function.
A application window is created then a title "Simple Calculator" is given to the application.

A display window is created for the calculator. 

For the calculator to work we need to make clickable buttons. 
So for the buttons to be clickable a separate function is made under "button_click(number)" which is applicable for all the buttons in the calculator.
This function makes the clicked buttons store the value as the first number.

Then separate functions are made for differet buttons like:
For adding the numbers
  "button_add()" function is made which does the work of adding any two user input numbers
For subtracting the numbers
  "button-sub()" function is made which does the work of subtracting any two user input numbers
For multiplying the numbers
  "button-mul()" function is made which does the work of multiplying any two user input numbers
For dividing the numbers
  "button-div()" function is made which does the work of dividing any two user input numbers

The "button_equal()" function here is a little tricky as it is the most important because it decides what operation should be done for the given two user input numbers.
The "button_clear()" function does the work of clearing the screen or it resets the value to zero for the user to input another new number.

Then after making the functions for performing different operations actual buttons are required to be made. 
So firstly the function is defined by using Tkinter Button widget and it is represented in the application window by using Tkinter grid method.
So all the required buttons like the numbers for the calculator, addition, subtraction, multiplication, division, etc are properly defined and displayed on the screen.
The user can input any two different numbers and can perform any mathematical calculation provided in the calculator.



![Preview](https://user-images.githubusercontent.com/63782923/115898885-cea94880-a47d-11eb-921e-3c2fe0d83c24.JPG)

