set -o errexit
set -o pipefail
set -o nounset
export DJANGO_SETTINGS_MODULE=config.settings.deployment

python manage.py install
python manage.py runserver 0.0.0.0:8080

