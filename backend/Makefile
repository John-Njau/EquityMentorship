serve:
	@echo "Serving on http://localhost:8000"
	python manage.py runserver 8000

# Path: Makefile
build:
	@echo "Building..."
	@npm run build

# Path: Makefile
deploy:
	@echo "Deploying..."
	@npm run deploy

migrations:
	@echo "Making migrations..."
	python manage.py makemigrations
	@echo "Migrating..."
	python manage.py migrate


# create superuser
superuser:
	@echo "Creating superuser..."
	python manage.py createsuperuser