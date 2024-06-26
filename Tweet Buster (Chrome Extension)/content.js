async function modifyTweets() {
    const tweets = document.querySelectorAll('[data-testid="tweet"]:not(.processed)');

    tweets.forEach(tweet => {
        // Check if the tweet already has a processed div
        if (tweet.querySelector('.marked')) {
            return; // Skip tweet
        }

        tweet.classList.add('processed');  // Mark tweet as processed

        const tweetText = tweet.textContent;
        fetch(`http://localhost:5000/process`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: tweetText })
        })
        .then(response => response.text())
        .then(data => {
            const div = document.createElement('div');
            const p = document.createElement('p');            
            p.innerHTML = data.replace(/"/g, '');
            p.style.backgroundColor = '#00161f';
            p.style.border = '2px solid #546e78';
            p.style.borderRadius = '10px';
            p.style.padding = '10px'; // Add padding to make the border more visible
            p.style.margin = '10px';
            p.style.fontFamily = 'Arial, sans-serif';
            div.className = 'marked'; // Mark div            
            div.appendChild(p); // Append <p> to <div>            
            if (!tweet.querySelector('.marked')) {
                tweet.appendChild(div);
            }
        })
        .catch(error => console.error('Error:', error));
    });
}

// Continue with the same observer setup
const observer = new MutationObserver(modifyTweets);
observer.observe(document, {
    subtree: true,
    childList: true,
    characterData: false, 
});