<?php
$signature = $_GET['signature'];
$timestamp = $_GET['timestamp'];
$nonce = $_GET['nonce'];
$echostr = $_GET['echostr'];

$array = array( $token, $timestamp, $nonce);
sort($array, SORT_STRING);
$str = implode($array);
if(sha1($str)==$signature){
    echo  $echostr;
}
echo  $echostr;