import psycopg2

from db_config import DB_HOST, DB_USER, DB_PASS, DB_NAME

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"


def check_user_in_db(login: str) -> bool:
    connection = None
    try:
        connection = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
        )
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT EXISTS (SELECT 1 FROM users WHERE login = '{login}');"""
            )
            execution_result = cursor.fetchone()
            if execution_result is None:
                raise ValueError("cursor return None")
            return bool(execution_result[0])
    except Exception as exc:
        raise exc
    finally:
        if connection:
            connection.close()


def return_w(login: str) -> str:
    connection = None
    try:
        connection = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
        )
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT w FROM users WHERE login = '{login}';""")
            execution_result = cursor.fetchone()
            if execution_result is None:
                raise ValueError("cursor return None")
            return str(execution_result[0])
    except Exception as exc:
        raise exc
    finally:
        if connection:
            connection.close()


def return_password(login: str) -> str:
    connection = None
    try:
        connection = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
        )
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT password FROM users WHERE login = '{login}';""")
            execution_result = cursor.fetchone()
            if execution_result is None:
                raise ValueError("cursor return None")
            return str(execution_result[0])
    except Exception as exc:
        raise exc
    finally:
        if connection:
            connection.close()


def insert_user_data(login: str, password: str, w: str, time) -> int:
    connection = None
    try:
        connection = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
        )
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO users (login, password, w, t) VALUES
            ('{login}', '{password}', '{w}', '{time}')
            RETURNING id;"""
            )
            connection.commit()
            execution_result = cursor.fetchone()
            if execution_result is None:
                raise ValueError("cursor return None")
            return int(execution_result[0])
    except Exception as exc:
        raise exc
    finally:
        if connection:
            connection.close()


def insert_rsa_data(id: int, p: int, q: int, n: int, phi: int, e: int, d: int) -> None:
    connection = None
    try:
        connection = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
        )
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO RSA (user_id, p, q, n, phi, e, d)
            VALUES ({id}, {p}, {q}, {n}, {phi}, {e}, {d});"""
            )
            connection.commit()
    except Exception as exc:
        raise exc
    finally:
        if connection:
            connection.close()
