#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df=pd.read_csv(r"Downloads\weatherAUS.csv")
df


# In[3]:


df["avg_temp"]=(df["Temp9am"]+df["Temp3pm"])/2


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[10]:


df["MinTemp"].skew()


# In[11]:


df["MinTemp"]=df["MinTemp"].fillna(df["MinTemp"].mean())


# In[12]:


df["MaxTemp"].skew()


# In[13]:


df["MaxTemp"]=df["MaxTemp"].fillna(df["MaxTemp"].mean())


# In[14]:


df["Rainfall"].skew()


# In[15]:


df["Rainfall"]=df["Rainfall"].fillna(df["Rainfall"].median())


# In[16]:


df["Evaporation"].skew()


# In[17]:


df["Evaporation"]=df["Evaporation"].fillna(df["Evaporation"].median())


# In[18]:


df["Sunshine"].skew()


# In[19]:


df["Sunshine"]=df["Sunshine"].fillna(df["Sunshine"].mean())


# In[20]:


df["WindGustDir"].value_counts()


# In[21]:


df["WindGustDir"]=df["WindGustDir"].fillna(value='W')


# In[22]:


df["WindGustSpeed"].skew()


# In[23]:


df["WindGustSpeed"]=df["WindGustSpeed"].fillna(df["WindGustSpeed"].median())


# In[24]:


df["WindDir9am"].value_counts().index[0]


# In[25]:


df["WindDir9am"]=df["WindDir9am"].fillna(value="N")


# In[26]:


df["WindDir3pm"].value_counts().index[0]


# In[27]:


df["WindDir3pm"]=df["WindDir3pm"].fillna(value="SE")


# In[28]:


df["WindSpeed9am"].skew()


# In[29]:


df["WindSpeed9am"]=df["WindSpeed9am"].fillna(df["WindSpeed9am"].median())


# In[30]:


df["WindSpeed3pm"].skew()


# In[31]:


df["WindSpeed3pm"]=df["WindSpeed3pm"].fillna(df["WindSpeed3pm"].median())


# In[32]:


df["Humidity9am"].skew()


# In[33]:


df["Humidity9am"]=df["Humidity9am"].fillna(df["Humidity9am"].mean())


# In[34]:


df["Humidity3pm"].skew()


# In[35]:


df["Humidity3pm"]=df["Humidity3pm"].fillna(df["Humidity3pm"].mean())


# In[36]:


df["Pressure9am"].skew()


# In[37]:


df["Pressure9am"]=df["Pressure9am"].fillna(df["Pressure9am"].mean())


# In[38]:


df["Pressure3pm"].skew()


# In[39]:


df["Pressure3pm"]=df["Pressure3pm"].fillna(df["Pressure3pm"].mean())


# In[40]:


df["Cloud9am"].skew()


# In[41]:


df["Cloud9am"]=df["Cloud9am"].fillna(df["Cloud9am"].mean())


# In[42]:


df["Cloud3pm"].skew()


# In[43]:


df["Cloud3pm"]=df["Cloud3pm"].fillna(df["Cloud3pm"].mean())


# In[44]:


df["Temp9am"].skew()


# In[45]:


df["Temp9am"]=df["Temp9am"].fillna(df["Temp9am"].mean())


# In[46]:


df["Temp3pm"].skew()


# In[47]:


df["Temp3pm"]=df["Temp3pm"].fillna(df["Temp3pm"].mean())


# In[48]:


df["RainToday"].value_counts().index[0]


# In[49]:


df["RainToday"]=df["RainToday"].fillna(value="No")


# In[50]:


df["RainTomorrow"].value_counts().index[0]


# In[51]:


df["RainTomorrow"]=df["RainTomorrow"].fillna(value="No")


# In[52]:


df["avg_temp"].skew()


# In[53]:


df["avg_temp"]=df["avg_temp"].fillna(df["avg_temp"].mean())


# In[54]:


df.isnull().sum()


# In[55]:


