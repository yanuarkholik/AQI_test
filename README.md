# AQI_test

[14/10/2022]-[yanuarkholik]-[python developer]

### Set up [Python](https://www.python.org/downloads/) dan Django
`python==3.9.1`

`python -m pip install Django==4.1.2` ( Windows )

### Run program
Baca Big Note dibawah 

# Installation

#### 1. Download [virtualenv](https://yasoob.me/2013/07/30/what-is-virtualenv/) untuk membuat Virtual Environment Django dengan command dibawah
```python
pip install virtualenv
```
*Note : aplikasi bisa berjalan tanpa virtualenv, virtualenv digunakan untuk mengoptimalkan development Python*
#### 2. Membuat virtualenv
```python
virtualenv nama_virtualenv
```
#### 3. Aktivasi virtualenv
```python
nama_virtualenv/Scripts/activate
```
#### 4. Install requirements.txt dengan command dibawah
```python 
pip install -r requirements.txt
```
Jika terjadi error atau ```requirements.txt``` tidak mau terinstall maka buka file ```requirements.txt``` install package/plugin satu-persatu dengan cara meng-copas nama dan versi package yang tertera. Contoh :
```python
pip install (nama_package==versi_package)
```
Kemudian hapus paket yang error tersebut pada ```requirements.txt``` untuk meninstall via requirements, jika ingin menginstall satu-persatu bisa pakai perintah diatas

#### 5. Menjalankan program
```python
python manage.py makemigrations
python manage.py migrate # Akan memunculkan banyak "OK", berarti program tidak ada masalah
python manage.py runserver
```
Web aplikasi dapat di buka pada browser apa saja di  
```python 
# user page
127.0.0.1:8000
```

#### 6. Super admin page
```python 
puthon manage.py runserver

# ketikkan pada browser
127.0.0.1:8000/admin/
```
Username / pass
1. admin / admin
2. terminal >> python manage.py createsuperuser 
3. Sign Up

# Note
1. Super admin bisa mengganti permission
2. Main navigator ada di ```127.0.0.1:8000/admin/```
3. Seharusnya program bisa jalan karena sudah di reinstall beberapa kali pada direktori dan device berbeda

