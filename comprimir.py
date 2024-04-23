import filecmp
import platform
import subprocess
import os
os.system('powershell -Command "(gc analisis_backup.sql) | ? {$_ -notmatch \'^--\'} | Out-File -encoding ASCII analisis_backup.sql"')
os.system('powershell -Command "(gc analisis_backup.sql) | ? {$_ -notmatch \'^/\\*\'} | Out-File -encoding ASCII analisis_backup.sql"')

os.system('powershell -Command "(gc analisis_backup.sql) | ? {$_ -notmatch \'^--\'} | Out-File -encoding ASCII analisis.sql"')
os.system('powershell -Command "(gc analisis_backup.sql) | ? {$_ -notmatch \'^/\\*\'} | Out-File -encoding ASCII analisis.sql"')


def comparar_archivos(file1, file2):
    return filecmp.cmp(file1, file2)
son_iguales = comparar_archivos('analisis.sql', 'analisis_backup.sql')
print(son_iguales)




# def subirBDLocal():
#     dump_cmd = "mysqldump --defaults-extra-file=analisis/my2.cnf -u root analisis > analisis.sql"
#     dump_cmd2 = "mysql --defaults-extra-file=analisis/my.cnf -u admin -h databaserafael.cj2mqqcw6wf0.us-east-2.rds.amazonaws.com analisis < analisis.sql"
#     if platform.system() == 'Windows':
#         try:
#             subprocess.run(dump_cmd, shell=True, check=True)
#         except subprocess.CalledProcessError as e:
#             print(f"Error al subir la base de datos: {str(e)}")


# subirBDLocal()