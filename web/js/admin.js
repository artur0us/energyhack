var Admin = {
	checkAuth: function() {
		$.ajax({
			type: 'GET',
			url: "api/checkAuth",
			data: 'login=' + Cookies.get("login") + "&&password=" + Cookies.get("password"),
			success: function(data) {
				if(data != "ok") {
					Cookies.remove("login");
					Cookies.remove("password");
					alert("Ошибка при авторизации!");
					window.location.href = "/";
				} else {
					Admin.init();
				}
			}
		});
	},
	init: function() {
		this.drawChart(1);
		this.drawChart(2);
	},
	drawChart: function(chartNumber) {
		switch(chartNumber) {
			case 1: {
				var ctx = document.getElementById("Pie1ChartCanvas").getContext('2d');
				window.myPie = new Chart(ctx, ChartsData.pie1Chart);
				break;
			};
			case 2: {
				var ctx = document.getElementById("StepSize2ChartCanvas").getContext('2d');
				window.myPie = new Chart(ctx, ChartsData.stepSize2Chart);
				break;
			};
			default: {
				break;
			};
		}
	},
}