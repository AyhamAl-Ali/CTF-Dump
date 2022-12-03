<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👨‍💻</title>
    
</head>
<body>

    <div>

    <h1>File Explorer</h1>
    <form action="/" method="POST">
        
        <input type="text" name="file" placeholder="index.php"> <input type="submit">

    </form>

    <?php 
    $file = $_POST['file'];

    if (isset($file)) {
        if (!str_contains($file, "flag") && !str_contains($file, "index.php")) { // txt file
            die("Are you trying to HACK ME?!!");
        }
        highlight_file($file);
    }
    ?>
    </div>

    
</body>
</html>
