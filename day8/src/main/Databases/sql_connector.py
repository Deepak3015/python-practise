# from loguru import logger
# import mysql.connector
# import configparser
# from src.crypto.crypt import decrypt

# class MySqlConnection :
#     def __init__(self,config):
#           self.config = config
#           self.connection = None
    
#     def connect(self):
#         try:
#             self.connection =mysql.connector.connect(
#             host = self.config["my_sql_credential"]["host"],
#             user = self.config["my_sql_credential"]["user"],
#             password = decrypt(self.config["my_sql_credential"]["password"]),
#             database = self.config["my_sql_credential"]["database"])
#             logger.info("Connection Has Been Successully Established :)")
#         except Exception as e:
#             logger.info(f"Error Has Occured {e}")
#             raise e
        
#     def close(self):
#         if self.connection.is_connected():
#             self.connection.close()
#             logger.info("Connection Has Successfully Closed")

# class MySqlCRUDOperation:
#     def __init__(self,connection):
#         self.connection = connection
    
#     def read_sql(self,query):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#         except Exception as e:
#             logger.info(f"Error occured in My Sql Query{e}")
#             raise e
#     def insert_sql(self,query,parameter):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#         except Exception as e:
#             logger.info(f"Error occured in My Sql Query{e}")
#             raise e        
    
        

            

# # def read_mysql(config,query):
# #     try: 
# #         connection =mysql.connector.connect(

# #             host = config["my_sql_credential"]["host"],
# #             user = config["my_sql_credential"]["user"],
# #             password = decrypt(config["my_sql_credential"]["password"]),
# #             database = config["my_sql_credential"]["database"]
# #         )
# #         logger.info(connection)
# #         cursor = connection.cursor()
# #         cursor.execute(query)
# #         result = cursor.fetchall()
# #         logger.info(f"{result}")
# #         logger.info("Query Has been execute successfully")
# #         return result 
# #     except Exception as e:
# #         logger.info(f"Error occured at data base as{e }")
# #         raise e
# #     finally:
# #             if cursor is not None:
# #                 cursor.close()
# #             if connection is not None:
# #                 connection.close()

    
    
from loguru import logger
import mysql.connector
from src.crypto.crypt import decrypt


class MySqlConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.config["my_sql_credential"]["host"],
                user=self.config["my_sql_credential"]["user"],
                password=decrypt(self.config["my_sql_credential"]["password"]),
                database=self.config["my_sql_credential"]["database"]
            )
            logger.info("Connection has been successfully established")

        except Exception as e:
            logger.error(f"Error occurred while connecting to DB: {e}")
            raise

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logger.info("Connection has been successfully closed")


class MySqlCRUDOperation:
    def __init__(self, connection):
        self.connection = connection

    def read_sql(self, query):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result

        except Exception as e:
            logger.error(f"Error occurred while reading data: {e}")
            raise

        finally:
            if cursor:
                cursor.close()

    def insert_sql(self, query, params):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            logger.info("Insert operation successful")

        except Exception as e:
            self.connection.rollback()
            logger.error(f"Error occurred while inserting data: {e}")
            raise

        finally:
            if cursor:
                cursor.close()
