import config
from database_lib import initialize


def main() -> None:
    initialize(
        username=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        host=config.MYSQL_HOST,
        port=config.MYSQL_PORT,
        database=config.MYSQL_DATABASE,
        debug=config.DEBUG
    )

    print("Hello, World!")


if __name__ == '__main__':
    main()
