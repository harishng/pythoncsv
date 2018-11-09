# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:01:06 2018

@author: hari
"""
print('\t\tSurface coverage analysis\n')
import os
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename

global row_tot,ir,tot,c
#c = int(input('Enter total number of Sets of readings: '))
c=8
tot  =int(input('Enter total number of Images per reading: '))
row_tot = int(input('Enter total number of Rows per reading: '))
imgs_row = int(tot/row_tot)
new_index = range(47)
#mean_el = int(input('Enter Mean elements in a row: '))
ir = imgs_row
def import_csv_data():
    global v,df,pat
    file_path = askopenfilename()
    pat = file_path
    v.set(file_path)
    df = pd.read_excel(file_path,names = new_index)
    return df

root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Close',command=root.destroy).grid(row=1, column=1)
root.mainloop()
df.T


def remove_unwanted():
    global con_df2
    cols =[4,10,16,22,28,34,40,46]
    cols2 = [0,4,6,10,12,16,18,22,24,28,30,34,36,40,42,46]
    con_df =df[cols]  
    con_df3 =df[cols2]
    str1=os.getcwd()
    #str1 = pat
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    #x = file_path
    a= (x+' file1.xlsx')
    con_df2 = con_df.T
    new_ind = range(c)
    new_ind2 = range(c*2)
    con_df4 = con_df3.T
    con_df4.index = new_ind2
    con_df2.index = new_ind
    con_df2 = con_df2/1000
    #con_dfy = con_df4/1000
    con_df2.to_excel(a)
    #con_df2 = con_dfx
    return con_df2



def group_sort_in_order():
    new_index = range(c*row_tot)
    global t_df,temp_df
    t_df =pd.DataFrame()
    temp_df =pd.DataFrame()
    df = con_df2
    dfx =[]
    #global p
    p =0
    for h in range(int(row_tot)):
        p =h*imgs_row
        df1 =[]
        dfx =[]
        # Here we run loops to the number of times needed´in a row i.e 'ir'
        if h==0:
            for l in range(ir):
                df1.append(df[l])
                
            temp_df = pd.concat(df1,axis=1,ignore_index=True)
            t_df = t_df.append(temp_df)
            
        elif h%2==0:
            for m in range(ir):
                df1.append(df[m+p])
            
            temp_df = pd.concat(df1,axis=1,ignore_index=True)
            t_df= t_df.append(temp_df)
    
        elif h%2!=0:
            for k in range(ir):
                dfx.append(df[k+p])
                
            dfx = dfx[::-1]
            temp_df = pd.concat(dfx,axis=1,ignore_index=True)
            t_df= t_df.append(temp_df)
            
        
    t_df.index= new_index
    #temp_df.index = new_index
    str1=os.getcwd()
    #str1 = file_path
    str2=str1.split('\\')
    n=len(str2)
    #x=file_path
    x=str2[n-1]
    b=(x+' file2.xlsx')
    t_df.T
    t_df.to_excel(b)
    
    return t_df,temp_df

def print_factors(x):
   # This function takes a number and prints the factors
   print("The factors of",x,"are: \n")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
    
   return

def row_del():
    global mean_el,tp_df
    tp_df =t_df
    rep = input('\nDo u want to Delete some images (y/n): ')
    if rep =="y":
        print('\nThe total number of rows evenly deleted on both sides')
        idel =int(input('\nEnter number of Rows to be Deleted: '))
        nero = imgs_row-(2*idel)
        print('\nThus available row after deletion: '+str(nero))
        print_factors(nero)
        mean_an =int(input('\nEnter Mean elements in a row: '))
        mean_el = mean_an
        st = int(0+idel)
        fi = int(imgs_row-idel)
        
        # we are assigning the remaining columns
        tp_df = tp_df.iloc[:,st:fi]
        #print(tp_df.columns)
        ni = range(int(nero))
        tp_df.columns = ni
    elif rep =="n":
        mean_el = int(input('\nEnter Mean elements in a row: '))
        
        
    
    return mean_el,tp_df



def group_mean_byrow():
    #jk=pd.DataFrame()
    app = []
    global df_app
    df_app = pd.DataFrame()
    t_df = tp_df
    for y in range(c):
        b=y
        
        
        if row_tot == 5:
            jk = pd.DataFrame([t_df.loc[b],t_df.loc[b+(c*1)],t_df.loc[b+(c*2)],t_df.loc[b+(c*3)],t_df.loc[b+(c*4)]])
            jk = jk.replace(0, np.NaN)
            jk = jk.mean()
        elif row_tot == 4:
            jk = pd.DataFrame([t_df.loc[b],t_df.loc[b+(c*1)],t_df.loc[b+(c*2)],t_df.loc[b+(c*3)]])
            jk = jk.replace(0, np.NaN)
            jk = jk.mean()
        elif row_tot == 3:
            jk = pd.DataFrame([t_df.loc[b],t_df.loc[b+(c*1)],t_df.loc[b+(c*2)]])
            jk = jk.replace(0, np.NaN)
            jk = jk.mean()
        elif row_tot == 2:
            jk = pd.DataFrame([t_df.loc[b],t_df.loc[b+(c*1)]])
            jk = jk.replace(0, np.NaN)
            jk = jk.mean()
        
        app.append(jk)
        df_app = pd.concat(app,axis=1,ignore_index=True)
        
    
    str1=os.getcwd()
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    b=(x+' file3.xlsx')
    #df_app.to_excel(b)
    return df_app



def mean_std():
    global df_fin
    ti = int(imgs_row/mean_el)
    tapp =[]
    tapp1=[]
    df_fin = pd.DataFrame()
    df_fin1 = pd.DataFrame()
    yy=0
    kk=0
    jj=0
    sub = mean_el-1
    
    global ges1,res1
    for h in range(ti):
        #tt =np.array([ df_app.loc[kk:kk+sub]])
        yy= df_app.loc[kk:kk+sub].mean(axis=0)
        jj= df_app.loc[kk:kk+sub].std(axis=0)
        kk= kk+mean_el
        tapp.append(yy)
        tapp1.append(jj)
        df_fin = pd.concat(tapp,axis=1,ignore_index=True)
        df_fin1 = pd.concat(tapp1,axis=1,ignore_index=True)
    
    
    
    nam = range(c)
    nam1=[]
    nam2=[]
    
    [nam1.append(str(nam[g])+'_mean')for g in range(c)]
    [nam2.append(str(nam[g])+'_std')for g in range(c)]
    
    df_fin.index =nam1
    df_fin1.index =nam2
    emp = pd.DataFrame(['Mean'])
    emp1 = pd.DataFrame(['Std'])
    fra = [emp,df_fin,emp1,df_fin1]
    fra1 = [df_fin,df_fin1]
    res =pd.concat(fra)
    res1 =pd.concat(fra1)
    #print(len(ind))
    #res.columns = ind
    str1=os.getcwd()
    #print(str1)
    #str1 = pat
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    #print(x)
    b=(x+' file4.xlsx')
    #res = res.round(3)
    ges = res.T
    ges1 = res1.T
    #ges.to_excel(b)
    
    return ges1,res1,df_fin

def std_fin():
    #global tapp,tapp1
    n = len(df_fin)
    n2 = len(df_fin.T)
    #print(n,n2)
    i = 0
    e = n2-1
    s =0
    final_df =pd.DataFrame()
    tapp = []
    tapp1 = []
    dfm = pd.DataFrame()
    p = ((n2-1)/2)
    dfs= pd.DataFrame()
    if n2%2==0:
        for b in range(int(n/2)):
            tapp = []
            tapp1 = []
            i = 0
            e = n2-1
            
            for c in range(int((n2-1)/2)):
                va =np.array([df_fin[i][s],df_fin[i][s+1],df_fin[e][s],df_fin[e][s+1]])
                
                a1 = np.mean(va)
                a2 = np.std(va)
                za =pd.DataFrame([a1])
                sa =pd.DataFrame([a2])
                tapp.append(za)
                tapp1.append(sa)
                #print(tapp)
                #print(c)
                i+=1
                e=e-1
                
            s+=2
            
            dfm = pd.concat(tapp,axis=1,ignore_index=True)
            dfs = pd.concat(tapp1,axis=1,ignore_index=True)
            final_df = final_df.append(dfm)
            final_df = final_df.append(dfs)
            
    elif n2%2!=0:
        for b in range(int(n/2)):
            tapp = []
            tapp1 = []
            i = 0
            e = n2-1
            
            for c in range(int((n2-1)/2)):
                va =np.array([df_fin[i][s],df_fin[i][s+1],df_fin[e][s],df_fin[e][s+1]])
                
                a1 = np.mean(va)
                a2 = np.std(va)
                za =pd.DataFrame([a1])
                sa =pd.DataFrame([a2])
                tapp.append(za)
                tapp1.append(sa)
                #print(tapp)
                #print(c)
                i+=1
                e=e-1
                
            
            
            va2 = np.array([df_fin[p][s],df_fin[p][s+1]])
            am = np.mean(va2)
            astd = np.std(va2)
            am =pd.DataFrame([am])
            astd =pd.DataFrame([astd])
            tapp.append(am)
            tapp1.append(astd)
            dfm = pd.concat(tapp,axis=1,ignore_index=True)
            dfs = pd.concat(tapp1,axis=1,ignore_index=True)
            final_df = final_df.append(dfm)
            final_df = final_df.append(dfs)
            s+=2
    
    
    #le =range(8)
    s = int(len(final_df))
    s = range(s)
    final_df =final_df.T
    final_df.columns =s
    str1=os.getcwd()
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    b=(x+'filex.xlsx')
    #print(le)
    #final_df.reindex( columns= le)
    final_df.to_excel(b)
    
    return final_df
    

def new_mean_fun():
    global yy
    df_1 = tp_df
    rl = int(len(df_1))
    cl = int(len(df_1.T))
    yy=pd.DataFrame()
    loop_row= int(cl/mean_el)
    #print (rl)
    nw_ind = range(rl)
    kk=0
    jj=[]
    ri=0
    re=mean_el-1
    ci =0
    ce =7
    tapp =[]
    fi_df =pd.DataFrame()
    fi_df1 =pd.DataFrame()
    fi_df2 =pd.DataFrame()
    tapp = []
    tapp1 = []
    for r in range(8):
        ci = r
        
        for c in range(row_tot):
           ne= df_1.loc[ci]
           jj.append(ne)
           ci +=8
    yy = pd.DataFrame(jj)
    yy.index =nw_ind
    ri=0
    re=mean_el-1
    ci =0
    ce =row_tot-1
    
    
    for e in range(8):
        ri=0
        re=mean_el-1
        tapp = []
        tapp1 = []
        
        for q in range(loop_row):
            kk =(yy.loc[ci:ce,ri:re])
            kk =np.array(kk)
            #print(kk)
            #print(ri,re,ci,ce)
            ri +=mean_el
            re +=mean_el
            me = np.nanmean(kk)
            st =np.nanstd(kk,ddof=1)
            #me =kk.mean()
            #st =kk.std()
            za =pd.DataFrame([me])
            sa =pd.DataFrame([st])
            tapp.append(za)
            tapp1.append(sa)
            kk =0
        #tapp = pd.DataFrame(tapp)
        #tapp1 = pd.DataFrame(tapp1)
        dfm = pd.concat(tapp,axis=1,ignore_index=True)
        dfs = pd.concat(tapp1,axis=1,ignore_index=True)
        fi_df1 = fi_df1.append(dfm)
        fi_df2 = fi_df2.append(dfs)
        ci +=row_tot
        ce +=row_tot
    
    #fi_df =pd.DataFrame([fi_df])
    nam =[]
    nam = range(8)
    nam1=[]
    nam2=[]
    #print(fi_df1)
    [nam1.append(str(nam[g])+'_mean')for g in range(8)]
    [nam2.append(str(nam[g])+'_std')for g in range(8)]
    #print(nam1,nam2)
    emp = pd.DataFrame(['Mean'])
    emp1 = pd.DataFrame(['Std'])
    fi_df1.index = nam1
    fi_df2.index =nam2
    #print(fi_df1)
    fi_df = pd.concat([emp,fi_df1,emp1,fi_df2])
    
    s = len(fi_df)
    fi_df = fi_df.T
    
    s =range(s)
    #fi_df.columns = s
    str1=os.getcwd()
    str2=str1.split('\\')
    n=len(str2)
    x=str2[n-1]
    b=(x+'file3.xlsx')
    f=(x+'file4.xlsx')
    yy.to_excel(b)
    fi_df.to_excel(f)
    
    return yy
    











print('\nStep 2:')
remove_unwanted()

print('\nStep 3:')
group_sort_in_order()

print('\nStep 4:')
row_del()

new_mean_fun()

print('\nStep 5:')
group_mean_byrow()

print('\nStep 6:')
mean_std()

print('\nstep 7:')
std_fin()


#input('Press Enter to exit')