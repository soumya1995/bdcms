#!/usr/bin/env php
<?php
    /* Don't mess with my vim tag
     * vim: number ts=4 sw=4 expandtab tw=76
     */

    define( 'DB_NAME',   'bdcms'     );
    define( 'DB_HOST',   'localhost' );
    define( 'DB_UNAME',  'root'      );
    define( 'DB_PASSWD', ''          );

    try {
        /* connect */
        $pdo = new PDO( 'mysql:host=' . DB_HOST,
            DB_UNAME, DB_PASSWD );

        /* prepare statement & execute */
        $stmt = $pdo->prepare( 'SHOW DATABASES' );
        $stmt->execute( );

        /* find our database */
        echo 'Looking up database name ' . DB_NAME . "...\n";

        $db_found = false;
        $db_list  = $stmt->fetchAll( PDO::FETCH_ASSOC );

        for( $i = 0; $i < sizeof( $db_list ); ++$i ) {
            if( ! strcmp( $db_list[ $i ][ "Database" ], DB_NAME ) )
                $db_found = true;
        }

        /* if database not found then create one */
        if( ! $db_found ) {
            echo 'Creating database ' . DB_NAME . "...\n";

            $stmt = $pdo->prepare( 'CREATE DATABASE ' . DB_NAME );
            $stmt->execute( );

            echo 'Database ' . DB_NAME . " created!\n";
        }

        /* database found */
        echo 'Database ' . DB_NAME . " found!\n";
        $stmt = $pdo->prepare( 'USE ' . DB_NAME );

        /* now we need our database schema */

        $pdo = null;
    } catch( PDOException $ex ) {
        echo 'Connection failed: ' . $ex->getMessage( ) . "\n";
    }
?>
