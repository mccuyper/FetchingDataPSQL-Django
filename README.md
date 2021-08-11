# FetchingDataPostgreSQL-Django
!------TUTORIAL------!
Fetching Data from existing DB (postgreSQL) using Django


REQUIREMENTS: 
1. install PostgreSQL -> create table using cli or pgAdmin | or you can use your existing table in PostgreSQL | just make sure you have an access
2. Create virtual env (e.g.: <code> python -m venv venv </code>)
3. Activate your virtual environment (<code>source venv/bin/activate</code> for linux users or <code>venv/Scripts/activate</code> for Win users)
4. Install dependencies from requirements.txt (<code>pip install -r requirements.txt</code>)

I. EXAMPLE OF TABLE:

![Screenshot from 2021-08-11 13-24-58](https://user-images.githubusercontent.com/49821742/129013645-6eed97c4-6f9c-4589-badc-7c918f1b9dee.png)


BEFORE YOU RUN:
1. Connect to your DB in setting.py

![Screenshot from 2021-08-11 13-31-40](https://user-images.githubusercontent.com/49821742/129014381-1bb36b99-0b5e-4613-ba51-2c30899f57c5.png)

2. Change models.py's vars:

![Screenshot from 2021-08-11 13-33-46](https://user-images.githubusercontent.com/49821742/129014625-4a297ecb-80e6-42c5-81c8-2f2bb6007214.png)

3. Change data in FOR loop  in index.html with your vars accordingly to your needs:

![Screenshot from 2021-08-11 13-38-52](https://user-images.githubusercontent.com/49821742/129015437-c0be0b13-a211-4b30-960d-cfb5d10c6ef8.png)



that's all, folks!

RUN SERVER: 
<code>
python manage.py runserver
</code>


TODO:
1. Create FORMS for filtering
2. Convert to csv format and download data 

