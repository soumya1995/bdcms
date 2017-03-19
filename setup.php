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
        $stmt->execute( );

        /* now we need our database schema */
        echo "Create Tags Table\n";
        $sql = <<<EOT
            CREATE TABLE IF NOT EXISTS `Tags`(
                `id` int(8),
                `tagname` varchar(16),
                PRIMARY KEY(`id`) );
EOT;
        $stmt = $pdo->prepare( $sql );
        $stmt->execute( );
        echo "Tags Table Created\n";
        echo "Create Page Table\n";
        $sql = <<<EOT
            CREATE TABLE IF NOT EXISTS `Page`(
                `id` int(8),
                `title` varchar(32) NOT NULL,
                `author_ids` varchar(32),
                `content` varchar(4040),
                PRIMARY KEY(`id`) );
EOT;
        $stmt = $pdo->prepare( $sql );
        $stmt->execute( );
        echo "Page Table Created\n";
        echo "Create Users Table\n";
        $sql = <<<EOT
            CREATE TABLE IF NOT EXISTS `Users`(
                `id` int(8),
                `username` varchar(16),
                `md5hash` varchar(16),
                PRIMARY KEY(`id`) );
EOT;
        $stmt = $pdo->prepare( $sql );
        $stmt->execute( );
        echo "Users Table Created\n";
        echo "Create Post Table\n";
        $sql = <<<EOT
            CREATE TABLE IF NOT EXISTS `Post`(
                `id` int(8),
                `title` varchar(32),
                `category_id` varchar(12) NOT NULL,
                `tags_ids` varchar(16),
                `mmedia_ids` varchar(16),
                `content` varchar(3984),
                PRIMARY KEY(`id`) );
EOT;
        $stmt = $pdo->prepare( $sql );
        $stmt->execute( );
        echo "Post Table Created\n";
        echo "Create Categories Table\n";
        $sql = <<<EOT
            CREATE TABLE IF NOT EXISTS `Categories`(
                `id` int(8),
                `category` varchar(24),
                PRIMARY KEY(`id`) );
EOT;
        $stmt = $pdo->prepare( $sql );
        $stmt->execute( );
        echo "Categories Table Created\n";
        echo "Create Multimedia Table\n";
        $sql = <<<EOT
            CREATE TABLE IF NOT EXISTS `Multimedia`(
                `id` int(8),
                `filecontent` LONGBLOB,
                `filesize` unsigned(8),
                PRIMARY KEY(`id`) );
EOT;
        $stmt = $pdo->prepare( $sql );
        $stmt->execute( );
        echo "Multimedia Table Created\n";
        echo "Done setting up database schema configuration\n";
        $pdo = null;
    } catch( PDOException $ex ) {
        echo 'Connection failed: ' . $ex->getMessage( ) . "\n";
    }
?>
