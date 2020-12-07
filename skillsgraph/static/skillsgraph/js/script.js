let chart_button = document.querySelector(".chart-icon");
let content_div = document.querySelector(".content");
let chart_div = document.querySelector(".chart-div");
let back_chart_button = document.querySelector("#back-chart-btn");
let category_select = document.querySelector('.link-list');

chart_button.addEventListener("click", function () {
    content_div.style.display = "none";
    chart_div.style.display = "block";
});
back_chart_button.addEventListener("click", function () {
    content_div.style.display = "block";
    chart_div.style.display = "none";
});

category_select.addEventListener("change", function () {
    let cat_selected = category_select.value;
    let url = "/skills/" + cat_selected;
    window.location.href = url;

});

let myChart = document.getElementById('myChart').getContext('2d');

// Global Options
Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 18;
Chart.defaults.global.defaultFontColor = '#777';

let massPopChart = new Chart(myChart, {
    type: 'pie', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
    data: {
        labels: [{% for row in rows %}
          "{{ row.0 }}",
          {% endfor %}

        ],
datasets: [{
    label: '{{ category }}',
    data: [
        {% for row in rows %}
              {{ row.1 }},
{% endfor %}
],
    //backgroundColor:'green',
    backgroundColor: [
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(255, 0, 0, .6)',

    ],
        borderWidth: 1,
            borderColor: '#777',
                hoverBorderWidth: 3,
                    hoverBorderColor: '#000'
          }]
        },
options: {
    title: {
        display: true,
            text: 'Most wanted skills in {{ category }}',
                fontSize: 25
    },
    legend: {
        display: false,
            position: 'right',
                labels: {
            fontColor: '#000'
        }
    },
    layout: {
        padding: {
            left: 0,
                right: 0,
                    bottom: 0,
                        top: 0
        }
    },
    tooltips: {
        enabled: true
    }
}
      });