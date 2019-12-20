plus = 'child[sibling distance=2em, level distance=2em]{{node{{+}}}}'
star = 'child[sibling distance=2em, level distance=2em]{{node{{*}}}}'
epsilon = 'child[sibling distance=2em, level distance=2em]{{node{{$\\varepsilon$}}}}'
intlit = 'child[sibling distance=5em]{{node{{INTLIT}}}}'
floatlit = 'child[sibling distance=5em]{{node{{FLOATLIT}}}}'
identifier = 'child[sibling distance=5em]{{node{{ID}}}}'
s = '\\node{S}'
e = 'child[sibling distance=10em]{{node{{E}}{}}}'  # .format(child)
t = 'child[sibling distance=10em]{{node{{T}}{}}}'  # .format(child)
f = 'child[sibling distance=10em]{{node{{F}}{}}}'  # .format(child)
ep = 'child[sibling distance=5em]{{node{{Ep}}{}}}'  # .format(child)
tp = 'child[sibling distance=5em]{{node{{Tp}}{}}}'  # .format(child)

header = '\\documentclass[preview]{standalone} \n\n' \
         '\\usepackage{tikz} \n\n' \
         '\\begin{document} \n' \
         '\\begin{tikzpicture}' \
         '[level distance=6em, every node/.style={fill=red!30,rounded corners,font=\\ttfamily}]\n\n'
footer = ';\n' \
         '\\end{tikzpicture}\n' \
         '\\end{document}\n'

result = ''


def visual(ast):
    print(1)


visual(1)
