import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Jika Pada streamlit gunakan simbol "\"

#Pembacaan Dataset
path = "PRSA_Data_20130301-20170228"
df_Aotizhongxin = pd.read_csv(path+'/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
df_Changping = pd.read_csv(path+'/PRSA_Data_Changping_20130301-20170228.csv')
df_Dingling = pd.read_csv(path+'/PRSA_Data_Dingling_20130301-20170228.csv')

df = pd.concat([df_Aotizhongxin,df_Changping,df_Dingling], ignore_index=True)
df.drop(columns = ['No'], axis = 1, inplace=True)
df['year'] = df['year'].astype("str")

#Kolom Utama yang digunakan untuk analisis
kolom_yang_digunakan = df.select_dtypes(include='number').columns[3:13]

#Filter Data Berdasarkan Kolom
filter_Aotizhongxin = df[df['station'] == 'Aotizhongxin'].iloc[:,0:10]
filter_Changping = df[df['station'] == 'Changping'].iloc[:,0:10]
filter_Dingling = df[df['station'] == 'Dingling'].iloc[:,0:10]

#Aggerasi Mean Semua Feature
mean_Aotizhongxin = df[df['station'] == 'Aotizhongxin'].iloc[:,4:10].mean()
mean_Changping = df[df['station'] == 'Changping'].iloc[:,4:10].mean()
mean_Dingling = df[df['station'] == 'Dingling'].iloc[:,4:10].mean()


#Aggerasi Mean Semua Feature Berdasarkan Tahun
year_Aotizhongxin_params = pd.DataFrame(filter_Aotizhongxin.groupby(filter_Aotizhongxin['year'])[mean_Aotizhongxin.index].mean()).reset_index()
year_Changping_params = pd.DataFrame(filter_Changping.groupby(filter_Changping['year'])[mean_Aotizhongxin.index].mean()).reset_index()
year_Dingling_params = pd.DataFrame(filter_Dingling.groupby(filter_Dingling['year'])[mean_Aotizhongxin.index].mean()).reset_index()


with st.sidebar:
    st.header("Home")


col1,col2,col3 = st.columns(3)

with col1:
    st.header("Aotizhogxin")
    with st.expander("Dataset Aotizhogxin"):
        st.dataframe(df_Aotizhongxin, width=500, height= 150)

with col2:
    st.header("Changping")
    with st.expander("Dataset Changping"):
        st.dataframe(df_Changping, width=500, height=150)

with col3:
    st.header("Dingling")
    with st.expander("Dataset Dingling"):
        st.dataframe(df_Dingling, width=500, height=150)


tab1,tab2,tab3 = st.tabs(["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"])


with tab1:
    st.subheader("1. Apakah terdapat korelasi faktor penting yang disebutkan di atas terhadap TEMP (Temperature), DEWP (Dew Point), PRES (Pressure), Rain?")
    # Function Korelasi
    fig, ax = plt.subplots(4,6, figsize=(15,5), sharex = False)

    sns.scatterplot(data = df, x = kolom_yang_digunakan[0], y = kolom_yang_digunakan[6], ax = ax[0][0])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[1], y = kolom_yang_digunakan[6], ax = ax[0][1])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[2], y = kolom_yang_digunakan[6], ax = ax[0][2])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[3], y = kolom_yang_digunakan[6], ax = ax[0][3])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[4], y = kolom_yang_digunakan[6], ax = ax[0][4])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[5], y = kolom_yang_digunakan[6], ax = ax[0][5])

    ax[0][0].xaxis.set_visible(False)
    ax[0][1].xaxis.set_visible(False)
    ax[0][2].xaxis.set_visible(False)
    ax[0][3].xaxis.set_visible(False)
    ax[0][4].xaxis.set_visible(False)
    ax[0][5].xaxis.set_visible(False)

    ax[0][1].yaxis.set_visible(False)
    ax[0][2].yaxis.set_visible(False)
    ax[0][3].yaxis.set_visible(False)
    ax[0][4].yaxis.set_visible(False)
    ax[0][5].yaxis.set_visible(False)


    sns.scatterplot(data = df, x = kolom_yang_digunakan[0], y = kolom_yang_digunakan[7], ax = ax[1][0])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[1], y = kolom_yang_digunakan[7], ax = ax[1][1])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[2], y = kolom_yang_digunakan[7], ax = ax[1][2])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[3], y = kolom_yang_digunakan[7], ax = ax[1][3])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[4], y = kolom_yang_digunakan[7], ax = ax[1][4])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[5], y = kolom_yang_digunakan[7], ax = ax[1][5])

    ax[1][0].xaxis.set_visible(False)
    ax[1][1].xaxis.set_visible(False)
    ax[1][2].xaxis.set_visible(False)
    ax[1][3].xaxis.set_visible(False)
    ax[1][4].xaxis.set_visible(False)
    ax[1][5].xaxis.set_visible(False)

    ax[1][1].yaxis.set_visible(False)
    ax[1][2].yaxis.set_visible(False)
    ax[1][3].yaxis.set_visible(False)
    ax[1][4].yaxis.set_visible(False)
    ax[1][5].yaxis.set_visible(False)


    sns.scatterplot(data = df, x = kolom_yang_digunakan[0], y = kolom_yang_digunakan[8], ax = ax[2][0])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[1], y = kolom_yang_digunakan[8], ax = ax[2][1])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[2], y = kolom_yang_digunakan[8], ax = ax[2][2])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[3], y = kolom_yang_digunakan[8], ax = ax[2][3])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[4], y = kolom_yang_digunakan[8], ax = ax[2][4])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[5], y = kolom_yang_digunakan[8], ax = ax[2][5])

    ax[2][0].xaxis.set_visible(False)
    ax[2][1].xaxis.set_visible(False)
    ax[2][2].xaxis.set_visible(False)
    ax[2][3].xaxis.set_visible(False)
    ax[2][4].xaxis.set_visible(False)
    ax[2][5].xaxis.set_visible(False)

    ax[2][1].yaxis.set_visible(False)
    ax[2][2].yaxis.set_visible(False)
    ax[2][3].yaxis.set_visible(False)
    ax[2][4].yaxis.set_visible(False)
    ax[2][5].yaxis.set_visible(False)


    sns.scatterplot(data = df, x = kolom_yang_digunakan[0], y = kolom_yang_digunakan[9], ax = ax[3][0])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[1], y = kolom_yang_digunakan[9], ax = ax[3][1])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[2], y = kolom_yang_digunakan[9], ax = ax[3][2])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[3], y = kolom_yang_digunakan[9], ax = ax[3][3])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[4], y = kolom_yang_digunakan[9], ax = ax[3][4])
    sns.scatterplot(data = df, x = kolom_yang_digunakan[5], y = kolom_yang_digunakan[9], ax = ax[3][5])

    ax[3][1].yaxis.set_visible(False)
    ax[3][2].yaxis.set_visible(False)
    ax[3][3].yaxis.set_visible(False)
    ax[3][4].yaxis.set_visible(False)
    ax[3][5].yaxis.set_visible(False)

    plt.show()

    st.pyplot(fig)
    with st.expander("Hasil Analisis"):
        st.write("""Hasil menunjukkan, nilai korelasi faktor penting udara dengan TEMP, RES, DEWP dan RAIN 
        berada pada jenis Moderate Correlation (Tingkat Menengah) menuju Low Correlation (Tingkat Lemah). 
        Hal ini dikarenakan nilai tersebut berada pada -0.5 hingga 0.6. Sehingga bisa disimpulkan pengaruh 
        keempat feature terhadap faktor penting kualitas udara tidak terlalu signifikan""")

