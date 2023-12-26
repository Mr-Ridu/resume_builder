from django.db import models



class Resume(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100,default='No Name')
    last_name = models.CharField(max_length=100,default='No Name')
    contact = models.CharField(max_length=100,blank=True)
    email = models.EmailField(null=True)
    city = models.CharField(max_length=150,blank=True)
    postcode = models.CharField(max_length=20,blank=True)
    country = models.CharField(max_length=100,blank=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    objective = models.TextField(blank=True)
    
     
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=150, blank=True)
    subject = models.CharField(max_length=150, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Allow for ongoing education
    still_here = models.BooleanField(default=False)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2)  # Use DecimalField for GPA


class experiance(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=150, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Allow for ongoing job
    still_here = models.BooleanField(default=False)


class certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=500, blank=True)
    details = models.TextField()


class awards(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    awards_name = models.CharField(max_length=500, blank=True)
    details = models.TextField()