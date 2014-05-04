#encoding:utf-8
#to do:
#support Chinese File name yet...  [ok]
#support paging yet[ok]
#support sort the diaries by time [ok]
__author__ = 'Jayin Ton'

import os
import re
import json
import copy
import time

"""
  项目文件目录结构换了，这是最新的生成脚本
"""
#config
limit = 10
ignore = [
    'README.md',
    '.+\.json',
    '.+\.py',
    '.+\.db'
]


def get_current_timestamp():
    return long(time.time() * 1000)


def create_dir_info_json(cwd, dirs):
    json_string = json.dumps({
        'result': dirs,
        'last_motify': get_current_timestamp()
    })
    with open(os.path.join(cwd, 'info.json'), mode='w') as f:
        f.write(json_string)
    print "created_dir_info_json ---> ", os.path.join(cwd, 'info.json')


def generation(page, l, cwd):
    file_name = cwd + os.path.sep + str(page) + ".json"
    with open(file_name, mode="w") as f:
        if len(l) > 0:
            res = []
            for f_name in l:
                res.append(f_name.decode('gbk'))
            f.write(json.dumps({
                'result': res
            }))
        else:
            f.write(json.dumps({'result': []}))


def cleanup(cwd):
    """
    clean up the `json` files
    """
    l = list(os.listdir(cwd))
    pattern = re.compile(r'.+\.json', re.IGNORECASE)
    for x in l:
        #
        if re.findall(pattern, x):
            os.remove(cwd + os.path.sep + x)
            print 'remove file--', cwd + os.path.sep + x
    print 'clean up .json files finished'


def main_work(cwd):
    """
     cwd : the current working directory.
    """
    cleanup(cwd)
    l = list(os.listdir(cwd))
    raw = copy.deepcopy(l)
    for ig in ignore:
        pattern = re.compile(ig, re.IGNORECASE)
        for t in l:
            if re.findall(pattern, t):
                raw.remove(t)
    raw.sort(reverse=False)
    size = len(raw)
    # print size
    page = 1
    while page * limit <= size:
        # print page, '--> ', raw[(page - 1) * limit:page * limit]
        generation(page, raw[(page - 1) * limit:page * limit], cwd)
        page += 1
    # print page, '--> ', raw[(page - 1) * limit:]
    generation(page, raw[(page - 1) * limit:], cwd)

    with open(cwd + os.path.sep + 'info.json', mode='w') as f:
        f.write(json.dumps({'pages': page,
                            'last_motify': get_current_timestamp()}))
    print 'total=', size, 'pages=', page
    print "Build finished."
    print ""


def main(cwd):
    """
     cwd = [program lang]/kind*/....
    """
    cwd_list = list(os.listdir(cwd))
    print 'deal with dir: ', cwd
    dirs  = []
    for file_name in cwd_list:
        if os.path.isdir(os.path.join(cwd, file_name)):
            print os.path.join(cwd, file_name)
            main_work(os.path.join(cwd, file_name))
            dirs.append(file_name.decode('gbk'))
    print("in -->", cwd, " create-->", dirs)
    create_dir_info_json(cwd, dirs)
    print 'finish: ', cwd


def t(d):
    print d


if __name__ == "__main__":
    #deal with the directory below [program_lang] (java/)
    dirs = []
    for f in filter(lambda _dir: os.path.isdir(_dir), os.listdir(os.getcwd())):
        main(os.path.join(os.getcwd(), f))
        dirs.append(f)
    print("in -->", os.getcwd(), " create-->", dirs)
    create_dir_info_json(os.getcwd(),dirs)