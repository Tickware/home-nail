import json
import psycopg2
from psycopg2.extras import RealDictCursor
import shutil

conn = psycopg2.connect(database = 'db_homeNailTeste',
                        user = 'postgres',
                        password = 'postgres',
                        host = '127.0.0.1',
                        port = '5432')


def exporta_json():
    cur = conn.cursor(cursor_factory=RealDictCursor)

    tables = ['t_clientes', 't_fornecs',  't_agenda']

    jsonOut = ''
    for table in tables:
        cur.execute(f'SELECT * FROM {table}')
        jsonOut += json.dumps(cur.fetchall(), indent=2)

        arqJson = open(f'dados/{table}.json', 'w')
        arqJson.write(jsonOut)
        arqJson.close()


    output_filename = 'dados'
    dir_name = 'F:\TICKWARE\Home-Nail\dados'

    shutil.make_archive('tabelas', 'zip', 'F:\TICKWARE\Home-Nail\dados', 'F:\TICKWARE\Home-Nail\dados')
