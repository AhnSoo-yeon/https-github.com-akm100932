const positiveWords = ['good', 'great', 'awesome', 'happy', 'love', 'excellent', 'fantastic', 'amazing', 'nice'];
const negativeWords = ['bad', 'sad', 'terrible', 'awful', 'hate', 'poor', 'horrible', 'angry', 'worst'];

document.getElementById('analyzeBtn').addEventListener('click', function () {
    const text = document.getElementById('input').value.toLowerCase();
    let score = 0;

    positiveWords.forEach(word => {
        if (text.includes(word)) score++;
    });

    negativeWords.forEach(word => {
        if (text.includes(word)) score--;
    });

    let resultText;
    if (score > 0) {
        resultText = 'The sentiment seems positive.';
    } else if (score < 0) {
        resultText = 'The sentiment seems negative.';
    } else {
        resultText = 'The sentiment seems neutral.';
    }

    document.getElementById('result').innerText = resultText;
});
