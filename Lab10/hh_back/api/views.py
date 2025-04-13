from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

# Список всех компаний
class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

# Получение одной компании по ID
class CompanyDetailAPIView(APIView):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)

# Вакансии компании по ID
class CompanyVacanciesAPIView(APIView):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
            vacancies = company.vacancies.all()
            serializer = VacancySerializer(vacancies, many=True)
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)

# Список всех вакансий
class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

# Получение одной вакансии по ID
class VacancyDetailAPIView(APIView):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
            serializer = VacancySerializer(vacancy)
            return Response(serializer.data)
        except Vacancy.DoesNotExist:
            return Response({"error": "Vacancy not found"}, status=404)

# Топ 10 вакансий по убыванию зарплаты
class VacancyTopTenAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)