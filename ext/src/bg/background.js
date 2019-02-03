var toggle = false;
chrome.browserAction.onClicked.addListener(function(tab) {
  toggle = !toggle;
  if(toggle){
    chrome.browserAction.setIcon({path: "on.png", tabId:tab.id});
  }
  else{
    var existingEntries = [];
    chrome.browserAction.setIcon({path: "off.png", tabId:tab.id});
      chrome.history.search({text: '', maxResults: 50}, function(data) {
        data.forEach(function(page) {

            if(existingEntries == null) existingEntries = [];
            var myStrText=JSON.stringify(page.url);
            console.log(myStrText);
            object = {"url":page.url};


            existingEntries.push(object);
            var dat = JSON.stringify(existingEntries);

            localStorage.setItem("url", dat);


        });

      });
    }


});
