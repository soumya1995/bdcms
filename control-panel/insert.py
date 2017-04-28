#!/usr/bin/python3
# Copyright 2017 Benevolent Developers.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pymongo
import sys

def print_usage( ):
    print( """
Insert document into a collection.
{0} [--select collection] [--from database] [--insert field=value]
    Options:
    --select collection     Selects a collection from a database
    --from   database       Selects a database
    --insert field=value    Inserts a field w/ value if field already exists
                            then it's value is overwritten
""".format( sys.argv[0] )
    sys.exit( -1 )

if( __name__ != '__main__' ):
    sys.exit( -1 )
else:
    try:
        client = pymongo.MongoClient( 'localhost', 27017 )
    except pymongo.errors.ConnectionFailure:
        print( "Failed to connect to mongod!" )
        sys.exit( -1 )

    argv = sys.argv
    argc = len( sys.argv )

    for i in range( 1, argc ):
        if( argv[ i ].lower( ) == "--select" ):
            if( i + 1 >= argc ):
                print_usage( )
            selected_collection = argv[ i + 1 ]
            i = i + 1
        elif( argv[ i ].lower( ) == "--from" ):
            if( i + 1 >= argc ):
                print_usage( )
            selected_database = argv[ i + 1 ]
            i = i + 1
        elif( argv[ i ].lower( ) == "--insert" ):
            if( i + 1 >= argc ):
                print_usage( )
            condition = argv[ i + 1 ].split( '=' )
            field = condition[ 0 ]
            value = condition[ 1 ]
            i = i + 1

    # debugging
    # print( "Selected Database   {0}".format( selected_database ) )
    # print( "Selected Collection {0}".format( selected_collection ) )
    # print("field = {0}, value = {1}".format( field, value ) )

    try:
        database = client[ selected_database ]
    except pymongo.errors.InvalidName:
        print( "No such database named {0}".format( database_selected ) )
        sys.exit( -1 )

    try:
        collection = database[ selected_collection ]
    except pymongo.errors.CollectionInvalid:
        print("No such collection named {0}".format(collection_selected))
        sys.exit( -1 )

    try:
        result = database[selected_collection].insert_one({ field : value })
    except pymongo.errors.PyMongoError:
        print("No such field where {0}={1}".format( field, value ) )
        sys.exit( -1 )
