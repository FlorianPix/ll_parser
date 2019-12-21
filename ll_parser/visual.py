import subprocess
import ll_parser.ast as AbstractST

intlit = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{{}}}}}\n'  # .format(value)
floatlit = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{{}}}}}\n'  # .format(value)
identifier = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{ID}}}}\n'

exp = '\\node{Exp}\n'
add = 'child[sibling distance=6em]{\n'  # .format(child)
mul = 'child[sibling distance=6em]{\n'  # .format(child)

header = '\\documentclass[preview]{standalone} \n\n' \
         '\\usepackage{tikz} \n\n' \
         '\\begin{document} \n' \
         '\\begin{tikzpicture}' \
         '[level distance=6em, every node/.style={fill=red!30,rounded corners,font=\\ttfamily}]\n\n'
footer = ';\n' \
         '\\end{tikzpicture}\n' \
         '\\end{document}\n'


def visual(ast):
    latex_file = open('..\\ll_parser\\visual.tex', 'w', encoding='utf8')
    tex = ''
    tex += header
    tex += exp
    tex += rec(ast)
    tex += footer
    latex_file.write(tex)
    p = subprocess.Popen(["pdflatex", "-interaction", "nonstopmode", "visual.tex"])


def rec(ast):
    t = type(ast)
    if t is AbstractST.BinOp:
        return handle_bin_op(ast)
    elif t is AbstractST.Identifier:
        return identifier.format(ast.name)
    elif t is AbstractST.IntLit:
        return intlit.format(ast.value)
    elif t is AbstractST.FloatLit:
        return floatlit.format(ast.value)
    return ''


def handle_bin_op(ast):
    if ast.kind is 'ADD':
        next = add
        next += 'node{ADD}'
        next += rec(ast.left) + rec(ast.right)
        next += '}\n'
    else:
        next = mul
        next += 'node{MUL}'
        next += rec(ast.left) + rec(ast.right)
        next += '}\n'
    return next
