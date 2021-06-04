// const colors = {
//     "Happy": 'rgb(255, 99, 132)',
//     "Angry": 'rgb(255, 193, 167)',
//     "Surprise": 'rgb(255, 229, 196)',
//     "Sad": 'rgb(90, 129, 158)',
//     "Fear":'rgb(125, 122, 162)'
// }

const dummyChartData = {
    type: "line",
    data: {
        labels: ['place', 'food', 'service', 'time', 'restaurant', 'staff', 'steak'],
        datasets: [
            {
                label: "Top 10 nouns used in positive reviews",
                data: [60, 53, 39, 26, 17, 15, 14],
                backgroundColor: [
                    'rgba(217,30,30,0.8)',
                    'rgba(240, 135, 54,0.8)',
                    'rgba(242, 177, 56,0.8)',
                    'rgba(242,211,56,0.8)',
                    'rgba(172, 188, 95,0.8)',
                    'rgba(125, 173, 122,0.8)',
                    'rgba(10,136,186,0.8)',
                    'rgba(11, 92, 158,0.8)',
                    'rgba(12,51,131,0.8)',
                    'rgba(2,30,83,0.8)',

                ],
                borderColor: [
                    'rgb(217,30,30)',
                    'rgb(240, 135, 54)',
                    'rgb(242, 177, 56)',
                    'rgb(242,211,56)',
                    'rgb(172, 188, 95)',
                    'rgb(125, 173, 122)',
                    'rgb(10,136,186)',
                    'rgb(11, 92, 158)',
                    'rgb(12,51,131)',
                    'rgb(2,30,83)',
                ],
                borderWidth: 3
            }
        ]
    },
    options: {
        responsive: true,
        // lineTension: 1,
        scales: {
            xAxes: [{
                gridLines: {
                    color: "rgba(0, 0, 0, 0)",
                }
            }],
            yAxes: [{
                gridLines: {
                    color: "rgba(0, 0, 0, 0)",
                },
                ticks: {
                    beginAtZero:true
                }
            }]
        },
        legend: {
            display: false
        }
    }
};

export const info = {
    data: dummyChartData['data'],
    options: dummyChartData['options']
};

export default info