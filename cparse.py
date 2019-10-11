import sys
import clex
import ply.yacc as yacc
from classes import AST

# Get the token map
tokens = clex.tokens


ast_roots_lits = []

# translation-unit:


def p_translation_unit_1(t):
    'translation_unit : external_declaration'
    t[0] = ast_roots_lits.append(AST("translation_unit", [t[1]]))


def p_translation_unit_2(t):
    'translation_unit : translation_unit external_declaration'
    t[0] = ast_roots_lits.append(AST("translation_unit", [t[1], t[2]]))


# external-declaration:


def p_external_declaration_1(t):
    'external_declaration : function_definition'
    t[0] = AST("external_declaration", [t[1]])


def p_external_declaration_2(t):
    'external_declaration : declaration'
    t[0] = AST("external_declaration", [t[1]])


# function-definition:


def p_function_definition_1(t):
    'function_definition : declaration_specifiers declarator declaration_list compound_statement'
    t[0] = AST("function_definition", [t[1], t[2], t[3], t[4]])


def p_function_definition_2(t):
    'function_definition : declarator declaration_list compound_statement'
    t[0] = AST("function_definition", [t[1], t[2], t[3]])


def p_function_definition_3(t):
    'function_definition : declarator compound_statement'
    t[0] = AST("function_definition", [t[1], t[2]])


def p_function_definition_4(t):
    'function_definition : declaration_specifiers declarator compound_statement'
    t[0] = AST("function_definition", [t[1], t[2], t[3]])


# declaration:


def p_declaration_1(t):
    'declaration : declaration_specifiers init_declarator_list SEMI'
    t[0] = AST("declaration", [t[1], t[2]])


def p_declaration_2(t):
    'declaration : declaration_specifiers SEMI'
    t[0] = AST("declaration", [t[1]])


# declaration-list:


def p_declaration_list_1(t):
    'declaration_list : declaration'
    t[0] = AST("declaration_list", [t[1]])


def p_declaration_list_2(t):
    'declaration_list : declaration_list declaration '
    t[0] = AST("declaration_list", [t[1], t[2]])


# declaration-specifiers


def p_declaration_specifiers_1(t):
    'declaration_specifiers : storage_class_specifier declaration_specifiers'
    t[0] = AST("declaration_specifiers", [t[1], t[2]])


def p_declaration_specifiers_2(t):
    'declaration_specifiers : type_specifier declaration_specifiers'
    t[0] = AST("declaration_specifiers", [t[1], t[2]])


def p_declaration_specifiers_3(t):
    'declaration_specifiers : type_qualifier declaration_specifiers'
    t[0] = AST("declaration_specifiers", [t[1], t[2]])


def p_declaration_specifiers_4(t):
    'declaration_specifiers : storage_class_specifier'
    t[0] = AST("declaration_specifiers", [t[1]])


def p_declaration_specifiers_5(t):
    'declaration_specifiers : type_specifier'
    t[0] = AST("declaration_specifiers", [t[1]])


def p_declaration_specifiers_6(t):
    'declaration_specifiers : type_qualifier'
    t[0] = AST("declaration_specifiers", [t[1]])


# storage-class-specifier


def p_storage_class_specifier(t):
    '''storage_class_specifier : AUTO
                               | REGISTER
                               | STATIC
                               | EXTERN
                               | TYPEDEF
                               '''
    t[0] = AST("storage_class_specifier", [t[1]])


# type-specifier:


def p_type_specifier(t):
    '''type_specifier : VOID
                      | CHAR
                      | SHORT
                      | INT
                      | LONG
                      | FLOAT
                      | DOUBLE
                      | SIGNED
                      | UNSIGNED
                      | struct_or_union_specifier
                      | enum_specifier
                      | TYPEID
                      '''
    t[0] = AST("type_specifier", [t[1]])


# type-qualifier:


def p_type_qualifier(t):
    '''type_qualifier : CONST
                      | VOLATILE'''
    t[0] = AST("type_qualifier", [t[1]])


# struct-or-union-specifier


def p_struct_or_union_specifier_1(t):
    'struct_or_union_specifier : struct_or_union ID LBRACE struct_declaration_list RBRACE'
    t[0] = AST("struct_or_union_specifier", [t[1], t[2], t[3], t[4], t[5]])


def p_struct_or_union_specifier_2(t):
    'struct_or_union_specifier : struct_or_union LBRACE struct_declaration_list RBRACE'
    t[0] = AST("struct_or_union_specifier", [t[1], t[2], t[3], t[4]])


