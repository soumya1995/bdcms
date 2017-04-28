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

if( __name__ != '__main__' ):
    sys.exit( -1 )
else:
    print( "Content-Type: text/plain\r\n" )
    print( "Connecting to mongod.. ", end='' )
    client = pymongo.MongoClient( 'localhost', 27017 )

    try:
        client.admin.command( 'ismaster' )
        print( "OK" )
    except pymongo.ConnectionFailure:
        print( "FAIL" )

    print( "Acquiring bdcms database.. ", end='' )
    bdcms = client.bdcms
    print( "OK" )

    print( "Acquiring ``users\'\' collection.. ", end='' )
    users = bdcms.users
    print( "OK" )

    print( "Populating ``users\'\' collection.. ", end='' )
    bdcms.users.create_index([( 'usrid', pymongo.ASCENDING )],
            unique = True )
    many_users = [
            { 'usrid' : 0,
              'fname' : 'Rimack',
              'lname' : 'Zelnick',
              'email' : 'rzelnick@cs.stonybrook.edu',
              'uname' : 'rzelnick',
              'passw' : 'password123' },
            { 'usrid' : 1,
              'fname' : 'Soumya',
              'lname' : 'Das',
              'email' : 'soumya.das@stonybrook.edu',
              'uname' : 'sodas',
              'passw' : 'pass123' },
            { 'usrid' : 2,
              'fname' : 'Parth',
              'lname' : 'Gupta',
              'email' : 'parth.gupta@stonybrook.edu',
              'uname' : 'pgupta',
              'passw' : 'pass345' },
            { 'usrid' : 3,
              'fname' : 'Harkirat',
              'lname' : 'Randhawa',
              'email' : 'harkirat.randhawa@stonybrook.edu',
              'uname' : 'kirat',
              'passw' : 'password' } ]
    users.insert( many_users )

    print( "OK" )

    print( "Acquiring ``pages\'\' collection.. ", end='' )
    pages = bdcms.pages
    print( "OK" )

    print( "Populating ``pages\'\' collection.. ", end='' )
    bdcms.pages.create_index([( 'page_id', pymongo.ASCENDING )],
            unique = True )
    page = {
        # list of authors
        "authors" : [ bdcms.users.find_one({ "uname" : "rzelnick" }),
            bdcms.users.find_one({ "uname" : "pgupta" }) ],

        # title & subtitle
        "title" : "Home",
        "subtitle" : "",

        # language
        "language" : "english",

        # category
        "category" : "homepage",

        # tags
        "tags" : [ "welcome", "hello", "about", "donations" ],

        # introduction
        "introduction" : "This is the homepage of Suffolk County TASC",

        # paragraph1
        "paragraph1" : """Our organization is dedicated in informing the
community about DUI/DWI legislation that first time offenders may
not know about""",
        
        # paragraph2
        "paragraph2" : """This website provides useful links and information
regarding DMV legislation additionally you may support our
organization by donating to us""",

        # paragraphN
        # footer
        "footer" : "Copyright &copy; Suffolk County TASC" }
    bdcms.pages.insert( page )
    print( "OK" )

    print( "Acquiring ``posts\'\' collection.. ", end='' )
    posts = bdcms.posts
    post = {
        # list of authors
        "authors" : [ bdcms.users.find_one({ "uname" : "rzelnick" }),
            bdcms.users.find_one({ "uname" : "pgupta" }) ],

        # title & subtitle
        "title" : "What you should know about Interlock Ignitions",
        "subtitle" : "You thought you knew better",

        # language
        "language" : "english",

        # category
        "category" : "faq",

        # tags
        "tags" : [ "dmv", "dwi", "dui", "ignition", "interlock" ],

        # introduction
        "introduction" : "This is the homepage of Suffolk County TASC",

        # paragraph1
        "paragraph1" : """Our organization is dedicated in informing the
        community about DUI/DWI legislation that first time offenders may
        not know about""",
        
        # paragraph2
        "paragraph2" : """This website provides useful links and information
        regarding DMV legislation additionally you may support our
        organization by donating to us""",

        # paragraphN
        # footer
        "footer" : "Copyright &copy; Suffolk County TASC" }
    result = bdcms.posts.insert( post )

    print( "OK" )

    print( "Acquiring ``multimedia\'\' collection.. ", end='' )
    multimedia = bdcms.multimedia
    print( "OK" )
