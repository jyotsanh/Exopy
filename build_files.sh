echo " BUILD START..."
python3.9 -m pip install -r requirements.txt

# Set MYSQLCLIENT_CFLAGS and MYSQLCLIENT_LDFLAGS
export MYSQLCLIENT_CFLAGS=$(mysql_config --cflags)
export MYSQLCLIENT_LDFLAGS=$(mysql_config --libs)


echo " Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput


python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END..."