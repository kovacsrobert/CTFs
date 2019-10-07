<?php

$username = "natas15\"/*";
$password = "*/; -- ";

$link = mysql_connect('172.17.0.2:3306', 'root', 'root');
mysql_select_db('natas15', $link);

$query = "SELECT * from users where username=\"".$username."\" and password=\"".$password."\"";
//$query = "SELECT * from users";
echo "Executing query: $query<br>";

if(mysql_num_rows(mysql_query($query, $link)) > 0) {
  echo "Successful login! The password for natas15 is <censored><br>";
} else {
  echo "Access denied!<br>";
}
mysql_close($link);

?>
