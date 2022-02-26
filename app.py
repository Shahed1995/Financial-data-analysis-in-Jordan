# library in python code 
import matplotlib as plt 
from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st

# Read the data file 
Economic_df = pd.read_csv('Economic_activity_current_basic_prices_years_2002_2009 _million_dinars.csv')


st.title("الناتج المحلي الإجمالي حسب النشاط الاقتصادي بالأسعار الأساسية الجارية للسنوات 2002-2009 (مليون دينار) مع تعداد السكاني")
st.subheader("تحليل البيانات باستخدام بايثون")
df1=pd.DataFrame(Economic_df)

if Economic_df is not None:
    if st.checkbox("إظهار قاعدة البيانات"):
        if st.button("إظهار كامل  قاعدة البيانات"):
            st.write(df1)
        if st.button("إظهار أول خمس صفوف في قاعدة البيانات"):
            st.write(Economic_df.head())
        if st.button("إظهار آخر خمس صفوف في قاعدة البيانات"):
            st.write(Economic_df.tail())
            
        
if Economic_df is not None:
    if st.checkbox("اظهار اسماء الأعمدة في قاعدة البيانات المستخدمة"):
        st.text("الأعمدة ")
        st.write(Economic_df.columns)

if Economic_df is not None:
    if st.checkbox(" اعلى القيم في  كل عمود"):
        st.text("أعلى القيم في كل عامود في اللون الأصفر")
        st.write(df1.style.highlight_max())
        
if Economic_df is not None:
    if st.checkbox(" اقل القيم في  كل عمود"):
        st.text("أقل القيم في كل عامود في اللون الأصفر")
        st.write(df1.style.highlight_min())        


if Economic_df is not None:
    if st.checkbox("اظهار متوسط صافي الدخل  القومي الإجمالي من عام 2002 الى عام 2009"):
        st.text("صافي الدخل القومي الإجمالي في الاردن خلال 9 سنوات ")
        revenue_mean = Economic_df['Gross national income'].mean()
        st.write(revenue_mean)
        



if Economic_df is not None:
    df=st.radio ("ما البعد الذي تريد التحقق منه؟ "  ,   ('الصفوف','الأعمدة'))
    if df=='الصفوف':
        st.text("عدد الصفوف هو ")
        st.write(Economic_df.shape[0])
    if df=='الأعمدة':
        st.text("عدد الأعمدة هو")
        st.write(Economic_df.shape[1])


if st.button("هل هنالك بيانات مفقودة ؟"):
    if Economic_df is not None:
        test=Economic_df.isnull().values.any()
        if test==True:
            st.success( "توجد قيم مفقودة في قاعدة البيانات")
        else:
            st.success("لا توجد قيم مفقودة")

if st.button("فحص الطول قاعدة البيانات"):
      st.write(len(Economic_df))
        
if st.checkbox("إظهار ملخص عن قاعدة البيانات"):
        st.write(Economic_df.describe(include='all'))




def bar_chart1():

    Year = Economic_df["Year"]
    values = Economic_df["number of population"]

    fig = plt.figure(figsize = (10, 5))

    plt.bar(Year, values)
    plt.xlabel("The years from 2000-2009")
    plt.ylabel("population (Million)")
    plt.title("A study of the relationship between population numbers with progress in years in Jordan")
    st.pyplot(fig)


if st.checkbox("إظهار العلاقة ما بين عدد السكان و السنوات"):
    bar_chart1()
    st.success("ملخص العلاقة ما بين معدل اعداد السكان في الاردن عبر السنوات ")
    st.text("بحسب ما هو ظاهر في الشكل انه العلاقة طردية ما بين معدلالسكان في  الاردن في ازدياد اي ان العلاقة طردية ما بين اعداد السكان و  السنوات")





def bar_chart2():

    Year = Economic_df["Year"]
    Agriculture = Economic_df["Agriculture, hunting, forestry and fishing"]
    fig = plt.figure(figsize = (10, 5) )
    plt.bar(Year, Agriculture)
    plt.xlabel("The years from 2000-2009")
    plt.ylabel("production rate of  Agriculture, hunting, forestry and fishing")
    plt.title("A study of the relationship between production rate of [Agriculture, hunting, forestry and fishing]  with progress in years in Jordan")
    plt.plot(color="r")
    st.pyplot(fig)




if st.checkbox(" إظهار العلاقة ما بين معدل انتاج الزراعة و الصيد "):
    st.bar_chart(Economic_df)

    bar_chart2()
    st.success("ملخص العلاقة ما بين معدل انتاج الزراعةو الصيد حسب السنوات ")
    st.text("بحسب ما هو ظاهر في الشكل انه العلاقة طردية ما بين معدل انتاج الزراعة في الاردن مع عدد السنوات مما يؤدي الى زيادة الإنتاجية عبر السنوات")





if st.checkbox(" إظهار العلاقة ما بين اعداد السكان في الأردن و معدل الدخل القومي خلال 9 سنوات "):

    chart_data = pd.DataFrame(
        Economic_df,
        columns=['number of population', 'Gross national income'])

    st.line_chart(chart_data)
    st.success("ملخص العلاقة ما اعداد السكان في الأردن و معدل الدخل القومي ")
    st.text(" العلاقة طردية")






if st.button("عن موقع الويب"):
    st.success("53تم بنائه من مجتمع رقم ")
    st.text("تحدي مجتمعات البرمجة")




if st.button("من نحن"):
    st.success("أعضاء الفريق ")
    st.text("شهد الخطيب")
    st.text("روان ابو ليلى")
    st.text("وعد الخطيب")
    st.text("رغد الخطيب")