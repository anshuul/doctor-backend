import qrcode
from django.conf import settings
import os

LINK_TEMPLATE_FOR_QRCODE = 'https://gastroawareness.online/{}'

def generate_qrcode_for_doctor(doctor):
    print('reached here services')
    qr_code = qrcode.make(LINK_TEMPLATE_FOR_QRCODE.format(doctor.id))
    image_dest = f'qr_codes\\{doctor.id}_{doctor.name}_{doctor.sales_officer.region}.jpg'
    storage_path = os.path.join(settings.MEDIA_ROOT_URL, image_dest)
    qr_code.save(storage_path)
    print(storage_path)
    return image_dest
    