def p_struct_or_union_specifier_3(t):
    'struct_or_union_specifier : struct_or_union ID'
    t[0] = AST("struct_or_union_specifier", [t[1], t[2]])


# struct-or-union:


def p_struct_or_union(t):
    '''struct_or_union : STRUCT
                       | UNION
                       '''
    t[0] = AST("struct_or_union", [t[1]])


# struct-declaration-list:


def p_struct_declaration_list_1(t):
    'struct_declaration_list : struct_declaration'
    t[0] = AST("struct_declaration_list", [t[1]])


def p_struct_declaration_list_2(t):
    'struct_declaration_list : struct_declaration_list struct_declaration'
    t[0] = AST("struct_declaration_list", [t[1], t[2]])


# init-declarator-list:


def p_init_declarator_list_1(t):
    'init_declarator_list : init_declarator'
    t[0] = AST("init_declarator_list", [t[1]])


def p_init_declarator_list_2(t):
    'init_declarator_list : init_declarator_list COMMA init_declarator'
    t[0] = AST("init_declarator_list", [t[1], t[2], t[3]])


# init-declarator


def p_init_declarator_1(t):
    'init_declarator : declarator'
    t[0] = AST("init_declarator", [t[1]])


def p_init_declarator_2(t):
    'init_declarator : declarator EQUALS initializer'
    t[0] = AST("init_declarator", [t[1], t[2], t[3]])


# struct-declaration:


def p_struct_declaration(t):
    'struct_declaration : specifier_qualifier_list struct_declarator_list SEMI'
    t[0] = AST("struct_declaration", [t[1], t[2]])


# specifier-qualifier-list:


def p_specifier_qualifier_list_1(t):
    'specifier_qualifier_list : type_specifier specifier_qualifier_list'
    t[0] = AST("specifier_qualifier_list", [t[1], t[2]])


def p_specifier_qualifier_list_2(t):
    'specifier_qualifier_list : type_specifier'
    t[0] = AST("specifier_qualifier_list", [t[1]])


def p_specifier_qualifier_list_3(t):
    'specifier_qualifier_list : type_qualifier specifier_qualifier_list'
    t[0] = AST("specifier_qualifier_list", [t[1], t[2]])


def p_specifier_qualifier_list_4(t):
    'specifier_qualifier_list : type_qualifier'
    t[0] = AST("specifier_qualifier_list", [t[1]])


# struct-declarator-list:


def p_struct_declarator_list_1(t):
    'struct_declarator_list : struct_declarator'
    t[0] = AST("struct_declarator_list", [t[1]])


def p_struct_declarator_list_2(t):
    'struct_declarator_list : struct_declarator_list COMMA struct_declarator'
    t[0] = AST("struct_declarator_list", [t[1], t[2], t[3]])


# struct-declarator:


def p_struct_declarator_1(t):
    'struct_declarator : declarator'
    t[0] = AST("struct_declarator", [t[1]])


def p_struct_declarator_2(t):
    'struct_declarator : declarator COLON constant_expression'
    t[0] = AST("struct_declarator", [t[1], t[2], t[3]])


def p_struct_declarator_3(t):
    'struct_declarator : COLON constant_expression'
    t[0] = AST("struct_declarator", [t[1], t[2]])


# enum-specifier:


def p_enum_specifier_1(t):
    'enum_specifier : ENUM ID LBRACE enumerator_list RBRACE'
    t[0] = AST("enum_specifier", [t[1], t[2], t[3], t[4], t[5]])


def p_enum_specifier_2(t):
    'enum_specifier : ENUM LBRACE enumerator_list RBRACE'
    t[0] = AST("enum_specifier", [t[1], t[2], t[3], t[4]])


def p_enum_specifier_3(t):
    'enum_specifier : ENUM ID'
    t[0] = AST("enum_specifier", [t[1], t[2]])


# enumerator_list:


def p_enumerator_list_1(t):
    'enumerator_list : enumerator'
    t[0] = AST("enumerator_list", [t[1]])


def p_enumerator_list_2(t):
    'enumerator_list : enumerator_list COMMA enumerator'
    t[0] = AST("enumerator_list", [t[1], t[2], t[3]])


# enumerator:


def p_enumerator_1(t):
    'enumerator : ID'
    t[0] = AST("enumerator", [t[1]])


