import subprocess
import datetime
import boto3
import os

def backup_postgresql_db(db_name, db_user, db_password, db_host, db_port, output_dir, s3_bucket, s3_key_prefix):
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
        
        s3 = boto3.client('s3')
        s3_key = f"{s3_key_prefix}/{os.path.basename(backup_file)}"
        s3.upload_file(backup_file, s3_bucket, s3_key)
        print(f"Arquivo de backup '{backup_file}' enviado para o bucket S3 '{s3_bucket}' com a chave '{s3_key}'")
        
        os.remove(backup_file)
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao realizar o backup: {e.stderr}")
    except Exception as e:
        print(f"Erro ao enviar o arquivo para o S3: {str(e)}")

if __name__ == "__main__":
    db_name = 'testdb'
    db_user = 'admin'
    db_password = 'admin'
    db_host = 'localhost'
    db_port = 5432
    output_dir = '/home'
    
    # Configurações do S3
    s3_bucket = 'backupbucketgabriel'
    s3_key_prefix = 'backups'

    backup_postgresql_db(db_name, db_user, db_password, db_host, db_port, output_dir, s3_bucket, s3_key_prefix)