df["Date"]=pd.to_datetime(df["Date"])
df["date"]=df["Date"].dt.day
df["month"]=df["Date"].dt.month
df["year"]=df["Date"].dt.year


# In[56]:


df


# In[57]:


df2=df.iloc[:,1:]
df2


# In[58]:


df2.columns


# In[59]:


#EDA Analysis
df["Location"].unique()


# In[60]:


plt.figure(figsize=(10,9))
sns.countplot(data=df2,x="Location",palette="winter_r")
plt.xticks(rotation="vertical")


# In[61]:


sns.distplot(a=df2["MinTemp"])


# In[62]:


sns.boxplot(data=df2,x="MinTemp")


# In[63]:


sns.violinplot(data=df2,x="MinTemp",color="green")


# In[64]:


sns.distplot(a=df2["MaxTemp"],color="red")


# In[65]:


sns.boxplot(data=df2,x="MaxTemp")


# In[66]:


sns.violinplot(data=df2,x="MaxTemp",color="grey")


# In[67]:


sns.distplot(df2["Rainfall"],color="black")


# In[68]:


sns.distplot(a=df2["Evaporation"],color="brown")


# In[69]:


sns.distplot(a=df2["Sunshine"],color="orange")


# In[70]:


sns.boxplot(data=df2,x="Sunshine")


# In[71]:


sns.violinplot(data=df2,x="Sunshine",color="brown")


# In[72]:


sns.countplot(data=df2,x="WindGustDir")


# In[73]:


sns.distplot(a=df2["WindGustSpeed"])


# In[74]:


sns.boxplot(data=df2,x="WindGustSpeed")


# In[75]:


sns.violinplot(data=df2,x="WindGustSpeed",color="red")


# In[76]:


sns.countplot(data=df2,x="WindDir9am")


# In[77]:


sns.countplot(data=df2,x="WindDir3pm")


# In[78]:


sns.distplot(a=df["WindSpeed9am"])


# In[79]:


sns.boxplot(data=df2,x="WindSpeed9am")


# In[80]:


sns.violinplot(data=df,x="WindSpeed9am")


# In[81]:


sns.distplot(a=df2["WindSpeed3pm"])


# In[82]:


sns.boxplot(data=df2,x="WindSpeed3pm")


# In[83]:


sns.violinplot(data=df2,x="WindSpeed3pm")


# In[84]:


sns.distplot(a=df2["Humidity9am"])


# In[85]:


sns.boxplot(data=df2,x="Humidity9am")


# In[86]:


sns.violinplot(data=df2,x="Humidity9am")


# In[87]:


sns.distplot(a=df2["Humidity3pm"])


# In[88]:


sns.boxplot(data=df2,x="Humidity3pm")


# In[89]:


sns.violinplot(data=df2,x="Humidity3pm")


# In[90]:


sns.distplot(a=df2["Pressure9am"])


# In[91]:


sns.boxplot(data=df,x="Pressure9am")


# In[92]:


sns.violinplot(data=df2,x="Pressure9am")


# In[93]:


sns.distplot(a=df2["Pressure3pm"])


# In[94]:


sns.boxplot(data=df2,x="Pressure3pm")


# In[95]:


sns.violinplot(data=df2,x="Pressure3pm")


# In[96]:


sns.distplot(a=df2["Cloud9am"])


# In[97]:


sns.boxplot(data=df2,x="Cloud9am")


# In[98]:


sns.violinplot(data=df2,x="Cloud9am")


# In[99]:


sns.distplot(a=df2["Cloud3pm"])


# In[100]:


sns.boxplot(data=df2,x="Cloud3pm")


# In[101]:


sns.violinplot(data=df2,x="Cloud3pm")


# In[102]:


sns.distplot(a=df2["Temp9am"])


# In[103]:


sns.boxplot(data=df2,x="Temp9am")


# In[104]:


sns.violinplot(data=df2,x="Temp9am")


# In[105]:


sns.distplot(a=df2["Temp3pm"])


# In[106]:


sns.boxplot(data=df2,x="Temp3pm")


# In[107]:


sns.violinplot(data=df2,x="Temp3pm")