def p_enumerator_2(t):
    'enumerator : ID EQUALS constant_expression'
    t[0] = AST("enumerator", [t[1], t[2], t[3]])


# declarator:


def p_declarator_1(t):
    'declarator : pointer direct_declarator'
    t[0] = AST("declarator", [t[1], t[2]])


def p_declarator_2(t):
    'declarator : direct_declarator'
    t[0] = AST("declarator", [t[1]])


# direct-declarator:


def p_direct_declarator_1(t):
    'direct_declarator : ID'
    t[0] = AST("direct_declarator", [t[1]])


def p_direct_declarator_2(t):
    'direct_declarator : LPAREN declarator RPAREN'
    t[0] = AST("direct_declarator", [t[1], t[2], t[3]])


def p_direct_declarator_3(t):
    'direct_declarator : direct_declarator LBRACKET constant_expression_opt RBRACKET'
    t[0] = AST("direct_declarator", [t[1], t[2], t[3], t[4]])


def p_direct_declarator_4(t):
    'direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN '
    t[0] = AST("direct_declarator", [t[1], t[2], t[3], t[4]])


def p_direct_declarator_5(t):
    'direct_declarator : direct_declarator LPAREN identifier_list RPAREN '
    t[0] = AST("direct_declarator", [t[1], t[2], t[3], t[4]])


def p_direct_declarator_6(t):
    'direct_declarator : direct_declarator LPAREN RPAREN '
    t[0] = AST("direct_declarator", [t[1], t[2], t[3]])


# pointer:


def p_pointer_1(t):
    'pointer : TIMES type_qualifier_list'
    t[0] = AST("pointer", [t[1], t[2]])


def p_pointer_2(t):
    'pointer : TIMES'
    t[0] = AST("pointer", [t[1]])


def p_pointer_3(t):
    'pointer : TIMES type_qualifier_list pointer'
    t[0] = AST("pointer", [t[1], t[2], t[3]])


def p_pointer_4(t):
    'pointer : TIMES pointer'
    t[0] = AST("pointer", [t[1], t[2]])


# type-qualifier-list:


def p_type_qualifier_list_1(t):
    'type_qualifier_list : type_qualifier'
    t[0] = AST("type_qualifier_list", [t[1]])


def p_type_qualifier_list_2(t):
    'type_qualifier_list : type_qualifier_list type_qualifier'
    t[0] = AST("type_qualifier_list", [t[1], t[2]])


# parameter-type-list:


def p_parameter_type_list_1(t):
    'parameter_type_list : parameter_list'
    t[0] = AST("parameter_type_list", [t[1]])


def p_parameter_type_list_2(t):
    'parameter_type_list : parameter_list COMMA ELLIPSIS'
    t[0] = AST("parameter_type_list", [t[1], t[2], t[3]])


# parameter-list:


def p_parameter_list_1(t):
    'parameter_list : parameter_declaration'
    t[0] = AST("parameter_list", [t[1]])


def p_parameter_list_2(t):
    'parameter_list : parameter_list COMMA parameter_declaration'
    t[0] = AST("parameter_list", [t[1], t[2], t[3]])


# parameter-declaration:


def p_parameter_declaration_1(t):
    'parameter_declaration : declaration_specifiers declarator'
    t[0] = AST("parameter_declaration", [t[1], t[2]])


def p_parameter_declaration_2(t):
    'parameter_declaration : declaration_specifiers abstract_declarator_opt'
    t[0] = AST("parameter_declaration", [t[1], t[2]])


# identifier-list:


def p_identifier_list_1(t):
    'identifier_list : ID'
    t[0] = AST("identifier_list", [t[1]])


def p_identifier_list_2(t):
    'identifier_list : identifier_list COMMA ID'
    t[0] = AST("identifier_list", [t[1], t[2], t[3]])


# initializer:


def p_initializer_1(t):
    'initializer : assignment_expression'
    t[0] = AST("initializer", [t[1]])


def p_initializer_2(t):
    '''initializer : LBRACE initializer_list RBRACE
                   | LBRACE initializer_list COMMA RBRACE'''
    if len(t) == 4:
        t[0] = AST("initializer", [t[1], t[2], t[3]])
    else:
        t[0] = AST("initializer", [t[1], t[2], t[3], t[4]])


# initializer-list:


def p_initializer_list_1(t):
    'initializer_list : initializer'
    t[0] = AST("initializer_list", [t[1]])


