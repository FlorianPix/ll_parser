import subprocess

intlit = 'child[level distance=2em, sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{{}}}}}\n'
floatlit = 'child[level distance=2em, sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{{}}}}}\n'
identifier = 'child[level distance=2em, sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{ID}}}}\n'
dollar = 'child[level distance=2em, sibling distance=3em]{node[fill=green!30,rounded corners,font=\\ttfamily]{\\$}}\n'
rparan = 'child[sibling distance=1.5em]{node[fill=green!30,rounded corners,font=\\ttfamily]{(}}\n'
lparan = 'child[sibling distance=1.5em]{node[fill=green!30,rounded corners,font=\\ttfamily]{)}}\n'
plus = 'child[level distance=2em, sibling distance=3em]{node[fill=green!30,rounded corners,font=\\ttfamily]{+}}\n'
star = 'child[level distance=2em, sibling distance=3em]{node[fill=green!30,rounded corners,font=\\ttfamily]{*}}\n'
epsilon = 'child[level distance=2em, sibling distance=2em]{node[fill=green!30,rounded corners,font=\\ttfamily]{$\\varepsilon$}}\n'

S = '\\node{S}\n'
E = 'child[sibling distance=%sem]{\n'
T = 'child[sibling distance=%sem]{\n'
F = 'child[sibling distance=%sem]{\n'
Ep = 'child{\n'
Tp = 'child{\n'
F0 = 'child[level distance=2em, sibling distance=3em]{\n'
Ep0 = 'child[level distance=2em, sibling distance=3em]{\n'
Tp0 = 'child[level distance=2em, sibling distance=3em]{\n'

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
    return result


def E_vis(ast):
    result = E % get_len(ast.children)
    result += 'node{E}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def T_vis(ast):
    result = T % get_len(ast.children)
    result += 'node{T}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def F_vis(ast):
    if (ast.children[0].kind is 'E'
            or ast.children[0].kind is ')'
            or ast.children[0].kind is '('):
        result = F % get_len(ast.children)
    else:
        result = F0
    result += 'node{F}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def Ep_vis(ast):
    if ast.children[0].kind is not 'EPSILON':
        result = Ep
    else:
        result = Ep0
    result += 'node{Ep}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def Tp_vis(ast):
    if ast.children[0].kind is not 'EPSILON':
        result = Tp
    else:
        result = Tp0
    result += 'node{Tp}'
    for child in ast.children:
        result += rec(child)
    result += '}\n'
    return result


def epsilon_vis(ast):
    return epsilon


def lparan_vis(ast):
    return lparan


def rparan_vis(ast):
    return rparan


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
    '*': star_vis,
    '(': lparan_vis,
    ')': rparan_vis
}


def get_len(children):
    ln = len(children) + 1
    for child in children:
        if hasattr(child, 'children'):
            ln += get_len(child.children)
    return ln
