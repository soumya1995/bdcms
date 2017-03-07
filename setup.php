<?php
    define( 'DB_NAME',   'bd-cms'    );
    define( 'DB_HOST',   'localhost' );
    define( 'DB_UNAME',  'user'      );
    define( 'DB_PASSWD', 'password'  );

    try {
        $pdo = new PDO( 'mysql:dbname=' . DB_NAME . ';host=' . DB_HOST,
            DB_UNAME, DB_PASSWD );

        $st = $pdo->prepare( 'SHOW DATABASES',
            array( PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL ) );

        $st->execute( );

        while( $row = $st->fetch( ) )
            print $row;

        $pdo = null;
    } catch( PDOException $ex ) {
        echo 'Connection failed: ' . $ex->getMessage( );
    }
?>
