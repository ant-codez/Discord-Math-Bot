############################
############################

#TODO: Make this a singleton

############################
############################
import psycopg2

class Database:

    def __init__(self):
        # connect to the mathbot database
        self.session = psycopg2.connect(
            host = "ec2-3-233-43-103.compute-1.amazonaws.com",
            database = "d6ecpf8hf6sdte",
            user = "fmlhlahbtfonwl",
            port = "5432",
            password = "b39b8847a5036a2530975f1a366b7901178d3fcfe43d9679532af802010d1553",
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
            where ID = 0;
        """)

    def increment_incorrect(self):
        self.custom_query("""
            update Person
            set incorrect = incorrect + 1;
            where ID = 0;
        """)

    def get_correct(self):
        self.custom_query("""
            select correct FROM Person
            where ID = 0;
        """)

    def get_incorrect(self):
        self.custom_query("""
            SELECT incorrect FROM Person
            WHERE ID = 0;
        """)
