
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
<html>
<head>
        <META HTTP-EQUIV="Pragma" CONTENT="no-cache">
        <META HTTP-EQUIV="Expires" CONTENT="-1">
        <META HTTP-EQUIV="Cache-Control" CONTENT="no-store">
        <title>MARCTracker - Train Status View</title>
        <link rel="stylesheet" type="text/css" href="styles/public_style.css">
        <script src="jscripts/func.js" language="JavaScript"></script>
        <META HTTP-EQUIV="Refresh" content="60">
<script type="text/javascript">
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-44674559-1', 'marctracker.com');
  ga('send', 'pageview');

</script>
</head>

<body topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginwidth="0" marginheight="0" onLoad="populate('<nobr>Thank you for riding MARC train service</nobr>')">

<!-- Header/Menu -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/header_back2.gif" height="113">
        <tr>
                <td rowspan="2">&nbsp;&nbsp;</td>
                <td rowspan="2" width="282"><a href="http://www.mtamaryland.com/"><img src="images/mta_logo.gif" width="282" height="113" alt="Maryland Transit Administration" border="0"></a></td>
                <td rowspan="2">&nbsp;&nbsp;&nbsp;</td>
                <td align="right">
                        <table cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                        <td align="left">
                                                <img src="images/spacer.gif" width="1" height="21">
                                                <table border="0" cellpadding="2" cellspacing="0">
                                                        <tr>
                                                                <td class="tickerBlack" width="115" nowrap align="left"><span class="mainTitle">MARCTracker</span><br>Live GPS Train Locations</td>
                                                                <td class="tickerYellow" width="110" valign="middle" nowrap>MARC Train<br>Emergency News &amp; Service Update</td>
<!--
                                                                <td valign="middle" class="tickerYellow"><img src="images/blue_light.gif" width="22" height="22" alt="Blue Service Indicator"></td>
-->
                                                        </tr>
                                                </table>
                                        </td>
                                        <td>
                                                <img src="images/spacer.gif" width="1" height="21" border="0">
                                                <div id="msgBox" class="hiddenBar"><nobr>Thank you for riding MARC train service</nobr></div>
                                                <div class="scrollMessage" onMouseover="pause(0)" onMouseout="resume(2)"><div id="scroller" class="scrollBar"></div></div>
                                        </td>
                                </tr>
                        </table>
                </td>
                <td rowspan="2">&nbsp;&nbsp;&nbsp;</td>
        </tr>
        <tr>
                <td valign="bottom">
                        <table cellpadding="0" cellspacing="0" border="0" name="link_table" id="link_table">
                                <tr>
                                        <td class="menuUp" onMouseOver="mDown(0)" onMouseOut="mUp(0)" onclick="window.location='location.html?11469758836270';">TRAIN LOCATION</td>
                                        <td width="1"></td>
                                        <td class="menuOff" onMouseOver="mDown(2)" onMouseOut="mOff(2)" onclick="window.location='status.html?11469758836270';">TRAIN STATUS</td>
                                        <td width="1"></td>
                                        <td class="menuUp" onMouseOver="mDown(4)" onMouseOut="mUp(4)" onclick="window.location='schedule.html';">TRAIN SCHEDULE</td>
                                </tr>
                        </table>
                </td>
        </tr>
</table>
<!-- Submenu -->
<table cellpadding="0" cellspacing="0" border="0" name="sublink_table" id="sublink_table">
<!-- bgcolor="#CCCCFF" width="800" -->
        <tr>
                <td class="submenuUp" onMouseOver="subDown(0)" onMouseOut="subUp(0)" onclick="window.location='northCamden.html?11469758836270';">Northbound<br>Camden</td>
                <td class="submenuUp" onMouseOver="subDown(1)" onMouseOut="subUp(1)" onclick="window.location='southCamden.html?11469758836270';">Southbound<br>Camden</td>
                <td class="submenuUp" onMouseOver="subDown(2)" onMouseOut="subUp(2)" onclick="window.location='westBrunswick.html?11469758836270';">Westbound<br>Brunswick</td>
                <td class="submenuUp" onMouseOver="subDown(3)" onMouseOut="subUp(3)" onclick="window.location='eastBrunswick.html?11469758836270';">Eastbound<br>Brunswick</td>
                <td class="submenuUp" onMouseOver="subDown(4)" onMouseOut="subUp(4)" onclick="window.location='northPenn.html?11469758836270';">Northbound<br>Penn</td>
                <td class="submenuUp" onMouseOver="subDown(5)" onMouseOut="subUp(5)" onclick="window.location='southPenn.html?11469758836270';">Southbound<br>Penn</td>

        </tr>
</table>
<!-- <br> -->
<!-- Subheader -->
<!--
<table cellpadding="0" cellspacing="0" border="0">
        <tr>
                <td width="175"><img src="images/train_status.gif" width="175" height="20"></td>
                <td><hr class="lineRule"></td>
        </tr>
