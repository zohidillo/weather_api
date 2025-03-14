WEATHER_TRANSLATIONS = {
    "clear sky": "Ochiq osmon",
    "few clouds": "Kam bulutli",
    "scattered clouds": "Tarqoq bulutlar",
    "broken clouds": "Parchalangan bulutlar",
    "overcast clouds": "Qorong‘i bulutlar",
    "shower rain": "Yomg‘ir yog‘moqda",
    "rain": "Yomg‘ir",
    "thunderstorm": "Momaqaldiroq",
    "snow": "Qor",
    "mist": "Tuman",
}


def translate_weather(description):
    return WEATHER_TRANSLATIONS.get(description.lower(), description)
