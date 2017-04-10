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
function googleplus_share( event ) {
    window.open( this.href, '', ''
            + 'menubar=no,'
            + 'toolbar=no,'
            + 'resizable=yes,'
            + 'scrollbars=yes,'
            + 'width=780,'
            + 'height=539' );
    return false;
}
function facebook_share( event ) {
    window.open( this.href, '', ''
            + 'menubar=no,'
            + 'toolbar=no,'
            + 'resizable=yes,'
            + 'scrollbars=yes,'
            + 'width=780,'
            + 'height=675' );
    return false;
}
function twitter_share( event ) {
    window.open( this.href, '', ''
            + 'menubar=no,'
            + 'toolbar=no,'
            + 'resizable=yes,'
            + 'scrollbars=yes,'
            + 'width=780,'
            + 'height=539' );
    return false;
}
