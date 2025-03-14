from drf_yasg import openapi


def filter_weather_data(for_file=False):
    city = openapi.Parameter('city', openapi.IN_QUERY,
                             description="Shahar ID bo‘yicha filterlash",
                             type=openapi.TYPE_INTEGER)

    search = openapi.Parameter('search', openapi.IN_QUERY,
                               description="Shahar nomi bo‘yicha qidirish",
                               type=openapi.TYPE_STRING)

    added_at__gte = openapi.Parameter('added_at__gte', openapi.IN_QUERY,
                                      description="Sana bo‘yicha filterlash (dan boshlab)",
                                      type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE)

    added_at__lte = openapi.Parameter('added_at__lte', openapi.IN_QUERY,
                                      description="Sana bo‘yicha filterlash (gacha)",
                                      type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE)

    file_type = openapi.Parameter(
        'file_type',
        openapi.IN_QUERY,
        description="Qanday fayl formatida yuklab olmoqchisiz? (csv yoki xlsx)",
        type=openapi.TYPE_STRING,
        enum=["csv", "xlsx"]
    )

    data = [city, search, added_at__gte, added_at__lte]
    data if not for_file else data.append(file_type)
    return data
