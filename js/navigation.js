/*
 * Copyright (C) 2016 Haxorsoft, Inc. All Rights Reserved.
 *
 * No part of this publication may be reproduced, distributed, or
 * transmitted in any form or by any means, including photocopying,
 * recording, or other electronic or mechanical methods, without the prior
 * written permission of the publisher, except in the case of brief
 * quotations embodied in critical reviews and certain other noncommercial
 * uses permitted by copyright law. For permission requests, write to the
 * publisher, addressed “Attention: Permissions Coordinator,” at the address
 * below.
 *
 * Haxorsoft, Inc
 * 10 Bay Ave
 * Huntington, NY 11743
 * www.haxorsoft.com
 */
function toggle_menu( event ) {
    var i, navs = document.getElementsByClassName( 'item' );

    if( toggle_menu.toggled == 'undefined' )
        toggle_menu.toggled = false;

    if( toggle_menu.toggled ) {
        for( i = 0; i < navs.length; ++i )
            navs[ i ].style.display = 'none';
    } else if( ! toggle_menu.toggled ) {
        for( i = 0; i < navs.length; ++i )
            navs[ i ].style.display = 'block';
    }

    toggle_menu.toggled = ! toggle_menu.toggled;

    return false;
}
function dropdown( event ) {
    var i, n = this.children;

    for( i = 0; i < n.length; ++i )
        if( n[ i ].className == 'dropdown' )
            n[ i ].style.display = 'block';

    return false;
}
function rollup( event ) {
    var i, n = this.children;

    for( i = 0; i < n.length; ++i )
        if( n[ i ].className == 'dropdown' )
            n[ i ].style.display = 'none';

    return false;
}
