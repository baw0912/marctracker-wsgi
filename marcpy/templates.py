
south_t = '''
                                        <tr><td>
                                                <table border=0 cellpadding=3 cellspacing=0>
                                                                <tr><th>Number</th><th>Odenton</th><th>Washington</th></tr>
                                                                <tr><td>${Number}</td><td>${OdentonTime}</td><td>${WashingtonTime}</td></tr>
                                                                <tr><th colspan=3>Next Station</th></tr>
                                                                <tr><td colspan=3>${NextStation}</td></tr>
                                                                <tr><th>Status</th><th></th><th>Est. Depart</th></tr>
                                                                <tr><td>${Status}</td><td>${Delay}</td><td>${EstDepart}</td></tr>
                                                                <tr><th colspan=3>Last Updated</th></tr>
                                                                <tr><td colspan=3>${LastUpdated}</td></tr>
                                                </table>
                                        </td></tr>
'''

north_t = '''
                                        <tr><td>
                                                <table border=0 cellpadding=3 cellspacing=0>
                                                                <tr><th>Number</th><th>Washington</th><th>Odenton</th></tr>
                                                                <tr><td>${Number}</td><td>${WashingtonTime}</td><td>${OdentonTime}</td></tr>
                                                                <tr><th colspan=3>Next Station</th></tr>
                                                                <tr><td colspan=3>${NextStation}</td></tr>
                                                                <tr><th>Status</th><th></th><th>Est. Depart</th></tr>
                                                                <tr><td>${Status}</td><td>${Delay}</td><td>${EstDepart}</td></tr>
                                                                <tr><th colspan=3>Last Updated</th></tr>
                                                                <tr><td colspan=3>${LastUpdated}</td></tr>
                                                </table>
                                        </td></tr>
'''

index_t = '''
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <title>Odenton MarcTracker</title>
  
  <link rel="stylesheet" href="https://d10ajoocuyu32n.cloudfront.net/mobile/1.3.1/jquery.mobile-1.3.1.min.css">
  
  <!-- Extra Codiqa features -->
  <link rel="stylesheet" href="codiqa.ext.css">
  
  <!-- jQuery and jQuery Mobile -->
  <script src="https://d10ajoocuyu32n.cloudfront.net/jquery-1.9.1.min.js"></script>
  <script src="https://d10ajoocuyu32n.cloudfront.net/mobile/1.3.1/jquery.mobile-1.3.1.min.js"></script>

  <!-- Extra Codiqa features -->
  <script src="https://d10ajoocuyu32n.cloudfront.net/codiqa.ext.js"></script>
   
</head>
<body>
<!-- Home -->
<div data-role="page" id="page1">
    <div data-role="content">
		Updated: ${TIME}
      <h2>Status</h2>
        <div data-role="collapsible-set" data-theme="b" data-content-theme="b">
            <div data-role="collapsible" data-collapsed="true">
                <h3>
                    Penn South (to DC)
                </h3>
				<table border=1 cellspacing=0 cellpadding=2>
${SOUTH}
				</table>
            </div>
            <div data-role="collapsible" data-collapsed="true">
                <h3>
                    Penn North (to Odenton)
                </h3>
				<table border=1 cellspacing=0 cellpadding=2>
${NORTH}
				</table>
            </div>
        </div>
         <h2>Schedule</h2>
         <h4>Weekday</h4>
        <div data-role="collapsible-set" data-theme="c" data-content-theme="c">
            <div data-role="collapsible" data-collapsed="true">
                <h3>
                    Penn South (To DC)
                </h3>
		      <table border=1 cellspacing=0 cellpadding=2>
               <tr><th>Number</th><th>Odenton</th><th>Washington</th></tr>
${SOUTH_SCHEDULE}
				</table>
            </div>
            <div data-role="collapsible" data-collapsed="true">
                <h3>
                    Penn North (To Odenton)
                </h3>
				<table border=1 cellspacing=0 cellpadding=2>
               <tr><th>Number</th><th>Washington</th><th>Odenton</th></tr> 
${NORTH_SCHEDULE}
				</table>
            </div>
        </div>
                 <h4>Saturday</h4>
        <div data-role="collapsible-set" data-theme="c" data-content-theme="c">
            <div data-role="collapsible" data-collapsed="true">
                <h3>
                    Penn South (To DC)
                </h3>
		      <table border=1 cellspacing=0 cellpadding=2>
               <tr><th>Number</th><th>Odenton</th><th>Washington</th></tr>
${SOUTH_SA_SCHEDULE}
				</table>
            </div>
            <div data-role="collapsible" data-collapsed="true">
                <h3>
                    Penn North (To Odenton)
                </h3>
				<table border=1 cellspacing=0 cellpadding=2>
               <tr><th>Number</th><th>Washington</th><th>Odenton</th></tr> 
${NORTH_SA_SCHEDULE}
				</table>
            </div>
        </div>
                 <h4>Sunday</h4>
        <div data-role="collapsible-set" data-theme="c" data-content-theme="c">
            <div data-role="collapsible" data-collapsed="true">
                <h3>
                    Penn South (To DC)
                </h3>
		      <table border=1 cellspacing=0 cellpadding=2>
               <tr><th>Number</th><th>Odenton</th><th>Washington</th></tr>
${SOUTH_SU_SCHEDULE}
				</table>
            </div>
            <div data-role="collapsible" data-collapsed="true">
                <h3>
                    Penn North (To Odenton)
                </h3>
				<table border=1 cellspacing=0 cellpadding=2>
               <tr><th>Number</th><th>Washington</th><th>Odenton</th></tr> 
${NORTH_SU_SCHEDULE}
				</table>
            </div>
        </div>
    </div>
</div>
</body>
</html>
'''
