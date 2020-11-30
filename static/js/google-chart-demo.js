/*
 Template Name: Ubazo - Admin & Dashboard Template
 Author: Myra Studio
 File: Google Charts
*/


$(function () {
  'use strict';
  // Bar chart

  google.charts.load('current', {packages: ['corechart', 'bar']});
  google.charts.setOnLoadCallback(drawMultSeries);
  // google.charts.setOnLoadCallback(drawMultSeries1);

  function drawMultSeries() {
    var data = google.visualization.arrayToDataTable([
      ['Category', 'Amount'],
      ['A', 81000,],
      ['B', 37000,],
      ['C', 26000,],
      ['D', 20000,],
      ['E', 15000,]
    ]);

    var options = {
      title: 'Amounts for each category',
      chartArea: {width: '100%'},
      hAxis: {
        title: 'USD',
        minValue: 15000
      },
      backgroundColor: {
        fill: "transparent"
      },
      fontName: 'inherit',
      height: 180,
      fontSize: 12,
      vAxis: {
        title: 'Categories'
      },
      colors: ['#2e7ce4', '#ae5af8'],
      legend: {position: 'none'}
    };

    var chart = new google.visualization.BarChart(document.getElementById('bar-chart1'));
    chart.draw(data, options);
  }


  function drawMultSeries1(x=category,y=count) {
    var data = google.visualization.arrayToDataTable([
      [x, y],
      ['A', 80,],
      ['B', 30,],
      ['C', 20,],
      ['D', 20,],
      ['E', 10,]
    ]);

    var options = {
      title: 'Counts for each category',
      chartArea: {width: '60%'},
      hAxis: {
        title: 'Count',
        minValue: 10
      },
      backgroundColor: {
        fill: "transparent"
      },
      fontName: 'inherit',
      height: 180,
      fontSize: 12,
      vAxis: {
        title: 'Categories'
      },
      colors: ['#ae5af8'],
      legend: {position: 'none'}
    };

    var chart = new google.visualization.BarChart(document.getElementById('bar-chart2'));
    chart.draw(data, options);
  }

});