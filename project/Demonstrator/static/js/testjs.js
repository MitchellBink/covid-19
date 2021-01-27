// Instantiate the map
$(document).ready(function () {
    try {
        $(chart_id).highcharts({
            chart: {map: 'custom/europe', renderTo: 'chartID'},
            title: title,
            xAxis: xAxis,
            yAxis: yAxis,
            series: series,
            mapNavigation: mapNavigation
        });
    } catch (error){
        console.log(error);
    }

});


