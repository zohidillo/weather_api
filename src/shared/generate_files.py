import csv
from openpyxl import Workbook
from django.http import HttpResponse

from src.shared.excel_style import set_title, excel_style

HEADERS = [
    "Id", "Shahar nomi", "Koordinata kengligi", "Koordinata uzunligi",
    "Harorat (°C)", "Namlik (%)", "Atmosfera bosimi (hPa)",
    "Shamol tezligi (m/s)", "Ob-havo holati", "Sana"
]
TITLE = "Ob-havo malumoti"


def generate_csv(data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(TITLE)

    writer = csv.writer(response)
    writer.writerow(HEADERS)

    for i in data:
        writer.writerow(
            [
                i["id"],
                i.get("city", {})["name"],
                i.get("city", {})["latitude"],
                i.get("city", {})["longitude"],
                i["temperature"],
                i["humidity"],
                i["pressure"],
                i["wind_speed"],
                i["weather_description"],
                i["added_at"]
            ]
        )

    return response


def generate_excel(data):
    wb = Workbook()
    ws = wb.active

    set_title(ws, TITLE)
    ws.append(HEADERS)

    for i in data:
        ws.append(
            [
                i["id"],
                i.get("city", {})["name"],
                i.get("city", {})["latitude"],
                i.get("city", {})["longitude"],
                i["temperature"],
                i["humidity"],
                i["pressure"],
                i["wind_speed"],
                i["weather_description"],
                i["added_at"]
            ]
        )
    excel_style(ws)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="{}.xlsx"'.format(TITLE)
    wb.save(response)

    return response
