import subprocess

intlit = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{{}}}}}\n'
floatlit = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{{}}}}}\n'
identifier = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{ID}}}}\n'
dollar = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{$}}}}\n'
plus = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{+}}}}\n'
star = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{*}}}}\n'
epsilon = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{$\\varepsilon$}}}}\n'

S = '\\node{S}\n'
E = 'child[sibling distance=6em]{\n'
T = 'child[sibling distance=6em]{\n'
F = 'child[sibling distance=6em]{\n'
Ep = 'child[sibling distance=6em]{\n'
Tp = 'child[sibling distance=6em]{\n'

header = '\\documentclass[preview]{standalone} \n\n' \
         '\\usepackage{tikz} \n\n' \
         '\\begin{document} \n' \
         '\\begin{tikzpicture}' \
         '[level distance=6em, every node/.style={fill=red!30,rounded corners,font=\\ttfamily}]\n\n'
footer = ';\n' \
         '\\end{tikzpicture}\n' \
         '\\end{document}\n'


def vis(ast):
    latex_file = open('..\\ll_parser\\visual.tex', 'w', encoding='utf8')
    tex = ''
    tex += header
    tex += rec(ast)
    tex += footer
    latex_file.write(tex)
    p = subprocess.Popen(["pdflatex", "-interaction", "nonstopmode", "visual.tex"])


def rec(ast):
    ret = switcher.get(ast.kind)(ast)
    return ret


def S_vis(ast):
    result = S
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def E_vis(ast):
    result = E
    result += 'node{E}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def T_vis(ast):
    result = T
    result += 'node{T}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def F_vis(ast):
    result = F
    result += 'node{F}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def Ep_vis(ast):
    result = Ep
    result += 'node{Ep}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def Tp_vis(ast):
    result = Tp
    result += 'node{Tp}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def epsilon_vis(ast):
    return epsilon


def dollar_vis(ast):
    return dollar


def plus_vis(ast):
    return plus


def star_vis(ast):
    return star


def floatlit_vis(ast):
    return floatlit.format(ast.value)


def intlit_vis(ast):
    return intlit.format(ast.value)


def identifier_vis(ast):
    return identifier


switcher = {
    'S': S_vis,
    'E': E_vis,
    'T': T_vis,
    'F': F_vis,
    'Ep': Ep_vis,
    'Tp': Tp_vis,
    'EPSILON': epsilon_vis,
    'INTLIT': intlit_vis,
    'FLOATLIT': floatlit_vis,
    'IDENTIFIER': identifier_vis,
    '$': dollar_vis,
    '+': plus_vis,
    '*': star_vis
}
