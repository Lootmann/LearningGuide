# create app .env
cat <<EOF > ./app/.env
SECRET_KEY=$(python3.10 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
EOF


# create db .env
cat <<EOF > ./db/.env
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
EOF
