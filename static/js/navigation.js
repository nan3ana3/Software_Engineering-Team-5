var buttonMain = document.getElementById("buttonMain");
if (buttonMain) {
    buttonMain.addEventListener("click", function (e) {
        window.location.href = "/";
    });
}

var buttonDM = document.getElementById("buttonDM");
if (buttonDM) {
    buttonDM.addEventListener("click", function (e) {
        window.location.href = "/receivedDM";
    });
}

var buttonMypage = document.getElementById("buttonMypage");
if (buttonMypage) {
    buttonMypage.addEventListener("click", function (e) {
        window.location.href = "/mypage";
    });
}

var buttonLogout = document.getElementById("buttonLogout");
if (buttonLogout) {
    buttonLogout.addEventListener("click", function (e) {
        window.location.href = "/";
    });
}