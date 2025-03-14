from src.core.models.base import *


class Weather(BaseModel):
    city = models.ForeignKey("City", on_delete=models.CASCADE, related_name="weather_datas")

    temperature = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    wind_speed = models.FloatField()
    weather_description = models.CharField(max_length=255)

    def __str__(self):
        return (f"Temperature is {self.temperature}°C in "
                f"{self.city.name} on {self.added_at.strftime('%Y-%m-%d %H:%M:%S')}")

    class Meta:
        db_table = "weathers"
        ordering = ["-added_at"]
