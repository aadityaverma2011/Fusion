from rest_framework import serializers
from applications.department.models import Announcements
from applications.academic_information.models import Spi, Student
from applications.globals.models import (Designation, ExtraInfo,
                                         HoldsDesignation,Faculty)
from applications.eis.models import (faculty_about, emp_research_projects)
from applications.department.models import Information
from applications.department.models import Lab

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements 
        fields = ('__all__')
        
        extra_kwargs = {
            'maker_id': {'required': False}
        }
        
    def create(self, validated_data):
        user = self.context['request'].user
        user_info = ExtraInfo.objects.all().select_related('user','department').filter(user=user).first()
        validated_data['maker_id'] = user_info
        return Announcements.objects.create(**validated_data)
    
class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo 
        fields = ('__all__')

class SpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spi 
        fields = ('__all__')
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  
        fields = ('__all__')
        
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation 
        fields = ('__all__')
        
class HoldsDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoldsDesignation 
        fields = ('__all__')
        
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty 
        fields = ('__all__')

class faculty_aboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty_about 
        fields = ('__all__')
        
class emp_research_projectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = emp_research_projects 
        fields = ('__all__')

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'  # or specify fields as needed

class LabSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = Lab
        fields = '__all__'

    def get_department(self, obj):
        # Return the department name instead of the primary key
        return obj.department.name