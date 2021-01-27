// Instantiate the map
$(document).ready(function(){
    Highcharts.mapChart('container', {
        chart: {
            map: 'custom/europe',
            spacingBottom: 20
        },
    
        title: {
            text: 'Density, Covid Cases'
        },
    
        legend: {
            enabled: true
        },
    
        plotOptions: {
            map: {
                allAreas: false,
                joinBy: ['iso-a2', 'code'],
                dataLabels: {
                    enabled: true,
                    color: '#FFFFFF',
                    style: {
                        fontWeight: 'bold'
                    },
                    // Only show dataLabels for areas with high label rank
                    format: null,
                    formatter: function () {
                        if (this.point.properties && this.point.properties.labelrank.toString() < 5) {
                            return this.point.properties['iso-a2'];
                        }
                    }
                },
                tooltip: {
                    headerFormat: '',
                    pointFormat: '{point.name}: <b>{series.name}</b>'
                }
            }
        },
    
        series: [
        {
            name: 'UTC - 2',
            data: ['IS'].map(function(code){
                return { code: code };
                })
            }
            ],
            
            credits: {
                enabled:false
            },
             mapNavigation: {
                enabled: true,
                enableButtons: false
            },

            exporting: {
                enabled:true
            }
    });

});
