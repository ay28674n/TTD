# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 19:16:36 2019

@author: Arunkumar
"""



import pandas as pd
import numpy as np

jan2018=pd.read_excel("FY15.xlsx")
col=jan2018.columns.tolist()


jan2018.loc[jan2018['Beaureau']== 0,'Beaureau']=0
jan2018.loc[jan2018['Beaureau'] == -1, 'Beaureau']=-1
jan2018.loc[(jan2018['Beaureau']>=1)& (jan2018['Beaureau']<=650),'Beaureau']=2
jan2018.loc[(jan2018['Beaureau']>650) & (jan2018['Beaureau']<=700),'Beaureau']=3
jan2018.loc[(jan2018['Beaureau']>700),'Beaureau']=4


jan2018.loc[jan2018['Beaureau']== 0,'Beaureau']= '0'
jan2018.loc[jan2018['Beaureau']== -1,'Beaureau']= -1
jan2018.loc[jan2018['Beaureau']== 2,'Beaureau']= '1-650'
jan2018.loc[jan2018['Beaureau']== 3,'Beaureau']= '651-700'
jan2018.loc[jan2018['Beaureau']== 4,'Beaureau']= '>750'









jan2018['jan2018']
'BRANCHNAME'
a = pd.pivot_table(jan2018,index='BRANCHNAME', columns='May DPD', values='FP',aggfunc=['count','sum'])

'Disb Cheque Amount'
b = pd.pivot_table(jan2018,index='Disb Cheque Amount', columns='May DPD', values='FP',aggfunc=['count','sum'])

'Disbursement Amount'
c = pd.pivot_table(jan2018,index='Disbursement Amount', columns='May DPD', values='FP',aggfunc=['count','sum'])

'Bal Disb'
d = pd.pivot_table(jan2018,index='Bal Disb', columns='May DPD', values='FP',aggfunc=['count','sum'])

'Noof Coapp'
e = pd.pivot_table(jan2018,index='Noof Coapp', columns='May DPD', values='FP',aggfunc=['count','sum'])

'Product'
e2 = pd.pivot_table(jan2018,index='Product', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Disb scheme'
f = pd.pivot_table(jan2018,index='Disb scheme', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Disb Sch Pattern'
g = pd.pivot_table(jan2018,index='Disb Sch Pattern', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Property Type'
h = pd.pivot_table(jan2018,index='Property Type', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Cust Profile'
i = pd.pivot_table(jan2018,index='Cust Profile', columns='May DPD', values='FP',aggfunc=['count','sum'])


'AppIncomeNivara Assesment'
j = pd.pivot_table(jan2018,index='AppIncomeNivara Assesment', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Co App1Income'
k = pd.pivot_table(jan2018,index='Co App1Income', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Co App2Income'
l = pd.pivot_table(jan2018,index='Co App2Income', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Co App3Income'
m = pd.pivot_table(jan2018,index='Co App3Income', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Co App4Income'
n = pd.pivot_table(jan2018,index='Co App4Income', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Co App5Income'
o = pd.pivot_table(jan2018,index='Co App5Income', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Total Income of Case'
p = pd.pivot_table(jan2018,index='Total Income of Case', columns='May DPD', values='FP',aggfunc=['count','sum'])



'Assessed Income combined Income'
q = pd.pivot_table(jan2018,index='Assessed Income combined Income', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Prpsl Proprty Val'
r = pd.pivot_table(jan2018,index='Prpsl Proprty Val', columns='May DPD', values='FP',aggfunc=['count','sum'])


'FOIR'
s = pd.pivot_table(jan2018,index='FOIR', columns='May DPD', values='FP',aggfunc=['count','sum'])


'LTV'
t = pd.pivot_table(jan2018,index='LTV', columns='May DPD', values='FP',aggfunc=['count','sum'])



'Tenure'
u = pd.pivot_table(jan2018,index='Tenure', columns='May DPD', values='FP',aggfunc=['count','sum'])


'ROI'
v = pd.pivot_table(jan2018,index='ROI', columns='May DPD', values='FP',aggfunc=['count','sum'])


'PAYMETHOD'
w = pd.pivot_table(jan2018,index='PAYMETHOD', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Cycle Date'
x = pd.pivot_table(jan2018,index='Cycle', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Ptype'
y = pd.pivot_table(jan2018,index='Ptype', columns='May DPD', values='FP',aggfunc=['count','sum'])



'Current Tenure'
z = pd.pivot_table(jan2018,index='Current Tenure', columns='May DPD', values='FP',aggfunc=['count','sum'])

'New Resale'
a1 = pd.pivot_table(jan2018,index='New Resale', columns='May DPD', values='FP',aggfunc=['count','sum'])


'ROI'
b1 = pd.pivot_table(jan2018,index='ROI', columns='May DPD', values='FP',aggfunc=['count','sum'])

'Plot Area (sqft)'
c1 = pd.pivot_table(jan2018,index='Plot Area (sqft)', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Actual Built-up Area (sqft)'
d1 = pd.pivot_table(jan2018,index='Actual Built-up Area (sqft)', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Income Earning Members'
e1 = pd.pivot_table(jan2018,index='Income Earning Members', columns='May DPD', values='FP',aggfunc=['count','sum'])



'Plot Cost (lacs) at Current Mkt Value'
f1 = pd.pivot_table(jan2018,index='Plot Cost (lacs) at Current Mkt Value', columns='May DPD', values='FP',aggfunc=['count','sum'])

'Estimated Construction Cost (lacs)'
g1 = pd.pivot_table(jan2018,index='Estimated Construction Cost (lacs)', columns='May DPD', values='FP',aggfunc=['count','sum'])

'Total' 
h1 = pd.pivot_table(jan2018,index='Total', columns='May DPD', values='FP',aggfunc=['count','sum'])


'DISBURSEMENTSTATUS'
i1 = pd.pivot_table(jan2018,index='DISBURSEMENTSTATUS', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Gender'
k1 = pd.pivot_table(jan2018,index='Gender', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Loc Type'
l1 = pd.pivot_table(jan2018,index='LOCATIONTYPE', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Scheme'
m1 = pd.pivot_table(jan2018,index='Scheme', columns='May DPD', values='FP',aggfunc=['count','sum'])


'age'
n1 = pd.pivot_table(jan2018,index='age', columns='May DPD', values='FP',aggfunc=['count','sum'])



'Type of Khatha'
o1 = pd.pivot_table(jan2018,index='Type of Khatha', columns='May DPD', values='FP',aggfunc=['count','sum'])



'Customer Category'
p1 = pd.pivot_table(jan2018,index='Customer Category', columns='May DPD', values='FP',aggfunc=['count','sum'])



'Religion'
q1 = pd.pivot_table(jan2018,index='Religion', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Original Tenure'
r1 = pd.pivot_table(jan2018,index='Original Tenure', columns='May DPD', values='FP',aggfunc=['count','sum'])


'Apprv Ln Amt'
s1 = pd.pivot_table(jan2018,index='Apprv Ln Amt', columns='May DPD', values='FP',aggfunc=['count','sum'])



horizontal_stack.to_csv("mARCH ftf 2018.csv")
horizontal_stack = pd.concat([a,b,c,d,e,e2,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,z,a1,b,1,c1,d1,e1,f1,g1,h1,i1,h1,k1,m1,n1,p1,q1,r1,s1], axis=0)
