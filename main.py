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
            | return
            | execute
            

assignment: var   " = " literal | var   " = " string 

ALPHA: "'"|"ף"|"א" | "ב" | "ג" | "ך" | "ח" | "ו" | "ז" | "ה" | "ס"  | "י" "כ" | "ל" | "מ" | "נ" | "ם" | "ץ" | "פ"  | "ע" | "ק"  | "ר" | "ש"  | "ת" |"ד" | "_" | "(" | ")" | "ז" | "צ" 

var : ALPHA+
?function_name: var
parameter: (ALPHA)* | operation



END: "סוף" 

end: END->end




return: "לחזור" num_var | "לחזור" execute


?print_output: string | var | operation | NUMBER

string: "'" ALPHA*  "'"

condition: comparison
block: statement_list end
while_condition: condition end

if_statement: "אם(" condition "):" block  

do_while_statement: "עשה:"statement_list "בעוד" while_condition


print_statement: "הדפס(" print_output ")" 

user_defined_function:  "להגדיר" function_name "(" parameter "):" statement_list end

execute: "לבצע{" function_name "(" parameter ")}"

?expression: num_var
            |comparison
            | operation

comparison: expression ">" expression -> gt
            | expression "<" expression -> lt
            | expression ">=" expression -> ge
            | expression "<=" expression -> le
            | expression "==" expression -> eq

operation: num_var operator num_var

operator: "*" -> mult
        |"+" -> add
        |"-" -> sub
        | "/" -> divide

literal: NUMBER

num_var: literal | var


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
    
    elif t.data ==  'print_statement':
        if t.children[0].data == "var" or t.children[0].data == 'operation':
            
            return 'print(' + translate(t.children[0]) + ')'
        else:
            
            return 'print("' + translate(t.children[0])+'")'
            
    elif t.data == 'user_defined_function':
        function_name, parameter, u_statement_list, end = t.children

        return "def " + translate(function_name) + " ("+translate(parameter)+"):\n \t"+ translate(u_statement_list)

    elif t.data == 'operation':
        lhs, operator, rhs = t.children
        
        return translate(lhs) + translate(operator) + translate(rhs)

    elif t.data =='var':
        output =""
        for child in t.children:
            output+=child

        #NOTE: the return needs to be reverse because hebrew is right to left and the parse reads it left to right.
        return output[::-1]
    
    elif t.data == 'literal':
        return t.children[0]
    
    elif t.data == 'ALPHA':
        return t.children[0]

    elif t.data == 'gt':
        lhs, rhs = t.children
        return translate(lhs) +' > ' + translate(rhs)
    
    elif t.data == 'lt':
        lhs, rhs = t.children
        return translate(lhs) +' < ' + translate(rhs)
    
    elif t.data == 'ge':
        lhs, rhs = t.children
        return translate(lhs) +' >= ' + translate(rhs)
    
    elif t.data == 'le':
        lhs, rhs = t.children
        return translate(lhs) +' <= ' + translate(rhs)
    
    elif t.data == 'eq':
        lhs, rhs = t.children
        return translate(lhs) +' == ' + translate(rhs)

    elif t.data == 'block':
        statement, end = t.children
        
        return translate(statement) + '\n' + translate(end)
    
    elif t.data == 'condition':

        return translate(t.children[0])
    
    elif t.data == 'while_condition':
        return translate(t.children[0])
    
    elif t.data == 'output_statement':
        output =""
        for child in t.children:
            output+=child

        #NOTE: the return needs to be reverse because hebrew is right to left and the parse reads it left to right.
        return output[::-1]
    
    elif  t.data == 'string':
        output =""
        for child in t.children:
            output+=child

        #NOTE: the return needs to be reverse because hebrew is right to left and the parse reads it left to right.
        return output[::-1]

    elif t.data == 'parameter':

       

        if t.children[0] != "operation":
            
            return t.children[0]
       
        return translate(t.children[0]) 

        
    


    elif t.data == 'add':
        return '+'
    elif t.data == 'sub':
        return '-'
    elif t.data == 'mult':
        return '*'
    elif t.data == 'divide':
        return '/'
    
    elif t.data == 'num':
        return t.children[0]
    

    elif t.data == "end":
        return '\n'
    
    
    elif t.data == 'return':
       
        return "return " + translate(t.children[0])

    elif t.data == 'execute':
        
        function_n , parameter = t.children
        return translate(function_n) + translate(parameter)
    elif t.data =='num_var':

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

program_print = """

הדפס('גש ףשד')

"""

program_userfunction = """

להגדיר ש_דשד( ש):
ש = 8

סוף

"""
#https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/
program_fibonacci = """

להגדיר פ(מ):

אם(מ == 0):

לחזור 0

סוף



אם(מ == 1 ):

לחזור 1

סוף


אם(מ == 2 ):

לחזור 1

סוף


לחזור לבצע{ פ(מ-1)} 






סוף






"""




program_print_variable = """

ש = 9


הדפס(ש)



"""

program_addition = """



הדפס( 9 + 9 )


"""
program_basic_math = """



הדפס( 10 + 9 )


הדפס( 10 * 9 )


הדפס( 100 / 25 )


הדפס( 100 - 25 )


"""

program_math_with_variable = """

ף = 4

א = 10


הדפס( א - ף )




"""

program_variable_with_string = """

ה = 'דלג'


הדפס(ה)

"""




parse_tree = parser.parse(program_fibonacci)

print(parse_tree.pretty())

translation = translate(parse_tree)
print(translation)

exec(translation)




