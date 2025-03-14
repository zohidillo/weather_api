from src.core.models.base import *


class City(BaseModel):
    external_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()  # 70.36955
    longitude = models.FloatField()  # 15.36894

    def __str__(self):
        return f"{self.name} (External ID: {self.external_id}, Lat: {self.latitude}, Lon: {self.longitude})"

    class Meta:
        db_table = "cities"
        ordering = ["name"]
