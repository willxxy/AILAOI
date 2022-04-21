from arcgis.gis import GIS
from arcgis.geocoding import geocode
from IPython.display import display

from arcgis.features import FeatureLayerCollection
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

import io
import base64
import shutil
from PIL import Image

our_gis = GIS(username="Ming_Wang_LearnArcGIS", password="pestai666")
our_webmap = our_gis.content.search("Pest.ai_background", item_type="Web Map")
item = our_webmap[0]


thumbnail = item.thumbnail
if thumbnail:
    bn = os.path.basename(thumbnail)
    image_bytes = item.get_thumbnail()
    img = Image.open(io.BytesIO(image_bytes))
    img.save('pic.png')
    # b64_item = base64.b64encode(image_bytes)
    # b64thmb = "data:image/png;base64," + str(b64_item,"utf-8") + "' width='200' height='133"
    # item_thumbnail = """<img src='""" + str(b64thmb) + """' class="itemThumbnail">"""
img.close()

df = pd.read_csv('prediction.csv')
df

num_no = df[df.D_holes == "No Infestation"].shape[0]
num_moderate = df[df.D_holes == "Moderate Infestation"].shape[0]
num_serve = df[df.D_holes == "Severe Infestation"].shape[0]
print(num_no, num_moderate, num_serve)


class_l = [("No Infestation", num_no),
           ("Moderate Infestation", num_moderate),
           ("Severe Infestation", num_serve),]
class_l


class_str = ""
for k, v in class_l:
    class_str += (' '*8 + k + ": ")
    class_str += ((50 - 2 *  len(k))*' ' + str(v) + "\n")
class_str


serve_df = df[df.D_holes == "Severe Infestation"]
l = serve_df['city_name'].value_counts().to_frame()

serve_l = []
for k, v in zip(l.index.to_list(), l['city_name']):
    serve_l.append((k, v))
serve_l

city_str = ""
for i, (k, v) in enumerate(serve_l):
    city_str += (' '*8 + k + ": ")
    city_str += ((50 - 2 * len(k))*' ' + str(v) + "\n")
city_str


from datetime import date

today = date.today()
print("Today's date:", today)

message = dict()
message['class_str'] = class_str
message['city_str'] = city_str
message['date'] = str(date.today())
for k, v in message.items():
    print(v)


s = "Risk Level: \n" + message['class_str'] +\
    "\nInfected # of Trees (est.): \n" + message['city_str'] +\
    "\nDate of Report: " + message['date'] + "\n\n" +\
    "Link to the ArcGIS Portal: " + "https://www.arcgis.com/apps/dashboards/e24632dc37fc484985e3a355e665512e" + "\n"
print(s)

import smtplib, ssl
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def notifiy(message, address):
    l = []
    ImgFileName = 'pic.png'
    with open(ImgFileName, 'rb') as f:
        img_data = f.read()
    
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "yanhaoshen97@gmail.com"
    receiver_email = address
    # receiver_email = "yanhaosh@usc.edu"
    # receiver_email = "jiminyoo@usc.edu"
    password = "pestai666"

    msg = MIMEMultipart()
    msg['Subject'] = '[Alert] Warning Pest Risk Alert'
    # msg['From'] = 'e@mail.cc'
    # msg['To'] = 'e@mail.cc'
    text = MIMEText(message)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

import sys
address = sys.argv[1]

notifiy(s, address)