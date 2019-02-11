---

layout: post

title: RBCDSAI - Web Science Symposium

venue: ICSR Auditorium

date: 2019-02-25 09:00:00 +0530

categories: events

---



<html>

<head>

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

body {

  margin: 0;

  font-family: "Times New Roman", Times, serif;

}



.topnav {

  overflow: hidden;

  background-color: #ffffff;

}



.topnav a {

  float: left;

  color: #c0c0c0;

  text-align: center;

  padding: 7px 8px;

  text-decoration: none;

  font-size: 18px;

  

}



.topnav a:hover {

  background-color: #ffffff;

  color: black;

}



.topnav a.active {

  background-color: #ffffff;

  color: black;

}

</style>

 <script>


        function makeitactiveonload() {


             document.getElementById('dynamiccontent').innerHTML = '<div style="padding-left:16px"><img src="/assets/wst.jpg" alt="wst-image" style="width:1100px;height:250px;"><br><br>h5>Date: <strong>February 25, 2019 - February 26, 2019 </strong></h5><br>Venue: <strong>ICSR Auditorium, IIT Madras</strong><br><h4><strong>RBCDSAI Web Science Symposium </strong></h4></div>'


        }


        function disableothersonclick(elementtoactive) {


            if(elementtoactive == 'overviewid')


            {


                document.getElementById('dynamiccontent').innerHTML = '<div style="padding-left:16px"><img src="/assets/wst.jpg" alt="wst-image" style="width:1100px;height:250px;"><br><br>h5>Date: <strong>February 25, 2019 - February 26, 2019 </strong></h5><br>Venue: <strong>ICSR Auditorium, IIT Madras</strong><br><h4><strong>RBCDSAI Web Science Symposium </strong></h4></div>'


            }


            else 


            {


                document.getElementById('dynamiccontent').innerHTML = '<p>Agenda</p>';


            }


        }


    </script>

</head>

<body>



<div class="topnav" onload="makeitactiveonload()">


        <a  class="active"  onclick="disableothersonclick('overviewid')">Overview</a>


        <a  onclick="disableothersonclick('agendaid')" >Agenda</a>


</div>

<div id="dynamiccontent">


        <div style="padding-left:16px"><img src="/assets/wst.jpg" alt="wst-image" style="width:1100px;height:250px;"><br><br><h5>Date: <strong>February 25, 2019 - February 26, 2019 </strong></h5><br>Venue: <strong>ICSR Auditorium, IIT Madras</strong><br><h4><strong>RBCDSAI Web Science Symposium </strong></h4></div>


</div>



</body>

</html>
