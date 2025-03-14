# Weather App

Bu loyiha **Django** asosida yaratilgan bo'lib, ob-havo ma'lumotlarini olish va saqlash uchun ishlatiladi. **Celery** va **Redis** yordamida fon vazifalarini bajaradi.

## Talablar

Loyihani ishga tushirish uchun quyidagilar kerak:

- **Docker** va **Docker Compose**
- https://openweathermap.org/api dan **API kalit**

## O'rnatish

Loyihani yuklab oling:

```bash
git clone https://github.com/zohidillo/weather_api.git
cd weather-app
```

`.env.dev` faylini yarating va quyidagi ma'lumotlarni kiriting:

```env
DEBUG=1
SECRET_KEY=django_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=database_name

DOCKER=0
WEATHER_API=<weather_api>
```

## Docker bilan ishga tushirish

Barcha xizmatlarni ishga tushirish:

```bash
docker-compose up --build
```

Agar fon rejimida ishga tushirmoqchi bo‘lsangiz:

```bash
docker-compose up -d --build
```

## Xizmatlar

- **web** - Django ilovasi
- **db** - PostgreSQL bazasi
- **redis** - Fon vazifalari uchun
- **celery_worker** - Celery ishlovchisi
- **celery_beat** - Celery Beat (jadval bo‘yicha vazifalar)

## Loglarni ko‘rish

```bash
docker logs -f weather_web
docker logs -f weather_celery_worker
docker logs -f weather_celery_beat
```

## API Endpointlar

### 1. Ob-havo ro‘yxatini olish

- **Endpoint:** `GET /api/weather/`
- **Tavsif:** Barcha ob-havo ma’lumotlarini olish
- **Misol:**
  ```bash
  GET /api/weather/?city=1&added_at__gte=2024-03-01
  ```

### 2. Ob-havo ma’lumotlarini faylga yuklash

- **Endpoint:** `GET /api/weather/generate-file/`
- **Tavsif:** Ma’lumotlarni Excel yoki CSV formatida yuklab olish
- **Misol:**
  ```bash
  GET /api/weather/generate-file/?file_type=csv
  ```

### 3. Ob-havo ma’lumotlarini yangilash

- **Endpoint:** `GET /api/weather/manual-refresh/`
- **Tavsif:** API orqali yangi ob-havo ma’lumotlarini olish va bazaga saqlash
- **Misol:**
  ```bash
  GET /api/weather/manual-refresh/
  ```
  **Eslatma:** Agar bu API chaqirilmasa, ma’lumotlar avtomatik ravishda har **10 daqiqada** yangilanadi.