</table>
-->
<!-- Main Body -->
<table cellpadding="0" cellspacing="0" border="0" width="100%">
        <tr>
                <!-- Menu -->
                <td valign="top" colspan="2">
                </td>
        </tr>
        <tr>
                <!-- Content -->
                <td valign="top">&nbsp;</td>
                <td valign="top">
                <br>


                                <table cellpadding="0" cellspacing="0" border="0" width="950">
                                        <tr>
                                                <td colspan="6" class="textStatusLine">CAMDEN NORTH</td>
                                                <!-- <td><img src="images/line_end.gif" width="22" height="22"></td> -->
                                                <td colspan="2">&nbsp;</td>
                                        </tr>


                                        <tr class="textStatusHdr">
                                                <th>&nbsp;</th>
                                                <th width="70">Train No.</th>
                                                <th width="200">Next Station</th>
                                                <th width="80">EST Depart</th>
                                                <th width="100">Status</th>
                                                <th width="80">Delay</th>
                                                <th width="180">Last Update</th>
                                                <th width="220">Message</th>
                                        </tr>
                                    
                          
                          
              

                </table>
                 <br> 


                                <table cellpadding="0" cellspacing="0" border="0" width="950">
                                        <tr>
                                                <td colspan="6" class="textStatusLine">CAMDEN SOUTH</td>
                                                <!-- <td><img src="images/line_end.gif" width="22" height="22"></td> -->
                                                <td colspan="2">&nbsp;</td>
                                        </tr>


                                        <tr class="textStatusHdr">
                                                <th>&nbsp;</th>
                                                <th width="70">Train No.</th>
                                                <th width="200">Next Station</th>
                                                <th width="80">EST Depart</th>
                                                <th width="100">Status</th>
                                                <th width="80">Delay</th>
                                                <th width="180">Last Update</th>
                                                <th width="220">Message</th>
                                        </tr>
                                    
                          
                          
              

                </table>
                 <br> 


                                <table cellpadding="0" cellspacing="0" border="0" width="950">
                                        <tr>
                                                <td colspan="6" class="textStatusLine">BRUNSWICK WEST</td>
                                                <!-- <td><img src="images/line_end.gif" width="22" height="22"></td> -->
                                                <td colspan="2">&nbsp;</td>
                                        </tr>
                                         



                                        <tr class="textStatusHdr">
                                                <th>&nbsp;</th>
                                                <th width="70">Train No.</th>
                                                <th width="200">Next Station</th>
                                                <th width="80">EST Depart</th>
                                                <th width="100">Status</th>
                                                <th width="80">Delay</th>
                                                <th width="180">Last Update</th>
                                                <th width="220">Message</th>
                                        </tr>
                                    
                          
                          
              

                </table>
                 <br> 


                                <table cellpadding="0" cellspacing="0" border="0" width="950">
                                        <tr>
                                                <td colspan="6" class="textStatusLine">BRUNSWICK EAST</td>
                                                <!-- <td><img src="images/line_end.gif" width="22" height="22"></td> -->
                                                <td colspan="2">&nbsp;</td>
                                        </tr>
                                         



                                        <tr class="textStatusHdr">
                                                <th>&nbsp;</th>
                                                <th width="70">Train No.</th>
                                                <th width="200">Next Station</th>
                                                <th width="80">EST Depart</th>
                                                <th width="100">Status</th>
                                                <th width="80">Delay</th>
                                                <th width="180">Last Update</th>
                                                <th width="220">Message</th>
                                        </tr>
                                    
                          
                          
              

                </table>
                 <br> 


                                <table cellpadding="0" cellspacing="0" border="0" width="950">
                                        <tr>
                                                <td colspan="6" class="textStatusLine">PENN NORTH</td>
                                                <!-- <td><img src="images/line_end.gif" width="22" height="22"></td> -->
                                                <td colspan="2">&nbsp;</td>
                                        </tr>


                                        <tr class="textStatusHdr">
                                                <th>&nbsp;</th>
                                                <th width="70">Train No.</th>
                                                <th width="200">Next Station</th>
                                                <th width="80">EST Depart</th>
                                                <th width="100">Status</th>
                                                <th width="80">Delay</th>
                                                <th width="180">Last Update</th>
                                                <th width="220">Message</th>
                                        </tr>
                                    
                                                <tr class="textStatusAll">
                                                                        <td><table width="15" height="15"><tr><td class="textStatusUN"></td></tr></table></td>
                                        <td width="70">452</td>
                                                                <td width="200">Washington Union Station</td>
                                                                <td width="80">10:30 PM</td>

                                            <td width="100">


                                            
                                            
                                            On Time                                                 
                                            
                                            </td>



                                        <td width="80"></td>
                            
                                        <td width="180">
                            
                            
                            
                                        </td>
                                                <td width="220"></td>
                                        </tr>
                      
                          
                                                <tr class="textStatusAll">
                                                                        <td><table width="15" height="15"><tr><td class="textStatusOT"></td></tr></table></td>
                                        <td width="70">548</td>
                                                                <td width="200">Edgewood</td>
                                                                <td width="80">10:27 PM</td>

                                            <td width="100">


                                            
                                            
                                            On Time
                                            
                                            </td>



                                        <td width="80">3 Min</td>
                            
                                        <td width="180">
                            
                            
                            
                                                10:20 PM 7/28/16
                            
                            
                            
                                        </td>
                                                <td width="220"></td>
                                        </tr>
                      
                          
              

                </table>
                 <br> 


                                <table cellpadding="0" cellspacing="0" border="0" width="950">
                                        <tr>
                                                <td colspan="6" class="textStatusLine">PENN SOUTH</td>
                                                <!-- <td><img src="images/line_end.gif" width="22" height="22"></td> -->
                                                <td colspan="2">&nbsp;</td>
                                        </tr>


                                        <tr class="textStatusHdr">
                                                <th>&nbsp;</th>
                                                <th width="70">Train No.</th>
                                                <th width="200">Next Station</th>
                                                <th width="80">EST Depart</th>
                                                <th width="100">Status</th>
                                                <th width="80">Delay</th>
                                                <th width="180">Last Update</th>
                                                <th width="220">Message</th>
                                        </tr>
                                    
                          
                          
              

                </table>
                 <br> 

          </td>
        </tr>
</table>
<!-- Footer -->
</body>
<head>
        <META HTTP-EQUIV="Pragma" CONTENT="no-cache">
</head>
</html>
'''