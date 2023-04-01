from lark import Lark

my_grammar = """
?start: statement_list

statement_list: statement+

?statement: assignment 
            | if_statement
            

assignment: expression  "=" var

var: "א" | "ב" | "ג" | "ך" | "ח" | "ו" | "ז" | "ה" | "ס"  | "י" "כ" | "ל" | "מ" | "נ" | "ם" | "ץ" | "פ"  | "ע" | "ק"  | "ר" | "ש"  | "ת"

output_statement: NAME

if_statement: "אִם" expression   statement_list "סוף"
while_statement: "עשה" statement_list  "בעוד" expression "סוף"
print_statement: "(" output_statement ")הדפס"

?expression: var
            | literal
            | expression "<" expression -> gt
            | expression ">" expression -> lt
            | expression ">=" expression -> ge
            | expression "<=" expression -> le
            | expression "==" expression -> eq

literal: NUMBER

%import common.CNAME -> NAME
%import common.WS
%import common.INT -> NUMBER 
%ignore WS

"""
