from jinja2 import Environment, Template
import pdfkit

# Define data context

data = {

    "img_path" : r"C:\Users\khuba\PycharmProjects\scraping\images.jpg",
    "main_keyword": "digital marketing",
    "vol": "90000" ,
    "rating": "3.9",
    "review": "129",
    "k1": "online money making",
    "r1": "3.9",
    "k2": "money make",
    "r2": "2.9",
    "k3": "how to make money",
    "r3": "1.9",
    "k4": "easy money",
    "r4": "3.0",
}

# Create Jinja2 environment
env = Environment()

# Create a template string with basic styling

template_string = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Table with Colored Cells and Spacing</title>
    <link rel="stylesheet" href="./style.css">

<style>

  body{
     font-family: 'Roboto', sans-serif;



  }

.container {
  display: flex;
  align-items: center; /* Vertically center items */
}

.container img {
  margin-right: 10px; /* Adjust margin as needed */
}

img{
width:100px;
height:70px;
}

h3, p{
padding-left:50px;
}

table {
  width: 50%;
  border-collapse: separate; /* Separate borders for each cell */
  border-spacing: 10px;  /* Add spacing between cells */
}

th, td {

  padding: 15px;
  text-align: center;
  border: 1px solid #ddd; /* Add a visible border around each cell */
}

th {
  background-color: #ddd;
}

.cell1 {
  width:50px;
  height:50px;
  border-radius:20px;
  background-color: #CCD1D1;
}

.cell2 {
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #CCD1D1;
}

.cell3 {
color:white;
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #E74C3C;
}

.cell4 {
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #CCD1D1;
}

  .cell5 {
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #F4D03F;
}


  .cell6 {
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #F4D03F;
}

.cell7 {
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #F4D03F;
}


  .cell8 {
  color:white;
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #27AE60;
}


  .cell9 {
  color:white;
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #27AE60;
}


.cell10 {
color:white;
 width:50px;
  height:50px;
    border-radius:20px;
  background-color: #E74C3C;
}


</style>
</head>
<body>
<div class="container">
    <img src="{{ img_path }}" alt="map img">
    <h1>Google Maps Ranking Report</h1>
  </div>
      <h3> How do you rank for your main keyword </h3>
  <table>
    <tr>
      <td class="cell1">Main keyword <br> {{ main_keyword }} </td>
      <td class="cell2">Monthly Volume <br> {{ vol }}</td>
      <td class="cell3">Your Rating <br> {{ rating }}</td>
      <td class="cell4">Your Review  <br> {{ review }}</td>
    </tr>
  </table>

  <p>**If you do not rank in the top 3, you're missing &gt;90% of Google traffic.</p>


      <h3>Hpw do you rank for your main keyword </h3>
  <table>
    <tr>
      <td class="cell5">{{ k1 }} <br> <b> Reviews {{ r1 }} </b></td>
        <td class="cell6">{{ k2 }} <br> <b> Reviews {{ r2 }} </b></td>
      <td class="cell7">{{ k3 }} <br> <b> Reviews {{ r3 }} </b></td>
    </tr>
  </table>

  <p>Top 3 rankers attract the 90% of people searching for the main keyword. Your job is to reach the top 3 so you can attract these new clients every month.</p>


      <h3>Which main factors do influence Google ranking </h3>
  <table>
    <tr>
    <td class="cell8"><b> Relevance </b>  <br>How relevant the main keyword is to your business. </td>
    <td class="cell9"><b> Distance </b>  <br> How close the client's location is to your business.</td>
    <td class="cell10"><b> Reviews </b>  <br> Quantity, quality, recency, authority, variety of reviews.</td>

    </tr>
  </table>
  <p>Relevance and distance are uninfluenced factors. The only factor you can influence to climb the ranking and reach the top 3 positions is reviews.</p>



<div class="section">
  <h2>How can you reach the top 3 position?</h2>
  <ul>
    <li>Get reviews consistently every week, or better, every day.</li>
    <li>Get dozens of high-scoring, 4 or 5-star reviews.</li>
    <li>Make sure you always have very recent reviews.</li>
    <li>Make sure you get reviews left by Local Guides.</li>
    <li>Get text reviews, as varied as possible.</li>
  </ul>
</div>
</body>
</html>

"""


# Generate template object
template = env.from_string(template_string)

# Render the template with data
output_html = template.render(data)

# Output filename and optional CSS path (if needed)
output_filename = "report.pdf"


try:
  # Convert HTML to PDF using pdfkit
  pdfkit.from_string(output_html, output_filename, options={'enable-local-file-access': ''})
  print(f"PDF generated successfully: {output_filename}")
except Exception as e:
  print(f"Error converting HTML to PDF: {e}")
