# HebrewScript

# Project Outline
Semester Project for CSCI 3200, Programming Languages. Creating a new programming language, parsing it, translate it to python and compile/execute.

# About the language 

HebrewScript is an odd combination of Python and Java. Instead of the Roman alphabet this language uses the Hebrew alphabet. 

## Writing in HebrewScript
The language is read right to left, top to bottom. Typing the language follows all of the conventions of typing in Hebrew. The symbols like, brackets, parenthesis, etc... are typed using the reverse. For example, the open parenthesis is typed using the closed parenthesis button. It is best to familirize yourself with how Hebrew is tpyed before attempting to write programs. There are many instances that the line you are typing appears incorrect until you are finished typing the line. 

## Code structure
The best way to understand the language is to look at the translations outlined in the [Translations](#translations) section. Statement lines such as if, do, and user defined functions end with a colon(':'). <br> 
<br>

block is the code executed within a function.
### Functions are structure as such:

(paramter) function_type: <br> <br>
block <br> <br>
end

<br>

### While statements are in a do-while foramt:
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



"אם" - if

print("Hello World") - ('שלום עולם')הדפס  

do - עשה:
while - בעוד

end - סוף 


define user_function_name(paramter): - להגדיר פ(מ):


return - לחזור


execute{thing to be executed} - {ש}לבצע



## Alphabet:
 Outlined below are all the characters accepted as part of HebrewScript's alphabet. It contains the Hebrew alphabet,minus some vowels, and a few characters. Different fonts can make characters look drastically different.

 <br> Not in any particular order:

 " ' "  &nbsp; "ף"  &nbsp;"א"  &nbsp; "ב"  &nbsp; "ג"  &nbsp; "ך" &nbsp;"ח"  &nbsp; "ו" &nbsp; "ז"  &nbsp; "ה"  &nbsp; "ס"   &nbsp; "י" &nbsp; "כ"   &nbsp;"ל"  &nbsp; "מ"  &nbsp; "נ"  &nbsp;  "ם"  &nbsp;"ץ"  &nbsp; "פ"  &nbsp;  "ע"  &nbsp; "ק"   &nbsp; "ר"  &nbsp; "ש"  &nbsp;  "ת" &nbsp; "ד"  &nbsp; "_"  &nbsp;  "ז"  &nbsp; "צ" 


# Running the Code:

Running the sample programs is as simple as: 
1. Run the main.py file
2. Select a progam to run using the corresponding number.
3. Select whether or not the HebrewScript for the program will be printed to the screen.
4. Select whether or not the parse tree is printed to the screen.
5. Select whether or not the python translation of HebrewScript is printed to the screen. 