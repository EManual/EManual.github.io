# encoding:utf-8
import re
import os


def is_md_file(filename):
    pattern = re.compile(r'.[Mm]{1}[Dd]{1}')
    return len(re.findall(pattern, filename)) > 0


def deal_with(filename):
    with open(filename) as f:
        content = f.read()
    # print content
    p_img = re.compile(r'(\[code=img\].+\[/code\])+?', re.IGNORECASE)
    p_color = re.compile(r'(\[color=.+\])', re.IGNORECASE)
    p_code_begin = re.compile(r'\[code=java\]')
    p_code_end = re.compile(r'\[/code\]')

    # 移除他自己的定义的高亮部分文字
    content = content.replace('#', '')
    content = content.replace('[Comments]', '')
    content = content.replace('[Fields]', '')
    content = content.replace('[Keywords]', '')

    content = re.sub(p_img, '![img](P)  ', content)
    content = re.sub(p_color, '#### ', content)
    content = re.sub(p_code_begin, '```  ', content)
    content = re.sub(p_code_end, '```', content)
    print content
    with open(filename, mode='w') as f:
        f.write(content)


def visit(args, dirname, names):
    if os.path.isdir(dirname):
        for n in names:
            if is_md_file(n):
                deal_with(os.path.join(dirname, n))


def main():
    # cwd =os.getcwd()
    cwd = os.path.join(os.getcwd(), 'test')
    os.path.walk(cwd, visit, 'walk')


if __name__ == '__main__':
    main()
