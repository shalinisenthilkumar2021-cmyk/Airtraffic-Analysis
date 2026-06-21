new Chart(
document.getElementById('trendChart'),
{
type:'line',
data:{
labels:[
'Jan',
'Feb',
'Mar',
'Apr',
'May',
'Jun'
],
datasets:[{
label:'Passenger Growth',
data:[
1200,
1800,
2500,
3200,
4100,
5200
]
}]
}
}
);

new Chart(
document.getElementById("trendChart"),
{
    type:"line",
    data:{
        labels:["Jan","Feb","Mar","Apr","May","Jun"],
        datasets:[{
            label:"Passengers",
            data:[12000,15000,18000,22000,26000,30000]
        }]
    }
});