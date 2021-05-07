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
from django.shortcuts import redirect
import json
from analysisapp.forms import upload_file_form,claim_form
from analysisapp.file_upload.file_upload_handling import handle_upload_file
from django.http import HttpResponseRedirect
import csv
from django.http import StreamingHttpResponse
from analysisapp.models import Data

#from analysisapp.working_code2 import pre_process as prep
from analysisapp.working_code2 import pre_process
import pandas as pd 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
import pickle
from django.urls import reverse
from login.models import CustomUser
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
    for i in range(0,101,20):
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
    for i in range(0,150001,30000): 
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
    noofsuppliersListCount.reverse()
    supbenList=['0-100', '100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800', '800-900', '900-1000']
    supbenListCount=supplier_beneficiaries()
    supbenListCount.reverse()
    supclaList=['0-500', '500-1000', '1000-1500', '1500-2000', '2000-2500']
    supclaListCount=supplier_claims()
    supclaListCount.reverse()
    supserList=['0-30000', '30000-60000', '60000-90000', '90000-120000', '120000-150000', '150000-180000']
    supserListCount=supplier_services()
    supserListCount.reverse()


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
                pred.append("Suspicious")
            else:
                pred.append("Not Suspicious")

        npivalues=list(dataframe['npi'])
        claimid=list(dataframe['claimid'])
        n=len(pred)
        return render(request, 'index.html',{'claimid':claimid,'npivalues':npivalues,'prediction':pred,'n':list(range(n)),'dc':average_dc,
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
    totalclaimcountListCount.reverse()

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

class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def submit_claim(request):
    form = claim_form()
    if request.method =='POST':
        form = claim_form(request.POST)
        if form.is_valid():
            #npi = int(request.POST.get("provider_id"))
            submitted_amount =  int(request.POST.get("submitted_amount"))
            amount_to_be_paid_by_medicare = int(request.POST.get("amount_to_be_paid_by_medicare"))
            supplier_submitted_charges = int(request.POST.get("supplier_submitted_charges"))
            supplier_medicare_amount = int(request.POST.get("supplier_medicare_amount"))
            #claim_id = request.POST.get("claim_id")
            specialty_description = request.POST.get("speciality_description")
            npi=int(request.user.npi)
            print(npi)
            print(specialty_description)

            df2 = pd.read_csv('check.csv')
            df1=pd.read_csv('labelled.csv')
            temp = df1[(df1['npi']==npi) & (df1['specialty_description']==specialty_description)]

            #print(temp['Average_Supplier_Submitted_Charge_median'])
            #
            print(temp)
            d=Data(npi=npi)
            d.specialty_description=specialty_description 
            #print(type(temp.get(key='bene_count_mean')))
            d.bene_count_mean=temp['bene_count_mean'].values[0]
            d.bene_count_min=temp['bene_count_min'].values[0]
            d.bene_count_max=temp['bene_count_max'].values[0]
           
            d. bene_count_sum =temp['bene_count_sum'].values[0]+1
            d. bene_count_median =temp['bene_count_median'].values[0]
            d. bene_count_std =temp['bene_count_std'].values[0]
            d. total_claim_count_mean =temp['total_claim_count_mean'].values[0]
            d. total_claim_count_min =temp['total_claim_count_min'].values[0]
            d. total_claim_count_max =temp['total_claim_count_max'].values[0]
            d. total_claim_count_sum =temp['total_claim_count_sum'].values[0]
            d. total_claim_count_median =temp['total_claim_count_median'].values[0]
            d. total_claim_count_std =temp['total_claim_count_std'].values[0]
            d. total_30_day_fill_count_mean =temp['total_30_day_fill_count_mean'].values[0]
            d. total_30_day_fill_count_min =temp['total_30_day_fill_count_min'].values[0]
            d. total_30_day_fill_count_max =temp['total_30_day_fill_count_max'].values[0]
            d. total_30_day_fill_count_sum =temp['total_30_day_fill_count_sum'].values[0]
            d. total_30_day_fill_count_median =temp['total_30_day_fill_count_median'].values[0]
            d. total_30_day_fill_count_std =temp['total_30_day_fill_count_std'].values[0]
            d. total_day_supply_mean =temp['total_day_supply_mean'].values[0]
            d. total_day_supply_min =temp['total_day_supply_min'].values[0]
            d. total_day_supply_max =temp['total_day_supply_max'].values[0]
            d. total_day_supply_sum =temp['total_day_supply_sum'].values[0]
            d. total_day_supply_median =temp['total_day_supply_median'].values[0]
            d. total_day_supply_std =temp['total_day_supply_std'].values[0]
            d. total_drug_cost_mean =temp['total_drug_cost_mean'].values[0]
            d. total_drug_cost_min =temp['total_drug_cost_min'].values[0]
            d. total_drug_cost_max =temp['total_drug_cost_max'].values[0]
            d. total_drug_cost_sum =temp['total_drug_cost_sum'].values[0]
            d. total_drug_cost_median =temp['total_drug_cost_median'].values[0]
            d. total_drug_cost_std =temp['total_drug_cost_std'].values[0]
            d. Number_of_Services_mean =temp['Number_of_Services_mean'].values[0]
            d. Number_of_Services_min =temp['Number_of_Services_min'].values[0]
            d. Number_of_Services_max =temp['Number_of_Services_max'].values[0]
            d. Number_of_Services_sum =temp['Number_of_Services_sum'].values[0]
            d. Number_of_Services_median =temp['Number_of_Services_median'].values[0]
            d. Number_of_Services_std =temp['Number_of_Services_std'].values[0]
            d. Number_of_Medicare_Beneficiaries_mean =temp['Number_of_Medicare_Beneficiaries_mean'].values[0]
            d. Number_of_Medicare_Beneficiaries_min =temp['Number_of_Medicare_Beneficiaries_min'].values[0]
            d. Number_of_Medicare_Beneficiaries_max =temp['Number_of_Medicare_Beneficiaries_max'].values[0]
            d. Number_of_Medicare_Beneficiaries_sum =temp['Number_of_Medicare_Beneficiaries_sum'].values[0]
            d. Number_of_Medicare_Beneficiaries_median =temp['Number_of_Medicare_Beneficiaries_median'].values[0]
            d. Number_of_Medicare_Beneficiaries_std =temp['Number_of_Medicare_Beneficiaries_std'].values[0]
            d. Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_mean =temp['Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_mean'].values[0]
            d. Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_min =temp['Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_min'].values[0]
            d. Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_max =temp['Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_max'].values[0]
            d. Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_sum =temp['Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_sum'].values[0]
            d. Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_median =temp['Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_median'].values[0]
            d. Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_std =temp['Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_std'].values[0]
            d. Average_Submitted_Charge_Amount_mean =temp['Average_Submitted_Charge_Amount_mean'].values[0]
            d. Average_Submitted_Charge_Amount_min =temp['Average_Submitted_Charge_Amount_min'].values[0]
            d. Average_Submitted_Charge_Amount_max =temp['Average_Submitted_Charge_Amount_max'].values[0]
            d. Average_Submitted_Charge_Amount_sum =temp['Average_Submitted_Charge_Amount_sum'].values[0]+submitted_amount
            d. Average_Submitted_Charge_Amount_median =temp['Average_Submitted_Charge_Amount_median'].values[0]
            d. Average_Submitted_Charge_Amount_std =temp['Average_Submitted_Charge_Amount_std'].values[0]
            d. Average_Medicare_Payment_Amount_mean =temp['Average_Medicare_Payment_Amount_mean'].values[0]
            d. Average_Medicare_Payment_Amount_min =temp['Average_Medicare_Payment_Amount_min'].values[0]
            d. Average_Medicare_Payment_Amount_max =temp['Average_Medicare_Payment_Amount_max'].values[0]
            d. Average_Medicare_Payment_Amount_sum =temp['Average_Medicare_Payment_Amount_sum'].values[0]+amount_to_be_paid_by_medicare
            d. Average_Medicare_Payment_Amount_median =temp['Average_Medicare_Payment_Amount_median'].values[0]
            d. Average_Medicare_Payment_Amount_std =temp['Average_Medicare_Payment_Amount_std'].values[0]
            d. Number_of_Suppliers_mean =temp['Number_of_Suppliers_mean'].values[0]
            d. Number_of_Suppliers_min =temp['Number_of_Suppliers_min'].values[0]
            d. Number_of_Suppliers_max =temp['Number_of_Suppliers_max'].values[0]
            d. Number_of_Suppliers_sum =temp['Number_of_Suppliers_sum'].values[0]
            d. Number_of_Suppliers_median =temp['Number_of_Suppliers_median'].values[0]
            d. Number_of_Suppliers_std =temp['Number_of_Suppliers_std'].values[0]
            d. Number_of_Supplier_Beneficiaries_mean =temp['Number_of_Supplier_Beneficiaries_mean'].values[0]
            d. Number_of_Supplier_Beneficiaries_min =temp['Number_of_Supplier_Beneficiaries_min'].values[0]
            d. Number_of_Supplier_Beneficiaries_max =temp['Number_of_Supplier_Beneficiaries_max'].values[0]
            d. Number_of_Supplier_Beneficiaries_sum =temp['Number_of_Supplier_Beneficiaries_sum'].values[0]
            d. Number_of_Supplier_Beneficiaries_median =temp['Number_of_Supplier_Beneficiaries_median'].values[0]
            d. Number_of_Supplier_Beneficiaries_std =temp['Number_of_Supplier_Beneficiaries_std'].values[0]
            d. Number_of_Supplier_Claims_mean =temp['Number_of_Supplier_Claims_mean'].values[0]
            d. Number_of_Supplier_Claims_min =temp['Number_of_Supplier_Claims_min'].values[0]
            d. Number_of_Supplier_Claims_max =temp['Number_of_Supplier_Claims_max'].values[0]
            d. Number_of_Supplier_Claims_sum =temp['Number_of_Supplier_Claims_sum'].values[0]
            d. Number_of_Supplier_Claims_median =temp['Number_of_Supplier_Claims_median'].values[0]
            d. Number_of_Supplier_Claims_std =temp['Number_of_Supplier_Claims_std'].values[0]
            d. Number_of_Supplier_Services_mean =temp['Number_of_Supplier_Services_mean'].values[0]
            d. Number_of_Supplier_Services_min =temp['Number_of_Supplier_Services_min'].values[0]
            d. Number_of_Supplier_Services_max =temp['Number_of_Supplier_Services_max'].values[0]
            d. Number_of_Supplier_Services_sum =temp['Number_of_Supplier_Services_sum'].values[0]
            d. Number_of_Supplier_Services_median =temp['Number_of_Supplier_Services_median'].values[0]
            d. Number_of_Supplier_Services_std =temp['Number_of_Supplier_Services_std'].values[0]
            d. Average_Supplier_Submitted_Charge_mean =temp['Average_Supplier_Submitted_Charge_mean'].values[0]
            d. Average_Supplier_Submitted_Charge_min =temp['Average_Supplier_Submitted_Charge_min'].values[0]
            d. Average_Supplier_Submitted_Charge_max =temp['Average_Supplier_Submitted_Charge_max'].values[0]
            d. Average_Supplier_Submitted_Charge_sum =temp['Average_Supplier_Submitted_Charge_sum'].values[0]+supplier_submitted_charges
            d. Average_Supplier_Submitted_Charge_median =temp['Average_Supplier_Submitted_Charge_median'].values[0]
            d. Average_Supplier_Submitted_Charge_std =temp['Average_Supplier_Submitted_Charge_std'].values[0]
            d. Average_Supplier_Medicare_Payment_Amount_mean =temp['Average_Supplier_Medicare_Payment_Amount_mean'].values[0]
            d. Average_Supplier_Medicare_Payment_Amount_min =temp['Average_Supplier_Medicare_Payment_Amount_min'].values[0]
            d. Average_Supplier_Medicare_Payment_Amount_max =temp['Average_Supplier_Medicare_Payment_Amount_max'].values[0]
            d. Average_Supplier_Medicare_Payment_Amount_sum =temp['Average_Supplier_Medicare_Payment_Amount_sum'].values[0]+supplier_medicare_amount
            d. Average_Supplier_Medicare_Payment_Amount_median =temp['Average_Supplier_Medicare_Payment_Amount_median'].values[0]
            d. Average_Supplier_Medicare_Payment_Amount_std =temp['Average_Supplier_Medicare_Payment_Amount_std'].values[0]
            #d.claimid=claim_id
           
            temp['bene_count_sum']=temp['bene_count_sum']+1
            temp['Average_Medicare_Payment_Amount_sum'] = temp['Average_Medicare_Payment_Amount_sum']+amount_to_be_paid_by_medicare
            temp['Average_Supplier_Medicare_Payment_Amount_sum'] = temp['Average_Supplier_Medicare_Payment_Amount_sum']+ supplier_medicare_amount
            temp['Average_Supplier_Submitted_Charge_sum']= temp['Average_Supplier_Submitted_Charge_sum'] + supplier_submitted_charges
            temp['Average_Submitted_Charge_Amount_sum']= temp['Average_Submitted_Charge_Amount_sum'] + submitted_amount
            #p=Data.objects.latest('claimid')
            #temp['claimid']=int(p.claimid)+1
            temp['claimid']=0
            temp.drop(labels=['label_final','anomaly'], axis =1, inplace= True)

            final_model=pickle.load(open('finalized_model.sav','rb'))
            to_model_columns=temp.columns[2:98]
            prediction = final_model.predict(temp[to_model_columns])
            print(prediction)
            # df2 = df2.append(temp) 
            # df2.to_csv(r'C:\be project\Secure-Health-Insurance-master\check.csv', index =False)

            for each in prediction:
                if each==-1:
                    d.label="suspicious"
                else:
                    d.label="notsuspicious"

            d.save()
            l=Data.objects.latest('claimid')

            return render(request,'claim_successful.html',{'claim_id':l.claimid})
    else:
        return render(request,'submit_claim.html',{'form':form})


def provider(request):
    name = request.user.name
    context = {'name':name}
    return render(request, 'provider.html', context)

def status(request):
    table = (Data.objects.filter(npi =request.user.npi)).order_by('claimid')
    context = {'table': table }	
    return render(request,'status.html',context)

def docver(request, i):	
    Data.objects.filter(claimid=i).update(documentver='D')
    # context ={ 'i' : i}
    # return render(request, 'docver.html', context)
    # return HttpResponseRedirect(reverse('analysisapp:status'))
    return redirect("http://127.0.0.1:8005/")


def docverdone(request,i):

	Data.objects.filter(claimid=i).update(documentver='D')

	return HttpResponseRedirect(reverse('analysisapp:status'))

def claimapprove(request):
    table = (Data.objects.filter(label = 'suspicious').filter(documentver__in = ['ND','D'])).order_by('claimid')
    context = {'table': table}
    return render(request, 'claimapprove.html', context)

def approval(request,i,s):
    if s == 'A':
        Data.objects.filter(claimid=i).update(documentver='A')
    else:
        Data.objects.filter(claimid=i).update(documentver='R') 
    return HttpResponseRedirect(reverse('analysisapp:claimapprove'))