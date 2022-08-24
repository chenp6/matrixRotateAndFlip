# coding:UTF-8
import sys  #匯入sys模組
def readNwrite(inputfileNameF):   #定義readNwrite()
    inputfileNameF =  inputfileNameF.replace('\r','').replace('\n','')    #移除inputfileNameF的'\n'跟 '\r'
    outputfileName = inputfileNameF.replace('in','out')  #宣告outputfileName為inputfileNameF，並將其的'in'取代為'out'
    return open(inputfileNameF,'r') ,open(outputfileName,'w')    #以唯讀方式打開文件(inputfileNameF)，建立一個文件(outputfileName)並且功能只限定於寫入。
def readLine(readFileF):    #定義 readLine(readFileF)，參數readFileF為開啟欲讀入的檔案
    return readFileF.readline() #讀取該檔中的一行
def writeLine(writeFileF,s):    #定義 writeLine(writeFileF)，參數writeFileF為開啟欲寫入的檔案，參數s為欲寫入的字串
    return writeFileF.write(s)  #將s寫入此檔案
