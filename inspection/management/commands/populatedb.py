from django.core.management.base import BaseCommand
from inspection.models import Restaurant, InspectionResults
import pandas, numpy

class Command(BaseCommand):
    url = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'

    def _load_data(self):
        # Clear tables
        Restaurant.objects.all().delete()
        InspectionResults.objects.all().delete()

        # Open file
        data = pandas.read_csv(self.url)
        
        # Load file into table
        for i in range(len(data)):
            if i % 1000 == 0:
                print('Processed %d records' % i)
            
            # Parse parameters
            camis = data.CAMIS[i]
            name = data.DBA[i] if data.DBA[i] != '' else 'N/A'
            boro = data.BORO[i]
            building = data.BUILDING[i]
            street = data.STREET[i]
            zipcode = data.ZIPCODE[i]
            cuisine = data['CUISINE DESCRIPTION'][i]
            
            inspection_type = data['INSPECTION TYPE'][i]
            grade = data.GRADE[i] if data.GRADE[i] != '' else 'N/A'
            score = data.SCORE[i] if not numpy.isnan(data.SCORE[i]) else 100
            
            # Perform basic error handling
            try:
                phone = int(data.PHONE[i])
            except:
                phone = 0
            
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
            
            # Create inspection
            newRestaurant.inspectionresults_set.create(
                inspection_type = inspection_type,
                inspection_date = '%04d-%02d-%02d' % (iyear, imonth, iday),
                grade = grade,
                score = score,
                grade_date = '%04d-%02d-%02d' % (gyear, gmonth, gday),
            )

    def handle(self, *args, **options):
        self._load_data()