#411077013  軟體一  陳昶亨
#程式名稱:九宮格小遊戲
#使用說明:任何輸入完記得enter，先跟著提示輸入player1和player2的代號(o，x或任意符號)，
#接著會出現表格且宣布遊戲開始，表格是對照鍵盤數字鍵的位置，
#左下角1號，右上角9號，以此類推，玩家輪流輸入自己代號到格子裡，程式會顯示
#目前格子填入的狀況，並判斷輸贏，若贏家出現即宣布獲勝者並結束程式

a=input("player 1 :")#設定player1的代號
b=input("player 2 :")#設定player2的代號

line1="|   |   |   |"#預留每行的空格，之後填入代號
line2="|   |   |   |"
line3="|   |   |   |"

print("-------------")#畫出表格
print(line1)
print("-------------")#表格位置對應鍵盤上的數字鍵
print(line2)
print("-------------")#1號左下，3號右下，7號左上，9號右上，以此類推
print(line3)
print("-------------")

print("start")#遊戲開始

i=1#設定迴圈初始值

line1=list(line1)#把字串改為list才能替換特定位置字元
line2=list(line2)
line3=list(line3)

while (i<=9):#進入主程式(迴圈)
    if (i%2==0):#判斷輪到哪個玩家輸入
        c=b#偶數代表輪到player2
    else:
        c=a#基數代表輪到player1
    
    step=int(input())#在表格上標示號碼，1號左下，3號右下，7號左上，9號右上，以此類推
    
    #以下判斷輸入哪一格
    if (step==1):#若輸入1，為第三行第一格，進行後面程式碼
        line3[2]=c#把第三行第一格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    if (step==2):#若輸入2，為第三行第二格，進行後面程式碼
        line3[6]=c#把第三行第二格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    if (step==3):#若輸入3，為第三行第三格，進行後面程式碼
        line3[10]=c#把第三行第三格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    if (step==4):#若輸入4，為第二行第一格，進行後面程式碼
        line2[2]=c#把第二行第一格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    if (step==5):#若輸入5，為正中間那格，進行後面程式碼
        line2[6]=c#把第二行第二格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    if (step==6):#若輸入6，為第二行第三格，進行後面程式碼
        line2[10]=c#把第二行第三格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    if (step==7):#若輸入7，為第一行第一格，進行後面程式碼
        line1[2]=c#把第一行第一格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    if (step==8):#若輸入8，為第一行第二格，進行後面程式碼
        line1[6]=c#把第一行第二格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    if (step==9):#若輸入9，為第三行第三格，進行後面程式碼
        line1[10]=c#把第一行第三格的空白字元換成player代碼
        print("-------------")#輸出表格，顯示這一步的結果
        print(*line1,sep="")
        print("-------------")
        print(*line2,sep="")
        print("-------------")
        print(*line3,sep="")
        print("-------------")
    
    #以下判斷輸贏條件
    if (line1[2]==line1[6]==line1[10]==a):#上橫排的符號一致且等於player1的符號
        print("player 1 win")#宣告player1獲勝
    elif (line1[2]==line1[6]==line1[10]==b):#上橫排的符號一致且等於player2的符號
        print("player 2 win")#宣布player2獲勝
    elif (line2[2]==line2[6]==line2[10]==a):#中間橫排的符號一致且等於player1的符號
        print("player 1 win")#宣布player1獲勝
    elif (line2[2]==line2[6]==line2[10]==b):#中間橫排的符號一致且等於player2的符號
        print("player 2 win")#宣布player2獲勝
    elif (line3[2]==line3[6]==line3[10]==a):#下橫排的符號一致且等於player1的符號
        print("player 1 win")#宣布player1獲勝
    elif (line3[2]==line3[6]==line3[10]==b):#下橫排的符號一致且等於player2的符號
        print("player 2 win")#宣布player2獲勝
    elif (line1[2]==line2[2]==line3[2]==a):#左直排的符號一致且等於player1的符號
        print("player 1 win")#宣布player1獲勝
    elif (line1[2]==line2[2]==line3[2]==b):#左直排的符號一致且等於player2的符號
        print("player 2 win")#宣布player2獲勝
    elif (line1[6]==line2[6]==line3[6]==a):#中間直排的符號一致且等於player1的符號
        print("player 1 win")#宣布player1獲勝
    elif (line1[6]==line2[6]==line3[6]==b):#中間直排的符號一致且等於player2的符號
        print("player 2 win")#宣布player2獲勝
    elif (line1[10]==line2[10]==line3[10]==a):#右直排的符號一致且等於player1的符號
        print("player 1 win")#宣布player1獲勝
    elif (line1[10]==line2[10]==line3[10]==b):#右直排的符號一致且等於player2的符號
        print("player 2 win")#宣布player2獲勝
    elif (line1[2]==line2[6]==line3[10]==a):#左上到右下斜線的符號一致且等於player1的符號
        print("player 1 win")#宣布player1獲勝
    elif (line1[2]==line2[6]==line3[10]==b):#左上到右下斜線的符號一致且等於player2的符號
        print("player 2 win")#宣player2獲勝
    elif (line1[10]==line2[6]==line3[2]==a):#右上到左下斜線符號一致且等於player1的符號
        print("player 1 win")#宣布player1獲勝
    elif (line1[10]==line2[6]==line3[2]==b):#右上到左下斜線符號一致且等於player2的符號
        print("player 2 win")#宣布player2獲勝
    i+=1#迴圈計數器+1(步數+1)
print("平手")#宣布平手