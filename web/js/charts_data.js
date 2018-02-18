var ChartsData = {
	// Basic
	pie1Chart: {
		type: 'pie',
		data: {
			datasets: [{
				data: [
					/*Math.round(Math.random() * 100),
					Math.round(Math.random() * 100),
					Math.round(Math.random() * 100),*/
					252.7,
					81.5,
					1396.437,
				],
				backgroundColor: [
					"red",
					"green",
					"blue",
				],
				label: 'Ежегодное потребление'
			}],
			labels: [
				'Солнце',
				'Ветер',
				'ЕЭС'
			]
		},
		options: {
			responsive: true
		}
	},
	stepSize2Chart: {
		type: 'line',
		data: {
			labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
			datasets: [{
				label: 'Потребление',
				fill: false,
				backgroundColor: "blue",
				borderColor: "blue",
				data: [
					10,
					30,
					50,
					40,
					5,
					60,
					35
				],
			}]
		},
		options: {
			responsive: true,
			title: {
				display: true,
				text: 'График суточного потребления'
			},
			tooltips: {
				mode: 'index',
				intersect: false,
			},
			hover: {
				mode: 'nearest',
				intersect: true
			},
			scales: {
				xAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Month'
					}
				}],
				yAxes: [{
					display: true,
					scaleLabel: {
						display: true,
						labelString: 'Value'
					}
				}]
			}
		}
	},
	// From server
}