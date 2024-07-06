from gua import Gua

num2Char = ['-','初','二','三','四','五','上']

def get6or9(gx, nd):
    index = int(nd)-1
    if gx[index] == 0:
        return "六"
    else:
        return "九"

def printYaoResult(gx, nd):
    yy = get6or9(gx, nd) #6或者9
    if int(nd)==1 or int(nd)==6:
        print("使用[",num2Char[int(nd)],yy,'爻]','爻辞推之')    
    else:
        print("使用[",yy,num2Char[int(nd)],'爻]','爻辞推之')

def get_yao(gx, nd):
    if len(nd) == 1:
        if int(nd) == 0:
            print("本卦无动爻,使用本卦卦辞断之")
        else:
            printYaoResult(gx, nd)
    #两个动爻
    elif len(nd) == 2:
        if (gx[int(nd[0])-1]=='0' and gx[int(nd[1])-1]=='0') \
            or (gx[int(nd[0])-1]=='1' and gx[int(nd[1])-1]=='1'):
            printYaoResult(gx, nd[1])
        elif gx[int(nd[0])-1]=='0':
            printYaoResult(gx, nd[0])
        else:
            printYaoResult(gx, nd[1])
    elif len(nd) == 3:
        printYaoResult(gx, nd[1])
    elif len(nd) == 4: #最下面的非动
        temp = '123456'
        for i in nd:
            temp = temp.replace(i,'')
        printYaoResult(gx, temp[0])
    elif len(nd) == 5: #取非动
        temp = '123456'
        for i in nd:
            temp = temp.replace(i,'')
        printYaoResult(gx, temp)
    else:
        if '1' not in gx: #六阴爻
            print('坤卦，‘用六’断之')
        elif '0' not in gx: #六阳爻
            print('乾卦，‘用九’断之')
        else:
            print('按八宫卦的前一个卦辞断之')
                

def get_gua():
    gx  = input("自下而上输入卦相:")
    nd  = input("动爻在爻号,没有则输入0:")
    if len(nd) == 0:
        nd = '0'
    if (len(gx) != 6):
        print("输入卦相的长度错误，请重新输入！")
        return
    if (len(gx) >6):
        print("输入动爻的长度错误，请重新输入！")
        return
    for i in gx:
        if i not in ['0', '1']:
            print("卦相输入错误，请重新输入！")
            return 
    for i in nd:
        if int(i) > 6 or int(i) < 0:
            print("动爻输入错误，请重新输入！")
            return
    dt_gua64, ls_gua64 = Gua.get_gua64()
    if gx.strip() in dt_gua64:
        gua_name = dt_gua64[gx.strip()]
        print("输入卦象的卦名为：【"+gua_name+ "】(上"+Gua.num_to_gua(gx[3:6])
              +"下"+Gua.num_to_gua(gx[0:3])+gua_name+ ")")
        get_yao(gx, nd)
    else:
        print("输入的卦象，卦名为："+"未知卦")


if __name__ == '__main__':
    get_gua()