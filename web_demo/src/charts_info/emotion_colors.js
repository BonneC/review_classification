const colors = {
    "Happy": 'rgb(255, 99, 132)',
    "Angry": 'rgb(255, 193, 167)',
    "Surprise": 'rgb(255, 229, 196)',
    "Sad": 'rgb(90, 129, 158)',
    "Fear":'rgb(125, 122, 162)'
}



export default {
    get_emotion_colors(emotions){
        let arr = []

        emotions.forEach(function (e) {
            arr.push(colors[e])
        })

        console.log(arr)
        return arr

    },
}