import psycopg2


def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            port=config('PGSQL_PORT'),
            user=config('PGSQL_USER'),


        )
    except DatabaseError as ex:
        raise ex
