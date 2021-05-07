# def index(request):
#     occupationListCount,occupationList=pre_process.occupation()
#     educationListCount, educationList = pre_process.education()
#     sexListCount, sexList = pre_process.sex()
#     ageListCount,ageList=pre_process.age()
#     return render(request, 'index.html',{
#         'occupationList':json.dumps(occupationList),
#         'occupationListCount':json.dumps(occupationListCount),
#         'educationList':json.dumps(educationList),
#         'educationListCount':json.dumps(educationListCount),
#         'sexList':json.dumps(sexList),
#         'sexListCount':json.dumps(sexListCount),
#         'ageList':ageList,
#         'ageListCount':ageListCount,
        
#     })
from django.shortcuts import render
import json
from analysisapp.forms import upload_file_form
from analysisapp.file_upload.file_upload_handling import handle_upload_file
from django.http import HttpResponseRedirect

#from analysisapp.working_code2 import pre_process as prep
from analysisapp.working_code2 import pre_process
import pandas as pd 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
import pickle
# Create your views here.
# from analysisapp.working_code.cleaning import clean_data
# from analysisapp.working_code.createDatabase import create_database_excel


# def splash(request):
#     create_database_excel(100, 175)
#     clean_data()
#     return render(request, 'splash-screen.html')

    
df = pd.read_csv('dataset.csv')

def count(column1,values):
    
    valuecount=[]
    for each in values:
        c=0
        for ind in df.index: 

            if df[column1][ind]==each:
                c=c+1
        valuecount.append(c)
      
    return valuecount,values

def total_claim_count(column):

    valuecount=[]

    for i in range(0,601,100):
        c=0
        for ind in df.index:

            if df[column][ind]>=i and df[column][ind]<i+100:
                c+=1

        valuecount.append(c)
    return valuecount

def supplier_count():

    valuecount=[]
    for i in range(0,121,20):
        print (i)
        c=len(df[(i<df['Number of Suppliers_mean']) & (df['Number of Suppliers_mean']<i+20)])
        valuecount.append(c)
    return valuecount

def  supplier_beneficiaries():

    valuecount=[]
    for i in range(0,901,100):
        c=len(df[(i<df['Number of Supplier Beneficiaries_mean']) & (df['Number of Supplier Beneficiaries_mean']<i+100)])
        valuecount.append(c)
    return valuecount

def supplier_claims():
    valuecount=[]
    for i in range(0,2001,500):
        c=len(df[(i<df['Number of Supplier Claims_mean']) & (df['Number of Supplier Claims_mean']<i+500)])
        valuecount.append(c)
    return valuecount

def supplier_services():
    valuecount=[]
    for i in range(0,180001,30000): 
        c=len(df[(i<df['Number of Supplier Services_mean']) & (df['Number of Supplier Services_mean']<i+30000)])
        valuecount.append(c)
    return valuecount

def index(request):
    average_dc=str(int(df['total_drug_cost_mean'].mean()))+' $'
    average_sc=str(int(df[ 'Average Submitted Charge Amount_mean'].mean()))+' $'
    average_mc=str(int(df['Average Medicare Payment Amount_mean'].mean()))+' $'
    average_mb=int(df['Number of Medicare Beneficiaries_mean'].mean())

    noofsuppliersList=["0-20","20-40","40-60","60-80","80-100","100-120"]
    noofsuppliersListCount=supplier_count()

    supbenList=['0-100', '100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800', '800-900', '900-1000']
    supbenListCount=supplier_beneficiaries()

    supclaList=['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500']
    supclaListCount=supplier_claims()

    supserList=['0-30000', '30000-60000', '60000-90000', '90000-120000', '120000-150000', '150000-180000']
    supserListCount=supplier_services()


    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        dataframe=pd.read_csv(os.path.join(settings.MEDIA_ROOT,filename))
    
        final_model=pickle.load(open('finalized_model.sav','rb'))
        to_model_columns=dataframe.columns[2:98]
        prediction = final_model.predict(dataframe[to_model_columns])
        pred=[]
        for each in prediction:
            if each==-1:
                pred.append("Fraud")
            else:
                pred.append("Not Fraud")

        npivalues=list(dataframe['npi'])
        n=len(pred)
        return render(request, 'index.html',{'npivalues':npivalues,'prediction':pred,'n':list(range(n)),'dc':average_dc,
            'sc':average_sc,
            'mc':average_mc,
            'mb':average_mb,
            'noofsuppliersList':json.dumps(noofsuppliersList),
            'noofsuppliersListCount':json.dumps(noofsuppliersListCount),
            'supbenList':json.dumps(supbenList),
            'supbenListCount':json.dumps(supbenListCount),
            'supclaList':json.dumps(supclaList),
            'supclaListCount':json.dumps(supclaListCount),
            'supserList':json.dumps(supserList),
            'supserListCount':json.dumps(supserListCount),
        })
    return render(request, 'index.html',{
        'dc':average_dc,
        'sc':average_sc,
        'mc':average_mc,
        'mb':average_mb,
        'noofsuppliersList':json.dumps(noofsuppliersList),
        'noofsuppliersListCount':json.dumps(noofsuppliersListCount),
        'supbenList':json.dumps(supbenList),
        'supbenListCount':json.dumps(supbenListCount),
        'supclaList':json.dumps(supclaList),
        'supclaListCount':json.dumps(supclaListCount),
        'supserList':json.dumps(supserList),
        'supserListCount':json.dumps(supserListCount),
    })
    

