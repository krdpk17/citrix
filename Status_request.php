<html>
<head>
  <title>NetScaler CPX</title>
  <style type="text/css">

        .header {
            height: 50px;
            font: bold 30px Calibri, serif;
            background-color: #090775;
            color: #fff;
            padding: 5px;
        }   

        .button {
            padding: 12px 5px;
            font: bold 15px Calibri, serif;
            color: white;
            text-align: center;
            cursor: auto;
            background-color: #090775;
            border: none;
            border-radius: 3px;
            
        }

        input[type=number] {
            border: 1px solid #222;
            border-radius: 3px;
            padding: 3px;
            height: 40px;
        }

        td {
            font: 15px Calibri, serif;
            padding: 5px;
        }

        table {
            margin-top: 30px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0
              rgba(0, 0, 0, 0.19);
        }

  </style>
</head>

<script src="jquery-3.3.1.js"></script>

<?php 

  $nsip = $_POST['ip'];
  $username = $_POST['username'];
  $password = $_POST['password'];
  $res ="";
  $upVips = array();
  $downVips = array();

?>

<body>
  
<?php

  $res = json_decode(shell_exec("python Extract_VIP.py $nsip $username $password"));
  if($res=="")
  {
    echo "ERROR:<br> Please enter valid credintials.<br><br>";
    include 'home.html';  
    exit();
  }
 	
  else
  {
    $flag = 0;
	  foreach($res as $server)
    {
  	
  	  $ip = $server[1];
  	  $state = $server[2];
  	
      if($state == "UP")
      {
  		  array_push($upVips,$ip);
        $upString = $upString . "," . $ip;
        $flag1 = 1;    
  	  }

  	  else if($state == "DOWN")
      {
  		  array_push($downVips,$ip);
        $downString = $downString . "," . $ip;
        $flag2 = 1; 
  	  }
    }

    if($flag1 == 1)
    {
      exec("python publish_ip.py " . $upString, $output, $return);
      //sleep(1);
    }  
    if($flag12 == 1)
    {
      exec("python remove_ip.py " . $downString, $output, $return);
      //sleep(1);
    }  

  }

?>

<div class="header">
     NetScaler CPX VIP Status
</div>

<div class="timerSet">
     Set the time interval (in seconds) to wait between two successive health check.<br>
     <input type="number" id="timeVal" min="2">
     <input class="button" type="button" id="timerSetButton" value="Set Interval" onclick="settimer()">
</div>

<div id="sc">

<?php	

  unset($upString);
  unset($downString);
  $flag1 = 0;
  $flag2 = 0;

  $res = json_decode(shell_exec("python Extract_VIP.py $nsip $username $password"));

  echo "<table width='90%' align='center'>";
  echo "<tr><td><b>Server Name</b></td>
          <td><b>IP Address</b></td>
          <td><b>State</b></td>
          <td><b>Total packets sent</b></td>
          <td><b>Packet received rate</b></td>
          <td><b>Packet sent rate</b></td>
          <td><b>Primary port</b></td>
          <td><b>Total requests</b></td>
          <td><b>Invalid request response dropped</b></td>
          <td><b>VS Health</b></td>
          <td><b>Sort order</b></td>
          <td><b>Type</b></td>
          <td><b>Inactive services</b><td>
          </tr>";
  
  foreach($res as $server)
  {
  	
    $name = $server[0];
  	$ip = $server[1];
  	$state = $server[2];

  	if($state == "DOWN")
  	{
      $downString = $downString . "," . $ip;
  		array_push($downVips,$ip); 
  		unset($upVips[$ip]); 
      $flag2 = 1; 
  	}

  	else if($state == "UP")
  	{	
      $upString = $upString . "," . $ip;
  		array_push($upVips,$ip); 
  		unset($downVips[$ip]);
      $flag1 = 1;
  	}

  	echo "<tr><td>".$server[0]."</td>
               <td>".$server[1]."</td>
               <td>".$server[2]."</td>
               <td>".$server[3]."</td>
               <td>".$server[4]."</td>
               <td>".$server[5]."</td>
               <td>".$server[6]."</td>
               <td>".$server[7]."</td>
               <td>".$server[8]."</td>
               <td>".$server[9]."</td>
               <td>".$server[10]."</td>
               <td>".$server[11]."</td>
               <td>".$server[12]."</td>
           </tr>";
  }

  if($flag1 == 1)
    exec("python publish_ip.py " . $upString, $output1, $return);
  
  if($flag2 == 1)
    exec("python remove_ip.py " . $downString, $output2, $return);
 
  //sleep(2);
  echo "</table>";

?>
	
</div>

<script>

  var nsip = "<?php echo $nsip ?>";
  var uname = "<?php echo $username ?>";
  var pwd = "<?php echo $password ?>";
  var $scores = $("#sc");
  var timeVal = 4;
  var interval;

  function settimer() {
    clearInterval(interval);
    timeVal = parseInt(document.getElementById("timeVal").value);
    
    interval = setInterval(function () 
    {
      $scores.load("Status_request.php #sc", {ip:nsip, username:uname, password:pwd});
    }, timeVal * 1000);
  }

  interval = setInterval(function () 
  {
    $scores.load("Status_request.php #sc", {ip:nsip, username:uname, password:pwd});
  }, timeVal * 1000);

</script>


</body>
</html>



