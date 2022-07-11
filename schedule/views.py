import json
from schedule.models import Cal
from django.shortcuts import render
from django.views import View


class ScheduleView(View):

    def get(self, request):
        form = request.GET.dict()
        cal = Cal.objects.all()
        cal = list(cal.values())
        cal2 = json.dumps(cal)
        # print(cal2)

        date = Cal.objects.filter(regdate='2022.07.02')

        date1 = list(date.values())

        date2 = json.dumps(date1)
        date3 = date2.split(':')[6] # 날짜 출력은 6의 배수 (12,18,24...)
        date4 = date3.split('}')[0]

        # 날짜 출력
        # print(date4)

        time = date2.split(',')[1] # 시간은 1로 시작해서 5만큼 증가한다(1,6,11,16...)
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