def spiltTxt2Txt(filename, inputFileFath):
    '''

    :param filename: 读取文件名称
    :param inputFileFath: 存贮文件路径
    :return:
    将一个文本文件按行拆分
    '''
    #选择的行数
    limit = 2
    file_count = 0
    content_list = []

    with open(filename) as f:
        for line in f:
            content_list.append(line)
            if len(content_list) < limit:
                continue

            file_name = inputFileFath + '\\' + 'test' + str(file_count) + '.fasta'
            with open(file_name, 'w') as file:
                for content in content_list:
                    file.write(content)
                content_list = []
                file_count += 1
    if content_list:
        file_name = 'test' + str(file_count) + '.fasta'
        with open(inputFileFath + filename, 'w') as file:
            for content in content_list:
                file.write(content)

spiltTxt2Txt('TEST3585.txt',
             r'F:\NCBI\blast-2.3.0+\input\q\test')

