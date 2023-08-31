from rest_framework import serializers
from apis.models import SchoolStructure, Schools, Classes, Personnel, Subjects, StudentSubjectsScore


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'title']


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['id', 'first_name', 'last_name', 'personnel_type', 'school_class']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = ['title']


class StudentSubjectsScoreDetailsSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subjects')
    grade = serializers.SerializerMethodField()

    class Meta:
        model = StudentSubjectsScore
        fields = ['subject', 'credit', 'score', 'grade']

    def get_grade(self, studentsubjectsscore):
        score = studentsubjectsscore.score
        if score >= 80:
            grade = 'A'
        elif score >= 75:
            grade = 'B+'
        elif score >= 70:
            grade = 'B'
        elif score >= 65:
            grade = 'C+'
        elif score >= 60:
            grade = 'C'
        elif score >= 55:
            grade = 'D+'
        elif score >= 50:
            grade = 'D'
        else:
            grade = 'F'
        return grade

    def to_representation(self, instance):
        student_info = PersonnelSerializer(instance.student).data
        student = {
            "id": student_info['id'],
            "full_name": student_info['first_name'] + ' ' + student_info['last_name'],
            "school": "student's school name"
        }
        rep = super().to_representation(instance)
        rep['student'] = PersonnelSerializer(instance.student).data
        rep['subject'] = SubjectsSerializer(instance.subjects).data

        return rep
