import sqlite3
from sqlite3 import Error
import emails
from datetime import datetime
con = sqlite3.connect('D:\wamp64\www\thereal.db')
cur = con.cursor()

def display(thedate = datetime.date(datetime.now())):
    cur.execute('SELECT event_name FROM event where date_time = (?)',(thedate,))
    rows = cur.fetchall()
    print("funcy")
    for row in rows:
        print(row)
    
    

def log(event_name = "no name", date_time = "no date", event_desc = "no desc", event_type = "no type", event_imp = 2):
    cur.execute('INSERT into event(event_name,date_time,event_desc, event_type,event_imp) values(?,?,?,?,?)',(event_name,date_time,event_desc, event_type,event_imp))
    con.commit()
    print("heysies")
    f = open("D:\wamp64\www\htmldays\{}.php".format(date_time), 'w')
    print("peeee")
    doc = """\
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

\
    """ 
    print("hekjqhkje")
    f.write(doc)
    f.close()

    print("done2")
log("anything","this is a adate")

# def changename(id_, event_name = "NULL"):
#     if event_name == "NULL":
#         print("error")
#     else:
#         cur.execute('UPDATE event SET event_name = (?) WHERE id = (?)',(event_name,id_))
#         con.commit()
# def changedate(id_, date_time = "NULL"):
#     if date_time == "NULL":
#         print("error")
#     else:
#         cur.execute('UPDATE event SET date_time = (?) WHERE id = (?)',(date_time,id_))
#         con.commit()
# def changedesc(id_, event_desc = "NULL"):
#     if event_desc == "NULL":
#         print("error")
#     else:
#         cur.execute('UPDATE event SET event_desc = (?) WHERE id = (?)',(event_desc,id_))
#         con.commit()
# def changetype(id_, event_type = "NULL"):
#     if event_type == "NULL":
#         print("error")
#     else:
#         cur.execute('UPDATE event SET event_type = (?) WHERE id = (?)',(event_type,id_))
#         con.commit()
# def changeimp(id_, event_imp = "NULL"):
#     if event_imp == "NULL":
#         print("error")
#     else:
#         cur.execute('UPDATE event SET event_imp = (?) WHERE id = (?)',(event_imp,id_))
#         con.commit()