from django.db import connection, transaction,IntegrityError
from django.db.utils import OperationalError

def saveGlobal(table_name, obj):

    try:
        sql = "INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        columns = ", ".join(obj.keys())
        placeholders = ", ".join("%s" for _ in obj.values())
        values = tuple(obj.values())
    
        formatted_sql = sql.format(table=table_name, columns=columns, placeholders=placeholders)

        with connection.cursor() as cc:
            cc.execute(formatted_sql, values)
            

            return  {'info':'success', 'code':0}
            
    except OperationalError as e:
        return  {'info': f"Error : {e}", 'code':20, 'data':None}


def updateGlobal(table_name, obj, condition):
    with transaction.atomic():
        try:
            sql = "UPDATE {table} SET {set_values} WHERE {condition}"
            
            set_values = ", ".join(f"{column} = %s" for column in obj.keys())
            values = tuple(obj.values())
            
            formatted_sql = sql.format(table=table_name, set_values=set_values, condition=condition)
            
            with connection.cursor() as cursor:
                cursor.execute(formatted_sql, values)
            
            return  {'info':'success', 'code':0, 'data':None}

        except Exception as e:
            transaction.set_rollback(True)
            return  {'info':str(e), 'code':20, 'data':None}

