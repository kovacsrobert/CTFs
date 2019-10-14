<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas20", "pass": "<censored>" };</script></head>
<body>
<h1>natas20</h1>
<div id="content">
<?php

function debug($msg) {
    print "DEBUG: $msg<br>";
}

function print_credentials() {
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
        print "You are an admin. The credentials for the next level are:<br>";
        print "<pre>Username: natas21\n";
        print "Password: <censored></pre>";
    } else {
        print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
    }
}

function myopen($path, $name) { 
    return true; 
}

function myclose() { 
    return true; 
}

function mydestroy($sid) {
    return true;
}
function mygarbage($t) {
    return true;
}

function myread($sid) { 
    debug("myread - sid: $sid"); 
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
        debug("myread - Invalid SID"); 
        return "";
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    if(!file_exists($filename)) {
        debug("myread - Session file doesn't exist");
        return "";
    }
    debug("myread - Reading from ". $filename);
    $data = file_get_contents($filename);
    $_SESSION = array();
    foreach(explode("\n", $data) as $line) {
        debug("myread - line [$line]");
        $parts = explode(" ", $line, 2);
        if($parts[0] != "") {
            $_SESSION[$parts[0]] = $parts[1];
        }
    }
    return session_encode();
}

function mywrite($sid, $data) { 
    // $data contains the serialized version of $_SESSION
    // but our encoding is better
    debug("mywrite - $sid $data"); 
    // make sure the sid is alnum only!!
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
        debug("mywrite - Invalid SID"); 
        return;
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    $data = "";
    debug("mywrite - Saving in ". $filename);
    ksort($_SESSION);
    foreach($_SESSION as $key => $value) {
        debug("mywrite - $key => $value");
        $data .= "$key $value\n";
    }
    debug("mywrite - data: $data");
    file_put_contents($filename, $data);
    chmod($filename, 0600);
    return true;
}

session_set_save_handler(
    "myopen", 
    "myclose", 
    "myread", 
    "mywrite", 
    "mydestroy", 
    "mygarbage");
session_start();

if(array_key_exists("name", $_REQUEST)) {
    $_SESSION["name"] = $_REQUEST["name"];
    debug("Name set to " . $_REQUEST["name"]);
}

print_credentials();

$name = "";
if(array_key_exists("name", $_SESSION)) {
    $name = $_SESSION["name"];
}

?>

<form action="natas20.php" method="POST">
Your name: <input name="name" value="<?=$name?>"><br>
<input type="submit" value="Change name" />
</form>
</div>
</body>
</html>