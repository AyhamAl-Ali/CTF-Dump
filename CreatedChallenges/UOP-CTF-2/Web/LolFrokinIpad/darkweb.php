<?php

    if ( $_GET['source'] == 1) {
        highlight_file(__FILE__);
    }

    echo "<!-- it's good to reload! -->\n";

    $email = $_POST['email'];
    $pass = $_POST['pass'];
    $test = $_POST['test'];

    if ( isset($_POST['email']) ) {
        
        
        $r = $_POST['test'];
        if ( $email != base64_decode("bWFoeWFAb25lc2hvdHRlYW0ubmV0") ) {
            die("Ops! Wrong Email");
        }

        $special = preg_replace("/[^a-zA-Z0-9$]/", "", $pass);
        if ( $special === base64_decode("T25lRGF5V2VHMHRJdEJlZjByZQ==") ) {
            die("Did you study Computer Science?! It's not that easy!");
        }

        if ( eval("return \$special=\"$special\";") ===  "OneDayWeG0tItBef0re" ) {
            highlight_file("flag.txt");
        } else {
            echo "Try Harder!";
        }
            
    }


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&display=swap" rel="stylesheet"> 
    <style>
        * {
            font-family: 'Silkscreen', cursive;
        }
    </style>
    <title>Dark Web Login Portal</title>
    
</head>
<body>

    <div style="margin: auto; width: max-content; text-align: center; margin-top: 100px;">

    <h1 style="">Access The Dark Web from your little broken chair!</h1>
    <form action="" method="POST">
        
        <input style="border: 1px solid rgba(0,0,0,.5); background: rgba(0,0,0,.1); font-size: 50px" type="text" name="email" placeholder="email">
        <input style="border: 1px solid rgba(0,0,0,.5); background: rgba(0,0,0,.1); font-size: 50px" type="submit" value="Login">
        <br>
        <br>
        <input style="border: 1px solid rgba(0,0,0,.5); background: rgba(0,0,0,.1); font-size: 50px" type="text" name="pass" placeholder="password">
        <input style="border: 1px solid rgba(0,0,0,.5); background: rgba(0,0,0,.1); font-size: 50px" type="submit" value="Login">

    </form>
    </div>

    
</body>
</html>
