<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$host = "mysql";  // Docker MySQL service name
$user = "root";
$pass = "root";   // MySQL root password
$db = "ctf_db";

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die("Database connection failed: " . $conn->connect_error);
}
?>
