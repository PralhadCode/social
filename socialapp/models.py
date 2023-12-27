from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class QRCode(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes',  blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Visitor(models.Model):
    OFFICE = 'office'
    RESTAURANT = 'restaurant'
    PURPOSE_CHOICES = [
        (OFFICE, 'Office'),
        (RESTAURANT, 'Restaurant'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField(blank=True, null=True)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    purpose_desc = models.TextField()
    number_of_people = models.IntegerField(null=True, blank=True)
    # # CR_DTM (creation date time)
    # cr_dtm = models.DateTimeField(auto_now_add=True)
    # # CURR_IND (current indicator)
    # curr_ind = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
