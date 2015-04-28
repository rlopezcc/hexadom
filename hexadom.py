import sys
import random


def column(n, f, tag, color):
    if n+1:
        n -= 1
        f.write(('<{tag} class="s" style="background:'
                 '{color};">').format(tag=tag, color=color))
        column(n, f, tag, color)
        f.write('</{tag}>'.format(tag=tag))
    return


def row(row, f, rnd):
    if rnd:
        tag = random.choice(['i', 'span'])
        color = {'i': '#333', 'span': 'green'}.get(tag)
    else:
        tag = 'i'
        color = '#FFF'
    f.write('<div>')
    for char in row:
        if char == ' ' or ord(char) == 10:
            f.write('<{tag} class="i">'.format(tag=tag))
        else:
            f.write(('<{tag} class="s" style="background:{color};">'
                     ).format(tag=tag, color=color))
            column(int(char, 16), f, tag, color)
        f.write('</{tag}>'.format(tag=tag))
    f.write('</div>')

style = ('.i{height:0; width:15px;overflow:visible; display:inline-block}'
         '.s{height:15px;width:15px; display:inline-block}'
         'div{margin-top:-4px}')


def handle(inp, out, rnd):
    with open(inp) as f:
        lines = f.readlines()
    with open(out, 'w+') as f:
        f.write(('<!DOCTYPE html><html>'
                 '<head><style>{style}</style></head>'
                 '<body>').format(style=style))
        for i in lines:
            row(list(i), f, rnd)
        f.write('</body></html>')

if __name__ == '__main__':
    try:
        rnd = {str(True): True, str(False): False}.get(sys.argv[3])
    except IndexError:
        rnd = True
    handle(sys.argv[1], sys.argv[2], rnd)
