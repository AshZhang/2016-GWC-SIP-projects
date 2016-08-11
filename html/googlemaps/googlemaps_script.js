function initMap() {
	var mapDiv = document.getElementById('map');
	var map = new google.maps.Map(mapDiv, {
	center: {lat: 37.8604307, lng: -122.1249312},
	zoom: 15,
	mapTypeId: "hybrid"
	});
	
	var infowindow = new google.maps.InfoWindow({
		maxWidth: 175,
		content: "This is an info window."
	});
	
	var cows = new google.maps.Marker({
	position: {lat: 37.8598132, lng: -122.1196743},
	map: map,
	title: "Cows?",
	icon: "images/triangle_icon.png"
	});
	
	cows.addListener('click', function() {
		infowindow.setContent("There used to be cows here. Now there is only an ugly construction site surrounded by depressing gray fence.");
		infowindow.open(map, cows);
	});
	
	var school = new google.maps.Marker({
	position: {lat: 37.8673953, lng: -122.12601},
	map: map,
	title: "School.",
	icon: "images/triangle_icon.png"
	});
	
	school.addListener('click', function() {
		infowindow.setContent("Campolindo High School, a school of jocks and not-jocks.");
		infowindow.open(map, school);
	});
	
	var theater = new google.maps.Marker({
	position: {lat: 37.8602354, lng: -122.1267907},
	map: map,
	title: "Theater.",
	icon: "images/triangle_icon.png"
	});
	
	theater.addListener('click', function() {
		infowindow.setContent("Rheem Theater, the theater that almost shut down twice because no one wanted to pay for it.");
		infowindow.open(map, theater);
	});
	
	var produce = new google.maps.Marker({
	position: {lat: 37.8570414, lng: -122.1259511},
	map: map,
	title: "Fruits 'n veg.",
	icon: "images/triangle_icon.png"
	});
	
	produce.addListener('click', function() {
		infowindow.setContent("Moraga Produce, an awesome produce store with delicious fruits and vegetables. Suffered a period of decline under different ownership, but has bounced back successfully under original ownership.");
		infowindow.open(map, produce);
	});
	
	var homegoods = new google.maps.Marker({
	position: {lat: 37.8560877, lng: -122.1262798},
	map: map,
	title: "Random store.",
	icon: "images/triangle_icon.png"
	});
	
	homegoods.addListener('click', function() {
		infowindow.setContent("HomeGoods, a store where you can buy random useless stuff that looks cool at first but quickly becomes a dust collector.");
		infowindow.open(map, homegoods);
	});
	
	var drugs = new google.maps.Marker({
	position: {lat: 37.8566775, lng: -122.1261256},
	map: map,
	title: "Drugstore.",
	icon: "images/triangle_icon.png"
	});
	
	drugs.addListener('click', function() {
		infowindow.setContent("CVS Pharmacy, the one-stop-shop for shampoo, drugs, and loitering middle schoolers.");
		infowindow.open(map, drugs);
	});
	
	var gas = new google.maps.Marker({
	position: {lat: 37.8598494, lng: -122.124642},
	map: map,
	title: "Gasoline.",
	icon: "images/triangle_icon.png"
	});
	
	gas.addListener('click', function() {
		infowindow.setContent("Moraga Stars, a gas station run by super nice people who don't make stupid jokes while you pay for your gas, unlike the people at Arco.");
		infowindow.open(map, gas);
	});
	
	var forest = new google.maps.Marker({
	position: {lat: 49.2526517, lng: -123.2215992},
	map: map,
	title: "Forest.",
	icon: "images/triangle_icon.png"
	});
	
	forest.addListener('click', function() {
		infowindow.setContent("The Pacific Spirit Regional Park, a beautiful forest in Vancouver. Visit in the summer to pick delicious salmonberries and huckleberries (the red kind) before the kids get to them.");
		infowindow.open(map, forest);
	});
	
}
