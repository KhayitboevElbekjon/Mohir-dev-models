from django.db import models
class Profil(models.Model):
    ism=models.CharField(max_length=25)
    username=models.CharField(max_length=15,unique=True)
    sana=models.DateField(auto_now_add=True)
    email=models.EmailField()
    tel=models.CharField(max_length=13)
    def __str__(self):
        return f"{self.ism}"
class Kurs(models.Model):
    daraja=[('Boshlangich','Boshlangich'),
            ("O'rta","O'rta"),
            ('Yuqori','Yuqori')]
    nom=models.CharField(max_length=25)
    rasm=models.ImageField(blank=True)
    daraja=models.CharField(max_length=15,choices=daraja)
    narx=models.FloatField()
    def __str__(self):
        return f"{self.nom}"
class Izoh(models.Model):
    baho=models.SmallIntegerField(default=5)
    matn=models.TextField()
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    kurs_fk=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    sana=models.DateField(blank=True,null=True)
class Tanlangan(models.Model):
    kurs_fk=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
class Ustoz(models.Model):
    ism=models.CharField(max_length=25)
    malumot=models.TextField()
    rasm=models.ImageField(blank=True)
    def __str__(self):
        return f"{self.ism}"
class Ustoz_kurs(models.Model):
    kurs_fk=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    ustoz_fk=models.ForeignKey(Ustoz,on_delete=models.CASCADE)
class Xarid(models.Model):
    kurs_fk=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    profil_fk=models.ForeignKey(Profil,on_delete=models.CASCADE)
    holat=models.CharField(max_length=15,default='Yangi')
    sana=models.DateField(blank=True,null=True)


