var Index = {
	checkAuth: function(login, password) {
		$.ajax({
			type: 'GET',
			url: "api/checkAuth",
			data: 'login=' + login + "&&password=" + password,
			success: function(data) {
				if(data == "ok") {
					Cookies.set("login", login, {expires: 7});
					Cookies.set("password", password, {expires: 7});
					window.location.href = "/admin";
				} else {
					alert("Ошибка при авторизации!");
					window.location.href = "/";
				}
			}
		});
	},
}