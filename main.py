from lark import Lark


# NOTE: some things do not appear to be right to left in the grammer but when displaying to the user, they are correctly right to left
# The above note may be because of ignoring white space causes issues. 
my_grammar = """
?start: statement_list

?statement_list: statement+

?statement: assignment 
            | if_statement
            | do_while_statement
            | print_statement
            | expression
            | user_defined_function
            

assignment: var   " = " expression

ALPHA: "ף"|"א" | "ב" | "ג" | "ך" | "ח" | "ו" | "ז" | "ה" | "ס"  | "י" "כ" | "ל" | "מ" | "נ" | "ם" | "ץ" | "פ"  | "ע" | "ק"  | "ר" | "ש"  | "ת" |"ד"

var : ALPHA+
function_name: var | var "_" var
parameter: ALPHA*

END: "סוף"


output_statement: ALPHA+

condition: comparison

if_statement: "אם(" condition "):" statement_list END

do_while_statement: "עשה:"statement_list "בעוד" condition END

print_statement: "הדפס('" output_statement "')"


user_defined_function:  "להגדיר" function_name "(" parameter "):" statement_list END


?expression: var
            | literal
            |comparison
            | operation

comparison: expression ">" expression -> gt
            | expression "<" expression -> lt
            | expression ">=" expression -> ge
            | expression "<=" expression -> le
            | expression "==" expression -> eq

operation: literal operator literal

operator: "*"|"+"|"-"| "/"

literal: NUMBER

%import common.CNAME -> NAME
%import common.WS
%import common.INT -> NUMBER 
%ignore WS
"""
