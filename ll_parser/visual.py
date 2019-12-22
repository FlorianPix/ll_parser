import subprocess

intlit = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{{}}}}}\n'
floatlit = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{{}}}}}\n'
identifier = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{ID}}}}\n'
dollar = 'child[sibling distance=3em]{{node[fill=green!30,rounded corners,font=\\ttfamily]{{$}}}}\n'
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


def visual(ast):
    latex_file = open('..\\ll_parser\\visual.tex', 'w', encoding='utf8')
    tex = ''
    tex += header
    tex += S
    tex += rec(ast)
    tex += footer
    latex_file.write(tex)
    p = subprocess.Popen(["pdflatex", "-interaction", "nonstopmode", "visual.tex"])


def rec(ast):
    switcher = {
        'S': S_vis(ast),
        'E': E_vis(ast),
        'T': T_vis(ast),
        'F': F_vis(ast),
        'Ep': Ep_vis(ast),
        'Tp': Tp_vis(ast),
        'INTLIT': intlit_vis(ast),
        'FLOATLIT': floatlit_vis(ast),
        'IDENTIFIER': identifier_vis(ast),
        'DOLLAR': dollar_vis(ast),
        'EPSILLON': epsilon_vis(ast)
    }
    return switcher.get(ast.kind)


def S_vis(ast):
    result = S
    for child in ast.children:
        result += rec(child) + rec(child)
    result += '}\n'

def E_vis(ast):
    result = E
    for child in ast.children:
        result += rec(child) + rec(child)
    result += '}\n'
