const dummyChartData2 = {
    type: "line",
    data: {
        labels: ['great food', 'great place', 'great service', 'good food',
            '5 star', 'good thing', 'friendly staff'],
        datasets: [
            {
                label: "Top 10 phrases used in positive reviews",
                data: [7, 6, 5, 5, 5, 4, 3],
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
        lineTension: 1,
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        padding: 25
                    }
                }
            ]
        },
        legend: {
            display: false
        },
    }
};

export const info2 = {
    data: dummyChartData2['data'],
    options: dummyChartData2['options']
};

export default info2