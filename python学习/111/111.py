import numpy as np
import os
import re

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

            file_name = inputFileFath + '/' + 'test' + str(file_count) + '.fasta'
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


def createPssm(inputFilePath, dbFilePath, outputFilePath):
    dirs = os.listdir(inputFilePath)
    for i in range(len(dirs)):
        if os.path.exists(outputFilePath + 'test' + str(i) + '.pssm' ):
            continue
        else:
            cmd = 'psiblast -in_msa ' + inputFilePath + 'test' + str(i) + '.fasta' + ' -db ' + dbFilePath + r' -comp_based_stats 1 -inclusion_ethresh  0.001 -num_iterations 3 -out_ascii_pssm ' + outputFilePath + 'test' + str(i) + '.pssm'
            status = os.system(cmd)
            assert status == 0

def savePssm():
    pssm = np.zeros((20, 61))
    count = 0
    numlist = []
    with open('../111/2.pssm', 'r') as f:
        for i in range(3):  # 前2行无用
            f.readline()
        lines = f.readlines()[0: 61]  # 第三行判断
        for line in lines:
            line = line[11:91]
            for num in line:
                if num == '-':
                    symbol = -1
                    continue
                else:
                    symbol = 1
                num = int(num) * symbol
                numlist.append(num)
        print(numlist)

def getPssmMat(filepath):
    '''

    :param filepath: 文件名
    :return: pssm矩阵
    '''
    f = open(filepath, 'r')
    for i in range(3):  # 前2行无用
        f.readline()
    lines = f.readlines()
    #矩阵大小 除去无用的九行
    pssm = np.zeros((len(lines) - 9, 20))
    #初始化列表
    l_list = []
    for line in lines[:len(lines) - 6]:
        l = line.split()[2:22]
        l = [int(x) for x in l]
        l_list.append(l)
    f.close()
    #列表转矩阵
    pssm = np.mat(l_list)
    return pssm

if __name__ == '__main__':
    # createPssm(r'F:\NCBI\blast-2.3.0+\input\D1\\', r'F:\NCBI\blast-2.3.0+\db\uniprot-all.fasta', r'F:\NCBI\blast-2.3.0+\output\D1\\')
    getPssmMat(r'F:\NCBI\blast-2.3.0+\output\D2\train\train0.pssm')