def p_initializer_list_2(t):
    'initializer_list : initializer_list COMMA initializer'
    t[0] = AST("initializer_list", [t[1], t[2], t[3]])


# type-name:


def p_type_name(t):
    'type_name : specifier_qualifier_list abstract_declarator_opt'
    t[0] = AST("type_name", [t[1], t[2]])


def p_abstract_declarator_opt_1(t):
    'abstract_declarator_opt : empty'
    t[0] = AST("abstract_declarator_opt", [t[1]])


def p_abstract_declarator_opt_2(t):
    'abstract_declarator_opt : abstract_declarator'
    t[0] = AST("abstract_declarator_opt", [t[1]])


# abstract-declarator:


def p_abstract_declarator_1(t):
    'abstract_declarator : pointer '
    t[0] = AST("abstract_declarator", [t[1]])


def p_abstract_declarator_2(t):
    'abstract_declarator : pointer direct_abstract_declarator'
    t[0] = AST("abstract_declarator", [t[1], t[2]])


def p_abstract_declarator_3(t):
    'abstract_declarator : direct_abstract_declarator'
    t[0] = AST("abstract_declarator", [t[1]])


# direct-abstract-declarator:


def p_direct_abstract_declarator_1(t):
    'direct_abstract_declarator : LPAREN abstract_declarator RPAREN'
    t[0] = AST("direct_abstract_declarator", [t[1], t[2], t[3]])


def p_direct_abstract_declarator_2(t):
    'direct_abstract_declarator : direct_abstract_declarator LBRACKET constant_expression_opt RBRACKET'
    t[0] = AST("direct_abstract_declarator", [t[1], t[2], t[3], t[4]])


def p_direct_abstract_declarator_3(t):
    'direct_abstract_declarator : LBRACKET constant_expression_opt RBRACKET'
    t[0] = AST("direct_abstract_declarator", [t[1], t[2], t[3]])


def p_direct_abstract_declarator_4(t):
    'direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list_opt RPAREN'
    t[0] = AST("direct_abstract_declarator", [t[1], t[2], t[3], t[4]])


def p_direct_abstract_declarator_5(t):
    'direct_abstract_declarator : LPAREN parameter_type_list_opt RPAREN'
    t[0] = AST("direct_abstract_declarator", [t[1], t[2], t[3]])


# Optional fields in abstract declarators


def p_constant_expression_opt_1(t):
    'constant_expression_opt : empty'
    t[0] = AST("constant_expression_opt", [t[1]])


def p_constant_expression_opt_2(t):
    'constant_expression_opt : constant_expression'
    t[0] = AST("constant_expression_opt", [t[1]])


def p_parameter_type_list_opt_1(t):
    'parameter_type_list_opt : empty'
    t[0] = AST("parameter_type_list_opt", [t[1]])


def p_parameter_type_list_opt_2(t):
    'parameter_type_list_opt : parameter_type_list'
    t[0] = AST("parameter_type_list_opt", [t[1]])


# statement:


def p_statement(t):
    '''
    statement : labeled_statement
              | expression_statement
              | compound_statement
              | selection_statement
              | iteration_statement
              | jump_statement
              '''
    t[0] = AST("statement", [t[1]])


# labeled-statement:


def p_labeled_statement_1(t):
    'labeled_statement : ID COLON statement'
    t[0] = AST("labeled_statement", [t[1], t[2], t[3]])


def p_labeled_statement_2(t):
    'labeled_statement : CASE constant_expression COLON statement'
    t[0] = AST("labeled_statement", [t[1], t[2], t[3], t[4]])


def p_labeled_statement_3(t):
    'labeled_statement : DEFAULT COLON statement'
    t[0] = AST("labeled_statement", [t[1], t[2], t[3]])


# expression-statement:


def p_expression_statement(t):
    'expression_statement : expression_opt SEMI'
    t[0] = AST("expression_statement", [t[1], t[2]])


# compound-statement:


def p_compound_statement_1(t):
    'compound_statement : LBRACE declaration_list statement_list RBRACE'
    t[0] = AST("compound_statement", [t[1], t[2], t[3], t[4]])


def p_compound_statement_2(t):
    'compound_statement : LBRACE statement_list RBRACE'
    t[0] = AST("compound_statement", [t[1], t[2], t[3]])


def p_compound_statement_3(t):
    'compound_statement : LBRACE declaration_list RBRACE'
    t[0] = AST("compound_statement", [t[1], t[2], t[3]])


