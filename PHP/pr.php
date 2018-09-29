<form action="">
<input type="number" name="number1"><br>
<input type="submit" name="submit"><br>
</form>

<?php

if(isset($_GET['submit'])){

$number1=$_GET['number1'];
if(number1%5==0){
	echo "the number is divisible";
}
else{
	
	echo "the number is not divisible";
}
	
}
?>