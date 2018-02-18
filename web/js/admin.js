var Admin = {
	stepSizeData: null,

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
	getInfo: function() {
		$.ajax({
			type: 'GET',
			url: "api/getInfo",
			data: 'login=' + Cookies.get("login") + "&&password=" + Cookies.get("password"),
			success: function(data) {
				if(data != "error") {
					data = JSON.parse(data);
					console.log(data);
					Admin.stepSizeData = data[1];
					data = data[0];
					$("#Info_FullNameText").html(data[0]);
					$("#Info_BirthDateText").html(data[1]);
					$("#Info_CityText").html(data[2]);
					$("#Info_AddressText").html(data[3]);
					$("#Info_MonthText").html(data[4]);
					$("#Info_ProfitText").html(data[5]);
					$("#Info_AutoPayText").html(data[6]);
					$("#Info_BalanceText").html(data[7]);
					//
					Admin.drawChart(1);
					Admin.drawChart(2);
				} else {
					Cookies.remove("login");
					Cookies.remove("password");
					alert("Ошибка при проверке авторизации!");
					window.location.href = "/";
				}
			}
		});
	},
	init: function() {
		this.getInfo();
	},
	drawChart: function(chartNumber) {
		switch(chartNumber) {
			case 1: {
				var ctx = document.getElementById("Pie1ChartCanvas").getContext('2d');
				window.myPie = new Chart(ctx, ChartsData.pie1Chart);
				break;
			};
			case 2: {
				ChartsData.stepSize2Chart.data.labels = [];
				ChartsData.stepSize2Chart.data.datasets[0].data = [];
				for(var i = 21; i < 45; i++) {
					ChartsData.stepSize2Chart.data.labels.push(Admin.stepSizeData[i][2243]);
					ChartsData.stepSize2Chart.data.datasets[0].data.push(Admin.stepSizeData[i][2254]);
				}
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