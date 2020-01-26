def model():
    import sys
    import numpy as np
    import pandas as pd
    import warnings
    from sklearn.model_selection import train_test_split
    warnings.filterwarnings('ignore')
    from sklearn.preprocessing import LabelEncoder,OneHotEncoder
    from sklearn.ensemble import RandomForestRegressor
    ab=pd.read_csv("./data.csv")
    hel=RandomForestRegressor(n_estimators=10,random_state=0)

    a=sys.argv

    x=ab.iloc[:,:-2].values
    y=ab.iloc[:,-1].values
    Us=float(a[1])
    temp=int(a[2])
    Fer=int(a[3])
    bri=int(a[4])
    yell=float(a[5])
    oil=float(a[6])
    pr=int(a[7])
    fibe=float(a[8])
    clim=a[9]
    state=a[10]
    month=a[11]
    hello=[Us,temp,Fer,bri,yell,oil,pr,fibe,clim,state,month]
    la=LabelEncoder()
    x[:,8]=la.fit_transform(x[:,8])
    x[:,9]=la.fit_transform(x[:,9])

    hello[4:]=hello
    if hello[12]=='winter':
        hello[0]=0
        hello[1]=0
    if hello[12]=='Monsoon':
        hello[0]=1
        hello[1]=0
    if hello[12]=='Summer':
        hello[0]=0
        hello[1]=1
    if hello[13]=='Gujarat':
        hello[2]=1
        hello[3]=0
    if hello[13]=='Haryana':
        hello[2]=0
        hello[3]=1
    if hello[13]=='Maharashtra':
        hello[2]=0
        hello[3]=0
    hello=hello[:-3]
    hello

    rav=np.asarray(hello).reshape(1,-1)
    ravi=OneHotEncoder(categorical_features=[8,9])
    x=ravi.fit_transform(x).toarray()
    x=pd.DataFrame(x)
    x.rename(columns={0:'Monsoon',1:'Summer',2:'Winter',3:'Gujarat',4:'Haryana',5:'Maharashtra',6:'US Dollar',7:'Temperature',8:'Fertilizer per Hectare',9:'Brightnes',10:'Yellowness',11:'Oil Price',12:'Price Of compiting crop',13:'Fiber Tenacity'},inplace=True)
    x.drop(['Winter','Maharashtra'],axis=1,inplace=True)
    x=x.values
    hel.fit(x,y)
    y_pred=hel.predict(rav)
    print(y_pred)
model()