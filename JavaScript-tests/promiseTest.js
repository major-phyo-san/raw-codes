function get(url){
	return new Promise(function(resolve,reject){
		var req = new XMLHttpRequest();
		req.open('get',url,true);

		req.onloadstart = function(){
			console.log(new Date());
		}
		req.onloadend = function(){
			console.log(new Date());
		}
		req.onprogress = function(){
			console.log(new Date());
		}

		req.onload = function(){
			let now = new Date();
			console.log(now);
			if(req.status == 200 && req.readyState == 4){
				console.log('Response status: ' + req.status);
				console.log('Status text ' + req.statusText);
				console.log('Ready state: ' + req.readyState);
				console.log('Response URL: ' + req.responseURL);

				resolve(req.response);
			}
				
			else
				reject(Error(req.statusText));			
		}

		req.onerror = function(){
				reject(Error('Network error'));
		}

		req.send();
	});
}

var apiReqPromise = get('http://localhost:8700/Weather.php');
apiReqPromise.then(function(result){
	console.log(result);
},function(error){
	console.log(error);
});