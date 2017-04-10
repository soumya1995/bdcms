#!/usr/bin/python3

import cgi
import cgitb
import os.environ
import mysql.connector

def main( ):
    cgi.enable( display = 0, logdir = "/var/log" )
    field_storage = cgi.FieldStorage( )

    print( "Content-Type: text/html\r\n" )

    try:
        cnx = mysql.connector.connect( user="root", password="", host="localhost" )

        cursor = cnx.cursor( )
        cursor.execute( "USE bdcms" )
        cursor.close( )

        cursor = cnx.cursor( )
        cursor.execute( "SELECT (username,md5hash) FROM Users" )
        cursor.close( )

        found = false
        for username,md5hash in cursor:
            if( field_storage[ "username" ] == username and md5(field_storage[ "password" ]) == md5hash ):
                found = true

        if( found ):
            if( "HTTP_COOKIE" not in os.environ ):
                if( "HTTP_USER_AGENT" in os.environ and "REMOTE_ADDR" in os.environ ):
                    print( "Set-Cookie: session_id=%s; expires=%s" % ( md5sum( os.environ[ "HTTP_USER_AGENT" ] + os.environ[ "REMOTE_ADDR" ] ), "2017-03-19T17:31:39Z" ) )
        else:
            quit( )

    except mysql.error.Error as err:
        if( err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR ):
            print( "Access denied!" )
        elif( err.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS ):
            print( "Database already exists!" )

    
    print( """
<!DOCTYPE html>
<html><head>
<title>Login Processor</title>
<meta http-equiv="refresh" content="0;URL=https://bdcms.org/login.php" />
<meta charset="utf-8" />
</head><body>
</body></html>
    """ )

if( __name__ == '__main__' ):
    main( )
