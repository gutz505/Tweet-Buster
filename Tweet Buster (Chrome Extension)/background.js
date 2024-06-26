chrome.runtime.onInstalled.addListener(function() {
    console.log("Twitter Enhancer extension installed.");
});

// Listen for messages from the content script and perform actions if needed
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    // Example: perform some background task when a message is received
    if (request.action === "processTweet") {
      console.log("Processing tweet in background:", request.data);
      // You can add more complex logic here if needed
      sendResponse({status: "Tweet processed"});
    }
  }
);