def start(request):
    return render(request, 'start.html')

# def table(request):
#     return render(request, 'data-tables.html')

def Maps(request):
         lat_long=pre_process.maps()
         print(lat_long)
         # print(json.dumps(lat_long))
         return render(request, 'map-vector.html',{
             'lat_long':json.dumps(lat_long,indent=2,sort_keys=True)
         })

def charts(request):

    # pre_process.load_data()
    
    
    
    values=sorted(list(df['Age'].unique()))
    ageListCount,ageList = count('Age',values)

    values=list(df['specialty_description'].unique())
    specialityListCount,specialityList=count('specialty_description',values)

    values=list(df['Gender'].unique())
    sexListCount,sexList=count('Gender',values)

    totalclaimcountList=["0-99","100-199","200-299","300-399","400-499","500-599","600-699"]
    totalclaimcountListCount=total_claim_count('total_claim_count_mean')

    # print(occupationListCount,occupationList)
    return render(request, 'chart-charts.html',{
        'specialityList':json.dumps(specialityList),
        'specialityListCount':json.dumps(specialityListCount),
        'totalclaimcountList':json.dumps(totalclaimcountList),
        'totalclaimcountListCount':json.dumps(totalclaimcountListCount),
        'sexList':json.dumps(sexList),
        'sexListCount':json.dumps(sexListCount),
        'ageList':ageList,
        'ageListCount':ageListCount,

    })
# #    pre_process.read_data()
#  #   occupationList,occupationListCount=pre_process.occupation()
#
#
#
#
#     return render(request, 'chart-charts.html',{
#         'occupationList':json.dumps(occupationList),
#         'occupationListCount':json.dumps(occupationListCount)
#
#     })

def charts2(request):

    pre_process.get_data()
    accuracy_headers, accuracy = pre_process.analysis_accuracy()
    print(accuracy_headers, accuracy)

    ogLabel = ["Original Data-Not Fraud", "Original Data-Fraud"]
    preLabel = ["Predicted Data-Not Fraud", "Predicted Data-Fraud"]
    original_count, predicted_count = pre_process.analysis_chart_data()
    print("sds", original_count, predicted_count)

    return render(request, 'chart-morris.html',{
        'accuracy_headers':json.dumps(accuracy_headers),
        'accuracy':json.dumps(accuracy),
        'original_count': json.dumps(original_count),
        'predicted_count':json.dumps(predicted_count),
        'ogLabel':json.dumps(ogLabel),
        'preLabel':json.dumps(preLabel)
    })
def table(request):
    data=pre_process.tableData()
    return render(request,'data-tables.html',{
        'data':data,
        'range':range(200)
    })

def morris(request):
    # data=[
    #     ['Credit','Debit','Value'],
    #     [12,30,20],
    # ]
    # data_source=SimpleDataSource(data=data)
    # chart=DonutChart(data_source)
    # context={'chart':chart}
    return render(request, 'chart-morris.html')


def fileforms(request):
    form = upload_file_form()

    # if request.method == "POST":
    #     form = upload_file_form(request.POST, request.FILES)
    #
    #     if form.is_valid():
    #         handle_upload_file(request.FILES['file'])
    #         return HttpResponseRedirect('success.html')
    #     # else:
    #     #     form = upload_file_form()
    #     #     return render(request, 'forms.html', {'form': form})

    return render(request, 'forms.html', context={'form':form})