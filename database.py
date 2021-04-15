############################
############################

#TODO: Make this a singleton

############################
############################
import psycopg2
import yaml

class Database:

    def __init__(self):
        credentials = yaml.load(open("config/database_login.yml"))
        # connect to the mathbot database
        self.session = psycopg2.connect(
            host = credentials['login']['host'],
            database = credentials['login']['database'],
            user = credentials['login']['user'],
            port = credentials['login']['port'],
            password = credentials['login']['password'],
        )

    def __del__(self):
        self.session.close()

    def commit_query(self, query: str):
        # bind cursor
        self.cursor = self.session.cursor()

        # execute query
        self.cursor.execute(query)

        # commit and unbind cursor
        self.session.commit()
        self.cursor.close()


    def query(self, query: str):
        # bind cursor
        self.cursor = self.session.cursor()

        # execute query
        self.cursor.execute(query)

        # commit and unbind cursor
        self.cursor.close()

    def select_all(self):
        # bind the cursor
        self.cursor = self.session.cursor()

        # find user_id that we are looking for
        self.cursor.execute(f"""
            select *
            from person;
        """)

        # fetch the record from our execution
        records = self.cursor.fetchone()

        if records == None:
            print("could not find any records!")
        else:
            print("gathering records")

        # close the cursor
        self.cursor.close()
        return records

    def record_from_user_id(self, user_id: int):
        # bind the cursor
        self.cursor = self.session.cursor()

        print("checking if user exists...")

        # find user_id that we are looking for
        self.cursor.execute(f"""
            select *
            from person
            where "user_id" = {user_id};
        """)

        # fetch the record from our execution
        user_record = self.cursor.fetchone()

        if user_record == None:
            print("user does not exist!")
        else:
            print("user exists!")

        # close the cursor
        self.cursor.close()

        # return it, it's either going to be None or a tuple
        return user_record

    def create_user(self, user_id: int, username: str):
        # find user_id that we are looking for
        self.commit_query(f"""
            insert into person ("user_id", "username", "correct", "incorrect", "source") values ({user_id}, '{username}', 0, 0, 'discord');
        """)

        print(f"created user: {username}!")

        return self.record_from_user_id(user_id)

    def inc_correct(self, key: int):
        self.commit_query(f"""
            update person set "correct" = "correct" + 1 where "key" = {key};
        """)

    def inc_incorrect(self, key: int):
        self.commit_query(f"""
            update person set "incorrect" = "incorrect" + 1 where "key" = {key};
        """)

    def record_from_key(self, key: int):
        # bind the cursor
        self.cursor = self.session.cursor()

        print("checking if user exists...")

        # find user_id that we are looking for
        self.cursor.execute(f"""
            select *
            from person
            where "key" = {key};
        """)

        # fetch the record from our execution
        user_record = self.cursor.fetchone()

        if user_record == None:
            print("user does not exist!")
        else:
            print("user exists!")

        # close the cursor
        self.cursor.close()

        # return it, it's either going to be None or a tuple
        return user_record