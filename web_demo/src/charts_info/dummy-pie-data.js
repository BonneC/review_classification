// const colors = {
//     "Happy": 'rgb(255, 99, 132)',
//     "Angry": 'rgb(255, 193, 167)',
//     "Surprise": 'rgb(255, 229, 196)',
//     "Sad": 'rgb(90, 129, 158)',
//     "Fear":'rgb(125, 122, 162)'
// }

const dummyPieData = {
    type: "pie",
    data: {
        labels: ['fear','anger','disgust'],
        datasets: [
            {
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                ],
                data: [40, 20, 10],
                hoverOffset: 10
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        radius: '10%',
        legend: {
            position: 'right'
        }
    }
};

export const info3 = {
    data: dummyPieData['data'],
    options: dummyPieData['options']
};

export default info3