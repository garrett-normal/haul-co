document.addEventListener("DOMContentLoaded", (e) => {
    const ticketsGraphCard = document.getElementById('tickets-graph-card');
    const employeesGraphCard = document.getElementById('employees-graph-card');

    if (ticketsGraphCard && employeesGraphCard) {
        const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        const data = [{
            labels: labels,
            label: "Ticket Volume by Month",
            data: [65, 59, 80, 81, 56, 55, 65, 59, 45, 81, 56, 55],
            fill: true,
            borderColor: '#f26b1d',
            tension: 0.05
        }]
        new Chart(ticketsGraphCard, {
            type: 'line',
            data: {
            labels: labels,
            datasets: data
            },
            options: {
            scales: {
                x: {
                    display: true,
                    text: "Month"
                },
                y: {
                    beginAtZero: true,
                    display: true
                }
            }
            }
        });

        
        new Chart(employeesGraphCard, {
            type: 'doughnut',
            data: {
            labels: ['Admin','Third Party','Unassigned','Company Driver', 'Owner/Operator'],
            datasets: [{
                labels: labels,
                label: "Amount",
                data: [2, 1, 4, 5, 2],
                fill: true,
                // borderColor: '#f26b1d',
                tension: 0.05
            }]
            },
            options: {}
        });
    }
})