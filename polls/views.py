import urllib.request
import time
import json
import requests
from django.shortcuts import render
import pandas as pd
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response


def index(request):

    return render(request, './index.html')


def cloth(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\패션의류_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/cloth.html', context)


def sports(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\스포츠_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/sports.html', context)


def cosmetics(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\화장품_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/cosmetics.html', context)


def fasioncloth(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\패션의류_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/fasioncloth.html', context)


def fasionitem(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\패션잡화_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/fasionitem.html', context)


def living(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\생활_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/living.html', context)


def baby(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\출산_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/baby.html', context)


def interior(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\인테리어_Scout_Filltered.csv')
    scoutComp = scoutComp.sort_values(by='경쟁량', ascending=True)
    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/interior.html', context)


def digital(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\디지털_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/digital.html', context)


def food(request):
    scoutComp = pd.read_csv(
        'D:\\dataBase\\categoryComp\\식품_Scout_Filltered.csv')

    scoutComp = scoutComp.values.tolist()
    context = {'scoutComp': scoutComp}
    return render(request, './category/food.html', context)


def post(request):
    category = request.POST['some_key1']
    print(category)

    name_array = []
    pc_bid_array = []
    mobile_bid_array = []
    prdCnt_array = []
    total_array = []
    average_array = []

    df = pd.read_csv('D:\\dataBase\\scoutShowme\\category.csv')
    df = df.values.tolist()

    # print(df)
    for li in df:
        try:

            if category[-1] == '/':
                category = category[:-1]

            if category == li[0]:

                category = li[-1]
            if category == '주방용품>냄비/솥>전자레인지/오븐':

                category = 4381

        except:
            continue

    conclusion = []
    duration_dict = {
        "duration": '30d',
        "genders": "f,m",
        "ages": "10,20,30,40"
    }
    print(category)
    json_trans = json.dumps(duration_dict)
    r = requests.post('https://api.itemscout.io/api/category/'+str(category)+'/data',
                      data=duration_dict)

    key_id = json.loads(r.text)
    print(category)
    # print(key_id)
    print(key_id)
    array = key_id['data']['data']
    i = 1
    json_key = []
    for li in array:
        json_key.append(li)
    # key_id = json.dumps(array)
    # print(key_id[0])

    for al in json_key:
        li = array[al]
        try:

            # if category != li['firstCategory']:
            #     continue
            name = li['keyword']
            bid = li['bid']
            pc_bid = bid['pc_bid']
            mobile_bid = bid['mobile_bid']
            prdCnt = li['prdCnt']
            monthly = li['monthly']
            total = monthly['total']
            average = prdCnt/total
            name_array.append(name)
            pc_bid_array.append(pc_bid)
            mobile_bid_array.append(mobile_bid)
            total_array.append(total)
            average = round(average, 2)
            average_array.append(average)
            prdCnt_array.append(prdCnt)

        # print(li['prdCnt'])
        # print(clicka['total'])
        # print(li['bid'])
        except:
            continue
    data = pd.DataFrame({
        '이름': name_array,
        '검색량': total_array,
        '상품량': prdCnt_array,
        '경쟁량': average_array,
        'pc단가': pc_bid_array,
        '모바일단가': mobile_bid_array
    })

    scout_pan = data.sort_values(by='검색량', ascending=False)
    scout_list = scout_pan.values.tolist()
    context = {'scout_list': scout_list}

    return render(request, './post.html', context)


@api_view(['POST'])
def transe(request):
    srcText = request.data
    client_id = "j6V6dD6f1YCjncBEOBas"
    client_secret = "9E9BIJvIQ5"
    trantext_list = []
    encText = urllib.parse.quote(srcText)
########################### ch ####################################
    data = "source=ko&target=zh-CN&text=" + encText

    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(
        request, data=data.encode("utf-8"))
    rescode = response.getcode()
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    # json 형 변환
    res = json.loads(response_body.decode('utf-8'))
    res = res['message']
    res = res['result']
    chtr = res['translatedText']
    trantext_list.append(chtr)
########################### en ####################################
    data = "source=ko&target=en&text=" + encText

    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(
        request, data=data.encode("utf-8"))
    rescode = response.getcode()
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    # json 형 변환
    res = json.loads(response_body.decode('utf-8'))

    res = res['message']
    res = res['result']
    entr = res['translatedText']
    trantext_list.append(entr)
########################### ja ####################################
    data = "source=ko&target=ja&text=" + encText

    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(
        request, data=data.encode("utf-8"))
    rescode = response.getcode()
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    # json 형 변환
    res = json.loads(response_body.decode('utf-8'))

    res = res['message']
    res = res['result']
    jatr = res['translatedText']
    trantext_list.append(jatr)
    print(trantext_list)
    return Response(trantext_list)
