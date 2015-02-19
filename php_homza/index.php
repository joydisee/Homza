<?php
	require_once 'lib/couch.php';
	require_once 'lib/couchClient.php';
	require_once 'lib/couchDocument.php';
	require_once 'lib/dataAccess.php';

	$view1 = last_seen();

	
include('includes/header.php');
	
?><!DOCTYPE html>
<html>
	<head>
	
        <link href='http://fonts.googleapis.com/css?family=Lato:300,400' rel='stylesheet' type='text/css'>
        <link href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes"/>
        <link href="assets/css/icon.css" rel="stylesheet" type="text/css">
        <link href="assets/css/style.css" rel="stylesheet" type="text/css">
        
                <link rel="stylesheet" href="http://cdn.oesmith.co.uk/morris-0.5.1.css">
                <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
                <script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
                <script src="http://cdn.oesmith.co.uk/morris-0.5.1.min.js"></script>

	</head>
	
<body>

	<div id="page">

		<div class="img_in" style="background-image:url('https://lh4.googleusercontent.com/-yGbpROABGlw/UHFTVY4qQ9I/AAAAAAAAAKg/AiluU0GSaIE/w601-h602-no/IMG_3361.JPG');"></div> <!-- Yahya-->
		<div class="img_out" style="background-image:url('https://fbcdn-sphotos-h-a.akamaihd.net/hphotos-ak-xpf1/v/t1.0-9/p206x206/10464400_10152450938589754_9088480680765082395_n.jpg?oh=1ed8fd4b01afeebf28866ce098fb02c6&oe=55827C27&__gda__=1435651377_3946885bf0ad47479018f6c1b361c95e');"></div> <!-- Gael-->
		<div class="img_just" style="background-image:url('https://lh6.googleusercontent.com/-wE_smH6tICw/ThTE50L4KNI/AAAAAAAASVI/M8LjNWA7dNs/w1051-h701-no/IMG_3687.JPG');"></div> <!-- Ilyass-->
		<div class="img_in" style="background-image:url('https://lh6.googleusercontent.com/kY8GSNBoURvFIXX2ox55AmN1QF7p-RbZsOhw_QyRsw=w717-h701-no');"></div> <!-- Joe-->

		<p style="clear: both;"> <!-- IMPORTANT: After the very last image -->

	</div>


    <div id="page">

            <h2>Last Seen</h2><br />
			<?php
				foreach ( $view1->rows as $row ){
					$word = $row->value;
					$date = $row->key;
					
					$nowdate = time();
					$timestamp = strtotime($date);
					$seen_since = $nowdate - $timestamp;
					$nowdate = gmdate("Y-m-d H:i", $nowdate);
					
					$newDate = date("Y-m-d H:i", strtotime($date));
					
					echo '<a href="detail_word.php?word='.$word.'">'.$word.'</a> : '.secondsToTime($seen_since).' ago ( '.$newDate.' )<br/>';


					
				} 
?>

    </div>




</body>
</html>