def p_compound_statement_4(t):
    'compound_statement : LBRACE RBRACE'
    t[0] = AST("compound_statement", [t[1], t[2]])


# statement-list:


def p_statement_list_1(t):
    'statement_list : statement'
    t[0] = AST("statement_list", [t[1]])


def p_statement_list_2(t):
    'statement_list : statement_list statement'
    t[0] = AST("statement_list", [t[1], t[2]])


# selection-statement


def p_selection_statement_1(t):
    'selection_statement : IF LPAREN expression RPAREN statement'
    t[0] = AST("selection_statement", [t[1], t[2], t[3], t[4], t[5]])


def p_selection_statement_2(t):
    'selection_statement : IF LPAREN expression RPAREN statement ELSE statement '
    t[0] = AST("selection_statement", [t[1], t[2], t[3], t[4], t[5], t[6], t[7]])


def p_selection_statement_3(t):
    'selection_statement : SWITCH LPAREN expression RPAREN statement '
    t[0] = AST("selection_statement", [t[1], t[2], t[3], t[4], t[5]])


# iteration_statement:


def p_iteration_statement_1(t):
    'iteration_statement : WHILE LPAREN expression RPAREN statement'
    t[0] = AST("iteration_statement", [t[1], t[2], t[3], t[4], t[5]])


def p_iteration_statement_2(t):
    'iteration_statement : FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN statement '
    t[0] = AST("iteration_statement", [t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9]])


def p_iteration_statement_3(t):
    'iteration_statement : DO statement WHILE LPAREN expression RPAREN SEMI'
    t[0] = AST("iteration_statement", [t[1], t[2], t[3], t[4], t[5], t[6], t[7]])


# jump_statement:


def p_jump_statement_1(t):
    'jump_statement : GOTO ID SEMI'
    t[0] = AST("jump_statement", [t[1], t[2], t[3]])


def p_jump_statement_2(t):
    'jump_statement : CONTINUE SEMI'
    t[0] = AST("jump_statement", [t[1], t[2]])


def p_jump_statement_3(t):
    'jump_statement : BREAK SEMI'
    t[0] = AST("jump_statement", [t[1], t[2]])


def p_jump_statement_4(t):
    'jump_statement : RETURN expression_opt SEMI'
    t[0] = AST("jump_statement", [t[1], t[2], t[3]])


def p_expression_opt_1(t):
    'expression_opt : empty'
    t[0] = AST("expression_opt", [t[1]])


def p_expression_opt_2(t):
    'expression_opt : expression'
    t[0] = AST("expression_opt", [t[1]])


# expression:


def p_expression_1(t):
    'expression : assignment_expression'
    t[0] = AST("expression", [t[1]])


def p_expression_2(t):
    'expression : expression COMMA assignment_expression'
    t[0] = AST("expression", [t[1], t[2], t[3]])


# assigment_expression:


def p_assignment_expression_1(t):
    'assignment_expression : conditional_expression'
    t[0] = AST("assignment_expression", [t[1]])


def p_assignment_expression_2(t):
    'assignment_expression : unary_expression assignment_operator assignment_expression'
    t[0] = AST("assignment_expression", [t[1], t[2], t[3]])


# assignment_operator:


def p_assignment_operator(t):
    '''
    assignment_operator : EQUALS
                        | TIMESEQUAL
                        | DIVEQUAL
                        | MODEQUAL
                        | PLUSEQUAL
                        | MINUSEQUAL
                        | LSHIFTEQUAL
                        | RSHIFTEQUAL
                        | ANDEQUAL
                        | OREQUAL
                        | XOREQUAL
                        '''
    t[0] = AST("assignment_operator", [t[1]])


# conditional-expression


def p_conditional_expression_1(t):
    'conditional_expression : logical_or_expression'
    t[0] = AST("conditional_expression", [t[1]])


def p_conditional_expression_2(t):
    'conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression '
    t[0] = AST("conditional_expression", [t[1], t[2], t[3], t[4], t[5]])


# constant-expression


def p_constant_expression(t):
    'constant_expression : conditional_expression'
    t[0] = AST("constant_expression", [t[1]])


# logical-or-expression


def p_logical_or_expression_1(t):
    'logical_or_expression : logical_and_expression'
    t[0] = AST("logical_or_expression", [t[1]])


