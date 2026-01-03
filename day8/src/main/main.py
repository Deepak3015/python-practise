import configparser
from loguru import logger
from src.main.Databases.sql_connector import MySqlConnection, MySqlCRUDOperation

config = configparser.ConfigParser()
config.read("/home/depliii/Desktop/GitHub/python-practise/day8/src/resources/config.ini")


def main():
    query = "SELECT * FROM labours_table"

    mysql_conn = MySqlConnection(config)
    mysql_conn.connect()

    crud = MySqlCRUDOperation(mysql_conn.connection)
    result = crud.read_sql(query)

    logger.info(result)

    mysql_conn.close()


if __name__ == "__main__":
    main()
