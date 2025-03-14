# Weather App

Bu loyiha Django asosida yaratilgan bo'lib, unda Celery va Redis yordamida fon vazifalarini bajarish mumkin. Loyihaning
asosiy maqsadi - ob-havo ma'lumotlarini qayta ishlash va saqlash.

## Talablar

Loyihani ishga tushirishdan oldin quyidagi dasturlar o'rnatilgan bo'lishi kerak:

- Docker
- Docker Compose
- https://openweathermap.org/api dan api key

## O'rnatish

Loyihani yuklab oling yoki klon qiling:

```bash
git clone https://github.com/username/weather-app.git
cd weather-app
```

`.env.dev` faylini yaratib, kerakli muhit o'zgaruvchilarini kiriting:

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

## Docker orqali ishga tushirish

Barcha xizmatlarni ishga tushirish uchun quyidagi buyruqni bajaring:

```bash
docker-compose up --build
```

Agar xizmatlarni fon rejimida ishlatmoqchi bo'lsangiz:

```bash
docker-compose up -d --build
```

## Xizmatlar haqida ma'lumot

- **web**: Django web ilovasi
- **db**: PostgreSQL bazasi
- **redis**: Redis broker
- **celery_worker**: Asosiy Celery worker
- **celery_beat**: Periodik vazifalarni bajarish uchun Celery Beat

## Loglarni ko'rish

Agar xizmatlarning loglarini tekshirmoqchi bo'lsangiz:

```bash
docker logs -f weather_web
docker logs -f weather_celery_worker
docker logs -f weather_celery_beat
```

## API larni ishlatish

## 1. Weather List API

**Endpoint:**

```
GET /api/weather/
```

**Tavsif:** Ob-havo ma’lumotlarini olish uchun ishlatiladi.

```
GET /api/weather/?city=1&added_at__gte=2024-03-01
```

---

## 2. Generate Weather File API

**Endpoint:**

```
GET /api/weather/generate-file/
```

**Tavsif:** Ob-havo ma’lumotlarini **Excel yoki CSV** formatida yuklab olish uchun ishlatiladi.

**Misol:**

```
GET /api/weather/generate-file/?file_type=csv
```

---

## 3. Manual Refresh Weather Data

**Endpoint:**

```
GET /api/weather/manual-refresh/
```

**Tavsif:** Shaharlar bo‘yicha **yangi ob-havo ma’lumotlarini** API orqali olish va bazaga saqlash uchun ishlatiladi.
bu api ishlatilmasa malumotlar har 10 daqiqada bazaga saqlamadi.

**Misol:**

```
GET /api/weather/manual-refresh/
```

**Natija:** Bazaga yangi ob-havo ma’lumotlari qo‘shiladi va qaytariladi.

---



