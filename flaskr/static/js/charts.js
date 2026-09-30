document.addEventListener("DOMContentLoaded", (e) => {
    const ticketsGraphCard = document.getElementById('tickets-graph-card');
    console.log(e)
    if (ticketsGraphCard) {
        console.log('element found')
        new ApexCharts(ticketsGraphCard, {
            chart: { type: 'line', fontFamily: 'inherit', height: 240 },
            series: [{ name: 'Ticket Volume', data: [37, 45, 32, 58, 41, 63, 37, 45, 32, 58, 41, 63] }],
        }).render();
    }
})