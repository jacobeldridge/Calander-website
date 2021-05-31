<?php
    $dir = 'sqlite:D:\wamp64\www\thereal.db';
    $dbh  = new PDO($dir) or die("cannot open the database");
    
    $fullname = basename($_SERVER['PHP_SELF']);
    $name = trim($fullname,".php");
    $query =  $dbh->query("SELECT * FROM event WHERE date_time='$name'");
    $second = "SELECT * FROM event WHERE date_time='$name'";
    $result = $query->fetch(PDO::FETCH_ASSOC);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="\css\secondary.css">
</head>
<body>
    <div class="headerdiv">
    <div class="border">
    <h class="header"><?php echo $name ?></h>
    </div>

    </div>

<div class="tablediv">

    <?php 

    if (is_array($result))
    {
        foreach ($dbh->query($second)  as $row)
        {
            echo "<table><tr><th>Event Name:</th><td>" . $row["event_name"]. "</td></tr><tr><th>Event Type:</th><td>" . $row["event_type"] . "</td></tr><tr><th>Description:</th><td>" . $row["event_desc"]. "</td></tr>
            <tr><th>Importance:</th><td>" . $row["event_imp"]. "</td></tr></table>";
        }
    }
    else{
        echo "</div><script>alert('unable to retrieve data from database'); window.location = '/caldisp.php'</script>";
    }
    ?>
</div>
   

</body>
</html>

    