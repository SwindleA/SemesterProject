# HebrewScript

# Project Outline
Semester Project for CSCI 3200, Programming Languages. Create a new programming language, parse it, translate it to python and compile/execute.

# About the language 

HebrewScript is an odd combination of Python and Java. Instead of the Roman alphabet this language uses the Hebrew alphabet. 

## Writing in HebrewScript
The language is read right to left, top to bottom. Typing the language follows all the conventions of typing in Hebrew. The symbols like, brackets, parenthesis, etc... are typed using the reverse. For example, the open parenthesis is typed using the closed parenthesis button. It is best to familiarize yourself with how Hebrew is typed before attempting to write programs. There are many instances that the line you are typing appears incorrect until you are finished typing the line. 

## Code structure
The best way to understand the language is to look at the translations outlined in the [Translations](#translations) section. Statement lines such as if, do, and user defined functions end with a colon (':'). <br> 
<br>

block is the code executed within a function.
### Functions are structure as such:

(parameter) function_type: <br> <br>
block <br> <br>
end

<br>

### While statements are in a do-while format:
<br>
   
do: <br>

 block<br>

condition while<br>

end<br><br>

### If statements:
<br>

condition if: <br>

block <br>

end <br>




## Translations


All translations were done using Google Translate. The Hebrew translation of a word is not always a direct translation. As with most things when translated, there is not always one way to translate. 



if - "אם" 

print("Hello World") - ('שלום עולם')הדפס  

do - עשה:

while - בעוד

end - סוף 


define user_function_name(parameter): - להגדיר פ(מ):


return - לחזור


execute{thing to be executed} - {ש}לבצע



## Alphabet:
 Outlined below are all the characters accepted as part of HebrewScript's alphabet. It contains the Hebrew alphabet, minus some vowels, and a few characters. Different fonts can make characters look drastically different.

 <br> Not in any particular order:

 " ' "  &nbsp; "ף"  &nbsp;"א"  &nbsp; "ב"  &nbsp; "ג"  &nbsp; "ך" &nbsp;"ח"  &nbsp; "ו" &nbsp; "ז"  &nbsp; "ה"  &nbsp; "ס"   &nbsp; "י" &nbsp; "כ"   &nbsp;"ל"  &nbsp; "מ"  &nbsp; "נ"  &nbsp;  "ם"  &nbsp;"ץ"  &nbsp; "פ"  &nbsp;  "ע"  &nbsp; "ק"   &nbsp; "ר"  &nbsp; "ש"  &nbsp;  "ת" &nbsp; "ד"  &nbsp; "_"  &nbsp;  "ז"  &nbsp; "צ" 


# Running the Code:

Running the sample programs is as simple as: 
1. Run the main.py file
2. Select a program to run using the corresponding number.
3. Output:
    * The output of the program is printed to the terminal.
    * The following files can be found in the `Output` folder
        * The original HebrewScript program is written to the `program.txt` file.
        * The parse tree is written to the `parse_tree.txt` file.
        * The python interpretation that is executed is written to the `python.txt` file.

NOTE: If an error occurs, simply rerun the program and it should work the second or third time. The errors only occur with programs 2 and 5. This may be due to inconsistancies with how Lark interprets the Hebrew letters. 

## Programs:
1. While loop that increments a counter 0 to 8.
2. Fibonacci Sequence for 9. 
3. Do basic math problems: 
    * 10 + 9
    * 10 * 9
    * 100 / 25 
    * 100 - 25
4. REMOVED - Print the word דלג to the screen
5. Find the Lucas Number for 9.
6. REMOVED - Concatination of strings.
7. REMOVED - String multiplication of a string to create a larger string

* Programs 4,6,7 were removed due to an error printing the Hebrew characters. 



# Known Errors:

1. Anything containing a Hebrew character cannot be printed to the screen. 