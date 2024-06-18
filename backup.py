import subprocess
import datetime

def backup_postgresql_db(db_name, db_user, db_password, db_host, db_port, output_dir):
    
    backup_file = f"{output_dir}/{db_name}_backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.sql"

    command = [
        'pg_dump',
        '-h', db_host,
        '-p', str(db_port),
        '-U', db_user,
        '-F', 'c', 
        '-f', backup_file,
        db_name
    ]

    env = {'PGPASSWORD': db_password}

    try:
        result = subprocess.run(command, env=env, check=True, capture_output=True, text=True)
        print(f"Backup do banco de dados '{db_name}' concluído com sucesso. Arquivo: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao realizar o backup: {e.stderr}")

if __name__ == "__main__":
    db_name = 'testdb'
    db_user = 'admin'
    db_password = 'admin'
    db_host = 'localhost'
    db_port = 5432
    output_dir = '/home'

    backup_postgresql_db(db_name, db_user, db_password, db_host, db_port, output_dir)