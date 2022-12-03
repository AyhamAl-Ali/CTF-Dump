<?php
if (count($_COOKIE) == 0) {
    setcookie('isAdmin', 'false');
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🍪</title>
    
</head>
<body>

    <div>

    <?php 
    if ($_COOKIE['isAdmin'] == 'true') {
        echo "<h1 style='font-size=150px; color: rgba(0,0,0,.1)'>UoP{C00ki3s_4r3_R1sky}</h1>";
    } else {
        echo '<img style="margin: auto;" src="./assets/images/this-is-not-flag.gif">';
    }
    ?>
    </div>

    
</body>
</html>
