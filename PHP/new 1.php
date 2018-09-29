<form action="">
<input type="number" name="number1"><br>
<input type="number" name="number2"><br>
<input type="submit" name="submit"><br>
</form>

<?php

if(isset($_GET['submit'])){

$number1=$_GET['number1'];
$number2=$_GET['number2'];
echo $number1+$number2;
	
}
?>