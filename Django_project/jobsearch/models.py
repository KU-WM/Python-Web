from django.db import models

class JodData(models.Model):
    company_name = models.CharField(verbose_name='C_name', max_length=100)      # 회사명
    job_notice_title = models.CharField(verbose_name='j_notice_title', max_length=100, blank=True)      # 구인광고 명
    career = models.CharField(max_length=20)        # 경력사항
    education = models.CharField(max_length=20)     # 학력
    permanent_worker = models.CharField(max_length=20)  # 정규직 여부
    company_location = models.CharField(max_length=50)  # 주소

    salary = models.CharField(max_length=50)        # 급여
    office_hour = models.CharField(max_length=50)   # 시간
    job_grade = models.CharField(max_length=20)     # 직급
    responsibilities_of_office = models.CharField(max_length=100)   # 직책
    selection_procedure = models.CharField(max_length=100)  # 상세요강
    recruitment_field = models.CharField(max_length=50)     # 전형절차
    recruit_number = models.CharField(max_length=200)    # 모집분야
    pic = models.CharField(max_length=50)   # 모집인원
    department_name = models.CharField(max_length=20)   # 인사담당자
    contact = models.CharField(max_length=50)   # 연락처

    applicant_statistics = models.CharField(max_length=300)   # 지원자 통계
    company_info = models.CharField(max_length=500)  # 기업 정보


    class Meta:
        verbose_name = 'jobdata'
        verbose_name_plural = 'jobdata'
        db_table = 'jobdatas'