def p_logical_or_expression_2(t):
    'logical_or_expression : logical_or_expression LOR logical_and_expression'
    t[0] = AST("logical_or_expression", [t[1], t[2], t[3]])


# logical-and-expression


def p_logical_and_expression_1(t):
    'logical_and_expression : inclusive_or_expression'
    t[0] = AST("logical_and_expression", [t[1]])


def p_logical_and_expression_2(t):
    'logical_and_expression : logical_and_expression LAND inclusive_or_expression'
    t[0] = AST("logical_and_expression", [t[1], t[2], t[3]])


# inclusive-or-expression:


def p_inclusive_or_expression_1(t):
    'inclusive_or_expression : exclusive_or_expression'
    t[0] = AST("inclusive_or_expression", [t[1]])


def p_inclusive_or_expression_2(t):
    'inclusive_or_expression : inclusive_or_expression OR exclusive_or_expression'
    t[0] = AST("inclusive_or_expression", [t[1], t[2], t[3]])


# exclusive-or-expression:


def p_exclusive_or_expression_1(t):
    'exclusive_or_expression :  and_expression'
    t[0] = AST("exclusive_or_expression", [t[1]])


def p_exclusive_or_expression_2(t):
    'exclusive_or_expression :  exclusive_or_expression XOR and_expression'
    t[0] = AST("exclusive_or_expression", [t[1], t[2], t[3]])


# AND-expression


def p_and_expression_1(t):
    'and_expression : equality_expression'
    t[0] = AST("and_expression", [t[1]])


def p_and_expression_2(t):
    'and_expression : and_expression AND equality_expression'
    t[0] = AST("and_expression", [t[1], t[2], t[3]])


# equality-expression:
def p_equality_expression_1(t):
    'equality_expression : relational_expression'
    t[0] = AST("equality_expression", [t[1]])


def p_equality_expression_2(t):
    'equality_expression : equality_expression EQ relational_expression'
    t[0] = AST("equality_expression", [t[1], t[2], t[3]])


def p_equality_expression_3(t):
    'equality_expression : equality_expression NE relational_expression'
    t[0] = AST("equality_expression", [t[1], t[2], t[3]])


# relational-expression:
def p_relational_expression_1(t):
    'relational_expression : shift_expression'
    t[0] = AST("relational_expression", [t[1]])


def p_relational_expression_2(t):
    'relational_expression : relational_expression LT shift_expression'
    t[0] = AST("relational_expression", [t[1], t[2], t[3]])


def p_relational_expression_3(t):
    'relational_expression : relational_expression GT shift_expression'
    t[0] = AST("relational_expression", [t[1], t[2], t[3]])


def p_relational_expression_4(t):
    'relational_expression : relational_expression LE shift_expression'
    t[0] = AST("relational_expression", [t[1], t[2], t[3]])


def p_relational_expression_5(t):
    'relational_expression : relational_expression GE shift_expression'
    t[0] = AST("relational_expression", [t[1], t[2], t[3]])


# shift-expression


def p_shift_expression_1(t):
    'shift_expression : additive_expression'
    t[0] = AST("shift_expression", [t[1]])


def p_shift_expression_2(t):
    'shift_expression : shift_expression LSHIFT additive_expression'
    t[0] = AST("shift_expression", [t[1], t[2], t[3]])


def p_shift_expression_3(t):
    'shift_expression : shift_expression RSHIFT additive_expression'
    t[0] = AST("shift_expression", [t[1], t[2], t[3]])


# additive-expression


def p_additive_expression_1(t):
    'additive_expression : multiplicative_expression'
    t[0] = AST("additive_expression", [t[1]])


def p_additive_expression_2(t):
    'additive_expression : additive_expression PLUS multiplicative_expression'
    t[0] = AST("additive_expression", [t[1], t[2], t[3]])


def p_additive_expression_3(t):
    'additive_expression : additive_expression MINUS multiplicative_expression'
    t[0] = AST("additive_expression", [t[1], t[2], t[3]])


# multiplicative-expression


def p_multiplicative_expression_1(t):
    'multiplicative_expression : cast_expression'
    t[0] = AST("multiplicative_expression", [t[1]])


def p_multiplicative_expression_2(t):
    'multiplicative_expression : multiplicative_expression TIMES cast_expression'
    t[0] = AST("multiplicative_expression", [t[1], t[2], t[3]])


def p_multiplicative_expression_3(t):
    'multiplicative_expression : multiplicative_expression DIVIDE cast_expression'
    t[0] = AST("multiplicative_expression", [t[1], t[2], t[3]])


