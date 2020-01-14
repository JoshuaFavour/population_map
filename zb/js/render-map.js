require([
    "esri/Map",
    "esri/views/MapView"
  ], function(Map, MapView) {

  var map = new Map({
    basemap: "topo-vector"
  });

  var view = new MapView({
    container: "mapview",
    map: map,
    center: [-118.80500, 34.02700], // longitude, latitude
    zoom: 13
  });
});