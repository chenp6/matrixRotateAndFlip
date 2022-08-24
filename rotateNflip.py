# coding:UTF-8
#順時針轉90度
def RF90 (rowF,colF,origListF):    #定義RF90(rowF,colF,origListF)，參數rowF為列數，參數colF為行數，參數origListF為原始矩陣
    newList = []    #先建一個新的空list來儲存經過旋轉後的資料
    rowCnt = 0      #origList列碼歸零
    colCnt = 0      #origList行碼歸零
    while (colCnt < colF):   #重複colF次
        newList.append([])      #增加一個空串列到newList
        while(rowCnt < rowF):    #重複rowF次
            newList[colCnt].append(origListF[rowF-1-rowCnt][colCnt])  #在newList[colCnt]的最後加入origList[rowF-1-列碼][行碼]
            rowCnt+=1   #列碼加一
        rowCnt =0       #列碼歸零
        colCnt+=1       #行碼加一
    rowF = len(newList)      #將rowF指定為newList的長度
    colF = len(newList[0])   #將colF指定為newList[0]的長度
    return rowF,colF,newList  #將rowF,colF,newList回傳
#順時針轉270度(逆時針轉90度)
def RB90 (rowF,colF,origListF):    #定義RB90(rowF,colF,origListF)，參數rowF為列數,參數colF為行數，參數origListF為原始矩陣
    newList = []    #先建一個新的空list來儲存經過旋轉後的資料
    rowCnt = 0      #origList列碼歸零
    colCnt = 0      #origList行碼歸零
    while (colCnt < colF ):  #重複colF次
        newList.append([])  #增加一個空串列到newList
        while(rowCnt < rowF):    #重複rowF次
            newList[colCnt].append(origListF[rowCnt][colF-1-colCnt])  #在newList[colCnt]的最後加入origListF[列碼][col-1-行碼]
            rowCnt+=1   #列碼加一
        rowCnt = 0  #列碼歸零
        colCnt+=1   #行碼加一
    rowF = len(newList)      #將rowF指定為newList的長度
    colF = len(newList[0])   #將colF指定為newList[0]的長度
    return rowF,colF,newList   #將rowF,colF,newList回傳
#上下翻轉
def FUD (origListF): #定義FUD (origListF)，參數origListF為原始矩陣
    origListF.reverse()  #將origListF裡面的元素顛倒
    newList = origListF #將newList指定為origListF
    return newList #將newList回傳
#左右翻轉
def FLR (rowF,origListF): #定義FLR (rowF,origListF)，參數rowF為列數，參數origListF為原始矩陣
    rowCnt =0   #origList 列碼
    while (rowCnt < rowF):   #重複rowF次
        origListF[rowCnt].reverse()  #將origListF[列碼]裡面的元素顛倒
        rowCnt+=1   #列碼加一
    newList = origListF #將newList指定為origListF
    return newList #將newList回傳
