# -*- conding:utf-8 -*-
def paixu(list):
    Cycle = 0 #总循环次数
    list_a = 0
    list_b = 1
    e = 0
    list_len = len(list) #计算出列表的长度
    if list_len < 2:   #如果列表长度小于2则返回原列表
        return list
    while Cycle < (list_len-1): #循环列表长度的次数
        Cycle += 1
        if Cycle > 1:
                list_a += 1  #用于对比的a值，通过while不断增加
                list_b += 1  #用与对比的b值。
        for i in range(list_b, list_len):  #通过for小循环不断的每次增加b值
            if list[list_a] > list[i]:  #让list[]的第a数字，和每个第b个数字对比
                e = list[list_a]        #如果第b个比较小就和第a个值对换
                list[list_a] = list[i]
                list[i] = e

    return list

