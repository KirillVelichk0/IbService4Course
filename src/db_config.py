import os


def TryImportFromEnv(env_name: str, default_val: str):
    val_env = os.environ.get(env_name)
    return default_val if val_env is None else val_env


DB_HOST = TryImportFromEnv("DB_HOST", "localhost")
DB_PORT = int(TryImportFromEnv("DB_PORT", "5432"))
DB_USER = TryImportFromEnv("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS")
if DB_PASS is None:
    raise ValueError("Db password not passed to DB_PASS env variable")
DB_NAME = TryImportFromEnv("DB_NAME", "bvs")
