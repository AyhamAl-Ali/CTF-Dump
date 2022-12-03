<?php

if ($_SERVER['REQUEST_METHOD'] == "UPDATE") {
    die("Updating... Failed!");
} elseif ($_SERVER['REQUEST_METHOD'] == "OPTIONS") {
    die("Hmmm good choice but not option here? try to erase me!");
} elseif ($_SERVER['REQUEST_METHOD'] == "HEAD") {
    die("NOT HEAD!");
} elseif ($_SERVER['REQUEST_METHOD'] == "DELETE") {
    $text = <<<EOD
    <div style='text-align: center; margin: auto;'>
    <h1>Ayyyyy! You got me dear!</h1>
    <p style='color: red; font-size: 10px;'>S1ZYVkE2MkNHUlpXS05SVUw1QkRJNDNGR01aRjZUUlJNTVpWNk1ET0dONlE9PT09</p>
    <p style='margin-top: 50px; color: rgba(0,0,0,.1); font-size: 5px;'>We can always try multiple times, multiple something ;)</p>
    </div>
    EOD;

    echo $text;
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.cdnfonts.com/css/weirdmojo" rel="stylesheet">
    <style>
        * {
            font-family: 'Weirdmojo', sans-serif;
        }
    </style>
    <title>✈🌐</title>
    
</head>
<body>

    <div style="margin: auto; width: max-content; text-align: center; margin-top: 100px;">

    <h1 style="">Your favorite UOP Talabat Website</h1>
    <form action="/" method="POST">
        
        <input style="border: 1px solid rgba(0,0,0,.5); background: rgba(0,0,0,.1); font-size: 25px" type="text" name="item" placeholder="layz chips">
        <input style="border: 1px solid rgba(0,0,0,.5); background: rgba(0,0,0,.1); font-size: 25px" type="submit">

    </form>

    <?php 

    $item = $_POST['item'];

    if (strlen($item) > 0) {
        echo "<p style='text-align: center; font-size: 30px;'>Thank you for your order! your order is on the way to your <b>127.0.0.1<b></p>";
        echo "<p style='text-align: center; font-size: 40px;'>Your order is x1337 of '" . $item . "'</p>";
    }
    ?>
    </div>

    
</body>
</html>
