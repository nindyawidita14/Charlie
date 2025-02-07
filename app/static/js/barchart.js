/*
    NAME:          barchart.js
    AUTHOR:        Alan Davies (Lecturer Health Data Science)
    EMAIL:         alan.davies-2@manchester.ac.uk
    DATE:          18/12/2019
    INSTITUTION:   University of Manchester (FBMH)
    DESCRIPTION:   JavaScript file for managing display of the bar chart using Chart.js
*/

function BarChart() {
  this.drawChart = function(pctData, elementId) {
      var ctx = document.getElementById(elementId).getContext('2d');
      new Chart(ctx, {
          type: 'bar',
          data: {
              labels: pctData.labels,
              datasets: [{
                  label: "Items",
                  backgroundColor: "#4e73df",
                  hoverBackgroundColor: "#2e59d9",
                  borderColor: "#4e73df",
                  data: pctData.data,
              }],
          },
          options: {
              maintainAspectRatio: true, // 确保图表不保持纵横比
              layout: {
                  padding: {
                      left: 10,
                      right: 25,
                      top: 25,
                      bottom: 0
                  }
              },
              scales: {
                  x: {
                      grid: {
                          display: false,
                          drawBorder: false
                      },
                      maxBarThickness: 25,
                  },
                  y: {
                      beginAtZero: true,
                      ticks: {
                          min: 0,
                          max: Math.max(...pctData.data) + 100, // 设置最大值为数据中的最大值加上一个偏移量
                          stepSize: 100, // 设置步长
                          padding: 10, // 调整 padding 值
                      },
                      grid: {
                          color: "rgb(234, 236, 244)",
                          zeroLineColor: "rgb(234, 236, 244)",
                          drawBorder: false,
                          borderDash: [2],
                          zeroLineBorderDash: [2]
                      }
                  },
              },
              plugins: {
                  legend: {
                      display: false
                  },
                  tooltip: {
                      titleMarginBottom: 10,
                      titleFont: {
                          size: 14
                      },
                      backgroundColor: "rgb(255,255,255)",
                      bodyColor: "#858796",
                      borderColor: '#dddfeb',
                      borderWidth: 1,
                      xPadding: 15,
                      yPadding: 15,
                      displayColors: false,
                      caretPadding: 10,
                      callbacks: {
                          label: function(tooltipItem) {
                              return tooltipItem.dataset.label + ': ' + tooltipItem.raw;
                          }
                      }
                  }
              }
          }
      });
  }
}