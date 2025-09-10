# Furnitica (Cleaned, DB-backed)

This project mirrors your n68-molla template structure.

## Run
```bash
pip install "Django>=5.2,<6"
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- Home: /
- Shop: /shop/
- Admin: /admin/

Add Categories & Products in admin. Use image paths under `assets/` (e.g., `img/home/armchair.png`).
