#R0='00'
#R1='01'
#R2='02'
#R3='03'
#R4='04'
#R5='05'
#R6='06'
#R7='07'
#R8='08'
#R9='09'
#R10='0A'
#R11='0B'
#R12='0C'
#R13='0D'
#R14='0E'
#R15='0F'
sim=68719476736
data_reg = []
for x in range (0,16):
    data_reg.insert(x,hex(0))
    
immediate=hex(8)
notepad = open("IR.txt", "r")       #membaca file dari notepad
dataa = notepad.readlines()         #IR = data[z]                        
notepad.close()


for z in range(len(dataa)):

    notepad = open("IR.txt", "r")       #membaca file dari notepad
    data = notepad.readlines()
    IR = data[z]                        #membaca file IR.txt
    IRR=IR[0:10]
    notepad.close()

    #parsing   
    dataIR=IR
    data_operand=dataIR[2:4]            #parsing operand
    a=data_operand                      #untuk mengetahui perintah operand
    data_regdepan=dataIR[4:6]           #Parsing R1
    b=data_regdepan                     #untuk mengetahui R1
    data_regtengah=dataIR[6:8]          #Parsing R2
    c=data_regtengah                    #untuk mengetahui R2
    data_regbelakang=dataIR[8:10]       #Parsing R3
    d=data_regbelakang                  #untuk mengetahui R3

    #menentukan fungsi ADDI
    if a=='20':                         
        a='ADDI'
    #menentukan fungsi SUBI
    if a=='22':                         
        a='SUBI'
    #menentukan fungsi ADD
    if a=='10':                         
        a='ADD'
    #menentukan fungsi SUB
    if a=='12':                         
        a='SUB'
    #menentukan fungsi SHL
    if a=='18':                         
        a='SHL'
    #menentukan fungsi SHR
    if a=='19':                         
        a='SHR'
    #menentukan fungsi AND
    if a=='14':                         
        a='AND'
    #menentukan fungsi OR    
    if a=='15':                         
        a='OR'
    #menentukan fungsi XOR
    if a=='16':                         
        a='XOR'
    #menentukan fungsi MOV   
    if a=='32':                         
        a='MOV'

    #menampilkan counter                              
    z=z+1                               
    z=hex(z+sim)
    z=z[4:12]
    #mengubah data variabel menjadi desimal agar bisa ditampilkan sebagai register
    b=int(b,16)                         
    c=int(c,16)
    d=int(d,16)
    #mengubah data variabel menjadi string
    b=str(b)                            
    c=str(c)
    d=str(d)

    #menampilkan instruksi
    if data_operand=='20' or data_operand=='22':
        d=dataIR[6:10]
        d=int(d,16)
        d=hex(d)
        d=str(d)
        data_regbelakang=dataIR[6:10]
        print('PC=',z,'IR=',IRR,a,'R'+b,'#'+'0x'+'{0:0>4x}'.format(int(d,16)))
        data_regtengah=int(data_regtengah,16)
        data_regbelakang=int(data_regbelakang,16)
    elif data_operand=='32':
        print('PC=',z,'IR=',IRR,a,'R'+b,'R'+c)
        data_regtengah=int(data_regtengah,16)
        data_regbelakang=int(data_regbelakang,16)
    else:
        data_regtengah=int(data_regtengah,16)
        data_regbelakang=int(data_regbelakang,16)
        print('PC=',z,'IR=',IRR,a,'R'+b,'R'+c,'R'+d)
        data_RB=int(data_reg[data_regtengah],16)
        data_RC=int(data_reg[data_regbelakang],16)
        
    #menentukan jenis operasi yang akan digunakan
    if data_operand=='10': 
        hasil = data_RB + data_RC

    if data_operand=='20':
        data_regdepan=int(data_regdepan,16)
        data_regdepan=int(data_reg[data_regdepan],16)
        hasil = data_regdepan + data_regbelakang

    if data_operand=='22':
        data_regdepan=int(data_regdepan,16)
        data_regdepan=int(data_reg[data_regdepan],16)
        hasil = data_regdepan - data_regbelakang
        
    if data_operand=='10': 
        hasil = data_RB + data_RC
        
    elif data_operand=='12':
        hasil = data_RB - data_RC

    elif data_operand=='18':
        hasil = data_RB << data_RC

    elif data_operand=='19':
        hasil = data_RB >> data_RC

    elif data_operand=='14':
        hasil = data_RB & data_RC

    elif data_operand=='15':
        hasil = data_RB | data_RC

    elif data_operand=='16':
        hasil = data_RB ^ data_RC

    elif data_operand=='32':
        data_regdepan=int(data_regdepan,16)
        data_reg[data_regdepan]=data_reg[data_regtengah]
        hasil=int(data_reg[data_regdepan],16)
        data_reg[data_regtengah]=hex(0)
        
    #memasukan data operasi ke dalam array
    hasil=hex(hasil)
    b=int(b)
    data_reg[b]=hasil

    #menampilkan hasil
    for x in range(0,4):
        y0=str(x*4)
        y1=str((x*4)+1)
        y2=str((x*4)+2)
        y3=str((x*4)+3)
        data_reg1=int(data_reg[x*4],16)
        data_reg2=int(data_reg[(x*4)+1],16)
        data_reg3=int(data_reg[(x*4)+2],16)
        data_reg4=int(data_reg[(x*4)+3],16)

        if data_reg1 < 0 :
            parsing_depan1=3
        else :
            parsing_depan1=4
        if data_reg2 < 0 :
            parsing_depan2=3
        else :
            parsing_depan2=4
        if data_reg3 < 0 :
            parsing_depan3=3
        else :
            parsing_depan3=4
        if data_reg4 < 0 :
            parsing_depan4=3
        else :
            parsing_depan4=4
        
        data_reg1=hex(data_reg1+sim)
        data_reg2=hex(data_reg2+sim)
        data_reg3=hex(data_reg3+sim)
        data_reg4=hex(data_reg4+sim)
        data_reg1=data_reg1[parsing_depan1:12]
        data_reg2=data_reg2[parsing_depan2:12]
        data_reg3=data_reg3[parsing_depan3:12]
        data_reg4=data_reg4[parsing_depan4:12]
        if x < 2:
            print('R'+y0+'=','','0x'+data_reg1,'R'+y1+'=','','0x'+data_reg2,'R'+y2+'=','','0x'+data_reg3,'R'+y3+'=','','0x'+data_reg4)
        elif x < 3:
            print('R'+y0+'=','','0x'+data_reg1,'R'+y1+'=','','0x'+data_reg2,'R'+y2+'=','0x'+data_reg3,'R'+y3+'=','0x'+data_reg4)
        else:
            print('R'+y0+'=','0x'+data_reg1,'R'+y1+'=','0x'+data_reg2,'R'+y2+'=','0x'+data_reg3,'R'+y3+'=','0x'+data_reg4) 
            print(' ')
