# coding:UTF-8
import sys,time,tkinter #匯入sys及time模組
import rotateNflip,readNwrite  #匯入rotateNflip及readNwrite模組
try :
    def Run():  #定義Run()
        inputfileName = fileNameEntry.get()  #輸入欲讀的檔案名稱
        readFile,writeFile = readNwrite.readNwrite(inputfileName)    #將inputfileName為參數，透過readNwrite模組中的readNwrite函數，開啟欲讀入文件及欲寫入文件
        
        """
        輸入檔案名稱: xxx_in.txt
        
        輸入檔案內容:
            矩陣row數 矩陣col數
            矩陣內容
            欲使用之旋轉/翻轉編號(1:順時針旋轉90度，2:逆時針旋轉90度，3:矩陣上下翻轉，4:矩陣左右翻轉)
            
        輸入檔案範例:
        (對 [[1,2,3],[4,5,6]] 進行順時針旋轉90度)
            3 2
            1 2 3
            4 5 6
            1
                
        輸出檔案名稱:xxx_out.txt 
        
        輸入檔案內容:
            旋轉/翻轉矩陣內容
            寫入運算時間差
        
        輸出檔案範例:
            4 1 
            5 2 
            6 3 
            8536.69230000000061409082ms
        """
        
        str = readNwrite.readLine(readFile)   #透過readNwrite模組中的readLine函數，從輸入檔讀取一行，作為列數與行數
        while(str!=''): #當直到str等於''(空字串)時，跳出迴圈
            rowCnt = 0  #原始矩陣 列碼
            colCnt = 0  #原始矩陣 行碼
            str = str.strip()   #去掉str頭尾的空白
            str = str.replace('\r','').replace('\n','') #移除str的'\n'跟 '\r'
            inputList = str.split() #建立串列['列數','行數']
            row = int(inputList[0]) #原始矩陣的列數
            col = int(inputList[1]) #原始矩陣的行數
            origList = []   #原始矩陣的串列(Original List)
            
            while(rowCnt < row):            #重複row次
                origList.append([])             #建立新的一列
                rowText = readNwrite.readLine(readFile)  #透過readNwrite模組中的readLine函數，從輸入檔讀取一行，作為該列內容
                rowText = rowText.strip()       #去掉rowText的頭尾空白
                rowText = rowText.replace('\r','').replace('\n','') #移除rowText的'\n'跟'\r'
                origList[rowCnt] = rowText.split()  #將rowText以空白分割成串列以字串的形式儲存到origList[列碼]
                rowCnt+=1   #列碼加一
                
            ##透過readNwrite模組中的readLine函數，從輸入檔讀取一行，作為矩陣旋轉/翻轉字串並assign到change
            #1表示順時針旋轉90度，2表示逆時針旋轉90度，3表示矩陣上下翻轉，4表示矩陣左右翻轉。   
            change = readNwrite.readLine(readFile)    
            change = change.strip() #去掉change的頭尾空白
            change = change.replace('\r','').replace('\n','')  #移除change的'\r'和'\n'
            changeList= change.split() #將change以空白分隔成串列changeList
            changeCnt = 0 #changeList的編號
            startClock =time.perf_counter() #開始計時
            while(changeCnt< len(changeList)):
                if (changeList[changeCnt] == '1'):   #遇到'1'時
                    row,col,origList=rotateNflip.RF90(row,col,origList)  #透過turn模組中的RF90(列數,行數,原始矩陣)函數，執行順時針旋轉，且回傳值到origList
                elif (changeList[changeCnt] == '2'): #遇到'2'時
                    row,col,origList=rotateNflip.RB90(row,col,origList)  #透過turn模組中的RB90(列數,行數,原始矩陣)函數，執行逆時針旋轉，且回傳值到origList
                elif(changeList[changeCnt] == '3'):  #遇到'3'時
                    origList=rotateNflip.FUD(origList)   #透過turn模組中的FUD(原始矩陣)函數，執行左右翻轉，且回傳值到origList
                elif (changeList[changeCnt] == '4'): #遇到'4'時
                    origList = rotateNflip.FLR(row,origList)   #透過turn模組中的FLR(列數,原始矩陣)函數，執行左右翻轉，且回傳值到origList
                changeCnt +=1  #編號加一
            endClock = (time.perf_counter())*1000   #結束計時
            rowCnt=0    #origList 列碼
            colCnt=0    #origList 行碼
            while(rowCnt < row):    #重複row次
                while(colCnt < col):    #重複col次
                    readNwrite.writeLine(writeFile,origList[rowCnt][colCnt]+' ') #透過readNwrite模組中的writeLine函數，#將origList[rowCnt][colCnt]寫入輸出檔
                    colCnt+=1   #行碼加一
                colCnt=0    #行碼歸零
                readNwrite.writeLine(writeFile,'\n')   #透過readNwrite模組中的writeLine函數，寫入'\n'於輸出檔，用來換行
                rowCnt+=1   #列碼加一
            readNwrite.writeLine(writeFile,'%.20fms\n\n'%(endClock))  #透過readNwrite模組中的writeline函數，寫入運算時間差於輸出檔
            blank= readNwrite.readLine(readFile)  #透過readNwrite模組中的readLine函數，從輸入檔讀取一行空白行
            str = readNwrite.readLine(readFile)  #透過readNwrite模組中的readLine函數，從輸入檔讀取一行，作為列數與行數
        readFile.close()    #關閉readFile
        writeFile.close()   #關閉writeFile

    capitalWin = tkinter.Tk()   #建立主視窗

    capitalWin.title("矩陣翻轉/旋轉")   #主視窗的標題


    capitalWin.geometry("400x200")  #主視窗的大小
    capitalWin.config(background='#c5e5ea') #主視窗的背景顏色

    Text = tkinter.Label(text="輸入檔案名稱",fg = "brown",font=("微軟正黑體",15),background='#c5e5ea') #建立內容為"輸入檔案名稱"的標籤
    Text.pack() #放置Text

    fileNameEntry = tkinter.Entry() #建立文字輸入區fileNameEntry
    fileNameEntry.pack()    #放置fileNameEntry

    btn =tkinter.Button(text="Enter",command=Run)   #建立文字內容為"Enter"的按鈕，命令執行Run()
    btn.pack()  #放置btn

    capitalWin.mainloop()  #常駐主視窗

except FileNotFoundError:   #沒有符合此檔名的檔案
    print('找不到此檔案')
except IndexError:  #List中沒有此index
    print('list index out of range，【提醒】有可能為矩陣輸入錯誤')
except ValueError:  #輸入無效的參數
    print('輸入無效的參數，【提醒】列數與行數必須為正整數')
except SyntaxError: #Python語法錯誤
    print('Python語法錯誤')
except NameError:   #有變數未被定義(宣告)
    print('有變數未被定義(宣告)')
except TypeError:   #對類型無效的操作
    print('對類型無效的操作')