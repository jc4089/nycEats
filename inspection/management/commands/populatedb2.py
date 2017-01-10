from django.core.management.base import BaseCommand
from inspection.models import Restaurant, InspectionResults

import csv
import urllib2
import pandas
import numpy

class Command(BaseCommand):
    url = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'

    def _load_data(self):
        # Clear tables
        Restaurant.objects.all().delete()
        InspectionResults.objects.all().delete()

        # Open file
        print 'Using pandas...'
        data = pandas.read_csv(self.url)
        #response = urllib2.urlopen(self.url)
        #cr = csv.reader(response)
        
        # Read header
#        headers = cr.next()
#
#        # Get index look-ups into data
#        inspection_vars = ['INSPECTION DATE', 'INSPECTION TYPE']
#        idate_idx, itype_idx = [headers.index(v) for v in inspection_vars]
#        
#        violation_vars = ['VIOLATION CODE', 'ACTION', 'VIOLATION DESCRIPTION', 'CRITICAL FLAG']
#        vc_idx, action_idx, vd_idx, cf_idx = [headers.index(v) for v in violation_vars]
#        
#        grade_vars = ['GRADE', 'SCORE', 'GRADE DATE']
#        grade_idx, score_idx, gdate_idx = [headers.index(v) for v in grade_vars]
        
        for i in range(len(data)):
            if i % 1000 == 0:
                print i
            
            camis = data.CAMIS[i]
            name = data.DBA[i] if data.DBA[i] != '' else 'N/A'
            boro = data.BORO[i]
            building = data.BUILDING[i]
            street = data.STREET[i]
            zipcode = data.ZIPCODE[i]
            
            cuisine = data['CUISINE DESCRIPTION'][i]
            
            try:
                phone = int(data.PHONE[i])
            except:
                phone = 0
            
            #print 'C=', camis
            #print name
            #print boro
            #print building
            #print street
            #print zipcode
            #print phone
            #print 'CI=', cuisine
            
            #print camis, name, boro, building, street, zipcode, phone, cuisine
            
            # Create restaurant
            newRestaurant, _ = Restaurant.objects.get_or_create(
                camis = camis,
                name = name,
                boro = boro,
                building = building,
                street = street,
                zipcode = zipcode,
                phone = phone,
                cuisine = cuisine,
            )
            
            inspection_type = data['INSPECTION TYPE'][i]
            grade = data.GRADE[i] if data.GRADE[i] != '' else 'N/A'
            score = data.SCORE[i] if not numpy.isnan(data.SCORE[i]) else 100
            
            try:
                imonth, iday, iyear = [int(d) for d in data['INSPECTION DATE'][i].split('/')]
                if iyear < 100:
                    iyear += 2000
            except:
                imonth = iday = 1
                iyear = 1970

            try:
                gmonth, gday, gyear = [int(d) for d in data['GRADE DATE'][i].split('/')]
                if gyear < 100:
                    gyear += 2000
            except:
                gmonth = gday = 1
                gyear = 1970
            
            # Create Inspection
            newRestaurant.inspectionresults_set.create(
                inspection_type = inspection_type,
                inspection_date = '%04d-%02d-%02d' % (iyear, imonth, iday),
                grade = grade,
                score = score,
                grade_date = '%04d-%02d-%02d' % (gyear, gmonth, gday),
            )

#class Command(BaseCommand):
#    url = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'
#
#    def _load_data(self):
#        # Clear tables
#        Restaurant.objects.all().delete()
#        InspectionResults.objects.all().delete()
#
#        # Open file
#        response = urllib2.urlopen(self.url)
#        cr = csv.reader(response)
#        
#        # Read header
#        headers = cr.next()
#
#        # Get index look-ups into data
#        inspection_vars = ['INSPECTION DATE', 'INSPECTION TYPE']
#        idate_idx, itype_idx = [headers.index(v) for v in inspection_vars]
#        
#        violation_vars = ['VIOLATION CODE', 'ACTION', 'VIOLATION DESCRIPTION', 'CRITICAL FLAG']
#        vc_idx, action_idx, vd_idx, cf_idx = [headers.index(v) for v in violation_vars]
#        
#        grade_vars = ['GRADE', 'SCORE', 'GRADE DATE']
#        grade_idx, score_idx, gdate_idx = [headers.index(v) for v in grade_vars]
#        
#        i = 0
#        for line in cr:
#            print line
#            if i % 1000 == 0:
#                print i
#            
#            # Create restaurant
#            newRestaurant, _ = Restaurant.objects.get_or_create(
#                camis = int(line[0]),
#                name = line[1],
#                boro = line[2],
#                building = line[3],
#                street = line[4],
#                zipcode = int(line[5]) if line[6].isdigit() else 0,
#                phone = int(line[6]) if line[6].isdigit() else 0,
#                cuisine = line[7],
#            )
#            
#            try:
#                imonth, iday, iyear = [int(d) for d in line[idate_idx].split('/')]
#                if iyear < 100:
#                    iyear += 2000
#            except:
#                imonth = iday = iyear = 1
#
#            try:
#                gmonth, gday, gyear = [int(d) for d in line[gdate_idx].split('/')]
#                if gyear < 100:
#                    gyear += 2000
#            except:
#                gmonth = gday = gyear = 1
#            
#            # Create Inspection
#            newInspection = newRestaurant.inspectionresults_set.create(
#                inspection_type = line[itype_idx],
#                inspection_date = '%04d-%02d-%02d' % (iyear, imonth, iday),
#                grade = line[grade_idx] if line[grade_idx] != '' else 'N/A',
#                score = int(line[score_idx]) if line[score_idx].isdigit() else 0,
#                grade_date = '%04d-%02d-%02d' % (gyear, gmonth, gday),
#            )
#     
#            i += 1
        
        
#        objs = []
#        i = 0
#        for line in cr:
#            if i % 1000 == 0:
#                print i
#            
#            try:
#                imonth, iday, iyear = [int(d) for d in line[idate_idx].split('/')]
#                if iyear < 100:
#                    iyear += 2000
#            except:
#                imonth = iday = iyear = 1
#
#            try:
#                gmonth, gday, gyear = [int(d) for d in line[gdate_idx].split('/')]
#                if gyear < 100:
#                    gyear += 2000
#            except:
#                gmonth = gday = gyear = 1
#            
#            # Create inspection
#            newInspection = Inspection(
#                camis = int(line[0]),
#                name = line[1],
#                boro = line[2],
#                building = line[3],
#                street = line[4],
#                zipcode = int(line[5]) if line[6].isdigit() else 0,
#                phone = int(line[6]) if line[6].isdigit() else 0,
#                cuisine = line[7],
#                inspection_type = line[itype_idx],
#                inspection_date = '%04d-%02d-%02d' % (iyear, imonth, iday),
#                grade = line[grade_idx] if line[grade_idx] != '' else 'N/A',
#                score = int(line[score_idx]) if line[score_idx].isdigit() else 0,
#                grade_date = '%04d-%02d-%02d' % (gyear, gmonth, gday),
#            )
#            objs.append(newInspection)
#                  
#            i += 1
#        
#        Inspection.objects.bulk_create(objs)

    def handle(self, *args, **options):
        self._load_data()