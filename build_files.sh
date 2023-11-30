echo " BUILD START..."
python3.9 -m pip install -r requirements.txt

# Install MySQL Client Dependencies
sudo apt-get install libmysqlclient-dev

# Set MYSQLCLIENT_CFLAGS and MYSQLCLIENT_LDFLAGS
export MYSQLCLIENT_CFLAGS=$(pkg-config --cflags mysqlclient)
export MYSQLCLIENT_LDFLAGS=$(pkg-config --libs mysqlclient)


echo " Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput


python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END..."