with tab2:
    st.subheader("""2. Bagaimana Komposisi stasiun yang memiliki tingkat rata-rata tertinggi dan terendah dari faktor penting kualitas udara?""")
    #Hasil Mean
    data = {'features': mean_Aotizhongxin.index,
        'Mean_Aotizhongxin': mean_Aotizhongxin.values,
        'Mean_Changping': mean_Changping.values,
        'Mean_Dingling': mean_Dingling.values}


    frame_mean = pd.DataFrame(data = data)
    frame_mean['Max Kota'] = ["Aotizhongxin" if np.max([frame_mean.Mean_Aotizhongxin[i],frame_mean.Mean_Changping[i],frame_mean.Mean_Dingling[i]]) == frame_mean.Mean_Aotizhongxin[i] else("Changping" if np.max([frame_mean.Mean_Aotizhongxin[i],frame_mean.Mean_Changping[i],frame_mean.Mean_Dingling[i]]) == frame_mean.Mean_Changping[i] else "Dingling") for i in range(len(frame_mean))]
    frame_mean['Min Kota'] = ["Aotizhongxin" if np.min([frame_mean.Mean_Aotizhongxin[i],frame_mean.Mean_Changping[i],frame_mean.Mean_Dingling[i]]) == frame_mean.Mean_Aotizhongxin[i] else("Changping" if np.min([frame_mean.Mean_Aotizhongxin[i],frame_mean.Mean_Changping[i],frame_mean.Mean_Dingling[i]]) == frame_mean.Mean_Changping[i] else "Dingling") for i in range(len(frame_mean))]

    figure,ax = plt.subplots(figsize=(15,5))

    fig.subplots_adjust(hspace=0.7, top=0.75)
    x = np.arange(len(frame_mean['features']))

    bar1 = ax.bar(x - 0.3, frame_mean['Mean_Aotizhongxin'], width=0.3,label = 'Aotizhongxin')
    bar2 = ax.bar(x, frame_mean['Mean_Changping'], width=0.3,label = 'Changping')
    bar3 = ax.bar(x + 0.3, frame_mean['Mean_Dingling'], width=0.3,label = 'Dingling')

    ax.set_xlabel('faktor kualitas udara', fontsize = 17, labelpad = 20)
    ax.set_ylabel('Values',fontsize = 20)
    plt.suptitle(x = 0.5, y=1.05 ,t="Perbandingan rata-rata fakotr kualiatas Udara", fontsize = 20, fontweight = 'bold')
    ax.set_title(x = 0.5, y=1.07, label='Berdasarkan Stasiun', fontsize = 18)
    plt.xticks(x, frame_mean['features'])
    ax.legend(loc = 2)

    st.pyplot(figure)
    with st.expander("Hasil Analisis"):
        st.write("""Aotizhongxin merupakan statsiun yang memiliki tingkat rata-rata faktor kualitas udara tertinggi 
        dari statsiun yang lain kecuali faktor O3, sedangkan Dingling merupakan stasiun yang memiliki 
        kualitas udara yang paling baik dimana faktor-faktor kualitas udara (kecuali O3) memiliki nilai paling rendah. 
        Pada statsiun Changping bersifat tidak buruk namun juga tidak baik dalam kualitas udaranya""")