def p_multiplicative_expression_4(t):
    'multiplicative_expression : multiplicative_expression MOD cast_expression'
    t[0] = AST("multiplicative_expression", [t[1], t[2], t[3]])


# cast-expression:


def p_cast_expression_1(t):
    'cast_expression : unary_expression'
    t[0] = AST("cast_expression", [t[1]])


def p_cast_expression_2(t):
    'cast_expression : LPAREN type_name RPAREN cast_expression'
    t[0] = AST("cast_expression", [t[1], t[2], t[3], t[4]])


# unary-expression:


def p_unary_expression_1(t):
    'unary_expression : postfix_expression'
    t[0] = AST("unary_expression", [t[1]])


def p_unary_expression_2(t):
    'unary_expression : PLUSPLUS unary_expression'
    t[0] = AST("unary_expression", [t[1], t[2]])


def p_unary_expression_3(t):
    'unary_expression : MINUSMINUS unary_expression'
    t[0] = AST("unary_expression", [t[1], t[2]])


def p_unary_expression_4(t):
    'unary_expression : unary_operator cast_expression'
    t[0] = AST("unary_expression", [t[1], t[2]])


def p_unary_expression_5(t):
    'unary_expression : SIZEOF unary_expression'
    t[0] = AST("unary_expression", [t[1], t[2]])


def p_unary_expression_6(t):
    'unary_expression : SIZEOF LPAREN type_name RPAREN'
    t[0] = AST("unary_expression", [t[1], t[2], t[3], t[4]])


# unary-operator


def p_unary_operator(t):
    '''unary_operator : AND
                    | TIMES
                    | PLUS
                    | MINUS
                    | NOT
                    | LNOT '''
    t[0] = AST("unary_operator", [t[1]])


# postfix-expression:


def p_postfix_expression_1(t):
    'postfix_expression : primary_expression'
    t[0] = AST("postfix_expression", [t[1]])


def p_postfix_expression_2(t):
    'postfix_expression : postfix_expression LBRACKET expression RBRACKET'
    t[0] = AST("postfix_expression", [t[1], t[2], t[3], t[4]])


def p_postfix_expression_3(t):
    'postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN'
    t[0] = AST("postfix_expression", [t[1], t[2], t[3], t[4]])


def p_postfix_expression_4(t):
    'postfix_expression : postfix_expression LPAREN RPAREN'
    t[0] = AST("postfix_expression", [t[1], t[2], t[3]])


def p_postfix_expression_5(t):
    'postfix_expression : postfix_expression PERIOD ID'
    t[0] = AST("postfix_expression", [t[1], t[2], t[3]])


def p_postfix_expression_6(t):
    'postfix_expression : postfix_expression ARROW ID'
    t[0] = AST("postfix_expression", [t[1], t[2], t[3]])


def p_postfix_expression_7(t):
    'postfix_expression : postfix_expression PLUSPLUS'
    t[0] = AST("postfix_expression", [t[1], t[2]])


def p_postfix_expression_8(t):
    'postfix_expression : postfix_expression MINUSMINUS'
    t[0] = AST("postfix_expression", [t[1], t[2]])


# primary-expression:


def p_primary_expression(t):
    '''primary_expression :  ID
                        |  constant
                        |  SCONST
                        |  LPAREN expression RPAREN'''
    if len(t) == 2:
        t[0] = AST("primary_expression", [t[1]])
    else:
        t[0] = AST("primary_expression", [t[1], t[2], t[3]])



# argument-expression-list:


def p_argument_expression_list(t):
    '''argument_expression_list :  assignment_expression
                              |  argument_expression_list COMMA assignment_expression'''
    if len(t) == 2:
        t[0] = AST("argument_expression", [t[1]])
    else:
        t[0] = AST("argument_expression", [t[1], t[2], t[3]])


# constant:


def p_constant(t):
    '''constant : ICONST
               | FCONST
               | CCONST'''
    t[0] = AST("constant", [t[1]])


def p_empty(t):
    'empty : '
    t[0] = AST("empty")


def p_error(t):
    print("Whoa. We're  hosed")


import profile

# Build the grammar

data = '''
 #include <stdio.h>

int main (void)
{
  puts ("Hello, World!");
  return 0;
}
 '''

parser = yacc.yacc()
yacc.yacc(method='LALR', write_tables=True, debug=True)
parser.parse(input=data)

print()