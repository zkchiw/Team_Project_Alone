import json

import stringify as stringify
from django.db.models import Count

from schedule.models import Cal
from django.shortcuts import render
from django.views import View


class ScheduleView(View):

    def get(self, request):

        form = request.GET.dict()
        print(form)
        cal = Cal.objects.all()
        cal = list(cal.values())    # 쿼리셋을 리스트 형태로 변환(json)
        cal2 = json.dumps(cal)
        # print(cal2)



        date = Cal.objects.filter(regdate='2022.07.02')
        date = Cal.objects.values()

        # for i in cal:
        #     print(i)

        date1 = list(date.values())
        date2 = json.dumps(date1)
        date3 = date2.split(':')[6] # 날짜 출력은 6의 배수 (12,18,24...)
        date4 = date3.split('}')[0]

        # cal의 데이터 갯수는 총 30개, len함수를 이용하니 총 데이터만큼의 count를 세어준다.
        # 이걸로 반복문 for i in range에서 range부분을 len(cal)을 이용해서 해결 가능할지도
        infoo = len(cal)
        # print(infoo)

        # 날짜 출력
        # print(date4)

        time = date2.split(',')[1]  # 시간은 1로 시작해서 5만큼 증가한다(1,6,11,16...)
        time2 = time.split('"')[3]

        # print(time2)

        gudan1 = date2.split(':')[4] # 구단1은 4로 시작해서 6만큼 증가(4,10,16,22..)
        gudan2 = gudan1.split(',')[0]

        # 구단1 출력
        # print(gudan2)

        gudan3 = date2.split(':')[5] # 구단2는 5로 시작해서 6만큼 증가 (5,11,17,23...)
        gudan4 = gudan3.split(',')[0]

        # 구단2 출력
        # print(gudan4)

        global context
        context = {}
        # 검색 기능을 이용해서 form을 억지로 넘겨주면 searchkey를 통해 검색할수 있다.


        try:
            if form['keyword'] == 'regdate' and form['searchkey'] =='2022.07.02':
                date = Cal.objects.filter(regdate=form['searchkey'])

                # 값이 넘어오는 것을 확인
                dateall = list(date.values())
                dateall = json.dumps(dateall)
                # print(dateall)

                dateall_01 = dateall.split(':')[6]  # 날짜 출력은 6의 배수 (12,18,24...)
                dateall_01 = dateall_01.split('}')[0]
                dateall_02 = dateall.split(':')[12]
                dateall_02 = dateall_02.split('}')[0]
                dateall_03 = dateall.split(':')[18]
                dateall_03 = dateall_03.split('}')[0]
                dateall_04 = dateall.split(':')[24]
                dateall_04 = dateall_04.split('}')[0]
                dateall_05 = dateall.split(':')[30]
                dateall_05 = dateall_05.split('}')[0]
                dateall_06 = dateall.split(':')[36]
                dateall_06 = dateall_06.split('}')[0]

                time_01 = date2.split(',')[1]  # 시간은 1로 시작해서 5만큼 증가한다(1,6,11,16...)
                time_01 = time_01.split('"')[3]
                time_02 = date2.split(',')[6]
                time_02 = time_02.split('"')[3]
                time_03 = date2.split(',')[11]
                time_03 = time_03.split('"')[3]
                time_04 = date2.split(',')[16]
                time_04 = time_04.split('"')[3]
                time_05 = date2.split(',')[21]
                time_05 = time_05.split('"')[3]
                time_06 = date2.split(',')[26]
                time_06 = time_06.split('"')[3]

                gudan_01 = date2.split(':')[4]  # 구단1은 4로 시작해서 6만큼 증가(4,10,16,22..)
                gudan_01 = gudan_01.split(',')[0]
                gudan_02 = date2.split(':')[10]
                gudan_02 = gudan_02.split(',')[0]
                gudan_03 = date2.split(':')[16]
                gudan_03 = gudan_03.split(',')[0]
                gudan_04 = date2.split(':')[22]
                gudan_04 = gudan_04.split(',')[0]
                gudan_05 = date2.split(':')[28]
                gudan_05 = gudan_05.split(',')[0]
                gudan_06 = date2.split(':')[34]
                gudan_06 = gudan_06.split(',')[0]

                gudan_11 = date2.split(':')[5]  # 구단2는 5로 시작해서 6만큼 증가 (5,11,17,23...)
                gudan_11 = gudan_11.split(',')[0]
                gudan_22 = date2.split(':')[11]
                gudan_22 = gudan_22.split(',')[0]
                gudan_33 = date2.split(':')[17]
                gudan_33 = gudan_33.split(',')[0]
                gudan_44 = date2.split(':')[23]
                gudan_44 = gudan_44.split(',')[0]
                gudan_55 = date2.split(':')[29]
                gudan_55 = gudan_55.split(',')[0]
                gudan_66 = date2.split(':')[35]
                gudan_66 = gudan_66.split(',')[0]


                # 어쨌든 날짜는 제대로 출력되는 것을 확인, 값을 context에 담아서 여러개 넘겨버리자.
                # 어차피 경기가 가장 많은 날도 6경기가 끝이라서... 근데 이러면 날짜만 해도 30줄 가까이되고 4개값 들어가면 120줄, 열흘치 들어가면 코드가 1200줄인데?
                # for 반복문을 이용해서 코드를 줄이고 싶지만 searchkey는 검색조건이라서 반복문을 못쓴다. 하루에 70줄가까이 들어갔으니 열흘만 해도 700줄.
                # 역설적이지만, 페이지 11개 생성하는게 가장 빨랐다고 느끼는 중...

                context = {'date_01':dateall_01,'date_02':dateall_02,'date_03':dateall_03,'date_04':dateall_04,'date_05':dateall_05,'date_06':dateall_06,
                           'time_01':time_01,'time_02':time_02,'time_03':time_03,'time_04':time_04,'time_05':time_05,'time_06':time_06,
                           'gudan_01':gudan_01,'gudan_02':gudan_02,'gudan_03':gudan_03,'gudan_04':gudan_04,'gudan_05':gudan_05,'gudan_06':gudan_06,
                           'gudan_11':gudan_11,'gudan_22':gudan_22,'gudan_33':gudan_33,'gudan_44':gudan_44,'gudan_55':gudan_55,'gudan_66':gudan_66}
        except:
                return render(request, 'schedule.html', context)

        context = {'date': date4, 'time':time2, 'gudan1':gudan2, 'gudan2':gudan4}
        return render(request, 'schedule.html', context)

        # 규칙성 자체는 찾았다. get방식을 쓰지만 form에는 데이터가 들어가지 않는다.(입력하지 않았으니)
        # 날짜 조건을 걸고 하나하나 objects.filter를 걸려면 날짜만 10번을 반복해야 한다.
        # 각 조건들의 규칙성 자체는 찾았으니까 차라리 objects.all로 모든 데이터를 가져온 뒤에
        # 구문을 작성하는게 차라리 나을지도 모르겠다. 하지만 split(':')[4]같은 형식의 구문에서
        # 뒤에 있는 [4]를 [4+6n]형식으로 반복문을 작성해줘야 하는데 이게 과연 가능할까?
        # 그리고 n이라는 수는 어떻게 잡아서 걸어줄 것인지도

    def post(self, request):
        pass

class JulyView(View):
    def get(self, request):
            return render(request, 'calender/july_all.html')
class JulyView02(View):
    def get(self, request):
            return render(request, 'calender/july_02.html')
class JulyView03(View):
    def get(self, request):
            return render(request, 'calender/july_03.html')
class JulyView05(View):
    def get(self, request):
            return render(request, 'calender/july_05.html')
class JulyView06(View):
    def get(self, request):
            return render(request, 'calender/july_06.html')
class JulyView08(View):
    def get(self, request):
            return render(request, 'calender/july_08.html')
class JulyView09(View):
    def get(self, request):
            return render(request, 'calender/july_09.html')
class JulyView10(View):
    def get(self, request):
            return render(request, 'calender/july_10.html')
class JulyView16(View):
    def get(self, request):
            return render(request, 'calender/july_16.html')
class JulyView30(View):
    def get(self, request):
            return render(request, 'calender/july_30.html')
class JulyView31(View):
    def get(self, request):
            return render(request, 'calender/july_31.html')