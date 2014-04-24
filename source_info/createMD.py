#endcoding:utf-8
import sqlite3
import os
import json
import time

source_config = {
    'type': 'design_pattern'
}

target_config = {
    'file_path': 'pattern',
}

#   types   :对应的数据库的表
#   kind    ：文件目录名称

types = ['java_basic', 'design_pattern', 'java_advance', 'database', 'arithmetic', 'framework', 'java_ee', 'java_web']
kinds = ['basic', 'pattern', 'advance', 'database', 'arithmetic', 'framework', 'java_ee', 'java_web']
program_language = 'java-lang'


def get_lang_root_dir():
    return os.path.join(os.path.split(os.getcwd())[0], program_language)


def remove_all_file():
    """
    remove_all_file with `kind`
    """
    for kind in kinds:
        dirtory = os.path.join(os.path.split(os.getcwd())[0], program_language, kind)
        print "on dirtory -->", dirtory
        for p in os.listdir(dirtory):
            if os.path.exists(os.path.join(dirtory, p)):
                print os.path.join(dirtory, p), " exist!"
                for f in os.listdir(os.path.join(dirtory, p)):
                    try:
                        print "remove:", os.path.join(dirtory, p, f)
                        os.remove(os.path.join(dirtory, p, f))
                    except WindowsError as e:
                        print e.message
            try:
                if os.path.isdir(os.path.join(dirtory, p)):
                    print "remove:", os.path.join(dirtory, p)
                    os.removedirs(os.path.join(dirtory, p))
            except WindowsError as e:
                print e.message
    print "remove finish"


def get_num(num):
    """
    1 -> 0001
    12 -> 0012
    123 -> 0123
    1234 -> 01234
    """
    return '0' * (4 - len(str(num))) + str(num)


def gerate_filename(index, title, kind, subkind):
    """
      生成目标文件md的名称(路径) 如：~[program_language]/[kind]/[subkind]/[00xx]-[title].md
    """
    path = os.path.join(os.path.split(os.getcwd())[0], program_language, kind, subkind,
                        get_num(index) + '-' + title + '.md')
    return path


def gerate_file(index, title, content, kind, subKind):
    """
       生成目标文件(.md)
    """
    filename = gerate_filename(index, title, kind, subKind)
    print 'prepare to gerate_file -->', filename
    with open(filename, mode='w') as f:
        f.write(str(content))
    print 'gerate_file ok -->', filename


def create_subkind(kind, subkind):
    """
        生成子目录 如：~[program_language]/[kind]/[subkind]
    """
    root = os.path.split(os.getcwd())[0]
    print root, program_language, kind, subkind
    path = os.path.join(root, program_language, kind, subkind)
    os.makedirs(path)
    print path, "|||| build"


def create_kind_info(kind, result):
    """
    last_motify:
    result:
    """
    json_string = json.dumps({'last_motify': time.time() * 100,
                              'result': result
    })
    path_name = os.path.join(get_lang_root_dir(), kind)
    print "----------------------"
    print "create info data in -->", path_name
    with open(os.path.join(path_name , 'info.json'),mode='w') as f:
        f.write(json_string)


def create_md():
    con = sqlite3.connect('source.db')
    cursor = con.cursor()
    index = 0
    for t in types:
        subkinds = []
        for row in cursor.execute('select title,content,importance from ' + t):
            # print row[0], '--importance===', row[2],
            if row[2] == 9:
                i = 0
                subkind = row[0]
                create_subkind(kinds[index], row[0])
                subkinds.append(row[0])
            else:
                print i, row[0], kinds[index], subkind
                gerate_file(i, row[0], row[1].encode('utf-8'), kinds[index], subkind)
                i += 1
        #表遍历完毕
        print subkinds
        create_kind_info(kinds[index], subkinds)
        index += 1
    con.close()
    print "create_md finish"


def create_root_file():
    root = os.path.join(os.path.split(os.getcwd())[0], program_language)
    for k in kinds:
        if not os.path.exists(os.path.join(root, k)):
            os.mkdir(os.path.join(root, k))


if __name__ == '__main__':
    create_root_file();
    remove_all_file()
    create_md()