with tab3:
    st.subheader("""3. Perkembangan nilai tahun secara rata-rata pada faktor di atas setiap stasiun, sehingga mengetahui tahun tertinggi nya""")
    #Parameter PM2.5,PM10, SO2, NO2, O3
    fig,ax = plt.subplots(1,3, figsize = (15,5), sharex=True)
    fig.subplots_adjust(hspace=0.7, top=0.7)
    fig.suptitle('Nilai rata-rata PM2.5, PM10, SO2, NO2, O3', fontsize = 20, fontweight='bold')
    fig.text(0.5,0.9,'Tahun 2013-2017', horizontalalignment="center")
    sns.set(style = 'darkgrid')

    ax[0].title.set_text('Aotizhongxin')
    ax[0].plot(year_Aotizhongxin_params['year'].values, year_Aotizhongxin_params['PM2.5'].values, label = 'PM2.5', linestyle = "--")
    ax[0].plot(year_Aotizhongxin_params['year'].values, year_Aotizhongxin_params['PM10'].values, label = 'PM10')
    ax[0].plot(year_Aotizhongxin_params['year'].values, year_Aotizhongxin_params['SO2'].values, label = 'SO2')
    ax[0].plot(year_Aotizhongxin_params['year'].values, year_Aotizhongxin_params['NO2'].values, label = 'NO2')
    ax[0].plot(year_Aotizhongxin_params['year'].values, year_Aotizhongxin_params['O3'].values, label = 'O3')
    ax[0].legend(bbox_to_anchor=(0.85,1.25), loc =2, borderaxespad = 0., ncol = len(ax[0].lines))
    ax[0].set_ylabel("Values", fontsize = 15, labelpad = 20)

    ax[1].title.set_text('Changping')
    ax[1].plot(year_Changping_params['year'].values, year_Changping_params['PM2.5'].values, label = 'PM2.5', linestyle = "--")
    ax[1].plot(year_Changping_params['year'].values, year_Changping_params['PM10'].values, label = 'PM10')
    ax[1].plot(year_Changping_params['year'].values, year_Changping_params['SO2'].values, label = 'SO2')
    ax[1].plot(year_Changping_params['year'].values, year_Changping_params['NO2'].values, label = 'NO2')
    ax[1].plot(year_Changping_params['year'].values, year_Changping_params['O3'].values, label = 'O3')
    ax[1].set_xlabel("Tahun", fontsize = 15, labelpad = 20)

    ax[2].title.set_text('Dingling')
    ax[2].plot(year_Dingling_params['year'].values, year_Dingling_params['PM2.5'].values, label = 'PM2.5', linestyle = "--")
    ax[2].plot(year_Dingling_params['year'].values, year_Dingling_params['PM10'].values, label = 'PM10')
    ax[2].plot(year_Dingling_params['year'].values, year_Dingling_params['SO2'].values, label = 'SO2')
    ax[2].plot(year_Dingling_params['year'].values, year_Dingling_params['NO2'].values, label = 'NO2')
    ax[2].plot(year_Dingling_params['year'].values, year_Dingling_params['O3'].values, label = 'O3')


    #Parameter CO
    fig2,ax = plt.subplots(1,3, figsize = (15,5), sharex=True)

    fig2.subplots_adjust(hspace=0.7, top=0.75)
    fig2.suptitle('Nilai rata-rata CO',fontsize = 20, fontweight='bold')
    fig2.text(0.5,0.9,'Tahun 2013-2017', horizontalalignment="center")
    sns.set(style = 'darkgrid')

    ax[0].title.set_text('Aotizhongxin')
    ax[0].plot(year_Aotizhongxin_params['year'].values, year_Aotizhongxin_params['CO'].values)
    ax[0].set_ylabel("Values", fontsize = 15, labelpad = 20)


    ax[1].title.set_text('Changping')
    ax[1].plot(year_Changping_params['year'].values, year_Changping_params['CO'].values)
    ax[1].set_xlabel("Tahun", fontsize = 15, labelpad = 20)


    ax[2].title.set_text('Dingling')
    ax[2].plot(year_Dingling_params['year'].values, year_Dingling_params['CO'].values)


    st.pyplot(fig)
    st.pyplot(fig2)

    with st.expander("Hasil Analisis"):
        st.markdown("""
        1. Pada Aotizhongxin 
    
        a. PM2.5 -> tingkat **tertinggi** berada pada **2017** dan tinggkat **terendah** nya berada pada **2016**

        b. PM10 -> tingkat **tertinggi** berada pada **2014** dan tingkat **terendah** nya berada pada **2016**

        c. SO2 -> tingkat **tertinggi** berada pada **2013** dan tingkat **terendah** nya berada pada **2016**

        d. NO2 -> tingkat **tertinggi** berada pada **2017** dan tingkat **terendah** nya berada pada **2016**
        
        e. O3 -> tingkat **tertinggi** berada pada **2015** dan tingkat **terendah** nya berada pada **2013**

    2. Pada Changping 
        
        a. PM2.5 -> tingkat **tertinggi** berada pada **2017** dan tinggkat **terendah** nya berada pada **2016**

        b. PM10 -> tingkat **tertinggi** berada pada **2014** dan tingkat **terendah** nya berada pada **2016**

        c. SO2 -> tingkat **tertinggi** berada pada **2014** dan tingkat **terendah** nya berada pada **2016**

        d. NO2 -> tingkat **tertinggi** berada pada **2017** dan tingkat **terendah** nya berada pada **2013**
        
        e. O3 -> tingkat **tertinggi** berada pada **2014** dan tingkat **terendah** nya berada pada **2017**

    3. Pada Dingling 
        
        a. PM2.5 -> tingkat **tertinggi** berada pada **2014** dan tinggkat **terendah** nya berada pada **2016**

        b. PM10 -> tingkat **tertinggi** berada pada **2014** dan tingkat **terendah** nya berada pada **2017**

        c. SO2 -> tingkat **tertinggi** berada pada **2014** dan tingkat **terendah** nya berada pada **2016**

        d. NO2 -> tingkat **tertinggi** berada pada **2017** dan tingkat **terendah** nya berada pada **2016**
        
        e. O3 -> tingkat **tertinggi** berada pada **2016** dan tingkat **terendah** nya berada pada **2017**
        

**Sehingga bisa disimpulkan**
Tahun 2014 dan 2017 merupakan tahun yang paling sering terjadi nya polusi udara dari ketiga stasiun tersebut dan 
Tahun 2016 merupakan tahun yang memiliki tingkat kualitas paling baik selama 5 tahun terakhir

        """)
