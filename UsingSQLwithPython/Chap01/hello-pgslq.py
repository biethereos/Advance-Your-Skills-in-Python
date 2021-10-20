from mysql.connector.errors import Error
import psycopg2 as pg

MY_HOST = 'localhost'
MY_USER = 'postgres'
MY_PASS = '***********'
MY_DATABASE = 'test'


def main():
    print('Postgreslq start ... ... ... ... ... ...')
    db = None # satisfy the warnings monster
    cur = None
    try:
        db = pg.connect(
            host=MY_HOST, 
            user=MY_USER, 
            password=MY_PASS,
            database=MY_DATABASE)
        cur = db.cursor()
        print('connected')
    except pg.Error as err:
        print(f'could not connect Postgreslq {err}')
        exit(1)

    try:
        cur.execute('DROP TABLE IF EXISTS person')
        # create a table
        sql_create = '''
            CREATE TABLE IF NOT EXISTS person(
                id BIGSERIAL NOT NULL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(150),
                gender VARCHAR(15) NOT NULL,
                date_of_birth DATE NOT NULL,
                country_of_birth VARCHAR(50) NOT NULL
            )
        '''
        cur.execute(sql_create)
        print('table created')
    except pg.Error as err:
        print(f'Could not create table {err}')
        exit(1)

    try:
        # insert row into the table using executemany
        row_data = (
            ('Orly', 'Conneau', None, 'Female', '2021-04-09', 'Gabon'),
            ('Jillie', 'Weighell', None, 'Genderfluid', '2021-01-19', 'Bosnia and Herzegovina'),
            ('Chere', 'Waldram', 'cwaldram2@addtoany.com', 'Genderqueer', '2021-03-07', 'Tanzania'),
            ('Betsey', 'Carolan', 'bcarolan3@plala.or.jp', 'Genderqueer', '2020-10-19', 'Indonesia'),
            ('Julius', 'Medgewick', 'jmedgewick4@hp.com', 'Polygender', '2021-06-10', 'Russia'),
            ('Luciana', 'Discombe', 'ldiscombe5@dyndns.org', 'Bigender', '2020-12-07', 'China'),
            ('Gawain', 'Argo', None, 'Polygender', '2021-01-03', 'Denmark'),
            ('Dyanna', 'Whittaker', 'dwhittaker7@toplist.cz', 'Male', '2020-10-24', 'China'),
            ('Angelo', 'Smallacombe', None, 'Male', '2021-05-19', 'France'),
            ('Hortense', 'Steinson', 'hsteinson9@imdb.com', 'Bigender', '2021-04-27', 'Indonesia'),
            ('Myrtie', 'Hargrove', None, 'Female', '2021-08-28', 'Venezuela'),
            ('Guenevere', 'Wooton', None, 'Agender', '2020-12-29', 'Kazakhstan'),
            ('Philipa', 'Piffe', 'ppiffec@google.com.hk', 'Genderqueer', '2021-07-06', 'Argentina'),
            ('Sarina', 'Chown', None, 'Male', '2021-10-01', 'Indonesia'),
            ('Heidi', 'Linguard', 'hlinguarde@shareasale.com', 'Genderqueer', '2021-09-07', 'China'),
            ('Goldi', 'Fortman', 'gfortmanf@odnoklassniki.ru', 'Female', '2020-10-12', 'Colombia'),
            ('Manolo', 'Dreus', 'mdreusg@wisc.edu', 'Genderqueer', '2021-05-22', 'China'),
            ('Bat', 'Gierke', 'bgierkeh@deliciousdays.com', 'Bigender', '2021-10-02', 'China'),
            ('Kippy', 'Laydon', 'klaydoni@telegraph.co.uk', 'Female', '2020-12-29', 'Poland'),
            ('Rodolfo', 'Tideswell', None, 'Agender', '2021-09-16', 'France'),
            ('Jada', 'Cowley', 'jcowleyk@cnet.com', 'Genderqueer', '2021-03-22', 'Guatemala'),
            ('Etan', 'Glabach', 'eglabachl@dailymail.co.uk', 'Bigender', '2021-02-04', 'South Korea'),
            ('Fielding', 'Caulcott', None, 'Bigender', '2021-01-05', 'Thailand'),
            ('Marven', 'Taig', 'mtaign@edublogs.org', 'Bigender', '2020-10-28', 'Malawi'),
            ('Catrina', 'Strowther', 'cstrowthero@kickstarter.com', 'Genderfluid', '2020-11-30', 'Portugal'),
            ('Chandal', 'Malthouse', None, 'Genderfluid', '2021-03-31', 'Bosnia and Herzegovina'),
            ('Ernestus', 'Coker', 'ecokerq@businessinsider.com', 'Genderfluid', '2021-05-11', 'United Kingdom'),
            ('Sybilla', 'Huey', 'shueyr@ovh.net', 'Polygender', '2021-02-12', 'Canada'),
            ('Merilyn', 'Altofts', 'maltoftss@yolasite.com', 'Polygender', '2021-02-24', 'Morocco'),
            ('Inigo', 'Shakesby', 'ishakesbyu@mediafire.com', 'Male', '2021-06-17', 'Philippines'),
            ('Jerri', 'Rowlin', 'jrowlinv@nytimes.com', 'Bigender', '2021-05-25', 'Indonesia'),
            ('Ricky', 'Domone', None, 'Non-binary', '2020-10-16', 'Syria'),
            ('Bartholomeus', 'Guiett', 'bguiettx@washingtonpost.com', 'Agender', '2021-06-12', 'Russia'),
            ('Lothaire', 'MacGinley', 'lmacginleyy@google.co.jp', 'Genderqueer', '2020-11-25', 'Brazil'),
            ('Grenville', 'Wettern', 'gwetternz@exblog.jp', 'Non-binary', '2021-01-01', 'China'),
            ('Bond', 'Pittford', None, 'Male', '2021-08-11', 'China'),
            ('Evania', 'Pierce', 'epierce11@google.co.jp', 'Genderqueer', '2020-12-06', 'Peru'),
            ('Eddie', 'Gerrietz', 'egerrietz12@theatlantic.com', 'Female', '2020-12-11', 'Burkina Faso'),
            ('Kermy', 'Cabel', None, 'Male', '2021-02-09', 'Philippines'),
            ('Carmella', 'Yellowlees', None, 'Female', '2020-10-22', 'Spain'),
            ('Shem', 'Vipan', 'svipan15@wunderground.com', 'Polygender', '2020-11-17', 'China'),
            ('Allie', 'Rowes', None, 'Bigender', '2021-01-16', 'China'),
            ('Hester', 'Hackford', 'hhackford17@engadget.com', 'Female', '2021-06-02', 'Malawi'),
            ('Hermine', 'Dagworthy', 'hdagworthy18@samsung.com', 'Agender', '2021-04-16', 'Peru'),
            ('Lucie', 'Cawcutt', 'lcawcutt19@businesswire.com', 'Bigender', '2021-06-15', 'Czech Republic'),
            ('Annissa', 'Ryves', 'aryves1a@howstuffworks.com', 'Male', '2021-04-02', 'Indonesia'),
            ('Loria', 'Carlick', None, 'Polygender', '2020-11-18', 'Greece'),
            ('Wadsworth', 'Semark', 'wsemark1c@qq.com', 'Genderqueer', '2021-02-02', 'Palestinian Territory'),
            ('Mag', 'Baldacchino', 'mbaldacchino1d@harvard.edu', 'Genderqueer', '2021-08-31', 'China'),
            ('Gillan', 'Barthelme', 'gbarthelme1e@sohu.com', 'Polygender', '2020-11-20', 'China'),
            ('Aridatha', 'Colecrough', 'acolecrough1f@earthlink.net', 'Genderfluid', '2021-02-28', 'Poland')
        )
        print('inserting rows')
        cur.executemany('INSERT INTO person(first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES(%s, %s, %s, %s, %s, %s)', row_data)
        count = cur.rowcount
        # cur.executemany('INSERT INTO person(first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES(%s, %s, %s, %s, %s, %s)', row_data)
        # count += cur.rowcount
        # cur.executemany('INSERT INTO person(first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES(%s, %s, %s, %s, %s, %s)', row_data)
        # count += cur.rowcount
        print(f'{count} rows added')
        db.commit()
    except pg.Error as err:
        print(f'could not add rows: {err}')
        exit(1)



if __name__ == '__main__':
    main()