# In[108]:


sns.countplot(data=df2,x="RainToday")


# In[109]:


sns.countplot(data=df2,x="RainTomorrow")


# In[110]:


sns.distplot(a=df2["avg_temp"])


# In[111]:


sns.violinplot(data=df2,x="avg_temp")


# In[112]:


sns.boxplot(data=df2,x="avg_temp")


# In[146]:


sns.pairplot(df2)


# In[114]:


plt.figure(figsize=(15,15))
sns.heatmap(df2.corr(),annot=True,cmap="viridis_r",linewidth=2,linecolor="black")


# In[115]:


sns.scatterplot(data=df2,x="avg_temp",y="Rainfall")


# In[116]:


sns.lmplot(data=df2,x="Temp9am",y="Pressure9am")


# In[117]:


sns.lmplot(data=df2,x="Temp3pm",y="Pressure3pm")


# In[118]:


X=df2.drop(columns="RainTomorrow").values


# In[119]:


y=df.loc[:,"RainTomorrow"].values
y


# In[120]:


from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
X[:,0]=label.fit_transform(X[:,0])


# In[121]:


X[:,6]=label.fit_transform(X[:,6])
X[:,8]=label.fit_transform(X[:,8])
X[:,9]=label.fit_transform(X[:,9])
X[:,20]=label.fit_transform(X[:,20])


# In[122]:


from sklearn.preprocessing import StandardScaler
std=StandardScaler()
X=std.fit_transform(X)


# In[123]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)


# In[124]:


from sklearn.linear_model import LogisticRegression
logit=LogisticRegression()
logit.fit(X_train,y_train)
y_pred=logit.predict(X_test)
y_pred


# In[125]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
cm


# In[126]:


bias=logit.score(X_train,y_train)
bias


# In[127]:


varience=logit.score(X_test,y_test)
varience


# In[128]:


(21555+2961)/(21555+1171+3405+2961)


# In[129]:


from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test,y_pred)
acc


# In[130]:


from sklearn.metrics import classification_report
report=classification_report(y_test,y_pred)
report


# In[131]:


y=label.fit_transform(y)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)


# In[132]:


from sklearn.tree import DecisionTreeClassifier
dtree=DecisionTreeClassifier()
dtree.fit(X_train,y_train)
y_pred=dtree.predict(X_test)


# In[133]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
cm


# In[134]:


bias=dtree.score(X_train,y_train)
bias


# In[135]:


varience=dtree.score(X_test,y_test)
varience


# In[136]:


from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test,y_pred)
acc


# In[137]:


from sklearn.metrics import classification_report
report=classification_report(y_test,y_pred)
report


# In[138]:


from sklearn.metrics import auc,roc_curve
fpr,tpr,threshold=roc_curve(y_test,y_pred)
plt.plot(fpr,tpr)
plt.show()


# In[139]:


from sklearn.model_selection import RandomizedSearchCV
params={"max_depth":[5,7,10],"min_samples_split":[2,5,8],"min_samples_leaf":[2,5,8]}
rncv=RandomizedSearchCV(estimator=dtree,param_distributions=params)
rncv.fit(X_train,y_train)
print("best_params:",rncv.best_params_)
print("best_score:",rncv.best_score_)


# In[140]:


from sklearn.ensemble import RandomForestClassifier
rndf=RandomForestClassifier()
rndf.fit(X_train,y_train)
y_pred=rndf.predict(X_test)
y_pred


# In[141]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
cm


# In[142]:


bias=rndf.score(X_train,y_train)
bias


# In[143]:


varience=rndf.score(X_test,y_test)
varience


# In[144]:


from sklearn.metrics import accuracy_score
acc=accuracy_score(y_test,y_pred)
acc


# In[145]:


from sklearn.metrics import classification_report
report=classification_report(y_test,y_pred)
report


# model:Decision Tree Classifier
# 
# accuracy:78
# 
# precision:87
# 
# recall:86
# 
# model:Random forest Classifier
# 
# accuracy:85
# 
# precision:87
# 
# recall:96
