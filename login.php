<?php
    // vim: number ts=4 sw=4 expandtab
    if( $_COOKIE ) {
        if( strcmp( $_COOKIE[ "session" ], "yes" ) ) {
            $session_id = $_COOKIE[ "session_id" ];
            header( 'Location: post.php' );
        }
    }
?>
<!DOCTYPE html>
<html><head>
<title></title>
<meta charset="utf-8" />
<link type="text/css" href="css/fonts/font-awesome.css" rel="stylesheet" />
<link type="text/css" href="css/fonts/opensans-fonts.css" rel="stylesheet" />
<link type="text/css" href="css/reset.css" rel="stylesheet" />
<link type="text/css" href="css/site.css" rel="stylesheet" />
<link type="text/css" href="css/navigation.css" rel="stylesheet" />
<link type="text/css" href="css/grid.css" rel="stylesheet" />
<style type="text/css">
html {
    min-height: 100%;
    position: relative;
}
.panel {
    margin: 1em 0;
    margin-right: auto;
    margin-left: auto;
    background: #00f;
    padding: 1em;
    color: #fff;
    width: 40%;
}
#footer {
    position: absolute;
    bottom: 0;
    width: 100%;
}
</style>
</head><body>
<div class="navigation">
<div class="container">
<div class="header">Control Panel</div>
<h1 style="color:#fff" class="align-center">Benevolent DevOps CMS</h1>
</div></div>
<div class="text container">
<div class="panel">
<form method="post" action="cgi-bin/login.py">
<h3 style="margin:0">Username:</h3>
<input type="text" name="username" placeholder="username" />
<h3 style="margin:0">Password:</h3>
<input type="password" name="password" />
<div><input type="checkbox" name="cookies" value="cookies"> Save my credentials
<div style="padding:1em 0"><input type="submit" value="Login" />
<input type="reset" value="Clear" /></div>
</div>
</form>
</div></div>
<div id="footer">
<div class="container">
<a class="links" href="#">About Us</a>
<a class="links" href="#">Tech Support</a>
<a class="links" href="#">Privacy</a>
<a class="links" href="#">Terms of Use</a>
<p class="align-center small">Copyright &copy; <?php echo date('Y'); ?> Benevolent DevOps. All Rights Reserved.</p>
</div></div>
</body></html>
