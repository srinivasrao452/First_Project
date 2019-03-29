from django.shortcuts import render
from django.http import HttpResponse

# view 1
def Emp_Data_FBV(request):
    emp_data = {
        'eno' : 100,
        'ename' :'Ramu',
        'esal' : 10000,
        'eaddr' : 'Hyd'
    }

    resp = "<h1>Employee Number :{}<br> Employee Name :{}<br> Employee Salary :{}<br> Employee Address :{}</h1> ".format(
      emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr']
    )

    return HttpResponse(resp)


#view 2
import json
def JsonData_View(request):
    emp_data = {
        'eno' : 200,
        'ename' : "Srinivas",
        'esal' : 20000,
        'eaddr' : 'Mumbai'
    }
    resp = json.dumps(emp_data)
    return HttpResponse(resp)


from django.http import JsonResponse
def JsonResponseData_View(request):
    emp_data = {
        'eno': 300,
        'ename': "Virat",
        'esal': 30000,
        'eaddr': 'Delhi'
    }

    return JsonResponse(emp_data)






# Create your views here.
# def c(request):
#     emp_data = {
#         'eno' : 100,
#         'ename' : 'Srinivas',
#         'esal' : 10000,
#         'eaddr' : 'Hyd'
#     }
#     resp = "Emploee Number : {} Emploee Name : {} Emploee Number : {} Emploee Number : {}".format(
#         emp_data['eno'] ,emp_data['ename'],emp_data['esal'],emp_data['eaddr']
#     )
#
#     return HttpResponse(resp)

#
# import json
# def JsonResponse(request):
#     emp_data = {
#         'eno' : 200 ,
#         'ename' : 'Virat' ,
#         'esal' : 20000,
#         'eaddr' : 'Pune'
#     }
#     json_data = json.dumps(emp_data)
#     return HttpResponse(json_data , content_type='application/json')
#
#
#
# def JsonResponse2(request):
#     emp_data = {
#         'eno': 300,
#         'ename': 'Rohit',
#         'esal': 30000,
#         'eaddr': 'Mumbai'
#     }
#     return JsonResponse(emp_data)
