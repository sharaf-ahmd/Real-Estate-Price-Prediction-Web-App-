function onPageLoad() {
    console.log('Document loaded');
    var url = "http://127.0.0.1:5000/get_city";
    $.get(url, function(data, status) {
        console.log("Got response for city");
        if (data) {
            var cities = data.city;
            var citySelect = $('#selectCity');
            citySelect.empty();
            citySelect.append('<option disabled selected>Choose a Location</option>');
            for (var i in cities) {
                var opt = new Option(cities[i]);
                citySelect.append(opt);
            }
        }
    });
}


function predictPrice(){
    var City =document.getElementById('selectCity')
    var Land =document.getElementById('land')
    var House =document.getElementById('house')
    var Lat =document.getElementById('lat')
    var Lon =document.getElementById('lon')
    var prediction =document.getElementById('result') 

    var url = "http://127.0.0.1:5000/predict_price"
    $.post(url, {
    city: City.value,
    land: Land.value,
    house: House.value,
    lat: parseFloat(Lat.value),
    lon: parseFloat(Lon.value)
}, function(data, status) {
    prediction.innerHTML = "<h2>" + data.Prediction.toString() + " LKR </h2>";
});


}

window.onload = onPageLoad;

