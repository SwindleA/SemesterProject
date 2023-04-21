from lark import Lark
from lark import lexer

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
            | execute
            

assignment: var   " = " literal | var   " = " string | var " = " operation

ALPHA: "'"|"ף"|"א" | "ב" | "ג" | "ך" | "ח" | "ו" | "ז" | "ה" | "ס"  | "י" "כ" | "ל" | "מ" | "נ" | "ם" | "ץ" | "פ"  | "ע" | "ק"  | "ר" | "ש"  | "ת" |"ד" | "_" |  "ז" | "צ" 

var : ALPHA+
?function_name: var
parameter: (ALPHA)* | operation | literal

function: function_name "(" parameter ")"

END: "סוף" 

end: END->end




return: "לחזור" expression | "לחזור" execute


?print_output: string | var | operation | NUMBER | function

string: "'" ALPHA*  "'"

condition: comparison

block: statement_list end
block_while: statement_list

while_condition: condition end

if_statement: "אם(" condition "):" block  

do_while_statement: "עשה:" block_while "בעוד" while_condition


print_statement: "הדפס(" print_output ")" 

user_defined_function:  "להגדיר" function ":" block

execute: "לבצע{" var "}"  

?expression: var
            | literal
            |comparison
            | operation
            | return

comparison: expression ">" expression -> gt
            | expression "<" expression -> lt
            | expression ">=" expression -> ge
            | expression "<=" expression -> le
            | expression "==" expression -> eq

operation: expression operator expression | function operator function

operator: "*" -> mult
        |"+" -> add
        |"-" -> sub
        | "/" -> divide

literal: NUMBER




%import common.CNAME -> NAME
%import common.WS
%import common.INT -> NUMBER 
%ignore WS
"""

tab_str = "\t"

#translating into python
def translate(t, tab):
    
    if t.data == 'statement_list':
        # return '\n'.join(map(translate , t.children ))
        return '\n'.join([translate(x,tab)for x in t.children])
    
    elif t.data == 'assignment':
        lhs, rhs = t.children
        return tab_str*tab+ translate(lhs,tab) + ' = ' +translate(rhs,tab)
        #return tab_str*tab +translate(lhs,tab) +"=" +''.join([translate(x,tab)for x in t.children[1:]])
    
    elif t.data == 'if_statement':
       
        condition, block = t.children
        return tab_str*tab + 'if ' + translate(condition,0) +":"+ '\n' + translate(block,tab) + '\n'
    
    elif t.data == 'do_while_statement':
        block, while_condition = t.children
        return tab_str*tab+'while ' + translate(while_condition,0) + ": \n" + translate(block,tab) + '\n'
    
    elif t.data ==  'print_statement':
        
       
        return tab_str*tab+'print(' + translate(t.children[0],0) + ')'
       
            
    elif t.data == 'user_defined_function':
        function_f, u_statement_list = t.children

        return tab_str*tab + "def " + translate(function_f,0) +":\n"+ translate(u_statement_list,tab)

    elif t.data == 'operation':
       
        lhs, operator, rhs = t.children
        
        return tab_str*tab + translate(lhs,0) + translate(operator,0) + translate(rhs,0)

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
        return tab_str*tab + translate(lhs,0) +' > ' + translate(rhs,0)
    
    elif t.data == 'lt':
        lhs, rhs = t.children
        return tab_str*tab + translate(lhs,0) +' < ' + translate(rhs,0)
    
    elif t.data == 'ge':
        lhs, rhs = t.children
        return tab_str*tab + translate(lhs,0) +' >= ' + translate(rhs,0)
    
    elif t.data == 'le':
        lhs, rhs = t.children
        return tab_str*tab + translate(lhs,0) +' <= ' + translate(rhs,0)
    
    elif t.data == 'eq':
        lhs, rhs = t.children
        
        return tab_str*tab + translate(lhs,0) +' == ' + translate(rhs,0)

    elif t.data == 'block':
        statement, end = t.children
        
        return tab_str*tab + translate(statement,tab+1) + '\n' + translate(end,tab)
    elif t.data == 'block_while':
        statement = t.children[0]
        
        return tab_str*tab + translate(statement,tab+1) + '\n' 
    
    elif t.data == 'condition':

        return translate(t.children[0],0)
    
    elif t.data == 'while_condition':
        return translate(t.children[0],0)
    
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
        return "'"+ output[::-1] + "'"

    elif t.data == 'parameter':

        
        if isinstance(t.children[0],lexer.Token):
            
            return "("+ t.children[0]+")"
        
        
        return  "("+ translate(t.children[0],0) + ")"
        
    elif t.data == 'function':
        function_name, parameter = t.children
        return translate(function_name,0) + translate(parameter,0)

        
    


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
        
        return tab_str*tab + "return " + translate(t.children[0],0)

    elif t.data == 'execute':
        
        # function_n , parameter = t.children
        
        # return tab_str*tab + translate(function_n,0) + "(" + translate(parameter,0)+")"
        return translate(t.children[0],0)
    
    elif t.data =='num_var':

        return translate(t.children[0],0)

    else:
        raise SyntaxError("bad tree")


parser = Lark(my_grammar)

program_if = """


אם(ש>9):

ש = 8

סוף

"""

program_while = """

ש = 0

עשה:

הדפס(ש)

ש = ש + 1

בעוד ש < 9

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


ף = פ(מ -1 )+פ( מ - 2 )

לחזור לבצע{ף}








סוף


הדפס(פ(9))


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

translation = translate(parse_tree,0)
print(translation)



exec(translation)




