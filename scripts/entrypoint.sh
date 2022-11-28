#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

cd /app/
echo "Making migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Collecting static and media files..."
python manage.py collectstatic --no-input

echo "Making messages"
python manage.py makemessages --locale $BASE_LANG_CODE

if [ "$REBUILD_ES" = "1" ]
then
    echo "Rebuilding ES index..."
    python manage.py search_index --rebuild -f
fi

if [ "$COMPILE_LOCALE" = "1" ]
then
    echo "Compiling Locale"
    python manage.py compilemessages
fi

if [ "$DEBUG" = "1" ]
then
    echo "Trying to create superuser..."
    python manage.py shell < tools/create_superuser.py
else
    echo "Compiling SCSS for production..."
    python manage.py compilescss
fi

if [ "$CREATE_CODELIST" = "1" ]
then
    echo "Trying to generate codelist..."
    python manage.py shell < tools/create_codelist.py
fi

exec "$@"
