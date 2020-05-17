// Initialize Firebase
var config = {
	apiKey: "AIzaSyCKQl74vgI56uxAGqVWYwAO_YmR6XoFwGo",
    authDomain: "images-5a37d.firebaseapp.com",
    databaseURL: "https://images-5a37d.firebaseio.com",
    projectId: "images-5a37d",
    storageBucket: "images-5a37d.appspot.com",
    messagingSenderId: "740161466118"
};
firebase.initializeApp(config);

var db = firebase.database();
var img1 = document.getElementById('image1');
var images = db.ref('image_refrences');

//Create a 3d array to fill our data with
var image_data = [];


function search_image_from_database(searhIndex){
	//Extract data from the database
	var tag;
	images.on('value', function(snapshot) {
		snapshot.forEach(function(childSnapshot) {
			var childData = childSnapshot.val();

			if(childData.url_tag.includes(searhIndex)){
				tag = childData.url_tag;
				var url = childData.url;
			}
			image_data.push([url, tag]);
			extract_done = true;
			//console.log(tag)
		});
		console.log(image_data[0][0])
	});
}

var string = "brightcove logo full  1  png";
var sub = "k" 
console.log(string.includes(sub))
search_image_from_database();



var dbref = db.ref('image_refrences').child('A Light in the Attic')



/*
var image_promise = new Promise(function(resolve, reject){
	images.once('value').then(function(snapshot){
		snapshot.forEach(function(childSnapshot){
			var childData = childSnapshot.val();

			var url = childData.url;
			var tag = childData.url_tag;

			image_data.push([url, tag]);
			extract_done = true;

			if (true) {
				resolve(image_data);
			}
			console.log(tag)
		})
	})
})

//Search for all Will Ma's in the database
images.orderByChild("url_tag").equalTo("Will Ma").on("value", function(snapshot){
	console.log(snapshot.val());
})
*/