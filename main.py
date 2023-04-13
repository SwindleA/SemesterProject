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
block: statement_list END
while_condition: condition END

if_statement: "אם(" condition "):" block  

do_while_statement: "עשה:"statement_list "בעוד" while_condition

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

operator: "*" -> mult
        |"+" -> add
        |"-" -> sub
        | "/" -> divide

literal: NUMBER | var

%import common.CNAME -> NAME
%import common.WS
%import common.INT -> NUMBER 
%ignore WS
"""

#translating into python
def translate(t):
    
    if t.data == 'statement_list':
        return '\n'.join(map(translate, t.children))
    elif t.data == 'assignment':
        lhs, rhs = t.children
        return translate(lhs) + ' = ' +translate(rhs)
    elif t.data == 'if_statement':
        condition, block = t.children
        return 'if ' + translate(condition) +":"+ '\n \t' + translate(block) + '\n'
    elif t.data == 'do_while_statement':
        statement_list, while_condition = t.children
        return 'while ' + translate(while_condition) + ": \n \t" + translate(statement_list) + '\n'
    

            # | print_statement
            # | expression
            # | user_defined_function
    elif t.data =='var' or t.data == 'literal':
        return t.children[0]
    elif t.data == 'gt':
        lhs, rhs = t.children
        return translate(lhs) +' > ' + translate(rhs)
    elif t.data == 'block':
        
        return translate(t.children[0]) + '\n'
    elif t.data == 'condition':
        return translate(t.children[0])
    elif t.data == 'while_condition':
        return translate(t.children[0])

    else:
        raise SyntaxError("bad tree")


parser = Lark(my_grammar)

program_if = """


אם(ש>9):

ש = 8

סוף

"""

program_while = """

עשה:

א = 9   

בעוד ש > 9

סוף 

"""

parse_tree = parser.parse(program_if)

print(parse_tree.pretty())

print(translate(parse_tree))


