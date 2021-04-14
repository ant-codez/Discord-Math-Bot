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

    def custom_query(self, query: str):
        # bind cursor
        self.cursor = self.session.cursor()

        # execute query
        self.cursor.execute(query)

        # commit and unbind cursor
        self.session.commit()
        self.cursor.close()

    ###############################################
    ###############################################

    #TODO: Figure out the correct queries to write

    ###############################################
    ###############################################

    def increment_correct(self):
        self.custom_query("""
            update person
            set correct = correct + 1;
            where id = 0;
        """)

    def increment_incorrect(self):
        self.custom_query("""
            update Person
            set incorrect = incorrect + 1;
            where id = 0;
        """)

    def get_correct(self):
        self.custom_query("""
            select correct from Person
            where id = 0;
        """)

    def get_incorrect(self):
        self.custom_query("""
            select incorrect from Person
            where id = 0;
        """)
