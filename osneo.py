# importing required modules
import PyPDF2
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import style

st.set_option('deprecation.showPyplotGlobalUse', False)

# creating a pdf file object
pdfFileObj = open('Sample 2022Aug.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

data = []
reqd = {}

for i in range(0,pdfReader.numPages):               # iterating through all pages
# creating a page object
    pageObj = pdfReader.getPage(i)                  # extracting text from page
    data += (pageObj.extractText().splitlines())    # printing text

# making a dictionary of keywords and their corresponding values

keywords = {'photometry':'Iron','hemoglobin':'Hemoglobin','Leucocyte':'Leucocyte','rbc':'Red Blood Cell Count (RBC)','mchc':'Mean corpuscular hemoglobin concentration (MCHC)','lymphocyte percentage':'Lymphocyte Percentage','B-12':'Vitamin B12','25-OH':'Vitamin D','MONOCYTES':'Monocytes','NEUTROPHILS':'Neutrophils','EOSINOPHILS':'Eosinophils','BASOPHILS':'Basophils','PLATELET COUNT':'Platelets'}

dates = ['2018','2020','2022']

iron = [54.7 , 21.82]
hemoglobin = [11.5 , 10.2]
leucocyte = [4.72, 7.54]
rbc = [4.4,4.33]
mchc = [33.2,28.5]
lymphocyte = [43.4,48.8]
b12 = [364, 507]
vitamin_d = [6.13,24.39]
monocytes = [4.0,3.4]
neutrophils = [49,45.8]
eosinophils = [3.2,1.6]
basophils = [0.2,0.1]
platelets = [237,364]

parameters = [iron,hemoglobin,leucocyte,rbc,mchc,lymphocyte,b12,vitamin_d,monocytes,neutrophils,eosinophils,basophils,platelets]

for j in keywords.keys():
    for i in data:
        if j.lower() in i.lower():
            if keywords[j] not in reqd:             # if the keyword is not in the dictionary, add it
                reqd[keywords[j]] = i

parameter_values = {}

iron_l = [50.0,50.0,50.0]
hemoglobin_l = [11.3,11.3,11.3]
leucocyte_l = [5.5,5.5,5.5]
rbc_l = [3.71,3.71,3.71]
mchc_l = [33.9,33.9,33.9]
lymphocyte_l = [8,8,8]
b12_l = [211,211,211]
vitamin_d_l = [30,30,30]
monocytes_l = [4,4,4]
neutrophils_l = [46.4,46.4,46.4]
eosinophils_l = [1,1,1]
basophils_l = [0,0,0]
platelets_l = [192,192,192]

#take the values of higher range from the dictionary and paste thrice into lists
iron_h =[170.0,170.0,170.0]
hemoglobin_h = [13.4,13.4,13.4]
leucocyte_h = [9.3,9.3,9.3]
rbc_h = [4.61,4.61,4.61]
mchc_h = [35.4,35.4,35.4]
lymphocyte_h = [39,39,39]
b12_h = [911,911,911]
vitamin_d_h = [100,100,100]
monocytes_h = [7,7,7]
neutrophils_h = [75.6,75.6,75.6]
eosinophils_h = [3,3,3]
basophils_h = [1,1,1]
platelets_h = [307,307,307]


low_range = {'Iron': 50.0, 'Hemoglobin': 11.3, 'Leucocyte': 5.5, 'Red Blood Cell Count (RBC)': 3.71, 'Mean corpuscular hemoglobin concentration (MCHC)': 33.9, 'Lymphocyte Percentage': 8, 'Vitamin B12': 211, 'Vitamin D': 30, 'MONOCYTES': 4, 'NEUTROPHILS': 46.4, 'EOSINOPHILS': 1, 'BASOPHILS': 0.0, 'PLATELETS': 192}


high_range = {'Iron': 170.0, 'Hemoglobin': 13.4, 'Leucocyte': 9.3, 'Red Blood Cell Count (RBC)': 4.61, 'Mean corpuscular hemoglobin concentration (MCHC)': 35.4, 'Lymphocyte Percentage': 39, 'Vitamin B12': 911, 'Vitamin D': 100, 'MONOCYTES': 7, 'NEUTROPHILS': 75.6, 'EOSINOPHILS': 3, 'BASOPHILS': 1, 'PLATELETS': 307}


for k in reqd.keys():
    i = reqd[k]
#    print(i.split())
    for j in i.split():
        if j != '10³' :
            try:
                if float(j) < 1000:
                    if k not in parameter_values:             # if the keyword is not in the dictionary, add it
                        parameter_values[k]  = float(j)
                        parameters[list(reqd.keys()).index(k)].append(float(j))
            except ValueError:
                pass

# closing the pdf file object
pdfFileObj.close()

para = []

st.image('Osneo_logo_white-font.png')

st.write('Select the parameter')
if st.button('Iron'):
    para = iron 
    lower = iron_l
    higher = iron_h
    label_graph = 'Iron'
    y = "μg/dl" + '\n'
if st.button('Hemoglobin'):   
    para = hemoglobin
    lower = hemoglobin_l
    higher = hemoglobin_h
    label_graph = 'Hemoglobin'
    y = "g/dl" + '\n'
if st.button('Leucocyte'):   
    para = leucocyte
    lower = leucocyte_l
    higher = leucocyte_h
    label_graph = 'Leucocyte'
    y = "10³/μl" + '\n'
if st.button('Red Blood Cell Count (RBC)'):
    para = rbc
    lower = rbc_l
    higher = rbc_h
    label_graph = 'Red Blood Cell Count (RBC)'
    y = "10³/μl" + '\n'
if st.button('Mean corpuscular hemoglobin concentration (MCHC)'):
    para = mchc
    lower = mchc_l
    higher = mchc_h
    label_graph = 'Mean corpuscular hemoglobin concentration (MCHC)'
    y = "g/dl" + '\n'
if st.button('Lymphocyte'):
    para = lymphocyte
    lower = lymphocyte_l
    higher = lymphocyte_h
    label_graph = 'Lymphocyte'
    y = "%" + '\n'
if st.button('Vitamin B-12'):
    para = b12
    lower = b12_l
    higher = b12_h
    label_graph = 'Vitamin B-12'
    y = "pg/ml" + '\n'
if st.button('Vitamin D'):
    para = vitamin_d
    lower = vitamin_d_l
    higher = vitamin_d_h
    label_graph = 'Vitamin D'
    y = "ng/ml" + '\n'
if st.button('Monocytes'):
    para = monocytes
    lower = monocytes_l
    higher = monocytes_h
    label_graph = 'Monocytes'
    y = "%" + '\n'
if st.button('Neutrophils'):
    para = neutrophils
    lower = neutrophils_l
    higher = neutrophils_h
    label_graph = 'Neutrophils'
    y = "%" + '\n'
if st.button('Eosinophils'):
    para = eosinophils
    lower = eosinophils_l
    higher = eosinophils_h
    label_graph = 'Eosinophils'
    y = "%" + '\n'
if st.button('Basophils'):
    para = basophils
    lower = basophils_l
    higher = basophils_h
    label_graph = 'Basophils'
    y = "%" + '\n'
if st.button('Platelets'):
    para = platelets
    lower = platelets_l
    higher = platelets_h
    label_graph = 'Platelets'
    y = "10³/μl" + "\n"

if para != []:
    plt.style.use('dark_background')
    plt.plot(dates,para,label = label_graph)
    plt.scatter(dates,para)
    plt.plot(dates,lower,label='Lower Range')
    plt.plot(dates,higher,label='Higher Range')
    plt.xlabel("\nDate")
    plt.ylabel(y)
    plt.title('\n' + label_graph + ' Graph\n')
    st.pyplot(plt.show())